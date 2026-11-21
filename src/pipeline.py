"""Datos, partición y pipelines de scikit-learn para clasificar billetes."""

import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from src.limpieza import FEATURES, TARGET, cargar_raw, limpiar

SEED = 42
FEATURES_SIN_ENTROPY = ["variance", "skewness", "curtosis"]


def cargar_datos() -> tuple[pd.DataFrame, pd.Series]:
    """Devuelve X, y a partir de los datos crudos limpios (no depende de archivos generados)."""
    df = limpiar(cargar_raw())
    return df[FEATURES], df[TARGET]


def partir(X: pd.DataFrame, y: pd.Series):
    """80 % entrenamiento / 20 % prueba, estratificado y con semilla fija."""
    return train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)


def construir(modelo, columnas: list[str] | None = None) -> Pipeline:
    """Pipeline: selecciona columnas, escala dentro del pipeline (sin fuga) y aplica el modelo."""
    columnas = columnas or FEATURES
    pre = ColumnTransformer([("escala", StandardScaler(), columnas)], remainder="drop")
    return Pipeline([("pre", pre), ("modelo", modelo)])


def _svm():
    """SVM con kernel RBF y probabilidades calibradas (para que la API pueda devolverlas)."""
    return CalibratedClassifierCV(SVC(kernel="rbf"), ensemble=False)


def candidatos() -> dict[str, Pipeline]:
    """Modelos a comparar. Los dos primeros son los baselines."""
    return {
        "baseline_mayoritaria": construir(DummyClassifier(strategy="most_frequent")),
        "baseline_solo_variance": construir(LogisticRegression(random_state=SEED), ["variance"]),
        "regresion_logistica": construir(LogisticRegression(random_state=SEED, max_iter=1000)),
        "knn": construir(KNeighborsClassifier(n_neighbors=5)),
        "svm_rbf": construir(_svm()),
        "svm_rbf_sin_entropy": construir(_svm(), FEATURES_SIN_ENTROPY),
        "random_forest": construir(RandomForestClassifier(n_estimators=200, random_state=SEED)),
        "gradient_boosting": construir(GradientBoostingClassifier(random_state=SEED)),
    }
