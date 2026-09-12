# Detección de Suplantación de Identidad mediante Dinámica de Mouse

Proyecto de la asignatura **Matemáticas y Programación para IA** (Máster en Inteligencia Artificial).

Este paquete contiene la implementación reproducible, análisis experimental, notebooks interactivos y el informe técnico en PDF para la autenticación biométrica continua basada en dinámica de mouse sobre el benchmark Balabit Mouse Dynamics Challenge.

---

## Contenido del Proyecto

- `01_proyecto_dinamica_mouse.ipynb`: Notebook principal con el pipeline completo para los 10 usuarios del dataset (ingesta, inspección cinemática, extracción de 17 características, baseline y modelo de detección de anomalías Isolation Forest, curvas FAR/FRR/EER y evaluación macro/micro).
- `02_analisis_un_usuario_y_funcion_perdida.ipynb`: Estudio detallado sobre `user12` enfocado en detección temprana (ventanas de 25 a 150 eventos), estabilidad temporal, análisis de importancia de características y calibración mediante función de pérdida con umbrales operacionales.
- `proyecto.pdf`: Documento técnico e informe final del proyecto.
- `El_rastro_invisible.pdf`: Documento complementario sobre el estudio ("El rastro invisible").
- `src/mouse_auth/`: Paquete modular con utilidades de extracción geométrica/cinemática, métricas biométricas y pipeline.
- `tests/`: Batería de pruebas unitarias sobre invarianza de traslación, consistencia temporal y métricas.
- `pyproject.toml` y `uv.lock`: Configuración del entorno reproducible gestionado con `uv`.
- `data/`: Directorio para los datos del benchmark Balabit (`public_labels.csv`, `training_files`, `test_files`).

---

## Requisitos y Configuración con `uv`

El proyecto utiliza [`uv`](https://docs.astral.sh/uv/) como gestor rápido y determinista de entornos y dependencias de Python (compatible con Python >= 3.11).

### 1. Instalar `uv` (si aún no está instalado)

- **macOS / Linux**:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Windows (PowerShell)**:
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
- **Con Homebrew (macOS)**:
  ```bash
  brew install uv
  ```

### 2. Sincronizar el entorno virtual y dependencias

Desde el directorio del proyecto, ejecuta:

```bash
uv sync
```

Esto descargará las dependencias fijadas en `uv.lock` y configurará automáticamente el entorno virtual (`.venv`) con Jupyter, IPython Kernel, Pandas, Scikit-Learn, Seaborn y Matplotlib.

---

## Cómo Ejecutar los Notebooks

Puedes interactuar con los notebooks de tres formas:

### Opción A: JupyterLab (Recomendado)
```bash
uv run jupyter lab
```

### Opción B: Jupyter Notebook clásico
```bash
uv run jupyter notebook
```

### Opción C: VS Code / Cursor / PyCharm
1. Abre la carpeta del proyecto en el editor.
2. Abre cualquiera de los dos notebooks (`01` o `02`).
3. En la esquina superior derecha, selecciona el kernel de Python apuntando al entorno virtual del proyecto (`.venv/bin/python` en macOS/Linux o `.venv\Scripts\python.exe` en Windows).

---

## Ejecución del Baseline y Tests desde CLI

- **Ejecutar pruebas unitarias**:
  ```bash
  uv run python -m unittest discover tests
  ```

- **Ejecutar el pipeline baseline completo y generar reportes**:
  ```bash
  uv run python run_baseline.py --data data --output reports
  ```
