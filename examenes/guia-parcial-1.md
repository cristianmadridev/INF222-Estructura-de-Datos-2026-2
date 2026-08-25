# Guía de Estudio — Parcial 1

**INF 222 Estructura de Datos · Semestre 2026-2**  
**Semana 7 · Cubre: Módulos 1 y 2 completos**

---

## Formato del examen

| Sección | Peso | Tipo de preguntas |
|---------|------|------------------|
| Teoría conceptual | 30% | Selección múltiple, V/F justificado, respuesta corta |
| Trazado de código | 35% | Se entrega código y debes indicar el estado de la estructura y/o la salida |
| Resolución de problemas | 35% | Completar funciones, corregir errores, diseñar algoritmos |

**Duración**: ~90 minutos · **Sin IA, sin dispositivos**

---

## Módulo 1 — Estructuras lineales

### Notación Big-O

- ¿Qué mide la notación Big-O? ¿Mejor caso, promedio o peor caso?
- Ordena de más eficiente a menos: O(n²), O(1), O(n log n), O(log n), O(n)
- ¿Cuál es la complejidad de recorrer una lista de n elementos? ¿Y de acceder a su primer elemento?
- Estima la complejidad de este fragmento:
  ```python
  for i in range(n):
      for j in range(n):
          print(i, j)
  ```

### Pilas (Stack)

- Principio LIFO: ¿qué significa? ¿qué operación entra primero, cuál sale primero?
- Operaciones: `push`, `pop`, `peek`, `is_empty` — complejidad de cada una con lista de Python
- **Ejercicio de trazado**: dada la secuencia `push(5), push(3), pop(), push(8), peek()`, ¿cuál es el estado de la pila después de cada operación?
- Aplicación: verificar que `"{[()]}"` tiene paréntesis balanceados paso a paso
- Implementación con lista vs. con nodos enlazados: ¿cuál es O(1) garantizado y cuál es O(1) amortizado?

### Colas (Queue)

- Principio FIFO: diferencia con LIFO
- Operaciones: `enqueue`, `dequeue`, `front` — complejidad con lista de Python
- Cola circular, cola de prioridad, deque: ¿cuándo se usa cada una?
- **Ejercicio**: simular una cola de impresión con 4 trabajos. ¿En qué orden salen?

---

## Módulo 2 — Estructuras dinámicas lineales

### Punteros y referencias en Python

- ¿Qué diferencia hay entre `b = a` y `b = a.copy()` cuando `a` es una lista?
- ¿Qué imprime este código?
  ```python
  x = [1, 2, 3]
  y = x
  y.append(4)
  print(x)
  ```
- ¿Cuándo usar `copy.deepcopy()`?

### Lista enlazada simple

- Estructura: dibuja un diagrama de 3 nodos enlazados
- Complejidad de: insertar al inicio, insertar al final, buscar, eliminar
- **Ejercicio de trazado**: lista `[10] → [20] → [30] → None`. Traza la eliminación del nodo con dato=20 paso a paso (qué punteros cambian)
- **Ejercicio de completar código**: implementa el método `eliminar(valor)` dado el esqueleto de la clase

### Lista circular y circular con nodo cabeza

- ¿Cómo evitar un bucle infinito al recorrer una lista circular?
- ¿Para qué sirve el nodo centinela (cabeza)?
- ¿Cómo saber si una lista circular con nodo cabeza está vacía?

### Lista doblemente enlazada

- Diferencia entre nodo de lista simple (una referencia) y nodo de lista doble (dos referencias)
- ¿Qué ventaja tiene sobre la lista simple para la eliminación de un nodo si ya tienes un puntero al nodo?
- Traza la inserción de un nuevo nodo entre dos nodos existentes

---

## Preguntas de práctica (tipo examen)

### Teoría

1. Explica la diferencia entre una lista enlazada circular y una lista enlazada circular con nodo cabeza. ¿Qué problema resuelve el nodo cabeza?
2. ¿Por qué `lista_b = lista_a` en Python no crea una copia de la lista? ¿Qué deberías hacer para crear una copia independiente?
3. Compara las complejidades de inserción al inicio: lista nativa de Python vs. lista enlazada simple propia.

### Trazado de código

4. Dado el siguiente fragmento, indica el estado de la pila después de cada línea:
   ```python
   p = Pila()
   p.push(1)
   p.push(2)
   p.pop()
   p.push(3)
   p.push(4)
   p.pop()
   ```

5. Dado el fragmento de aliasing, ¿qué imprime cada print?
   ```python
   a = [[1, 2], [3, 4]]
   b = a.copy()
   b[0].append(99)
   print(a[0])
   print(b[1])
   ```

### Resolución de problemas

6. Implementa una función `es_palindromo(cadena)` que use una pila para determinar si una cadena es palíndromo. Analiza su complejidad.

7. Completa el método `eliminar(valor)` de `ListaEnlazada`, manejando correctamente los 4 casos: valor en la cabeza, valor en el medio, valor al final, valor que no existe.

---

## Estrategia de estudio

1. **Trazado en papel**: practica trazando en papel, no en el computador. El examen es presencial.
2. **Complejidades de memoria**: aprende de cor las complejidades de cada operación de cada estructura.
3. **Casos borde**: siempre verifica: ¿qué pasa con lista vacía? ¿con un solo elemento? ¿con el primer o último elemento?
4. **Sin IA**: el examen es sin IA. Si algo solo lo "sabes" con IA, no lo sabes. Practica sin asistente.
