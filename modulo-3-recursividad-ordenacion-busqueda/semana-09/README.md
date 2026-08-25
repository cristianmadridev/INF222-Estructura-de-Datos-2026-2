# Semana 9 — Algoritmos de Ordenación

**Módulo 3: Recursividad, ordenación y búsqueda**

---

## Objetivos de aprendizaje

- Implementar burbuja (bubble sort), selección (selection sort) e inserción (insertion sort).
- Analizar y comparar la complejidad temporal de estos algoritmos en el mejor, promedio y peor caso.
- Medir empíricamente tiempos de ejecución con el módulo `time`.
- Reconocer merge sort y quick sort como la solución O(n log n) para datos grandes.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Clasificación de algoritmos de ordenación:
   - **In situ** vs. **no in situ** (requiere memoria extra)
   - **Estable** vs. **inestable** (preserva el orden relativo de elementos iguales)
2. Los tres algoritmos básicos:

   | Algoritmo | Mejor caso | Promedio | Peor caso | In situ | Estable |
   |-----------|-----------|---------|---------|---------|---------|
   | Burbuja | O(n) | O(n²) | O(n²) | Sí | Sí |
   | Selección | O(n²) | O(n²) | O(n²) | Sí | No |
   | Inserción | O(n) | O(n²) | O(n²) | Sí | Sí |

3. Introducción conceptual a merge sort y quick sort:
   - Idea de "dividir y vencer" (divide and conquer)
   - Complejidad O(n log n) — exponencialmente mejor para n grande

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar los 3 algoritmos en Python
2. Medir tiempos sobre arreglos de distintos tamaños y distintos estados de orden inicial
3. Elaborar tabla comparativa de resultados

---

## Entregable de la semana

**Laboratorio 8** — Algoritmos de ordenación + comparación de tiempos

- Archivo: `modulo-3-recursividad-ordenacion-busqueda/semana-09/laboratorio/lab09_ordenacion.py`

---

## Tarea / trabajo autónomo (ampliación)

Implementar opcionalmente una versión básica de **merge sort** o **quick sort** y agregar sus tiempos a la tabla comparativa del laboratorio.

---

## Trazado comparativo: el mismo arreglo con los 3 algoritmos

Arreglo inicial: `[5, 3, 8, 1, 4]`

```
BURBUJA (compara pares adyacentes, burbujea el mayor hacia el final):
Pasada 1: [3,5,8,1,4] → [3,5,8,1,4] → [3,5,1,8,4] → [3,5,1,4,8]  ✓ 8 en su lugar
Pasada 2: [3,5,1,4,8] → [3,1,5,4,8] → [3,1,4,5,8]                 ✓ 5 en su lugar
...

SELECCIÓN (busca el mínimo y lo pone al inicio):
i=0: mínimo=1 (pos 3) → intercambia con pos 0: [1,3,8,5,4]
i=1: mínimo=3 (pos 1) → ya está: [1,3,8,5,4]
i=2: mínimo=4 (pos 4) → intercambia con pos 2: [1,3,4,5,8]
...

INSERCIÓN (toma un elemento y lo inserta en la parte ordenada):
[5 | 3,8,1,4]  → toma 3: [3,5 | 8,1,4]
[3,5 | 8,1,4]  → toma 8: [3,5,8 | 1,4]
[3,5,8 | 1,4]  → toma 1: [1,3,5,8 | 4]
[1,3,5,8 | 4]  → toma 4: [1,3,4,5,8]
```

---

## Recursos de la semana

| Recurso | Propósito |
|---------|-----------|
| VisuAlgo → Sorting | Ver animación paso a paso de los 3 algoritmos |
| `06-Herramientas-recursos-IA.md` (del Plan 2026-2) | Tabla de complejidad Big-O de referencia |
