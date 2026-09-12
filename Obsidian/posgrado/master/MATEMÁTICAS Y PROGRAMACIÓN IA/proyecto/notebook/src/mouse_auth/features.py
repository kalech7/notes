"""Extracción de características por sesión para entrenar los detectores."""

from __future__ import annotations

import csv
import math
from pathlib import Path
import statistics


FEATURE_NAMES = [
    "event_count",
    "move_count",
    "click_count",
    "duration_s",
    "event_rate_hz",
    "path_length_px",
    "net_displacement_px",
    "path_efficiency",
    "speed_mean",
    "speed_std",
    "speed_max",
    "acceleration_abs_mean",
    "acceleration_abs_std",
    "angle_change_abs_mean",
    "pause_count",
    "pause_fraction",
    "valid_segment_fraction",
]

# Las derivadas cinemáticas se calculan con el reloj registrado por el cliente.
TIME_COLUMN = "client timestamp"


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _std(values: list[float]) -> float:
    return statistics.pstdev(values) if len(values) > 1 else 0.0


def _wrapped_angle_difference(a: float, b: float) -> float:
    return (a - b + math.pi) % (2.0 * math.pi) - math.pi


def extract_session_features(path: str | Path) -> dict[str, float]:
    """Resume una sesión en 17 características sin usar etiquetas de test."""
    session_path = Path(path)
    events: list[tuple[float, float, float, str, str]] = []
    with session_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {TIME_COLUMN, "button", "state", "x", "y"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"Columnas faltantes en {session_path}")
        for line_number, row in enumerate(reader, start=2):
            try:
                t = float(row[TIME_COLUMN])
                x = float(row["x"])
                y = float(row["y"])
            except (TypeError, ValueError) as error:
                raise ValueError(f"Fila inválida {session_path}:{line_number}") from error
            if not all(math.isfinite(value) for value in (t, x, y)):
                raise ValueError(f"Valor no finito {session_path}:{line_number}")
            events.append((t, x, y, row["button"], row["state"]))

    if len(events) < 2:
        raise ValueError(f"La sesión necesita al menos dos eventos: {session_path}")
    events.sort(key=lambda event: event[0])
    duration = max(0.0, events[-1][0] - events[0][0])
    distances: list[float] = []
    speeds: list[float] = []
    speed_times: list[float] = []
    angles: list[float] = []
    pauses = 0

    for previous, current in zip(events, events[1:]):
        dt = current[0] - previous[0]
        dx = current[1] - previous[1]
        dy = current[2] - previous[2]
        distance = math.hypot(dx, dy)
        distances.append(distance)
        if dt <= 0.0:
            continue
        speed = distance / dt
        speeds.append(speed)
        speed_times.append(current[0])
        if distance > 0.0:
            angles.append(math.atan2(dy, dx))
        if dt >= 0.5:
            pauses += 1

    accelerations = []
    for i in range(1, len(speeds)):
        dt = speed_times[i] - speed_times[i - 1]
        if dt > 0.0:
            accelerations.append(abs(speeds[i] - speeds[i - 1]) / dt)

    angle_changes = [abs(_wrapped_angle_difference(a, b)) for a, b in zip(angles[1:], angles[:-1])]
    path_length = sum(distances)
    displacement = math.hypot(events[-1][1] - events[0][1], events[-1][2] - events[0][2])
    move_count = sum(state.lower() == "move" for _, _, _, _, state in events)
    click_count = sum(button.lower() != "nobutton" or state.lower() != "move" for _, _, _, button, state in events)
    possible_segments = len(events) - 1

    result = {
        "event_count": float(len(events)),
        "move_count": float(move_count),
        "click_count": float(click_count),
        "duration_s": duration,
        "event_rate_hz": len(events) / duration if duration > 0.0 else 0.0,
        "path_length_px": path_length,
        "net_displacement_px": displacement,
        "path_efficiency": displacement / path_length if path_length > 0.0 else 0.0,
        "speed_mean": _mean(speeds),
        "speed_std": _std(speeds),
        "speed_max": max(speeds, default=0.0),
        "acceleration_abs_mean": _mean(accelerations),
        "acceleration_abs_std": _std(accelerations),
        "angle_change_abs_mean": _mean(angle_changes),
        "pause_count": float(pauses),
        "pause_fraction": pauses / possible_segments,
        "valid_segment_fraction": len(speeds) / possible_segments,
    }
    if list(result) != FEATURE_NAMES or not all(math.isfinite(value) for value in result.values()):
        raise AssertionError("Contrato de características roto")
    return result
