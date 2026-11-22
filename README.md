# Autenticación de billetes falsos

> Clasificar si un billete es auténtico o falso a partir de características extraídas de su imagen.

## Equipo

| Integrante | Rol principal | GitHub |
|---|---|---|
| Lina Marcela Carvajal Perez (equipo de una persona) | Datos, EDA, modelado y API | @lincarpe |

## Problema de negocio

_(se completa en el módulo 02)_

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
├── data/raw/          ← datos originales
├── data/processed/    ← datos limpios (generados)
├── docs/              ← problema, charter, decisiones
├── notebooks/         ← exploración
├── src/               ← código reutilizable (limpieza, train, api)
└── models/            ← modelos entrenados (generados)
```

## Avance

- [x] 00 Entorno con uv
- [ ] 01 Repositorio en GitHub
- [x] 02 Problema y KPIs
- [x] 03 Project charter
- [x] 04 Limpieza
- [x] 05 EDA
- [x] 06 Baseline
- [x] 07 Pipeline de entrenamiento
- [x] 08 API
- [ ] 09 Entrega final
