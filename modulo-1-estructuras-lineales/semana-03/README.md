# Semana 3 — Variantes de Colas, Taller Integrador y Kickoff del Proyecto Final

**Módulo 1: Estructuras de datos lineales — Cierre**

---

## Objetivos de aprendizaje

- Distinguir variantes de la cola: **cola circular**, **cola de prioridad** y **deque** (cola doblemente terminada).
- Integrar pilas y colas en la solución de un problema combinado (simulador de historial de navegador).
- Comprender los lineamientos del proyecto final y conformar tu equipo de trabajo.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Variantes de colas:
   - **Cola circular**: el puntero final "da la vuelta" al inicio del arreglo (evita desperdiciar espacio)
   - **Cola de prioridad**: los elementos salen según su prioridad, no por orden de llegada (usada en sistemas operativos, algoritmo de Dijkstra)
   - **Deque** (Double-ended Queue): inserción y eliminación en ambos extremos
2. Ejemplos de uso real: buffer circular en redes, reproducción de música en bucle, historial de comandos en terminal
3. Presentación formal del proyecto final: opciones de tema, cronograma, formación de equipos (ver `../INF222-Proyecto-Final-2026-2/README.md`)

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Taller integrador: simulador de historial de navegador web usando dos pilas (botones "Atrás" y "Adelante")
2. Quiz formativo corto (10-15 minutos) sobre pilas y colas — sin uso de IA

---

## Entregable de la semana

**Laboratorio 3 (Taller integrador)** — Simulador de historial de navegador

- Archivo: `modulo-1-estructuras-lineales/semana-03/laboratorio/lab03_historial_navegador.py`
- Adicionalmente: registra la formación de tu equipo de proyecto en `proyecto-final/propuesta/PLANTILLA-propuesta.md` (campo "Equipo")

---

## Tarea / trabajo autónomo

- Con tu equipo, explora las 5 opciones de tema propuestas para el proyecto final (ver `../INF222-Proyecto-Final-2026-2/README.md`).
- Repasa pilas y colas con VisuAlgo antes del quiz de la semana 4.

---

## Simulador de historial: cómo funciona

Tu navegador tiene:
- **Pila "atrás"**: cada vez que visitas una URL nueva, la URL actual va a la pila de atrás.
- **Pila "adelante"**: cuando presionas "Atrás", la URL actual va a la pila de adelante.

```
Estado inicial:  pila_atras=[], pila_adelante=[], actual="about:blank"

visitar("a.com"):   actual="a.com",  pila_atras=["about:blank"]
visitar("b.com"):   actual="b.com",  pila_atras=["about:blank","a.com"]
visitar("c.com"):   actual="c.com",  pila_atras=["about:blank","a.com","b.com"]

atrás():            actual="b.com",  pila_atras=["about:blank","a.com"], pila_adelante=["c.com"]
atrás():            actual="a.com",  pila_atras=["about:blank"],         pila_adelante=["c.com","b.com"]

adelante():         actual="b.com",  pila_atras=["about:blank","a.com"], pila_adelante=["c.com"]

visitar("d.com"):   actual="d.com",  pila_atras=["about:blank","a.com","b.com"], pila_adelante=[]
                    ↑ al visitar una página nueva, la pila adelante se vacía
```

## Recursos de la semana

| Recurso | Propósito |
|---------|-----------|
| VisuAlgo → Stack | Repasar antes del quiz formativo |
| VisuAlgo → Queue | Repasar antes del quiz formativo |
| `../INF222-Proyecto-Final-2026-2/README.md` | Leer para el kickoff del proyecto |
