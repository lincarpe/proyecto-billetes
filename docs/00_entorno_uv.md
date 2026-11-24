# 00 · Entorno con uv

## Qué es uv y por qué lo usamos

`uv` es la herramienta que crea el entorno virtual del proyecto, instala las librerías y ejecuta los comandos dentro de ese entorno. Con eso el proyecto funciona igual en cualquier computador.

Los archivos que definen el entorno son:

- `pyproject.toml`: lista de dependencias y versión mínima de Python (>= 3.14).
- `uv.lock`: versiones exactas de cada librería. Se sube al repositorio para que todos instalen lo mismo.
- `.venv/`: el entorno creado por `uv sync`. No se sube a GitHub (está en `.gitignore`).

## Instalación de uv (una sola vez)

```powershell
winget install --id=astral-sh.uv -e
```

o, si ya tienes Python:

```powershell
python -m pip install --user uv
```

Para comprobarlo:

```powershell
uv --version
```

Si el sistema no reconoce `uv`, usa `python -m uv` en lugar de `uv` en todos los comandos.

## Crear el entorno

Desde la carpeta del proyecto:

```powershell
uv sync
```

Esto instala las dependencias principales (pandas, scikit-learn, FastAPI, uvicorn, joblib, matplotlib, seaborn, JupyterLab) y el grupo `dev` (pytest, httpx).

## Ejecutar cosas dentro del entorno

```powershell
uv run python -m src.limpieza
uv run python -m src.train
uv run uvicorn api.main:app
uv run pytest
uv run jupyter lab
```

## Agregar una librería nueva

```powershell
uv add nombre-de-la-libreria          # dependencia del proyecto
uv add --group dev nombre-de-la-libreria   # solo para desarrollo
```

Después de agregarla, se sube el cambio de `pyproject.toml` y `uv.lock` en el mismo commit.
