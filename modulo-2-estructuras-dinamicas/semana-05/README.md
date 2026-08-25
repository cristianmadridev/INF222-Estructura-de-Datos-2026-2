# Semana 5 — Listas Enlazadas Simples

**Módulo 2: Estructuras de datos dinámicas lineales**

---

## Objetivos de aprendizaje

- Explicar la estructura y motivación de una lista enlazada simple frente a una lista basada en arreglo.
- Implementar las operaciones fundamentales: inserción al inicio, al final y en posición intermedia.
- Implementar eliminación por valor y por posición, búsqueda, recorrido y cálculo de longitud.
- Analizar la complejidad de cada operación y compararla con su equivalente en lista de Python.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. ¿Por qué lista enlazada? Comparativa con arreglo:
   - Inserción al inicio: O(n) en arreglo, O(1) en lista enlazada
   - Acceso aleatorio: O(1) en arreglo, O(n) en lista enlazada
   - Uso de memoria: arreglo contiguo vs. nodos dispersos
2. Estructura:
   - Clase `Nodo` (dato + siguiente)
   - Clase `ListaEnlazada` (referencia a la cabeza)
3. Operaciones y su trazado:
   - `insertar_inicio(dato)` → O(1)
   - `insertar_final(dato)` → O(n) sin puntero al final, O(1) con él
   - `insertar_en_posicion(pos, dato)` → O(n)
   - `eliminar(dato)` → O(n), casos: primero, intermedio, último, no existe
   - `buscar(dato)` → O(n)
   - `recorrer()` / `__str__()` → O(n)

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementación guiada, paso a paso, de `ListaEnlazada`
2. Comparación empírica de tiempos de inserción al inicio: lista de Python vs. lista enlazada
3. Pruebas con casos borde: lista vacía, un solo elemento, insertar en posición fuera de rango

---

## Entregable de la semana

**Laboratorio 4** — Lista Enlazada Simple completa

- Archivo: `modulo-2-estructuras-dinamicas/semana-05/laboratorio/lab05_lista_enlazada.py`

---

## Tarea / trabajo autónomo

Ampliar la implementación con:
- `invertir()` — invierte la lista in situ, sin crear nuevos nodos
- `obtener(indice)` — retorna el dato en la posición dada

---

## Análisis de complejidad de las operaciones

| Operación | Lista de Python | Lista Enlazada Simple |
|-----------|-----------------|-----------------------|
| Insertar al inicio | O(n) | O(1) |
| Insertar al final | O(1)* | O(n) sin ptr final / O(1) con él |
| Insertar en posición k | O(n) | O(n) |
| Eliminar por valor | O(n) | O(n) |
| Buscar | O(n) | O(n) |
| Acceder por índice | O(1) | O(n) |
| Longitud | O(1) | O(n) sin contador / O(1) con él |

*O(1) amortizado con lista dinámica de Python

---

## Diagrama de la estructura

```
cabeza
  │
  ▼
[dato=10|sig]──►[dato=20|sig]──►[dato=30|sig]──►None

Después de insertar 5 al inicio:
cabeza
  │
  ▼
[dato=5|sig]──►[dato=10|sig]──►[dato=20|sig]──►[dato=30|sig]──►None
```
