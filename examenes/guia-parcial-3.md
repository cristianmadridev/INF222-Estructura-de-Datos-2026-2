# Guía de Estudio — Parcial 3

**INF 222 Estructura de Datos · Semestre 2026-2**  
**Semana 15 · Cubre: Módulo 4 completo (árboles y grafos)**

---

## Formato del examen

| Sección | Peso | Tipo de preguntas |
|---------|------|------------------|
| Teoría conceptual | 25% | Terminología, diferencias entre estructuras, comparaciones |
| Trazado de código | 40% | Dado un árbol o grafo, indicar el resultado de recorridos |
| Resolución de problemas | 35% | Insertar en BST y dibujar resultado, completar BFS/DFS |

**Duración**: ~90 minutos · **Sin IA, sin dispositivos**

---

## Árboles generales y binarios

### Terminología (saber de memoria)

| Término | Definición |
|---------|-----------|
| Raíz | Nodo sin padre |
| Nodo interno | Nodo con al menos un hijo |
| Hoja | Nodo sin hijos |
| Nivel / profundidad | Distancia desde la raíz (raíz = 0) |
| Altura del árbol | Máximo nivel de cualquier hoja |
| Subárbol | Un nodo y todos sus descendientes |
| Árbol binario | Cada nodo tiene a lo sumo 2 hijos |

### Preguntas de práctica — teoría

1. ¿Cuántas hojas tiene un árbol binario lleno (full binary tree) de altura 3?
2. ¿Qué recorrido de un BST produce los elementos en orden ascendente?
3. ¿Cuál es la complejidad de `buscar(valor)` en un BST balanceado? ¿Y en uno degenerado?

### Preguntas de práctica — trazado de recorridos

4. Dado el árbol:
   ```
         8
        / \
       3   10
      / \    \
     1   6   14
        / \
       4   7
   ```
   Escribe la secuencia de nodos visitados en:
   - Inorden:
   - Preorden:
   - Postorden:
   - Por niveles (BFS):

5. ¿En qué se diferencia el recorrido preorden del postorden para el mismo árbol?

---

## Árbol Binario de Búsqueda (BST)

### Preguntas de práctica — inserción

6. Inserta los valores `[50, 30, 70, 20, 40, 60, 80]` en ese orden en un BST inicialmente vacío. Dibuja el árbol resultante. ¿Cuál es su altura?

7. Inserta los valores `[1, 2, 3, 4, 5]` en orden creciente en un BST vacío. Dibuja el árbol. ¿Qué problema presenta? ¿Cuánto tarda una búsqueda ahora?

### Preguntas de práctica — eliminación

8. Del árbol del ejercicio 6, elimina el nodo 30. Explica los pasos y dibuja el árbol resultante.

9. ¿Cuáles son los 3 casos de eliminación en un BST y cómo se resuelve cada uno?

---

## Grafos

### Preguntas de práctica — teoría

10. ¿Cuál es la diferencia entre representar un grafo con **matriz de adyacencia** vs. **lista de adyacencia**?

    | Aspecto | Matriz | Lista |
    |---------|--------|-------|
    | Espacio | O(?) | O(?) |
    | Verificar arista (u,v) | O(?) | O(?) |
    | Obtener todos los vecinos de v | O(?) | O(?) |
    | Preferida cuando... | Grafo denso | Grafo disperso |

11. ¿Cuál es la diferencia entre BFS y DFS? ¿Qué estructura de datos auxiliar usa cada uno?

12. ¿Para qué sirve BFS en un grafo no ponderado? ¿Por qué no funciona para grafos ponderados con costos distintos?

### Preguntas de práctica — trazado

13. Dado el grafo:
    ```
    A - B - D - F
    |   |
    C   E
    ```
    Traza **BFS desde A** indicando el estado de la cola en cada paso y el orden de visita.

14. Para el mismo grafo, traza **DFS desde A** (versión iterativa con pila). ¿Cuál es el orden de visita?

15. ¿Puede el orden de BFS y DFS coincidir? ¿En qué caso?

---

## Ejercicio integrador (tipo resolución de problemas)

16. Diseña un BST para almacenar los precios de 7 productos de una tienda en línea. Los precios son: `[45.99, 12.50, 89.00, 7.25, 33.00, 67.50, 99.99]`. 
    - Inserta en el orden dado y dibuja el árbol.
    - ¿Cuántas comparaciones hace `buscar(7.25)`?
    - ¿El árbol está balanceado? ¿Cómo lo determinas?

17. Modela el metro de Ciudad de Panamá como un grafo (cada estación es un vértice, cada tramo es una arista). Elige 5 estaciones reales. ¿Qué recorrido usarías para encontrar el camino más corto entre dos estaciones? ¿Por qué?
