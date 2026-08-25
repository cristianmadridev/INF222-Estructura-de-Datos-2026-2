"""
Lab 8 — Recursividad (con uso declarado de IA)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________

=============================================================
DECLARACIÓN DE USO DE IA (COMPLETAR ANTES DE ENTREGAR)
=============================================================
Herramienta usada      : (ej. Claude claude-sonnet-4-6, ChatGPT-4o, Copilot)
Para qué se usó        : (ej. "obtuve el trazado de fibonacci(5)")
Qué hice yo            : (ej. "implementé las funciones; reescribí el trazado con mis palabras")
Puedo explicar todo    : Sí / No
=============================================================
"""

import time
from functools import lru_cache


# =============================================================================
# PARTE 1 — FACTORIAL
# =============================================================================

def factorial(n):
    """
    Calcula n! de forma recursiva.
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n × factorial(n-1)
    Complejidad: O(n) tiempo, O(n) espacio (por la pila de llamadas).
    """
    # TODO: implementa la función
    pass


# =============================================================================
# PARTE 2 — FIBONACCI
# =============================================================================

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci recursivamente.
    ⚠️  Esta implementación es ineficiente: O(2^n) llamadas.
    Solo para propósitos de análisis y trazado.
    """
    # TODO: implementa la versión ingenua (sin memoización)
    pass


@lru_cache(maxsize=None)
def fibonacci_memoizado(n):
    """
    Calcula el n-ésimo número de Fibonacci con memoización.
    O(n) tiempo, O(n) espacio.
    """
    # TODO: implementa con memoización usando el decorador @lru_cache
    pass


def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci iterativamente.
    O(n) tiempo, O(1) espacio.
    """
    # TODO: implementa sin recursividad
    pass


# =============================================================================
# PARTE 3 — TORRES DE HANOI
# =============================================================================

movimientos = []  # lista global para registrar los movimientos

def torres_de_hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de Torres de Hanoi para n discos.
    Parámetros:
        n:         número de discos a mover
        origen:    poste donde están los n discos al inicio
        destino:   poste al que deben llegar todos los discos
        auxiliar:  poste auxiliar
    Efecto: agrega strings a `movimientos` con cada movimiento.
    Complejidad: O(2^n - 1) movimientos.
    """
    # TODO: implementa la solución recursiva
    # Recuerda:
    #   1. Mover n-1 discos de origen a auxiliar (usando destino como aux)
    #   2. Mover el disco n (el más grande) de origen a destino
    #   3. Mover n-1 discos de auxiliar a destino (usando origen como aux)
    pass


# =============================================================================
# PARTE 4 — TRAZADO CON IA (obligatorio)
# =============================================================================
"""
INSTRUCCIONES:
1. Ejecuta fibonacci_recursivo(5) en tu mente o en papel primero.
2. Luego consulta un asistente de IA con este prompt:
   "Muéstrame el trazado paso a paso de la pila de llamadas de fibonacci(5)
    usando la versión recursiva simple (sin memoización). Usa indentación para
    mostrar la jerarquía de llamadas."
3. Copia el trazado que generó la IA en el espacio de abajo.
4. Reescríbelo CON TUS PROPIAS PALABRAS en el espacio "Trazado propio".
   Dibuja también el diagrama ASCII de la pila de llamadas.

TRAZADO GENERADO POR IA:
[pega aquí el texto que generó el asistente de IA]


TRAZADO PROPIO (reescrito por el estudiante, sin copiar de la IA):
[escribe aquí tu explicación con tus propias palabras]


DIAGRAMA ASCII DE LA PILA DE LLAMADAS (dibujado por ti):
[dibuja aquí la pila de llamadas paso a paso]
"""


# =============================================================================
# CASOS DE PRUEBA Y COMPARACIÓN DE TIEMPOS
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 1 — Factorial")
    print("=" * 55)
    for n in [0, 1, 5, 10]:
        print(f"  factorial({n}) = {factorial(n)}")

    print("\n" + "=" * 55)
    print("PARTE 2 — Fibonacci: comparación de eficiencia")
    print("=" * 55)
    casos = [10, 20, 30, 35]
    for n in casos:
        t0 = time.perf_counter()
        r = fibonacci_recursivo(n)
        t_rec = time.perf_counter() - t0

        t0 = time.perf_counter()
        m = fibonacci_memoizado(n)
        t_mem = time.perf_counter() - t0

        t0 = time.perf_counter()
        i = fibonacci_iterativo(n)
        t_it = time.perf_counter() - t0

        assert r == m == i, f"Discrepancia en fib({n}): {r}, {m}, {i}"
        print(f"  fib({n:2d}) = {r:10d} | recursivo: {t_rec:.4f}s | memo: {t_mem:.6f}s | iter: {t_it:.6f}s")

    print("\n" + "=" * 55)
    print("PARTE 3 — Torres de Hanoi (n=3)")
    print("=" * 55)
    movimientos.clear()
    torres_de_hanoi(3, "A", "C", "B")
    print(f"  Total de movimientos para n=3: {len(movimientos)} (esperado: 7)")
    for mov in movimientos:
        print(f"  {mov}")

    print(f"\n  Para n=10: {2**10 - 1} movimientos (2^10 - 1)")
    print(f"  Para n=20: {2**20 - 1:,} movimientos — ¿ves por qué O(2^n) escala mal?")
