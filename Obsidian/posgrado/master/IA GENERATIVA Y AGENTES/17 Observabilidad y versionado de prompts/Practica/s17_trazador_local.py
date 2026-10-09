"""Laboratorio propio S17. Solo stdlib, datos ficticios, ninguna API o LLM.
Los tokens son cifras simuladas, la duración es medida con perf_counter.
La máscara demuestra correos dict/list/tuple, no elimina toda PII.
"""
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import statistics
import time
import uuid

BASE = Path(__file__).resolve().parent
CORREO = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def sanear(data):
    if isinstance(data, str):
        return CORREO.sub("<CORREO>", data)
    if isinstance(data, dict):
        return {sanear(k): sanear(v) for k, v in data.items()}
    if isinstance(data, (list, tuple)):
        return [sanear(v) for v in data]
    return data


def costo(tokens_in, tokens_out):
    # Tarifas hipotéticas históricas del ejercicio, NO cotización vigente.
    return (tokens_in + 5 * tokens_out) / 1_000_000


class Trazador:
    """Un trazador secuencial: no compartir esta pila entre tareas paralelas."""
    def __init__(self):
        self.trazas = []
        self.actual = None
        self.pila = []

    @contextmanager
    def traza(self, nombre, entrada, prompt_version):
        if self.actual is not None:
            raise RuntimeError("Este ejemplo solo admite una corrida activa")
        self.actual = {
            "trace_id": uuid.uuid4().hex,
            "nombre": nombre,
            "inicio_utc": datetime.now(timezone.utc).isoformat(),
            "input": sanear(entrada),
            "prompt_version": prompt_version,
            "datos_simulados": True,
            "status": "ok",
            "error": None,
            "spans": [],
        }
        started = time.perf_counter()
        try:
            yield self.actual
        except Exception as exc:
            self.actual["status"] = "error"
            self.actual["error"] = sanear(f"{type(exc).__name__}: {exc}")
            raise
        finally:
            self.actual["duracion_ms"] = round((time.perf_counter() - started) * 1000, 6)
            self.actual["costo_estimado_usd"] = round(
                sum(s.get("costo_estimado_usd", 0) for s in self.actual["spans"]), 8
            )
            self.trazas.append(sanear(self.actual))
            self.actual = None

    @contextmanager
    def span(self, nombre, tipo, entrada=None):
        if self.actual is None:
            raise RuntimeError("Abrir primero una traza")
        s = {
            "trace_id": self.actual["trace_id"],
            "span_id": uuid.uuid4().hex,
            "padre": self.pila[-1]["span_id"] if self.pila else None,
            "nombre": nombre,
            "tipo": tipo,
            "inicio_utc": datetime.now(timezone.utc).isoformat(),
            "prompt_version": self.actual["prompt_version"],
            "input": sanear(entrada),
            "error": None,
        }
        started = time.perf_counter()
        self.pila.append(s)
        try:
            yield s
        except Exception as exc:
            s["error"] = sanear(f"{type(exc).__name__}: {exc}")
            raise
        finally:
            s["duracion_ms"] = round((time.perf_counter() - started) * 1000, 6)
            self.pila.pop()
            self.actual["spans"].append(sanear(s))


def generation(t, nombre, tokens_in, tokens_out):
    with t.span(nombre, "generation", {"contexto": "Información ficticia"}) as s:
        s.update({
            "modelo": "modelo-ficticio-sin-llamada",
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "costo_estimado_usd": costo(tokens_in, tokens_out),
            "output": "Texto simulado",
        })


def ejecutar(t, numero):
    correo = "ana.perez@ejemplo.test"
    entrada = (f"Consulta ficticia {numero} de {correo}", {"contactos": [correo]})
    with t.traza("consulta_simulada", entrada, "v1-didactica") as tr:
        with t.span("agente", "agent", entrada):
            with t.span("validar_entrada", "guardrail", entrada) as g:
                ok = numero != 3
                g["output"] = {"permitida": ok, "entrada_saneada": sanear(entrada)}
            if not ok:
                tr["status"] = "blocked_input"
                tr["output"] = "Entrada bloqueada por regla simulada"
                return
            generation(t, "decidir", 20000 if numero == 7 else 1000, 80)
            with t.span("consultar_calendario", "tool", {"numero": numero}) as s:
                if numero == 4:
                    raise RuntimeError(f"Fallo simulado para {correo}")
                s["output"] = {"fecha": "2026-10-20", "contacto": correo}
            generation(t, "redactar", 500, 120)
            tr["output"] = f"Fecha ficticia 20 de octubre, contacto {correo}"


def percentil_lineal(valores, p):
    ordenados = sorted(valores)
    indice = (len(ordenados) - 1) * p / 100
    bajo = int(indice)
    alto = min(bajo + 1, len(ordenados) - 1)
    return ordenados[bajo] + (indice - bajo) * (ordenados[alto] - ordenados[bajo])


def main():
    t = Trazador()
    fallos_propagados = 0
    for numero in range(1, 11):
        try:
            ejecutar(t, numero)
        except RuntimeError:
            # La capa del laboratorio decide continuar con los otros casos.
            fallos_propagados += 1
    payload = "\n".join(json.dumps(tr, ensure_ascii=False) for tr in t.trazas) + "\n"
    (BASE / "s17_trazas_ficticias.jsonl").write_text(payload, encoding="utf-8")
    assert len(t.trazas) == 10
    assert fallos_propagados == 1
    assert "ana.perez@ejemplo.test" not in payload
    assert all(not tr["spans"] or all(s["trace_id"] == tr["trace_id"] for s in tr["spans"]) for tr in t.trazas)
    assert any(tr["status"] == "blocked_input" for tr in t.trazas)
    assert any(s["error"] for tr in t.trazas for s in tr["spans"] if s["tipo"] == "tool")
    assert t.pila == [] and t.actual is None
    assert sanear(("x@ejemplo.test", {"y": ["z@ejemplo.test"]})) == ["<CORREO>", {"y": ["<CORREO>"]}]
    latencias = [tr["duracion_ms"] for tr in t.trazas]
    mas_cara = max(enumerate(t.trazas, start=1), key=lambda it: it[1]["costo_estimado_usd"])
    mas_lenta = max(enumerate(t.trazas, start=1), key=lambda it: it[1]["duracion_ms"])
    resultado = {
        "alcance": "Ejemplo propio, sin API, tokens ficticios y latencias reales variables",
        "corridas": len(t.trazas),
        "spans": sum(len(tr["spans"]) for tr in t.trazas),
        "bloqueadas": sum(tr["status"] == "blocked_input" for tr in t.trazas),
        "fallidas": sum(tr["status"] == "error" for tr in t.trazas),
        "fallos_propagados": fallos_propagados,
        "costo_estimado_total_usd": round(sum(tr["costo_estimado_usd"] for tr in t.trazas), 8),
        "corrida_mas_cara": mas_cara[0],
        "costo_mas_caro_usd": mas_cara[1]["costo_estimado_usd"],
        "corrida_mas_lenta_en_esta_ejecucion": mas_lenta[0],
        "latencia_media_ms": statistics.mean(latencias),
        "latencia_p50_ms": percentil_lineal(latencias, 50),
        "latencia_p95_ms": percentil_lineal(latencias, 95),
        "latencia_maxima_ms": max(latencias),
        "verificaciones": {
            "diez_corridas_conservadas": True,
            "error_herramienta_y_corrida_conservados": True,
            "excepcion_propagada": True,
            "correo_ficticio_original_ausente_en_exportacion": True,
            "dict_list_tuple_saneados": True,
            "contexto_restaurado": True,
        },
    }
    (BASE / "s17_resultados_verificados.json").write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
