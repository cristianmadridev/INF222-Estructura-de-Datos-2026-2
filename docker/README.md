# Docker (opcional) — entorno reproducible para INF 222

Instalar Python 3 localmente (guía en `recursos/herramientas-setup.md`) sigue siendo la vía **recomendada**
para el semestre: es más simple y suficiente para todos los laboratorios. Docker es una alternativa
**opcional** para quien prefiera no instalar nada en su máquina, o para eliminar dudas de "en mi PC sí corre".

## Requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/macOS) o Docker Engine (Linux).

## Uso

```bash
# 1. Abrir una terminal con Python 3.12 + pytest ya instalados, con el repo montado en /workspace
docker compose -f docker/docker-compose.yml run --rm lab

# Dentro del contenedor puedes correr cualquier laboratorio normalmente:
python modulo-1-estructuras-lineales/semana-01/laboratorio/lab01_pila.py

# 2. Correr las pruebas de una carpeta específica sin entrar al contenedor
docker compose -f docker/docker-compose.yml run --rm test modulo-1-estructuras-lineales/semana-01/laboratorio
```

## Por qué existe esto

- Congela la versión de Python y de `pytest` para que "funciona en mi máquina" no sea excusa ni sorpresa al momento de la entrega o de la corrección.
- Es el mismo entorno que usa el flujo de autocalificación por GitHub Actions (`.github/workflows/autograding.yml`) — si tus pruebas pasan en Docker localmente, van a pasar en el autograder.
- Útil para el proyecto final en equipo: todos los integrantes corren exactamente la misma versión de Python, sin depender de lo que cada quien tenga instalado.

## Notas

- No se requiere Docker para ningún laboratorio individual — es puramente una comodidad técnica opcional.
- Si usas Docker, decláralo igual que cualquier herramienta en tu entrega (no requiere declaración de IA, no es IA).
