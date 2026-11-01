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

# Laboratorio 8 - Recursividad + trazado con IA declarada
# Módulo 3: Recursividad, ordenación y búsqueda - Semana 8
#
# === DECLARACIÓN DE USO DE IA ===
# Asistente utilizado: (Claude / ChatGPT / Copilot)
# Para qué lo usé: obtener el trazado paso a paso de fibonacci(5).
# Qué pedí exactamente: el archivo del laboratorio con las funciones, una
# explicación del trazado de fibonacci(5) y por qué es ineficiente.
# Qué entendí y qué corregí/modifiqué: La función baja por la pila hasta un
# caso base y desde ahí va sumando los resultados al subir. Vi que fib(3) y
# fib(2) se calculan varias veces, por eso es lento. Reescribí la explicación
# con mis palabras, dibujé yo el diagrama de la pila y ejecuté el programa
# para comprobar que fibonacci(5) da 5 y que Hanoi da 15 y 31 movimientos.
# ================================================


# ---------------------------------------------------------------
# 1. Factorial (recursividad directa)
# ---------------------------------------------------------------
def factorial(n):
    """Retorna n! de forma recursiva."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n == 0:              # caso base
        return 1
    return n * factorial(n - 1)   # caso recursivo


# ---------------------------------------------------------------
# 2. Fibonacci
# ---------------------------------------------------------------
def fibonacci(n):
    """Fibonacci recursivo ingenuo: O(2^n). Solo para n pequeño."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n <= 1:              # casos base
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterativo(n):
    """Versión iterativa: O(n)."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ---------------------------------------------------------------
# 3. Torres de Hanoi
# ---------------------------------------------------------------
def torres_de_hanoi(n, origen="A", destino="C", auxiliar="B", movimientos=None):
    """
    Mueve n discos de origen a destino usando auxiliar.
    Retorna la lista de movimientos [(disco, desde, hacia), ...].
    """
    if movimientos is None:
        movimientos = []
    if n == 0:              # caso base
        return movimientos
    torres_de_hanoi(n - 1, origen, auxiliar, destino, movimientos)
    movimientos.append((n, origen, destino))
    torres_de_hanoi(n - 1, auxiliar, destino, origen, movimientos)
    return movimientos


# ---------------------------------------------------------------
# TRAZADO DE fibonacci(5) - ESCRÍBELO CON TUS PROPIAS PALABRAS
# ---------------------------------------------------------------
# Explicación (con mis palabras):
#
#   (escribe aquí cómo se ejecuta fibonacci(5): qué llama a qué,
#    cuándo se llega a los casos base y cómo se suman los resultados)
#
# Diagrama ASCII de la pila de llamadas (dibujado por mí):
#
#   (dibújalo aquí)
#
# ¿Por qué es ineficiente? (con mis palabras):
#
#   (explica qué llamadas se repiten)
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("factorial(4) =", factorial(4))            # 24
    print("fibonacci(5) =", fibonacci(5))            # 5
    print("fibonacci_iterativo(5) =", fibonacci_iterativo(5))

    for n in (4, 5):
        movs = torres_de_hanoi(n)
        print(f"\nHanoi n={n}: {len(movs)} movimientos (esperado {2**n - 1})")
        for m in movs:
            print(f"  disco {m[0]}: {m[1]} -> {m[2]}")