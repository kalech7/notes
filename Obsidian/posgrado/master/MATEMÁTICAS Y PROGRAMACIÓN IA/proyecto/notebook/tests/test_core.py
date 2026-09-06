from __future__ import annotations

import csv
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mouse_auth.features import extract_session_features  # noqa: E402
from mouse_auth.metrics import classification_metrics, eer_operating_point  # noqa: E402
from mouse_auth.pipeline import quantile, select_labeled_paths  # noqa: E402


def write_session(path: Path, offset_x: float = 0.0, offset_y: float = 0.0) -> None:
    rows = [
        (0.0, "NoButton", "Move", 0.0 + offset_x, 0.0 + offset_y),
        (1.0, "NoButton", "Move", 3.0 + offset_x, 4.0 + offset_y),
        (2.0, "Left", "Pressed", 6.0 + offset_x, 8.0 + offset_y),
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["record timestamp", "client timestamp", "button", "state", "x", "y"])
        for timestamp, button, state, x, y in rows:
            writer.writerow([timestamp, timestamp, button, state, x, y])


class FeatureTests(unittest.TestCase):
    def test_geometry_and_translation_invariance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "a.csv"
            second = Path(directory) / "b.csv"
            write_session(first)
            write_session(second, 100.0, -50.0)
            a = extract_session_features(first)
            b = extract_session_features(second)
        self.assertAlmostEqual(a["path_length_px"], 10.0)
        self.assertAlmostEqual(a["net_displacement_px"], 10.0)
        self.assertAlmostEqual(a["speed_mean"], 5.0)
        for key in a:
            self.assertAlmostEqual(a[key], b[key], msg=key)

    def test_zero_time_segment_keeps_geometry_but_not_speed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            session = Path(directory) / "duplicate_timestamp.csv"
            with session.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["record timestamp", "client timestamp", "button", "state", "x", "y"])
                writer.writerows([
                    [0.0, 0.0, "NoButton", "Move", 0.0, 0.0],
                    [0.0, 0.0, "NoButton", "Move", 3.0, 4.0],
                    [1.0, 1.0, "NoButton", "Move", 6.0, 8.0],
                ])
            features = extract_session_features(session)
        self.assertAlmostEqual(features["path_length_px"], 10.0)
        self.assertAlmostEqual(features["speed_mean"], 5.0)
        self.assertAlmostEqual(features["valid_segment_fraction"], 0.5)


class MetricTests(unittest.TestCase):
    def test_metrics(self) -> None:
        metrics = classification_metrics([1, 1, 0, 0], [1, 0, 1, 0])
        self.assertEqual((metrics["tp"], metrics["fp"], metrics["fn"], metrics["tn"]), (1, 1, 1, 1))
        self.assertEqual(metrics["far"], 0.5)
        self.assertEqual(metrics["frr"], 0.5)

    def test_eer_and_quantile(self) -> None:
        point = eer_operating_point([0, 0, 1, 1], [0.1, 0.4, 0.6, 0.9])
        self.assertEqual(point["gap"], 0.0)
        self.assertAlmostEqual(quantile([0.0, 10.0], 0.25), 2.5)

    def test_only_publicly_labeled_test_sessions_are_selected(self) -> None:
        paths = [Path("session_a"), Path("session_b"), Path("session_c")]
        selected, missing = select_labeled_paths(paths, {"session_a": 0, "session_c": 1})
        self.assertEqual([path.name for path in selected], ["session_a", "session_c"])
        self.assertEqual(missing, 1)


if __name__ == "__main__":
    unittest.main()
