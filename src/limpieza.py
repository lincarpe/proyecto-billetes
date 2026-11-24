"""Carga y limpieza del dataset Banknote Authentication."""

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

RAIZ = Path(__file__).resolve().parent.parent
RUTA_RAW = RAIZ / "data" / "raw" / "banknote" / "data_banknote_authentication.txt"
RUTA_PROCESADO = RAIZ / "data" / "processed" / "billetes_limpio.csv"

COLUMNAS = ["variance", "skewness", "curtosis", "entropy", "class"]
FEATURES = COLUMNAS[:-1]
TARGET = "class"


def cargar_raw(ruta: Path = RUTA_RAW) -> pd.DataFrame:
    """Lee el archivo original (sin encabezados) y le pone nombres a las columnas."""
    return pd.read_csv(ruta, header=None, names=COLUMNAS)


def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas duplicadas exactas y reinicia el índice.

    No hay nulos ni valores fuera de rango que tratar (ver docs/03_decisiones_limpieza.md).
    """
    return df.drop_duplicates().reset_index(drop=True)


def main() -> None:
    df = cargar_raw()
    limpio = limpiar(df)
    RUTA_PROCESADO.parent.mkdir(parents=True, exist_ok=True)
    limpio.to_csv(RUTA_PROCESADO, index=False)
    logger.info("raw: %s -> limpio: %s. Guardado en %s", df.shape, limpio.shape, RUTA_PROCESADO)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    main()
