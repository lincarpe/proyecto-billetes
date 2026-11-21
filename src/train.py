"""Entrena y compara modelos, evalúa el elegido en test (una sola vez) y lo guarda.

Uso:  uv run python -m src.train
"""

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import confusion_matrix, f1_score, make_scorer, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold, cross_validate

from src.pipeline import SEED, candidatos, cargar_datos, partir

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
SCORING = {
    "accuracy": "accuracy",
    "recall": make_scorer(recall_score, zero_division=0),
    "precision": make_scorer(precision_score, zero_division=0),
    "f1": make_scorer(f1_score, zero_division=0),
}


def comparar(X_train, y_train) -> pd.DataFrame:
    """Validación cruzada estratificada (5 folds) solo con los datos de entrenamiento."""
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    filas = []
    for nombre, pipe in candidatos().items():
        r = cross_validate(pipe, X_train, y_train, cv=cv, scoring=SCORING)
        filas.append({"modelo": nombre, **{m: r[f"test_{m}"].mean() for m in SCORING}})
    return pd.DataFrame(filas).sort_values("f1", ascending=False).reset_index(drop=True)


def metricas_test(pipe, X_test, y_test) -> dict:
    pred = pipe.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
    return {
        "accuracy": float((pred == y_test).mean()),
        "recall_falso": float(recall_score(y_test, pred)),
        "precision_falso": float(precision_score(y_test, pred)),
        "f1_falso": float(f1_score(y_test, pred)),
        "tasa_rechazo_billetes_buenos": float(fp / (fp + tn)),
        "matriz": {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp)},
        "n_test": int(len(y_test)),
    }


def main() -> None:
    X, y = cargar_datos()
    X_train, X_test, y_train, y_test = partir(X, y)

    tabla = comparar(X_train, y_train)
    print(tabla.round(4).to_string(index=False))

    # Se elige por F1 en validación cruzada entre los modelos que no son baseline.
    elegido = tabla[~tabla["modelo"].str.startswith("baseline")].iloc[0]["modelo"]
    pipe = candidatos()[elegido].fit(X_train, y_train)

    # El conjunto de prueba se usa UNA sola vez, con el modelo ya elegido.
    resultado = {"modelo_elegido": elegido, "semilla": SEED, "test": metricas_test(pipe, X_test, y_test)}
    print("\nModelo elegido:", elegido)
    print(json.dumps(resultado["test"], indent=2))

    # Para producción, el modelo final se reentrena con todos los datos.
    final = candidatos()[elegido].fit(X, y)
    MODELS_DIR.mkdir(exist_ok=True)
    joblib.dump(final, MODELS_DIR / "modelo.joblib")
    tabla.to_csv(MODELS_DIR / "cv_resultados.csv", index=False)
    (MODELS_DIR / "metricas.json").write_text(
        json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nGuardado en {MODELS_DIR}")


if __name__ == "__main__":
    main()
