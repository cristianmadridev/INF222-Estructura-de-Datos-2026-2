# Entorno reproducible para INF 222 — Estructura de Datos (2026-2)
# Uso: ver docker/README.md o recursos/herramientas-setup.md §Docker
FROM python:3.12-slim

RUN pip install --no-cache-dir pytest pytest-cov

WORKDIR /workspace

# El código del curso se monta como volumen (ver docker-compose.yml);
# esta imagen solo fija la versión de Python y las herramientas de prueba.
CMD ["bash"]
