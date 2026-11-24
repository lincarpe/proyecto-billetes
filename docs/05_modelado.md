# Modelado  (módulo 06)

Código: `src/pipeline.py` (modelos) y `src/train.py` (comparación, evaluación y guardado).

## Tipo de problema y métrica principal (y por qué)

Clasificación binaria (0 = auténtico, 1 = falso). La métrica principal es el **recall de la clase falso**: aceptar un billete falso es lo más costoso. Se vigilan también la precisión sobre los rechazos y la tasa de rechazo de billetes buenos, que son los KPI del charter. Para elegir entre modelos se usa el **F1 de la clase falso**, que equilibra recall y precisión.

## Comparación (baseline vs. modelos)

Validación cruzada estratificada de 5 folds sobre el conjunto de entrenamiento (1078 billetes, 80 %). Semilla fija: 42.

| Modelo | Exactitud | Recall (falso) | Precisión (falso) | F1 (falso) |
|---|---|---|---|---|
| Baseline: siempre "auténtico" | 0,547 | 0,000 | 0,000 | 0,000 |
| Baseline: regresión logística solo con `variance` | 0,848 | 0,826 | 0,836 | 0,831 |
| Regresión logística | 0,994 | 0,998 | 0,990 | 0,994 |
| k vecinos (k = 5) | 0,994 | 1,000 | 0,988 | 0,994 |
| **SVM con kernel RBF** | **0,999** | **1,000** | **0,998** | **0,999** |
| SVM RBF sin `entropy` | 0,996 | 1,000 | 0,992 | 0,996 |
| Random forest | 0,992 | 0,998 | 0,984 | 0,991 |
| Gradient boosting | 0,989 | 0,994 | 0,982 | 0,988 |

Todos los modelos superan con mucha diferencia a ambos *baselines*. Un solo atributo (`variance`) ya da un F1 de 0,83, pero queda lejos de los modelos con las 4 variables.

## Modelo elegido y justificación

**SVM con kernel RBF** (escalado de las variables dentro del pipeline y probabilidades calibradas). Tiene el mejor F1 en validación cruzada y es el único con recall 1,000 y precisión por encima de 0,997. Las diferencias con k vecinos y regresión logística son pequeñas, así que cualquiera de los tres sería razonable. Se prefiere el SVM por el mejor F1 y porque la frontera entre clases es no lineal.

Sobre `entropy`: el EDA sugería que casi no aportaba, pero quitarla baja el F1 del SVM de 0,999 a 0,996. Aporta algo en combinación con las otras variables, así que se conserva.

## Métrica en test (una sola vez)

Conjunto de prueba: 270 billetes (20 %), usado una sola vez con el modelo ya elegido y entrenado solo con el conjunto de entrenamiento.

| Métrica | Resultado | Meta del charter |
|---|---|---|
| Recall (falso) | 1,000 | ≥ 0,99 |
| Precisión sobre los rechazos | 1,000 | ≥ 0,97 |
| Tasa de rechazo de billetes buenos | 0,000 | ≤ 0,02 |
| Exactitud | 1,000 | Baseline 0,547 |

Matriz de confusión: 148 auténticos bien clasificados, 122 falsos bien clasificados, 0 errores. Se cumplen las tres metas de los KPI.

## Análisis de errores y límites

- **El resultado perfecto en test no significa que el modelo sea perfecto.** Con 270 billetes, un 100 % es compatible con una tasa real de error de hasta cerca del 1 %. La validación cruzada (exactitud 0,999) es una estimación más estable: equivale a unos 1 error cada 1000 billetes.
- **Las clases están muy separadas** en este dataset, por eso todos los modelos serios rinden bien. Es una característica de los datos, no un mérito especial del SVM.
- **Alcance de los datos:** las características vienen de un único conjunto de imágenes de billetes. No sabemos cómo se comportaría el modelo con otro tipo de billete, otra cámara u otras condiciones de iluminación. Antes de usarlo de verdad habría que validarlo con datos nuevos.
- **Los falsos del dataset** son de un tipo concreto de falsificación. Un método de falsificación distinto podría quedar fuera de lo aprendido.
- **Costos asimétricos:** si aceptar un billete falso cuesta mucho más que rechazar uno bueno, se puede bajar el umbral de probabilidad de rechazo. Así se gana recall a cambio de más rechazos de billetes buenos.
