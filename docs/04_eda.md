# Hallazgos del EDA  (módulo 05)

Notebook: `notebooks/05_eda.ipynb` (datos limpios: 1348 filas).

| # | Hallazgo | Evidencia | Implicación para el modelo |
|---|---|---|---|
| 1 | `variance` es la variable que mejor separa las clases: los billetes falsos tienen varianza baja o negativa y los auténticos, positiva | Media 2,36 en auténticos y −1,87 en falsos. Correlación con la clase de −0,74 | Debe ser la variable principal. Un modelo solo con `variance` ya sería un buen *baseline* |
| 2 | `skewness` ayuda a separar; `curtosis` aporta poco y `entropy` casi nada | Correlación con la clase: `skewness` −0,45, `curtosis` 0,15, `entropy` −0,03 | `entropy` podría descartarse sin perder rendimiento. Se comprueba al modelar |
| 3 | Con `variance` y `skewness` las clases forman dos nubes casi separables | Gráfico de dispersión `variance` vs `skewness` | Se esperan métricas muy altas, incluso con modelos simples. Hay que evitar el *data leakage* y no sorprenderse por valores cercanos a 1 |
| 4 | Hay valores atípicos solo en `curtosis` (59) y `entropy` (32) | Regla 1,5·IQR. `variance` y `skewness` no tienen | Se conservan: son mediciones reales. Se prefiere un modelo robusto o con escalado |

## Hipótesis del charter

| Hipótesis | Resultado (Confirmada / Rechazada / No concluyente) | Evidencia |
|---|---|---|
| Las 4 características separan los billetes falsos de los auténticos | **Parcialmente confirmada** | Solo `variance` y `skewness` separan claramente. `entropy` casi no aporta |
| Un modelo puede alcanzar recall ≥ 0,99 en la clase falso | **No concluyente** | Se comprueba en el módulo 06, con el conjunto de prueba |
| El dataset está balanceado y no necesita remuestreo | **Confirmada** | 738 auténticos (54,7 %) y 610 falsos (45,3 %) |

## Variables candidatas / descartadas

| Variable | Decisión | Motivo |
|---|---|---|
| `variance` | Candidata | La mejor separadora |
| `skewness` | Candidata | Segunda mejor separadora |
| `curtosis` | Candidata | Aporta poco por sí sola, pero puede ayudar combinada |
| `entropy` | Candidata dudosa | Casi sin relación con la clase. Se decide al comparar modelos con y sin ella |
