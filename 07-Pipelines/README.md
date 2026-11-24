# 07 · Pipelines

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué es un pipeline

Es una cadena de pasos dentro de un solo objeto. Aquí son dos:

1. **Escalar** las 4 medidas del billete (`StandardScaler`).
2. **Aplicar el modelo** (SVM con kernel RBF, con probabilidades calibradas).

Sirve para que el escalado se aprenda solo con los datos de entrenamiento, sin filtrar información de los datos de prueba (*data leakage*). Además, el mismo objeto se usa luego en la API, así que un billete nuevo se procesa igual que los de entrenamiento.

## Qué se hizo

- Partición 80 % entrenamiento y 20 % prueba, estratificada, con semilla 42.
- Selección con validación cruzada solo sobre el entrenamiento. El conjunto de prueba se usa una sola vez.
- El modelo elegido se reentrena con todos los datos limpios y se guarda como pipeline en `models/modelo.joblib`.

## Dónde está

| Qué | Dónde |
|---|---|
| Función `construir` (el pipeline) y los 8 candidatos | [`src/pipeline.py`](../src/pipeline.py) |
| Entrenamiento y guardado | [`src/train.py`](../src/train.py) |
| Decisiones de diseño | [`docs/06_pipeline.md`](../docs/06_pipeline.md) |

## Cómo ejecutarlo

```bash
uv run python -m src.train   # genera models/modelo.joblib, metricas.json y cv_resultados.csv
```

La carpeta `models/` se genera al entrenar y no se sube a Git.
