# Imagen de la API de autenticación de billetes.
#   docker build -t billetes-api .
#   docker run --rm -p 8000:8000 billetes-api
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

# Primero las dependencias, para que Docker las guarde en caché.
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

# Solo lo necesario para entrenar y servir el modelo.
COPY src/ src/
COPY api/ api/
COPY data/raw/ data/raw/

# El modelo se entrena al construir la imagen (no se versiona en git).
RUN /app/.venv/bin/python -m src.train

# La API corre con un usuario sin privilegios.
RUN useradd --create-home app
USER app

EXPOSE 8000
CMD ["/app/.venv/bin/uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
