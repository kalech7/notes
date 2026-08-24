**es una herramienta moderna para gestionar proyectos de Python.** Sirve para crear entornos virtuales, instalar dependencias, manejar versiones de Python y mantener las librerías del proyecto organizadas y reproducibles.

> [!info] Lugar de esta nota en el grafo del posgrado
> `uv` es la base de ejecución para las demás notas: [[Estructuras de Python en un experimento de IA]], [[Programación orientada a objetos aplicada a Machine Learning]], [[numpy pandas parquet arrow]] y [[funcion de perdida]]. Para estudiar POO por sesiones, entra por [[poo ia/00 Índice - POO e IA]].

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

En macOS:

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

### `--app` vs `--lib`: cuándo usar cada uno

La pregunta clave para decidir es: **¿alguien más va a hacer `import` de este código, o solo se va a ejecutar?**

**`--app`** (o simplemente `uv init`, es el default) — úsalo cuando el proyecto es algo que **se ejecuta**, no algo que otros importan como dependencia:
- Un pipeline de entrenamiento o script de análisis para tu tesis/maestría.
- Una app web (FastAPI, Flask, Streamlit).
- Un bot, un cron job, un notebook de experimentos.
- Cualquier "proyecto final" que corres con `uv run main.py`.

El código vive suelto en la raíz del proyecto y uv no se preocupa por empaquetarlo para distribución.

**`--lib`** — úsalo cuando el objetivo es que el código sea **reutilizable e importable** desde otros proyectos:
- Una librería propia que vas a instalar en varios de tus proyectos de la maestría (ej. funciones de preprocesamiento que reusas en cada tarea).
- Algo que planeas publicar en PyPI con `uv publish`.
- Un paquete interno de un equipo que se comparte entre varios repositorios/microservicios.

Genera automáticamente el **src layout** (`src/nombre_paquete/`), incluye `__init__.py` y `py.typed`, y configura `pyproject.toml` para que el paquete sea instalable (`pip install .` o `uv add ../mi-libreria` desde otro proyecto funcionan).

| Pregunta | `--app` | `--lib` |
| --- | --- | --- |
| ¿Se ejecuta directamente (`uv run main.py`)? | Sí | No, se importa |
| ¿Otros proyectos harán `import` de este código? | No | Sí |
| ¿Se va a publicar en PyPI? | No | Sí (opcional) |
| ¿Usa src layout con `__init__.py`? | No | Sí |
| Ejemplo típico | script de entrenamiento, app, notebook | librería de utilidades compartidas |

> Regla práctica: si dudas, empieza con `--app`. Es más simple y es lo que necesitas la mayoría de las veces en trabajos de maestría/tareas. Cambia a `--lib` solo cuando de verdad vayas a reutilizar ese código como dependencia de otro proyecto.

`uv init` genera esta estructura inicial:

```
mi-proyecto/
├── .python-version      # versión de Python fijada para el proyecto
├── README.md
├── main.py
└── pyproject.toml       # declaración de dependencias y metadatos
```

Y en cuanto ejecutas el primer `uv add` o `uv sync`, uv añade tres piezas más:

```
mi-proyecto/
├── .venv/                # entorno virtual real (intérprete + paquetes instalados)
├── .python-version       # versión de Python fijada para el proyecto
├── README.md
├── main.py
├── pyproject.toml        # qué dependencias quieres (declarativo, lo editas tú)
└── uv.lock                # qué dependencias EXACTAS se instalaron (lo genera uv, no lo tocas)
```

### Para qué sirve cada pieza

- **`pyproject.toml`** — el corazón del proyecto. Aquí declaras el nombre, la versión, los requisitos de Python y las dependencias (`[project]`, `[project.optional-dependencies]`, `[dependency-groups]`). Es el único archivo que editas a mano (aunque normalmente lo hace `uv add`/`uv remove` por ti). Define **qué quieres**, no versiones exactas cerradas.

- **`uv.lock`** — el archivo de bloqueo. Contiene la resolución exacta y reproducible de *todas* las dependencias (incluidas las transitivas), con hashes, para cualquier sistema operativo y versión de Python compatibles. Es multiplataforma: el mismo `uv.lock` sirve tanto en tu Mac como en un servidor Linux. **Nunca lo edites a mano** — se regenera con `uv lock` o automáticamente al hacer `uv add`. Este es el archivo que garantiza que tú y un compañero de maestría tengan exactamente las mismas versiones instaladas.

- **`.python-version`** — un archivo de una sola línea (ej. `3.12`) que fija qué versión de Python usa el proyecto. Cuando ejecutas `uv run` o `uv sync`, uv lee este archivo y usa (o instala) esa versión automáticamente, sin que tengas que activar nada manualmente.

- **`.venv/`** — el entorno virtual real: el intérprete de Python y todos los paquetes instalados físicamente (via hardlinks desde la caché global). Es un venv estándar de Python, así que herramientas externas (VS Code, Jupyter) lo reconocen sin problema. **No se versiona en Git** — se reconstruye desde cero con `uv sync` a partir del `uv.lock`.

- **`main.py`** — el punto de entrada del proyecto que crea `uv init` por defecto; puedes borrarlo o renombrarlo, no tiene nada especial para uv.

- **`README.md`** — documentación estándar, sin relación con uv.

### La relación entre los tres archivos clave

```
pyproject.toml  →  "quiero numpy y pandas"           (lo escribes/editas tú)
       ↓  uv lock
uv.lock         →  "numpy 2.1.3, pandas 2.2.1, +47 dependencias transitivas..."  (lo genera uv)
       ↓  uv sync
.venv/          →  numpy y pandas instalados físicamente, listos para importar
```

Cada comando mueve el flujo en una dirección:
- **`uv add paquete`** → edita `pyproject.toml`, actualiza `uv.lock` e instala en `.venv/`, los tres pasos a la vez.
- **`uv lock`** → recalcula `uv.lock` a partir de `pyproject.toml`, sin tocar `.venv/`.
- **`uv sync`** → instala en `.venv/` exactamente lo que dice `uv.lock`, sin tocar `pyproject.toml`.

### Caché global (fuera del proyecto)

Además de estos archivos del proyecto, uv mantiene una **caché global** en el sistema (consultable con `uv cache dir`) donde guarda una sola copia de cada paquete descargado. Cuando `.venv/` "instala" un paquete, en realidad crea un *hardlink* hacia esa caché — por eso instalar es casi instantáneo y no duplica espacio en disco entre proyectos.

### `__init__.py` en detalle (cuando el proyecto es una librería)

No es un archivo de uv, sino un mecanismo de **Python puro** — uv simplemente lo genera automáticamente cuando el proyecto es una librería:

```bash
uv init --lib mi-libreria
```

que produce esta estructura (el llamado **"src layout"**):

```
mi-libreria/
├── src/
│   └── mi_libreria/
│       ├── __init__.py     # convierte la carpeta en un paquete importable
│       └── py.typed        # marca que el paquete tiene type hints
├── pyproject.toml
├── uv.lock
└── README.md
```

Con `uv init --app` (el modo por defecto) **no aparece**, porque una app se ejecuta directamente con `uv run` y nadie necesita hacerle `import`.

#### ¿Qué es exactamente un "paquete" en Python?

Un **módulo** es un solo archivo `.py`. Un **paquete** es una carpeta que agrupa varios módulos y se puede importar como una unidad (`import mi_libreria`). Lo que convierte a una carpeta cualquiera en un paquete es, precisamente, que contenga un `__init__.py`. Sin él, Python (en versiones modernas) puede tratarla como "namespace package" de forma implícita, pero es ambiguo y frágil — por eso la convención es siempre incluirlo explícitamente.

#### Qué pasa cuando haces `import`

Cuando escribes `import mi_libreria` en cualquier parte, Python:
1. Busca la carpeta `mi_libreria/`.
2. Ejecuta **todo el contenido de `mi_libreria/__init__.py`** de arriba a abajo, una sola vez (y lo cachea).
3. Lo que haya quedado definido en ese archivo (variables, funciones, clases, imports) queda disponible como atributos de `mi_libreria`.

Por eso es literalmente el **punto de entrada** del paquete: es el único código que se garantiza que corre siempre que alguien importa tu librería, sin importar qué submódulo use.

#### Usos concretos

**1. Vacío (el caso más común)** — simplemente marca la carpeta como paquete, no expone nada especial:

```python
# src/mi_libreria/__init__.py
```

El usuario tiene que conocer la ruta completa: `from mi_libreria.preprocesamiento import limpiar_texto`.

**2. Re-exportar (aplanar la API pública)** — esconde la estructura interna de carpetas para dar una interfaz más simple:

```python
# src/mi_libreria/__init__.py
from mi_libreria.preprocesamiento import limpiar_texto
from mi_libreria.modelos import entrenar_modelo

__all__ = ["limpiar_texto", "entrenar_modelo"]
```

Así, quien use tu librería escribe simplemente:
```python
from mi_libreria import limpiar_texto, entrenar_modelo
```
en vez de tener que saber que `limpiar_texto` vive en `mi_libreria.preprocesamiento`. `__all__` además controla qué se importa con `from mi_libreria import *`.

**3. Metadatos del paquete** — versión, autor, etc.:

```python
# src/mi_libreria/__init__.py
__version__ = "0.1.0"
```

Útil para que otro código (o tú mismo) pueda hacer `mi_libreria.__version__` en runtime.

**4. Inicialización real** (menos común, úsalo con cuidado) — configurar logging, cargar constantes, registrar plugins. Como se ejecuta una sola vez al primer `import`, es un lugar válido para setup global, pero abusar de esto puede generar efectos secundarios sorprendentes solo por importar el paquete.

#### `py.typed` (el archivo vecino)

Junto a `__init__.py`, `uv init --lib` también crea un archivo vacío `py.typed`. Es una convención de [PEP 561](https://peps.python.org/pep-0561/) que le dice a herramientas como `mypy` o `pyright`: "este paquete tiene type hints propios, revísalos" — sin él, otros proyectos que te importen no obtendrían autocompletado/chequeo de tipos desde tu librería.

#### Por qué todo esto vive dentro de `src/` y no en la raíz

Es el "src layout", la práctica recomendada actual en Python. Evita un bug clásico donde, al correr tests o importar el paquete durante desarrollo, Python encuentra primero la carpeta local del repo (porque el directorio actual siempre está en el `sys.path`) en vez de la versión realmente **instalada** en `.venv/` — lo que puede ocultar errores de empaquetado que solo aparecerían al publicar la librería de verdad. Poner el código un nivel más adentro (`src/mi_libreria/` en vez de `mi_libreria/` en la raíz) fuerza a que siempre se importe la copia instalada, detectando esos problemas antes. uv usa este layout por defecto con `--lib`.

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

**`uv run` es el comando que más vas a usar.** Antes de ejecutar, verifica que el entorno esté sincronizado con el lock, así que nunca trabajas con un entorno desactualizado. Como consecuencia, **ya no necesitas `source .venv/bin/activate`**.

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

Una de las funciones más elegantes de uv, y muy práctica para experimentos sueltos de la maestría:

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

Ese `.py` queda **autocontenido**: cualquiera con uv lo ejecuta con `uv run analisis.py` y las dependencias se resuelven solas, sin proyecto ni entorno previo. Ideal para compartir un script de análisis por correo o Slack.

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

