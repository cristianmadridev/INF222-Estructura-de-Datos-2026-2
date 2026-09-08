# Semana 6 — Listas Circulares y Listas Circulares con Nodo Cabeza

**Módulo 2: Estructuras de datos dinámicas lineales**

---

## Objetivos de aprendizaje

- Distinguir una lista enlazada simple de una lista enlazada circular.
- Implementar algoritmos de inserción, eliminación y recorrido en listas circulares (evitando bucles infinitos).
- Comprender y aplicar el **nodo centinela (cabeza)** para simplificar los casos borde.
- Resolver el problema de Josephus usando una lista circular.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Lista enlazada circular:
   - El último nodo apunta **de vuelta al primero** (no a None)
   - Recorrido controlado: condición de parada por conteo o por referencia al inicio
   - Inserción y eliminación: casos borde simplificados respecto a lista simple
2. Lista circular con nodo cabeza (sentinel node):
   - Nodo fijo que no contiene dato útil; `cabeza.siguiente` apunta al primer elemento real
   - Simplifica todos los algoritmos: ya no existe "lista vacía sin cabeza"
   - La lista está vacía cuando `cabeza.siguiente == cabeza`
3. Aplicaciones:
   - Turnos rotativos (problema de Josephus)
   - Buffer circular en comunicaciones
   - Reproducción de listas en bucle (playlist)

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar `ListaCircular` con recorrido controlado por conteo
2. Implementar `ListaCircularConCabeza` (con nodo sentinel)
3. Resolver el problema de Josephus usando tu lista circular

---

## Entregable de la semana

**Laboratorio 5** — Listas circulares + problema de Josephus

- Archivo: `modulo-2-estructuras-dinamicas/semana-06/laboratorio/lab06_listas_circulares.py`

---

## Tarea / trabajo autónomo

Documentar en el README del laboratorio (o como comentario en el archivo) un **diagrama ASCII** que muestre la diferencia estructural entre:
1. Lista enlazada simple (termina en None)
2. Lista circular (último apunta al primero)
3. Lista circular con nodo cabeza (sentinel siempre presente)

---

## El Problema de Josephus

Situación: `n` personas se sientan en círculo numeradas del 1 al n. Se cuenta hasta `k` y la persona en esa posición queda eliminada. Se vuelve a contar desde la siguiente. ¿Quién sobrevive?

Ejemplo con n=7, k=3:
```
Círculo inicial: 1→2→3→4→5→6→7→(vuelve a 1)
Cuenta 3: elimina 3. Queda: 1→2→4→5→6→7
Cuenta 3: elimina 6. Queda: 1→2→4→5→7
...
```

---

## Uso de IA en esta semana

Puedes consultar un asistente de IA para **aclarar dudas conceptuales** sobre el problema de Josephus, siempre que documentes la consulta y expliques la solución con tus propias palabras. Ver política completa en `politicas/politica-ia.md`.

---

## Diferencia visual entre las tres estructuras

```
Lista simple:
  [1] → [2] → [3] → None

Lista circular:
  [1] → [2] → [3] ─┐
   ↑________________┘

Lista circular con nodo cabeza (C = centinela):
  [C] → [1] → [2] → [3] ─┐
   ↑_______________________┘
  (lista vacía: [C] → [C])
```
