# 06 · Modelado y métricas

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué se hizo

Se comparó contra dos baselines y se evaluaron 6 modelos con validación cruzada estratificada de 5 folds (semilla 42). La métrica principal es el **recall de la clase falso**, porque aceptar un billete falso es lo más costoso. Para elegir entre modelos se usó el F1 de esa clase.

| Modelo | F1 (falso) en validación cruzada |
|---|---|
| Baseline: siempre "auténtico" | 0,000 |
| Baseline: regresión logística solo con `variance` | 0,831 |
| Regresión logística | 0,994 |
| k vecinos | 0,994 |
| **SVM con kernel RBF (elegido)** | **0,999** |
| Random forest | 0,991 |
| Gradient boosting | 0,988 |

## Resultado en test (usado una sola vez)

Con 270 billetes: recall de falsos 1,00, precisión 1,00 y 0 % de billetes buenos rechazados.

**Límite:** un 100 % con 270 billetes no significa que el modelo sea perfecto. Las clases están muy separadas en este dataset y no se sabe cómo se comportaría con otro tipo de billete u otra cámara.

## Dónde está

| Qué | Dónde |
|---|---|
| Modelos candidatos | [`src/pipeline.py`](../src/pipeline.py) |
| Comparación, test y guardado del modelo | [`src/train.py`](../src/train.py) |
| Notebook de baselines y comparación | [`notebooks/06_modelado.ipynb`](../notebooks/06_modelado.ipynb) |
| Resultados, justificación y límites | [`docs/05_modelado.md`](../docs/05_modelado.md) |
