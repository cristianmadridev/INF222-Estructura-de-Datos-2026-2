# Semana 7 — Listas Doblemente Enlazadas · PARCIAL 1 · Propuesta de Proyecto

**Módulo 2: Estructuras de datos dinámicas lineales — Cierre**

---

## Objetivos de aprendizaje

- Implementar una lista doblemente enlazada con operaciones de inserción y eliminación en ambos extremos y en posición intermedia.
- Reconocer aplicaciones: deque eficiente, navegación bidireccional, listas de reproducción editables.
- Integrar los contenidos de los módulos 1 y 2 para la evaluación parcial.
- Entregar la **propuesta formal del proyecto final** en equipo.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Lista doblemente enlazada:
   - Nodo con dos referencias: `anterior` y `siguiente`
   - Permite recorrer en ambas direcciones: O(n) hacia adelante Y hacia atrás
   - Inserción/eliminación en cualquier punto: O(1) si ya tienes el nodo, O(n) para buscarlo
2. Comparativa final de todas las variantes vistas en el Módulo 2:
   - Lista simple / Lista circular / Lista circular con cabeza / Lista doble
3. Repaso integrador de Módulos 1 y 2 para el Parcial 1

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar `ListaDoblementeEnlazada`
2. **PARCIAL 1** (evaluación presencial, sin IA)
3. Entrega de la propuesta formal del proyecto final

---

## Entregable de la semana

**Laboratorio 6** — Lista Doblemente Enlazada

- Archivo: `modulo-2-estructuras-dinamicas/semana-07/laboratorio/lab07_lista_doble.py`

**Propuesta formal del proyecto final** (en equipo)

- Archivo: `proyecto-final/propuesta/PLANTILLA-propuesta.md` → renombrar a `propuesta.md` con tu información real

---

## PARCIAL 1 — información clave

| Campo | Detalle |
|-------|---------|
| Semana | 7 |
| Cubre | Módulos 1 y 2 completos |
| Formato | Teoría (30%) + Trazado de código (35%) + Resolución de problemas (35%) |
| Duración | 90 minutos (referencia) |
| IA permitida | NO |
| Dispositivos | NO |

**Temas del Módulo 1**: pilas (operaciones, implementaciones, aplicaciones), colas (FIFO, variantes), notación Big-O.

**Temas del Módulo 2**: punteros/referencias en Python, aliasing, lista enlazada simple (todas las operaciones), lista circular, lista circular con nodo cabeza, lista doblemente enlazada.

Ver guía de estudio detallada en `examenes/guia-parcial-1.md`.

---

## Diagrama de la lista doblemente enlazada

```
None ←─ [1] ⇄ [2] ⇄ [3] ─→ None
          ↑
        cabeza

Insertar 0 al inicio:
None ←─ [0] ⇄ [1] ⇄ [2] ⇄ [3] ─→ None
          ↑
        cabeza

Eliminar el nodo [2]:
None ←─ [0] ⇄ [1] ⇄ [3] ─→ None
             ↑       ↑
         anterior  siguiente
         del 3     del 1 ahora
```

---

## Tarea / trabajo autónomo

Estudiar con la guía en `examenes/guia-parcial-1.md` y practicar trazado manual de pilas, colas y listas enlazadas sobre papel.
