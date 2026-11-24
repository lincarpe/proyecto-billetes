# CLASIFICACIÓN DE BILLETES AUTENTICOS Y FALSOS

> Clasificar si un billete es auténtico o falso a partir de características extraídas de su imagen.

## Equipo

| Integrante | Rol principal | GitHub |
|---|---|---|
| Lina Marcela Carvajal Perez (equipo de una persona) | Datos, EDA, modelado y API | @lincarpe |

## Problema de negocio

Quien opera un cajero automático, una máquina de conteo o una caja de un comercio decide si acepta o rechaza un billete. Rechazar uno bueno molesta al cliente. Aceptar uno falso es una pérdida directa de dinero y un problema legal. El proyecto clasifica cada billete como auténtico o falso a partir de 4 características de su imagen, priorizando detectar los falsos. Detalle y KPIs en [`docs/01_problema_y_kpis.md`](docs/01_problema_y_kpis.md).

## Dataset

- **Nombre:** Banknote Authentication
- **Fuente:** UCI Machine Learning Repository, https://archive.ics.uci.edu/dataset/267/banknote+authentication
- **Tamaño:** 1372 filas × 5 columnas (46 KB)
- **Variables:** 4 numéricas extraídas de imágenes de billetes (varianza, asimetría, curtosis y entropía de la transformada wavelet) y la clase.
- **Variable objetivo:** clase (0 = auténtico, 1 = falso)
- **Ubicación:** `data/raw/banknote/data_banknote_authentication.txt` (sin encabezados)

## Cómo ejecutar

```bash
uv sync
uv run python -m src.limpieza     # genera data/processed/billetes_limpio.csv
uv run python -m src.train        # compara modelos y guarda models/modelo.joblib
uv run uvicorn api.main:app       # levanta la API en http://127.0.0.1:8000/docs
uv run pytest                     # pruebas de la API
uv run jupyter lab                # notebooks de EDA y modelado
```

## API

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/health` | Estado de la API y si el modelo está cargado |
| GET | `/model-info` | Metadata del modelo: cuál es y qué métricas obtuvo en test |
| POST | `/predict/batch` | Igual que `/predict` pero recibe una lista de hasta 100 billetes |
| POST | `/predict` | Recibe `variance`, `skewness`, `curtosis` y `entropy`; devuelve la clase, la probabilidad de que sea falso y si hay que aceptar o rechazar el billete |

Ejemplo:

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json"   -d '{"variance": -1.3971, "skewness": 3.3191, "curtosis": -1.3927, "entropy": -1.9948}'
```

Respuesta: `{"clase": 1, "etiqueta": "falso", "probabilidad_falso": 0.9946, "accion": "rechazar"}`

## Resultados

Modelo: SVM con kernel RBF. En validación cruzada, exactitud 0,999. En test (270 billetes): recall de falsos 1,00, precisión 1,00 y 0 % de billetes buenos rechazados. Con tan pocos datos de prueba esto no significa que el modelo sea perfecto; ver límites en `docs/05_modelado.md`.

## Estructura

```
proyecto-billetes/
├── README.md                    ← este archivo
├── 00-Entornos-uv/ … 09-Proyecto-Final/   ← un índice por módulo del curso (enlazan al código y a docs/)
├── pyproject.toml, uv.lock      ← dependencias y versiones exactas (uv, Python 3.14)
├── api/
│   └── main.py                  ← API FastAPI: /health, /model-info, /predict, /predict/batch
├── data/
│   ├── raw/banknote/            ← dataset original (no se modifica)
│   └── processed/               ← datos limpios (se generan)
├── docs/                        ← un documento por etapa del proyecto
│   ├── 00_entorno_uv.md
│   ├── 01_problema_y_kpis.md
│   ├── 02_project_charter.md
│   ├── 03_decisiones_limpieza.md
│   ├── 04_eda.md
│   ├── 05_modelado.md
│   └── 06_pipeline.md
├── models/                      ← modelo entrenado y métricas (se generan)
├── notebooks/
│   ├── 05_eda.ipynb             ← análisis exploratorio
│   └── 06_modelado.ipynb        ← baselines y comparación de modelos
├── src/
│   ├── limpieza.py              ← limpieza de datos
│   ├── pipeline.py              ← preprocesamiento y candidatos de modelo
│   └── train.py                 ← entrena, evalúa en test y guarda el modelo
├── tests/
│   └── test_api.py              ← pruebas de la API
└── .github/
    └── pull_request_template.md
```

## Avance

| Módulo | Punto | Estado | Documento |
|---|---|---|---|
| [00](00-Entornos-uv/) | Entorno con uv | hecho | [`docs/00_entorno_uv.md`](docs/00_entorno_uv.md) |
| [01](01-Git-GitHub/) | Repositorio en GitHub | hecho | este repositorio |
| [02](02-BI-Analitica/) | Problema y KPIs | hecho | [`docs/01_problema_y_kpis.md`](docs/01_problema_y_kpis.md) |
| [03](03-CRISP-DM/) | Project charter | hecho | [`docs/02_project_charter.md`](docs/02_project_charter.md) |
| [04](04-Preparacion-Datos/) | Limpieza | hecho | [`docs/03_decisiones_limpieza.md`](docs/03_decisiones_limpieza.md) |
| [05](05-EDA/) | EDA | hecho | [`docs/04_eda.md`](docs/04_eda.md) |
| [06](06-Modelado-Metricas/) | Baseline y modelado | hecho | [`docs/05_modelado.md`](docs/05_modelado.md) |
| [07](07-Pipelines/) | Pipeline de entrenamiento | hecho | [`docs/06_pipeline.md`](docs/06_pipeline.md) |
| [08](08-API-FastAPI/) | API | hecho | sección "API" de este README |
| [09](09-Proyecto-Final/) | Entrega final | pendiente | |
