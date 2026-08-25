# Semana 8 — Recursividad

**Módulo 3: Recursividad, ordenación y búsqueda**

---

## Objetivos de aprendizaje

- Explicar qué hace a una función recursiva: **caso base** y **caso recursivo**.
- Trazar manualmente la pila de llamadas de una función recursiva.
- Distinguir recursividad directa (A→A) de recursividad indirecta (A→B→A).
- Identificar cuándo la recursividad es ineficiente (Fibonacci ingenuo) y qué alternativas existen.
- **Usar un asistente de IA de forma crítica** para obtener trazados y explicarlos con tus propias palabras.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Naturaleza de la recursividad:
   - Función que se llama a sí misma con un caso más simple
   - **Caso base**: condición de parada (sin esto → pila de llamadas se desborda)
   - **Caso recursivo**: llamada con argumento que acerca al caso base
2. Pila de llamadas (call stack):
   - Cada llamada recursiva apila un frame con sus propias variables locales
   - Cuando llega al caso base, empieza a "desapilar" y retornar valores
3. Tipos:
   - Directa: `factorial(n) → factorial(n-1)`
   - Indirecta: `es_par(n) → es_impar(n-1) → es_par(n-2)`
4. Casos a evitar:
   - Fibonacci ingenuo: O(2^n) llamadas, crece exponencialmente
   - Alternativas: memoización (`@lru_cache`), iteración
5. Ejemplos clásicos: factorial, Fibonacci, Torres de Hanoi

### Laboratorio (miércoles Gr. A / viernes Gr. B)

Actividad especial: **lab con IA declarada obligatoria**

---

## Entregable de la semana

**Laboratorio 7** — Recursividad + trazado con IA declarada

- Archivo: `modulo-3-recursividad-ordenacion-busqueda/semana-08/laboratorio/lab08_recursividad.py`

---

## Actividad obligatoria con IA (Semana 8)

1. Implementa las funciones `factorial`, `fibonacci` y `torres_de_hanoi` en Python.
2. Usa un asistente de IA (Claude, ChatGPT o Copilot) para obtener el **trazado paso a paso** de `fibonacci(5)`.
3. **Reescribe el trazado con tus propias palabras** en un comentario dentro del archivo, incluyendo un diagrama ASCII de la pila de llamadas que TÚ hayas dibujado.
4. Completa la sección de declaración de uso de IA al inicio del archivo.

**Lo que se evalúa**: que puedas explicar el trazado, no que hayas copiado el texto de la IA.

---

## Pila de llamadas de factorial(4) — ejemplo

```
factorial(4)
  └─ factorial(3)
       └─ factorial(2)
            └─ factorial(1)
                 └─ factorial(0)  ← CASO BASE: retorna 1
                 retorna 1
            retorna 2 (2 × 1)
       retorna 6 (3 × 2)
  retorna 24 (4 × 6)
```

---

## Comparación: Fibonacci recursivo vs. iterativo

```python
# Recursivo (O(2^n)) — NO hacer para n grande
def fib_recursivo(n):
    if n <= 1:
        return n
    return fib_recursivo(n-1) + fib_recursivo(n-2)

# Iterativo (O(n)) — correcto para producción
def fib_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
```

---

## Tarea / trabajo autónomo

Resolver Torres de Hanoi para n=4 y n=5 mediante **trazado manual en papel**, luego verificar con el programa.
