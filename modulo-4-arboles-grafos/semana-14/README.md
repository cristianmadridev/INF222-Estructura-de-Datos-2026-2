# Semana 14 — Grafos, BFS, DFS y Checkpoint 2 del Proyecto Final

**Módulo 4: Estructura avanzada de datos**

---

## Objetivos de aprendizaje

- Definir el concepto de grafo y su terminología (vértice, arista, dirigido, ponderado, ciclo).
- Representar un grafo con **matriz de adyacencia** y con **lista de adyacencia**.
- Implementar **BFS** (recorrido en anchura, con cola) y **DFS** (recorrido en profundidad, con pila o recursión).
- Presentar el **Checkpoint 2 del proyecto final** con avance funcional avanzado.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Grafos:
   - Conjunto de vértices (nodos) y aristas (edges)
   - **Dirigido** (dígrafo): aristas con dirección A→B ≠ B→A
   - **No dirigido**: arista A-B implica B-A
   - **Ponderado**: cada arista tiene un peso (distancia, costo, etc.)
   - Conceptos: grado, camino, ciclo, grafo conexo, grafo acíclico
2. Representaciones:
   - **Matriz de adyacencia**: matriz n×n, `mat[i][j]=1` si existe arista de i a j. Espacio O(n²), consulta O(1)
   - **Lista de adyacencia**: diccionario {vértice: [vecinos]}. Espacio O(n+m), consulta O(grado)
3. Recorridos:
   - **BFS** (Breadth-First Search): nivel por nivel, usa una **cola**. Útil para camino más corto (sin pesos)
   - **DFS** (Depth-First Search): va tan profundo como puede, usa una **pila** o recursión. Útil para detectar ciclos, explorar laberintos

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar `Grafo` con lista de adyacencia
2. Implementar BFS y DFS
3. Checkpoint 2 del proyecto final

---

## Entregable de la semana

**Laboratorio 12** — Grafo + BFS + DFS

- Archivo: `modulo-4-arboles-grafos/semana-14/laboratorio/lab14_grafos.py`

**Checkpoint 2 del proyecto final** (en equipo):

- Archivo: `proyecto-final/checkpoint-2/PLANTILLA-checkpoint-2.md` → renombrar a `checkpoint-2.md`
- El equipo debe tener al menos 2 de las 3 estructuras de datos requeridas integradas y funcionando

---

## BFS vs. DFS — comparación con el mismo grafo

```
Grafo (no dirigido):
  A - B - D
  |   |
  C   E

BFS desde A (cola):   A, B, C, D, E  (por niveles: vecinos de A, luego vecinos de B y C...)
DFS desde A (pila):   A, C, B, E, D  (va profundo primero, el orden exacto depende del orden de vecinos)
```

---

## Aplicaciones reales

| Aplicación | Qué representa | Recorrido típico |
|-----------|---------------|-----------------|
| GPS / mapas | Intersecciones=vértices, calles=aristas ponderadas | Dijkstra (extensión de BFS) |
| Redes sociales | Usuarios=vértices, amistades=aristas | BFS (grados de separación) |
| Recomendaciones | Usuarios y productos como vértices bipartitos | BFS / análisis de vecindad |
| Detección de ciclos | Dependencias entre módulos/tareas | DFS |

---

## Tarea / trabajo autónomo

Modelar como grafo un caso del dominio del proyecto final (si aplica) o una red de ciudades de Panamá, y ejecutar BFS y DFS sobre ese modelo.
