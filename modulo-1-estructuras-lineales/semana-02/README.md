# Semana 2 — Pilas avanzadas y Colas

**Módulo 1: Estructuras de datos lineales**

---

## Objetivos de aprendizaje

- Implementar una pila usando **nodos enlazados** (sin lista de Python como base) y comparar ventajas frente a la implementación con lista.
- Aplicar pilas a problemas reales: verificación de paréntesis balanceados, evaluación de notación postfija.
- Definir el concepto de **cola (queue)**, su principio FIFO y sus operaciones fundamentales.
- Implementar la clase `Cola` en Python.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Pilas con nodo enlazado:
   - Clase `Nodo` (dato + referencia al siguiente nodo)
   - `PilaEnlazada` que manipula nodos en lugar de índices de lista
2. Aplicaciones de pilas:
   - Verificación de paréntesis balanceados `{[()]}` → algoritmo clásico con pila
   - Evaluación de expresiones en **notación postfija** (Reverse Polish Notation)
   - Mecanismo de deshacer/rehacer (undo/redo)
3. Cola (Queue):
   - Principio **FIFO** (First In, First Out)
   - Operaciones: `enqueue(dato)`, `dequeue()`, `front()`, `is_empty()`, `size()`
   - Analogía: fila de banco, impresora, sistema de turnos

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar `PilaEnlazada` con clase `Nodo`
2. Implementar verificador de paréntesis balanceados usando `PilaEnlazada`
3. Implementar la clase `Cola`
4. Mini-proyecto: simulador de cola de impresión

---

## Entregable de la semana

**Laboratorio 2** — Pila enlazada + Cola + simulador de impresión

- Archivo: `modulo-1-estructuras-lineales/semana-02/laboratorio/lab02_pila_enlazada_cola.py`
- Subir con `git push` antes de la fecha límite del aula virtual

---

## Tarea / trabajo autónomo

Implementar la **evaluación de una expresión en notación postfija** usando tu propia `PilaEnlazada`. Agrega la función en el mismo archivo del laboratorio y documenta el algoritmo en comentarios.

Ejemplo: la expresión postfija `3 4 + 5 *` debe evaluar a `35`.

---

## Recursos de la semana

| Recurso | Propósito |
|---------|-----------|
| Python Tutor | Visualizar cómo los nodos se enlazan en memoria |
| VisuAlgo → Stack | Ver la diferencia conceptual con implementación por arreglo |
| VisuAlgo → Queue | Animación de enqueue/dequeue |
| Goodrich et al., cap. 6 (Stacks, Queues) | Implementación detallada |

---

## Conceptos clave para recordar

```
Pila con lista:    [1, 2, 3] → tope es el índice -1
Pila con nodos:    cabeza → [3] → [2] → [1] → None
                   (el tope es la cabeza de la lista enlazada)

Cola:              frente → [1] → [2] → [3] → final
                   enqueue agrega al final, dequeue saca del frente
```

---

## Algoritmo de paréntesis balanceados (pseudocódigo)

```
para cada caracter c en la cadena:
    si c es abre-paréntesis ('(', '[', '{'):
        pila.push(c)
    si c es cierra-paréntesis (')', ']', '}'):
        si pila.is_empty():
            retornar False      # cierra sin haber abierto
        tope = pila.pop()
        si no coinciden (tope, c):
            retornar False      # par no coincide
si pila.is_empty():
    retornar True               # todos los pares se balancearon
sino:
    retornar False              # quedaron pares sin cerrar
```
