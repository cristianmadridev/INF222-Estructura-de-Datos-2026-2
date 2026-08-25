"""
Lab 9 — Algoritmos de Ordenación y Comparación de Eficiencia
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""

import time
import random


# =============================================================================
# ALGORITMOS DE ORDENACIÓN
# Implementa cada función. IMPORTANTE: trabaja sobre una COPIA del arreglo
# (usa lista[:] o list(lista)) para no alterar el original en las comparaciones.
# =============================================================================

def burbuja(arr):
    """
    Ordena arr de menor a mayor usando bubble sort.
    Optimización: si en una pasada no hubo intercambios, el arreglo ya está ordenado.
    Retorna la lista ordenada (copia, no modifica el original).
    Complejidad: O(n) mejor caso (con flag), O(n²) promedio y peor caso.
    """
    lista = list(arr)  # trabaja sobre copia
    n = len(lista)
    # TODO: implementa burbuja con el flag de optimización
    return lista


def seleccion(arr):
    """
    Ordena arr de menor a mayor usando selection sort.
    En cada iteración, encuentra el mínimo del resto y lo lleva a su posición.
    Retorna la lista ordenada (copia).
    Complejidad: O(n²) en todos los casos.
    """
    lista = list(arr)
    n = len(lista)
    # TODO: implementa seleccion
    return lista


def insercion(arr):
    """
    Ordena arr de menor a mayor usando insertion sort.
    Eficiente para arreglos pequeños o casi ordenados.
    Retorna la lista ordenada (copia).
    Complejidad: O(n) mejor caso (casi ordenado), O(n²) promedio y peor caso.
    """
    lista = list(arr)
    # TODO: implementa insercion
    return lista


# =============================================================================
# AMPLIACIÓN OPCIONAL: merge sort (O(n log n))
# =============================================================================

def merge_sort(arr):
    """
    Ordena arr usando merge sort (dividir y vencer).
    Retorna una nueva lista ordenada.
    Complejidad: O(n log n) en todos los casos. No es in situ (requiere memoria extra).
    """
    # TODO (opcional / ampliación)
    pass


# =============================================================================
# GENERADORES DE ARREGLOS DE PRUEBA
# =============================================================================

def arreglo_aleatorio(n, minval=1, maxval=10_000):
    return [random.randint(minval, maxval) for _ in range(n)]

def arreglo_ordenado(n):
    return list(range(1, n + 1))

def arreglo_invertido(n):
    return list(range(n, 0, -1))

def arreglo_casi_ordenado(n, swaps=5):
    arr = list(range(1, n + 1))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# =============================================================================
# FUNCIÓN DE MEDICIÓN
# =============================================================================

def medir_tiempo(algoritmo, arr):
    """Ejecuta `algoritmo(arr)` y retorna (resultado, segundos)."""
    t0 = time.perf_counter()
    resultado = algoritmo(arr)
    t1 = time.perf_counter()
    return resultado, t1 - t0


# =============================================================================
# VERIFICACIÓN DE CORRECTITUD
# =============================================================================

def verificar_todos(casos_prueba):
    """Verifica que los tres algoritmos producen el mismo resultado que sorted()."""
    print("Verificando correctitud...")
    for desc, arr in casos_prueba:
        esperado = sorted(arr)
        for nombre, func in [("burbuja", burbuja), ("seleccion", seleccion), ("insercion", insercion)]:
            resultado = func(arr)
            ok = resultado == esperado
            print(f"  [{('OK' if ok else 'ERROR')}] {nombre:10s} en '{desc}'")
            if not ok:
                print(f"       esperado: {esperado[:10]}...")
                print(f"       obtenido: {resultado[:10]}...")


# =============================================================================
# EXPERIMENTO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    random.seed(42)

    # Verificación con arreglos pequeños
    casos_prueba = [
        ("vacío", []),
        ("un elemento", [5]),
        ("ya ordenado", [1, 2, 3, 4, 5]),
        ("invertido", [5, 4, 3, 2, 1]),
        ("aleatorio", [3, 1, 4, 1, 5, 9, 2, 6]),
    ]
    verificar_todos(casos_prueba)

    print("\n" + "=" * 65)
    print("Comparación de tiempos (en segundos)")
    print("=" * 65)

    tamanios = [100, 1_000, 5_000, 10_000]
    tipos = [
        ("aleatorio", arreglo_aleatorio),
        ("ordenado",  arreglo_ordenado),
        ("invertido", arreglo_invertido),
    ]

    encabezado = f"{'N':>7} | {'tipo':>10} | {'burbuja':>10} | {'seleccion':>10} | {'insercion':>10}"
    print(encabezado)
    print("-" * len(encabezado))

    for n in tamanios:
        for desc, generador in tipos:
            arr = generador(n)
            _, t_burbuja   = medir_tiempo(burbuja,   arr)
            _, t_seleccion = medir_tiempo(seleccion, arr)
            _, t_insercion = medir_tiempo(insercion, arr)
            print(f"{n:>7,} | {desc:>10} | {t_burbuja:>10.4f} | {t_seleccion:>10.4f} | {t_insercion:>10.4f}")

    print("\n¿Qué observas? Escribe tus conclusiones aquí:")
    print("  1. ___________")
    print("  2. ___________")
    print("  3. ___________")
