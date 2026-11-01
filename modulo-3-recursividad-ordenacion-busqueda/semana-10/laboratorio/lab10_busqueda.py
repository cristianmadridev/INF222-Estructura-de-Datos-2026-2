"""
Lab 10 — Búsqueda Secuencial y Binaria
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""

import random
import time


# =============================================================================
# BÚSQUEDA SECUENCIAL (LINEAL)
# =============================================================================

def busqueda_secuencial(arr, objetivo):
    """
    Recorre el arreglo elemento por elemento hasta encontrar el objetivo.
    Funciona en arreglos NO ordenados.
    Complejidad: O(1) mejor caso, O(n) promedio y peor caso.
    """
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


# =============================================================================
# BÚSQUEDA BINARIA
# PRECONDICIÓN: el arreglo DEBE estar ordenado de menor a mayor.
# =============================================================================

def busqueda_binaria_iterativa(arr, objetivo):
    """
    Mantiene los punteros izquierda y derecha y divide el espacio a la mitad.
    Complejidad: O(log n). Espacio extra: O(1).
    """
    izquierda = 0
    derecha = len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1   # buscar en la mitad derecha
        else:
            derecha = medio - 1     # buscar en la mitad izquierda
    return -1


def busqueda_binaria_recursiva(arr, objetivo, izquierda=0, derecha=None):
    """
    Versión recursiva: cada llamada trabaja sobre el rango [izquierda, derecha].
    Se usan índices en lugar de cortar el arreglo (arr[:mid]) para no copiar
    la lista en cada llamada, lo que costaría O(n) y arruinaría el O(log n).
    Complejidad: O(log n). Espacio extra: O(log n) por la pila de llamadas.
    """
    if derecha is None:
        derecha = len(arr) - 1
    if izquierda > derecha:          # caso base: no encontrado
        return -1
    medio = (izquierda + derecha) // 2
    if arr[medio] == objetivo:       # caso base: encontrado
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, izquierda, medio - 1)


# =============================================================================
# TRAZADO (opcional, para entender el algoritmo)
# =============================================================================

def busqueda_binaria_con_traza(arr, objetivo):
    """Igual que la iterativa, pero imprime cada iteración (como en clase)."""
    izquierda, derecha = 0, len(arr) - 1
    iteracion = 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        print(f"  Iteración {iteracion}: izq={izquierda}, der={derecha}, "
              f"mid={medio} → arr[{medio}]={arr[medio]}", end=" ")
        if arr[medio] == objetivo:
            print(f"== {objetivo} → ¡ENCONTRADO en pos {medio}!")
            return medio
        elif arr[medio] < objetivo:
            print(f"< {objetivo} → buscar en la mitad derecha")
            izquierda = medio + 1
        else:
            print(f"> {objetivo} → buscar en la mitad izquierda")
            derecha = medio - 1
        iteracion += 1
    print(f"  izq={izquierda} > der={derecha} → NO ENCONTRADO")
    return -1


# =============================================================================
# FUNCIÓN DE MEDICIÓN
# =============================================================================

def medir_tiempo(funcion, arr, objetivo, repeticiones=1):
    """
    Ejecuta funcion(arr, objetivo) `repeticiones` veces.
    Retorna (resultado, segundos_promedio_por_busqueda).
    Se repite porque una sola búsqueda binaria dura microsegundos.
    """
    t0 = time.perf_counter()
    for _ in range(repeticiones):
        resultado = funcion(arr, objetivo)
    t1 = time.perf_counter()
    return resultado, (t1 - t0) / repeticiones


# =============================================================================
# VERIFICACIÓN DE CORRECTITUD
# =============================================================================

def verificar_todos():
    print("Verificando correctitud...")
    funciones = [
        ("secuencial", busqueda_secuencial),
        ("binaria iter.", busqueda_binaria_iterativa),
        ("binaria recur.", busqueda_binaria_recursiva),
    ]
    arr = [5, 10, 20, 30, 40, 50, 60, 70, 80]
    casos = [
        ("arreglo vacío",           [],      7,  -1),
        ("un elemento (está)",      [7],     7,   0),
        ("un elemento (no está)",   [7],     3,  -1),
        ("primer elemento",         arr,     5,   0),
        ("último elemento",         arr,     80,  8),
        ("elemento del medio (40)", arr,     40,  4),
        ("no existe (35)",          arr,     35, -1),
        ("menor que todos",         arr,     1,  -1),
        ("mayor que todos",         arr,     99, -1),
    ]
    todo_ok = True
    for desc, a, objetivo, esperado in casos:
        for nombre, f in funciones:
            obtenido = f(a, objetivo)
            ok = obtenido == esperado
            todo_ok = todo_ok and ok
            print(f"  [{'OK' if ok else 'ERROR'}] {nombre:14s} en '{desc}'")
            if not ok:
                print(f"       esperado: {esperado}, obtenido: {obtenido}")

    # La secuencial sí debe funcionar en un arreglo desordenado
    desordenado = [42, 7, 19, 3, 88, 1]
    ok = busqueda_secuencial(desordenado, 88) == 4
    todo_ok = todo_ok and ok
    print(f"  [{'OK' if ok else 'ERROR'}] secuencial     en 'arreglo desordenado'")

    print("\n" + ("Todas las pruebas pasaron." if todo_ok else "HAY ERRORES."))


# =============================================================================
# EXPERIMENTO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    random.seed(42)

    verificar_todos()

    # Trazado de clase
    arr_clase = [5, 10, 20, 30, 40, 50, 60, 70, 80]
    print("\n" + "=" * 70)
    print("Trazado de búsqueda binaria en", arr_clase)
    print("=" * 70)
    print("Buscar 40:")
    busqueda_binaria_con_traza(arr_clase, 40)
    print("Buscar 35:")
    busqueda_binaria_con_traza(arr_clase, 35)

    # Comparación de tiempos
    print("\n" + "=" * 78)
    print("Comparación de tiempos (segundos por búsqueda, promedio)")
    print("Caso evaluado: el objetivo NO está (peor caso para ambas)")
    print("=" * 78)

    tamanios = [1_000, 10_000, 100_000, 1_000_000]
    encabezado = (f"{'N':>10} | {'secuencial':>12} | {'binaria iter.':>13} | "
                  f"{'binaria recur.':>14} | {'seq / bin':>10}")
    print(encabezado)
    print("-" * len(encabezado))

    for n in tamanios:
        arr = list(range(0, 2 * n, 2))   # pares ordenados: 0, 2, 4, ...
        objetivo = -1                    # impar, nunca está: peor caso

        # Menos repeticiones para la secuencial porque es mucho más lenta
        reps_seq = max(1, 200_000 // n)
        reps_bin = 20_000

        _, t_seq   = medir_tiempo(busqueda_secuencial,         arr, objetivo, reps_seq)
        _, t_iter  = medir_tiempo(busqueda_binaria_iterativa,  arr, objetivo, reps_bin)
        _, t_recur = medir_tiempo(busqueda_binaria_recursiva,  arr, objetivo, reps_bin)

        razon = t_seq / t_iter if t_iter > 0 else float("inf")
        print(f"{n:>10,} | {t_seq:>12.8f} | {t_iter:>13.8f} | "
              f"{t_recur:>14.8f} | {razon:>9.0f}x")

    print("\n¿Qué observas? Escribe tus conclusiones aquí:")
    print("  1. ___________")
    print("  2. ___________")
    print("  3. ___________")
   # https://www.youtube.com/watch?v=Ds61hiuBcOk Donde busque la informacion
   # Claude