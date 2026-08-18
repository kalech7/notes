---
epoch: 1787015183445
mode: agent
backendId: claude
sessionId: "b93328dc-4a6f-4fd7-80a0-379a108f86c2"
agentLabel: "que es uv y que comandos debo saber explicame a detalle"
usage: '{"usedTokens":63230,"contextWindow":1000000,"inputTokens":2,"outputTokens":2,"cacheReadTokens":60423,"cacheWriteTokens":2803,"updatedAt":1787016731506}'
tags:
  - copilot-conversation
---

**user**: que es uv y que comandos debo saber explicame a detalle
[Timestamp: 2026/08/17 20:06:23]

**ai**: I'll read your note first to see what you already have on UV.Tu nota tiene una sola línea. Te amplío el tema a detalle.

# ¿Qué es UV?

**uv** es un gestor de paquetes y proyectos de Python escrito en **Rust**, creado por [Astral](https://astral.sh) (los mismos de Ruff). Su propuesta es reemplazar con **una sola herramienta** todo el ecosistema fragmentado que tradicionalmente usabas por separado:

| Herramienta tradicional | Para qué servía | Reemplazo en uv |
| --- | --- | --- |
| `pip` | Instalar paquetes | `uv pip` / `uv add` |
| `venv` / `virtualenv` | Crear entornos virtuales | `uv venv` |
| `pyenv` | Instalar versiones de Python | `uv python` |
| `pip-tools` | Compilar y fijar dependencias | `uv lock` / `uv pip compile` |
| `pipx` | Ejecutar herramientas CLI aisladas | `uv tool` / `uvx` |
| `poetry` / `pdm` | Gestión de proyectos | `uv init` / `uv sync` |
| `twine` | Publicar paquetes | `uv publish` |

## Por qué importa (sobre todo en IA/ML)

- **Velocidad**: es entre 10x y 100x más rápido que pip. En proyectos con `torch`, `transformers`, `numpy`, `scipy` — donde la resolución de dependencias es dolorosa — la diferencia es de minutos a segundos.
- **Caché global**: guarda los paquetes una sola vez en disco y usa *hardlinks* hacia cada entorno virtual. Tener 10 proyectos con PyTorch ya no significa 10 copias de 2 GB.
- **Reproducibilidad**: genera un `uv.lock` multiplataforma que fija exactamente qué se instala. Tu compañero de maestría ejecuta `uv sync` y obtiene *exactamente* tu mismo entorno.
- **Gestiona el propio Python**: descarga e instala la versión de Python que necesites, sin depender de Homebrew ni de pyenv.

# Instalación

En macOS (tu caso):

```bash
# Opción recomendada — instalador oficial
curl -LsSf https://astral.sh/uv/install.sh | sh

# O con Homebrew
brew install uv
```

Para actualizarlo después:

```bash
uv self update
```

---

# Comandos que debes saber

## 1. Gestión de proyectos (el flujo principal)

Este es el modo en que deberías trabajar por defecto.

```bash
uv init mi-proyecto        # crea un proyecto nuevo con pyproject.toml
uv init                    # inicializa el proyecto en la carpeta actual
uv init --lib              # proyecto pensado como librería (con src/)
uv init --app              # aplicación (opción por defecto)
```

`uv init` te genera esta estructura:

```
mi-proyecto/
├── .python-version      # versión de Python fijada para el proyecto
├── README.md
├── main.py
└── pyproject.toml       # declaración de dependencias y metadatos
```

### Añadir y quitar dependencias

```bash
uv add numpy pandas                  # instala y registra en pyproject.toml
uv add "torch>=2.0"                  # con restricción de versión
uv add --dev pytest ruff             # dependencias solo de desarrollo
uv add --optional viz matplotlib     # grupo opcional (extra)
uv add -r requirements.txt           # importa un requirements existente
uv add git+https://github.com/user/repo   # desde un repositorio Git

uv remove pandas                     # elimina la dependencia
```

Lo importante: `uv add` **crea el entorno virtual solo si no existe, resuelve, actualiza el lock e instala** — todo en un solo paso. No necesitas activar nada antes.

### Sincronizar y bloquear

```bash
uv sync              # deja el entorno EXACTAMENTE igual al uv.lock
uv sync --frozen     # sincroniza sin volver a resolver (ideal para CI/Docker)
uv sync --all-extras # incluye todos los grupos opcionales
uv sync --no-dev     # omite dependencias de desarrollo (producción)

uv lock              # recalcula uv.lock sin instalar nada
uv lock --upgrade    # actualiza todas las dependencias al máximo permitido
uv lock --upgrade-package numpy   # actualiza solo un paquete
```

> `uv sync` es *destructivo* en el buen sentido: si instalaste algo a mano que no está en el lock, lo desinstala. Esa es justamente la garantía de reproducibilidad.

### Ejecutar código

```bash
uv run main.py               # ejecuta dentro del entorno del proyecto
uv run python -c "import torch; print(torch.__version__)"
uv run pytest                # corre tus pruebas
uv run jupyter lab           # levanta Jupyter en el entorno del proyecto
uv run --with rich script.py # añade un paquete solo para esa ejecución
```

**`uv run` es el comando que más vas a usar.** Antes de ejecutar, verifica que el entorno esté sincronizado con el lock, así que nunca trabajas con un entorno desactualizado. Y como consecuencia, **ya no necesitas `source .venv/bin/activate`**.

### Inspeccionar el árbol de dependencias

```bash
uv tree                  # muestra el árbol completo
uv tree --depth 1        # solo dependencias directas
uv tree --package numpy  # de dónde viene un paquete concreto
```

Muy útil cuando dos librerías de ML pelean por versiones distintas de la misma dependencia.

---

## 2. Gestión de versiones de Python

```bash
uv python list                 # versiones disponibles e instaladas
uv python install 3.12         # instala una versión concreta
uv python install 3.11 3.12 3.13   # varias a la vez
uv python pin 3.12             # fija la versión del proyecto (.python-version)
uv python find                 # muestra qué intérprete se está usando
uv python uninstall 3.11
```

Reemplaza a pyenv por completo, y descarga los binarios ya compilados (no compila nada, por eso tarda segundos).

---

## 3. Herramientas CLI (reemplazo de pipx)

Para instalar herramientas de línea de comandos aisladas del proyecto:

```bash
uvx ruff check .              # ejecuta SIN instalar (efímero)
uvx --from httpie http GET example.com

uv tool install ruff          # instala globalmente y de forma persistente
uv tool list
uv tool upgrade --all
uv tool uninstall ruff
```

`uvx` es un atajo de `uv tool run`. Es perfecto para probar una herramienta una sola vez sin ensuciar tu sistema.

---

## 4. Interfaz compatible con pip

Si necesitas control manual o estás migrando un proyecto viejo:

```bash
uv venv                        # crea .venv con el Python por defecto
uv venv --python 3.12          # con una versión específica
uv venv mi-entorno             # con otro nombre

uv pip install numpy           # como pip install, pero rapidísimo
uv pip install -r requirements.txt
uv pip install -e .            # instalación editable
uv pip uninstall numpy
uv pip list
uv pip freeze > requirements.txt
uv pip compile requirements.in -o requirements.txt   # como pip-tools
uv pip sync requirements.txt   # entorno exacto según el archivo
```

Ojo: `uv pip` **no actualiza `pyproject.toml` ni el lock**. Es una capa de compatibilidad de bajo nivel. En un proyecto nuevo, usa `uv add` en su lugar.

---

## 5. Scripts con dependencias en línea (PEP 723)

Esta es una de las funciones más elegantes de uv, y muy práctica para experimentos sueltos de la maestría:

```bash
uv init --script analisis.py --python 3.12
uv add --script analisis.py pandas matplotlib
uv run analisis.py
```

Esto inserta un bloque de metadatos en el propio archivo:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pandas",
#     "matplotlib",
# ]
# ///

import pandas as pd
import matplotlib.pyplot as plt
...
```

Ahora ese `.py` es **autocontenido**: cualquiera con uv lo ejecuta con `uv run analisis.py` y las dependencias se resuelven solas, sin proyecto ni entorno previo. Ideal para compartir un script de análisis por correo o Slack.

---

## 6. Publicación

```bash
uv build      # genera sdist y wheel en dist/
uv publish    # sube a PyPI
```

---

# Anatomía del `pyproject.toml`

```toml
[project]
name = "mi-proyecto"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "numpy>=2.0",
    "pandas>=2.2",
]

[project.optional-dependencies]
viz = ["matplotlib", "seaborn"]

[dependency-groups]
dev = ["pytest>=8.0", "ruff"]

[tool.uv]
package = false   # útil si es solo un conjunto de scripts, no una librería
```

Distinción importante:
- **`optional-dependencies`** (extras) — las ve quien instale tu paquete; se activan con `uv sync --extra viz`.
- **`dependency-groups`** — solo para desarrollo local, nunca se publican. `dev` se instala por defecto.

---

# Flujos de trabajo típicos

**Empezar un proyecto de IA desde cero:**

```bash
uv init tesis-ml && cd tesis-ml
uv python pin 3.12
uv add numpy pandas scikit-learn matplotlib
uv add --dev jupyter ruff pytest
uv run jupyter lab
```

**Clonar el proyecto de un compañero:**

```bash
git clone <repo> && cd <repo>
uv sync              # reconstruye el entorno idéntico desde uv.lock
uv run main.py
```

**Migrar un proyecto viejo con requirements.txt:**

```bash
cd proyecto-viejo
uv init --bare              # crea pyproject.toml sin tocar tus archivos
uv add -r requirements.txt  # importa las dependencias
uv sync
```

---

# Detalles que conviene tener claros

- **Qué versionar en Git**: sube `pyproject.toml`, `uv.lock` y `.python-version`. Ignora `.venv/`.
- **No necesitas activar el entorno**. `uv run` lo hace por ti. Si de todas formas quieres el prompt clásico, `source .venv/bin/activate` sigue funcionando porque `.venv` es un venv estándar.
- **`uv add` vs `uv pip install`**: el primero es declarativo (modifica `pyproject.toml` + lock); el segundo es imperativo y efímero. Mezclarlos genera entornos que no coinciden con el lock.
- **Caché**: `uv cache dir` te dice dónde vive; `uv cache clean` la limpia si necesitas espacio.
- **PyTorch con GPU**: uv soporta índices alternativos vía `[[tool.uv.index]]` en el `pyproject.toml`, lo que resuelve el clásico problema de instalar la build de CUDA correcta.

---

¿Quieres que reescriba tu nota [[UV]] con este contenido estructurado, o que arme una versión más corta tipo chuleta de comandos?
[Timestamp: 2026/08/17 20:06:23]

**user**: pero escribe en mi nota en formado md
[Timestamp: 2026/08/17 20:07:20]

**ai**: Voy a escribir la versión completa en tu nota UV.md.Listo, actualicé [[UV]] con la explicación completa en formato Markdown: qué es, por qué importa, instalación, y los comandos organizados por categoría (proyectos, versiones de Python, herramientas CLI, compatibilidad con pip, scripts PEP 723, publicación), más ejemplos de `pyproject.toml` y flujos de trabajo típicos.
[Timestamp: 2026/08/17 20:07:20]

**user**: en mi archivo quiero que me escribes como fucniona la estrutura denrto de uv y para que sirve cada cosa
[Timestamp: 2026/08/17 20:19:25]

**ai**: Voy a añadir una sección sobre la estructura de archivos/carpetas que genera y usa uv, explicando para qué sirve cada pieza.Voy a reemplazar ese bloque simple por una sección completa que explique la estructura entera del proyecto (incluyendo lo que aparece después de `uv add`, como `.venv` y `uv.lock`), con el propósito de cada archivo/carpeta.Añadí a [[UV]] la sección **"Para qué sirve cada pieza"**, justo después de `uv init`, que explica:

- La estructura completa del proyecto (antes y después del primer `uv add`).
- Qué hace cada archivo/carpeta: `pyproject.toml`, `uv.lock`, `.python-version`, `.venv/`, `main.py`, `README.md`.
- Un diagrama simple de cómo fluye la información entre `pyproject.toml` → `uv.lock` → `.venv/`, y qué comando mueve cada flecha.
- Cómo funciona la caché global fuera del proyecto (hardlinks).
[Timestamp: 2026/08/17 20:19:25]

**user**: y que es el init.py
[Timestamp: 2026/08/17 20:19:55]

**ai**: Buena pregunta — `__init__.py` no es algo de uv, es un mecanismo de **Python puro**, pero aparece cuando usas `uv init --lib`.No hay nada en tu vault sobre esto todavía. Te explico y lo agrego a la nota.

## ¿Qué es `__init__.py`?

Es un archivo especial de Python (no de uv) que le dice al intérprete: **"esta carpeta es un paquete importable, no solo una carpeta de archivos sueltos"**.

Aparece cuando usas:

```bash
uv init --lib mi-libreria
```

Que genera esta estructura:

```
mi-libreria/
├── src/
│   └── mi_libreria/
│       ├── __init__.py     # convierte la carpeta en un paquete
│       └── py.typed        # marca que el paquete tiene type hints
├── pyproject.toml
├── uv.lock
└── README.md
```

(con `uv init --app`, el modo por defecto, **no** se genera — porque una app no necesita ser importada por otros, solo ejecutarse).

### Para qué sirve

1. **Marca el paquete**: sin `__init__.py`, `import mi_libreria` fallaría (en versiones antiguas de Python; hoy existen los "namespace packages" que lo hacen opcional, pero uv sigue creándolo explícito por claridad y compatibilidad).
2. **Punto de entrada del paquete**: cuando alguien hace `import mi_libreria`, Python ejecuta ese `__init__.py`. Ahí puedes:
   - Exponer funciones/clases al nivel superior del paquete:
     ```python
     # mi_libreria/__init__.py
     from mi_libreria.core import mi_funcion

     __all__ = ["mi_funcion"]
     ```
     Así el usuario hace `from mi_libreria import mi_funcion` en vez de `from mi_libreria.core import mi_funcion`.
   - Definir la versión del paquete: `__version__ = "0.1.0"`.
3. **Puede estar vacío** — en la mayoría de los proyectos simplemente no contiene nada, y solo cumple el rol de "marcador de paquete".

### Por qué uv lo pone dentro de `src/`

Es el patrón llamado **"src layout"**: el código vive en `src/mi_libreria/` en vez de directamente en la raíz. Esto evita un bug clásico donde, al correr tests, Python importa accidentalmente el código desde la carpeta local sin pasar por la instalación real — lo que puede ocultar errores de empaquetado. uv lo usa por defecto en `--lib` porque es la práctica recomendada actual en el ecosistema Python.

¿Quieres que agregue esta explicación a tu nota [[UV]], en la sección de estructura?
[Timestamp: 2026/08/17 20:19:55]

**user**: pero agregalo en mi md
[Timestamp: 2026/08/17 20:20:37]

**ai**: Voy a insertar la nueva sección sobre `__init__.py` justo antes de "Añadir y quitar dependencias".Agregado a [[UV]] — nueva sección **`__init__.py` (cuando el proyecto es una librería)**, justo antes de "Añadir y quitar dependencias". Cubre cuándo aparece (`uv init --lib`), el src layout, para qué sirve, y por qué uv lo pone dentro de `src/`.
[Timestamp: 2026/08/17 20:20:37]

**user**: cuando usar uv init --lib              # proyecto pensado como librería (con src/)
uv init --app              # aplicación (opción por defecto)

casos de uso y agrega eso al md  y explica mejor la parte de init.py
[Timestamp: 2026/08/17 20:31:15]

**ai**: Voy a leer la nota actual para insertar bien las secciones.Ahora agrego, después de la lista de comandos `uv init`, una sección "¿Cuándo usar cada uno?" y reemplazo/expando la sección de `__init__.py` con una explicación más profunda.Ahora expando la sección de `__init__.py` con una explicación más completa y ejemplos concretos.Actualicé [[UV]] con dos mejoras:

1. **Nueva sección "`--app` vs `--lib`: cuándo usar cada uno"** — justo después de los comandos `uv init`, con casos de uso concretos para cada modo, una tabla comparativa, y una regla práctica (empezar por `--app` salvo que de verdad vayas a reutilizar el código como dependencia).

2. **Sección de `__init__.py` mucho más profunda** — ahora explica qué es un paquete en Python, qué pasa exactamente cuando se hace `import`, los 4 usos concretos (vacío, re-exportar/aplanar API, metadatos de versión, inicialización), el rol de `py.typed`, y por qué todo vive dentro de `src/`.
[Timestamp: 2026/08/17 20:31:15]