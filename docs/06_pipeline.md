# Diseño del pipeline  (módulo 07)

```
Pipeline
├── preprocesamiento (ColumnTransformer)
│   ├── numéricas: [variance, skewness, curtosis, entropy] → StandardScaler
│   ├── categóricas: ninguna
│   └── ordinales: ninguna
└── modelo: CalibratedClassifierCV(SVC(kernel="rbf"), ensemble=False)
```

## Decisiones de diseño

- **Todo el procesamiento está dentro del `Pipeline`.** El escalado se ajusta solo con los datos de entrenamiento de cada partición, así que no hay fuga de información.
- **Partición:** 80 % entrenamiento y 20 % prueba, estratificada, con `random_state=42`.
- **Selección:** validación cruzada estratificada de 5 folds solo sobre el entrenamiento. El conjunto de prueba se usa una vez con el modelo elegido.
- **Modelo final:** el modelo elegido se reentrena con todos los datos limpios y se guarda en `models/modelo.joblib` para la API.
- **Probabilidades calibradas:** `SVC` no da probabilidades fiables por sí solo. Se envuelve en `CalibratedClassifierCV` para que la API devuelva la probabilidad de que el billete sea falso.

## Cómo entrenar

```bash
uv sync
uv run python -m src.train
```

Genera en `models/` (carpeta que no se sube a Git):
- `modelo.joblib`: el pipeline entrenado.
- `metricas.json`: modelo elegido y métricas en test.
- `cv_resultados.csv`: la tabla comparativa de validación cruzada.
