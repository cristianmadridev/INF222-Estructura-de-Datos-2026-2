# Guía de Estudio — Parcial 2

**INF 222 Estructura de Datos · Semestre 2026-2**  
**Semana 11 · Cubre: Módulo 3 completo (recursividad, ordenación y búsqueda)**

---

## Formato del examen

| Sección | Peso | Tipo de preguntas |
|---------|------|------------------|
| Teoría conceptual | 25% | Definiciones, comparaciones, análisis de complejidad |
| Trazado de código | 40% | Pila de llamadas, pasadas de ordenación, ejecución de búsqueda |
| Resolución de problemas | 35% | Escribir/completar funciones recursivas, elegir y justificar algoritmos |

**Duración**: ~90 minutos · **Sin IA, sin dispositivos**

---

## Recursividad

### Conceptos clave

- **Caso base**: condición que detiene la recursión. Sin él → `RecursionError` (stack overflow)
- **Caso recursivo**: llamada a sí misma con argumento que se acerca al caso base
- **Pila de llamadas**: cada llamada apila un frame; el tope se desapila cuando llega al caso base

### Preguntas de práctica — teoría

1. ¿Qué pasa si una función recursiva no tiene caso base? ¿Qué error lanza Python?
2. ¿Cuál es la complejidad temporal de `fibonacci_recursivo(n)` sin memoización? Justifica.
3. ¿En qué escenarios conviene usar iteración en lugar de recursividad?

### Preguntas de práctica — trazado

4. Traza la pila de llamadas de `factorial(4)` indicando el valor de retorno en cada nivel.

5. ¿Cuántas llamadas hace `fibonacci_recursivo(5)` en total? Dibuja el árbol de llamadas.

6. Dado este código, ¿qué imprime?
   ```python
   def misterio(n):
       if n == 0:
           return 0
       return n + misterio(n - 1)
   print(misterio(5))
   ```

### Preguntas de práctica — resolución

7. Escribe una función recursiva `suma_digitos(n)` que retorne la suma de los dígitos de un entero positivo `n`. Ejemplo: `suma_digitos(123)` → 6. Indica claramente el caso base.

8. Escribe una función recursiva `potencia(base, exp)` que calcule `base^exp` sin usar el operador `**`. Complejidad: O(exp).

---

## Algoritmos de Ordenación

### Complejidades a conocer de memoria

| Algoritmo | Mejor | Promedio | Peor | In situ | Estable |
|-----------|-------|---------|------|---------|---------|
| Burbuja | O(n) | O(n²) | O(n²) | Sí | Sí |
| Selección | O(n²) | O(n²) | O(n²) | Sí | No |
| Inserción | O(n) | O(n²) | O(n²) | Sí | Sí |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | No | Sí |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | Sí | No |

### Preguntas de práctica — teoría

9. ¿En qué caso particular el algoritmo de inserción es O(n)? ¿Y el de burbuja (con flag)?
10. ¿Por qué la selección siempre es O(n²) aunque el arreglo ya esté ordenado?
11. ¿Qué significa que un algoritmo de ordenación sea "estable"? Da un ejemplo donde la estabilidad importa.

### Preguntas de práctica — trazado

12. Dado `[4, 2, 8, 1, 6]`, traza **cada pasada** del algoritmo de **burbuja** (con flag) hasta que el arreglo esté ordenado. ¿Cuántas pasadas necesitó?

13. Dado `[4, 2, 8, 1, 6]`, traza el algoritmo de **selección** indicando en cada iteración: i, índice del mínimo encontrado, intercambio realizado.

14. Dado `[3, 1, 5, 2, 4]`, traza el algoritmo de **inserción** indicando en cada paso el elemento tomado y dónde se inserta.

---

## Algoritmos de Búsqueda

### Preguntas de práctica — teoría

15. ¿Por qué la búsqueda binaria requiere que el arreglo esté ordenado? ¿Qué resultado incorrecto daría si no lo estuviera?
16. ¿Cuál es la complejidad de búsqueda binaria en el peor caso? Justifica con un ejemplo.
17. Para un arreglo de 1,024 elementos, ¿cuántas comparaciones hace como máximo la búsqueda binaria?

### Preguntas de práctica — trazado

18. Dado `[5, 10, 20, 30, 40, 50, 60, 70, 80]`, traza la búsqueda binaria del valor 45, mostrando en cada iteración: `izq`, `der`, `mid`, `arr[mid]`, y la decisión tomada.

19. Escribe la versión recursiva de búsqueda binaria e indica su caso base.

---

## Ejercicio integrador (tipo resolución de problemas en examen)

20. Tienes una lista de nombres de estudiantes desordenada. Los usuarios harán 10,000 búsquedas.
    - ¿Qué harías primero? ¿Con qué algoritmo? ¿Por qué ese y no otro?
    - ¿Qué método de búsqueda usarías para las 10,000 búsquedas? Justifica con complejidades.
    - ¿Cambia tu respuesta si solo hay 5 búsquedas? ¿Por qué?
