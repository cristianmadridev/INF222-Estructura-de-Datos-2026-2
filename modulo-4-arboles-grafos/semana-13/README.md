# Semana 13 — Árbol Binario de Búsqueda (BST)

**Módulo 4: Estructura avanzada de datos**

---

## Objetivos de aprendizaje

- Implementar inserción, búsqueda y eliminación en un **árbol binario de búsqueda (BST)**.
- Comprender el problema del desbalance y cómo degrada el BST a O(n) en el peor caso.
- Identificar el concepto de AVL como solución al desbalance.
- Relacionar el BST con aplicaciones reales: índices de bases de datos, autocompletado.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Propiedad del BST:
   - Para todo nodo N: todos los nodos del subárbol izquierdo < N.dato, todos los del derecho > N.dato
   - El inorden de un BST produce los elementos en orden ascendente
2. Operaciones:
   - **Insertar**: sigue la propiedad hasta encontrar un lugar vacío → O(log n) balanceado, O(n) degenerado
   - **Buscar**: similar a búsqueda binaria, siguiendo la propiedad → O(log n) / O(n)
   - **Eliminar**: tres casos — nodo hoja, nodo con un hijo, nodo con dos hijos (predecesor/sucesor inorden)
3. Árbol degenerado:
   - Si insertas en orden creciente: el árbol se convierte en una lista enlazada → O(n) para todo
4. AVL (ampliación):
   - Factor de balance: altura(der) - altura(izq), debe ser {-1, 0, 1}
   - Rotaciones para rebalancear (simple y doble, derecha e izquierda)

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar `ArbolBinarioBusqueda` con `insertar`, `buscar`, `eliminar`
2. Probar con secuencias que generen árboles balanceados y árboles degenerados
3. Medir la profundidad resultante en ambos casos

---

## Entregable de la semana

**Laboratorio 11** — BST completo

- Archivo: `modulo-4-arboles-grafos/semana-13/laboratorio/lab13_bst.py`

---

## Tarea / trabajo autónomo

Investigar (con o sin IA declarada) el concepto de **rotación simple en AVL** y explicarlo con un diagrama propio en un comentario al final del archivo del laboratorio.

---

## Los 3 casos de eliminación en BST

```
Caso 1: El nodo a eliminar es una hoja (sin hijos)
    Solución: simplemente desconecta el nodo

Caso 2: El nodo tiene exactamente un hijo
    Solución: conecta el padre del nodo directamente con el hijo

Caso 3: El nodo tiene dos hijos
    Solución: reemplaza el dato del nodo con el del SUCESOR INORDEN
              (el mínimo del subárbol derecho), luego elimina el sucesor

Ejemplo — eliminar 10 del árbol:
        10           →          12
       /  \                    /  \
      5    20                 5    20
          /  \                    /  \
         12   30                 15   30
           \
           15
    (12 es el sucesor inorden de 10 → mínimo del subárbol derecho)
```
