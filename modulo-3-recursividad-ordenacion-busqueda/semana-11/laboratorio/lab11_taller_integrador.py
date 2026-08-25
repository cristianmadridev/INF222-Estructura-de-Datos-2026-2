"""
Lab 11 — Taller Integrador: Ordenación + Búsqueda + Recursión
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________

Este taller integra los tres grandes temas del Módulo 3. Deberás:
  - Elegir el algoritmo de ordenación más adecuado según el contexto.
  - Aplicar búsqueda binaria sobre la colección ordenada.
  - Diseñar una solución recursiva para un sub-problema.
  - Justificar las complejidades en las celdas marcadas como [ANÁLISIS].
"""

import time
import random


# =============================================================================
# PARTE 1: AGENDA DE CONTACTOS (ordenación + búsqueda)
# =============================================================================
# Un sistema simple de agenda ordena contactos por apellido y permite
# buscarlos por nombre completo de manera eficiente.

CONTACTOS_EJEMPLO = [
    {"nombre": "Carlos", "apellido": "Zúñiga",   "telefono": "6001-0001"},
    {"nombre": "María",  "apellido": "Alvarado",  "telefono": "6001-0002"},
    {"nombre": "Luis",   "apellido": "Morales",   "telefono": "6001-0003"},
    {"nombre": "Ana",    "apellido": "Batista",   "telefono": "6001-0004"},
    {"nombre": "Pedro",  "apellido": "Rodríguez", "telefono": "6001-0005"},
    {"nombre": "Sandra", "apellido": "López",     "telefono": "6001-0006"},
    {"nombre": "Jorge",  "apellido": "Chávez",    "telefono": "6001-0007"},
    {"nombre": "Elena",  "apellido": "Morales",   "telefono": "6001-0008"},  # mismo apellido que Luis
]


def ordenar_contactos(contactos):
    """
    Ordena `contactos` (lista de dict) por 'apellido' y, en caso de empate,
    por 'nombre'. Debe retornar UNA NUEVA lista ordenada.
    Elige el algoritmo que consideres más adecuado para este caso.
    Justifica aquí: [ANÁLISIS] ¿Por qué elegiste ese algoritmo?
    Complejidad esperada: ...
    """
    # TODO
    pass


def buscar_por_apellido(contactos_ordenados, apellido_buscado):
    """
    Busca TODOS los contactos cuyo 'apellido' == apellido_buscado.
    `contactos_ordenados` ya está ordenado por apellido.
    Retorna lista de contactos encontrados (puede ser más de uno).

    Estrategia sugerida:
      1. Usa búsqueda binaria para encontrar CUALQUIER coincidencia.
      2. Luego expande hacia la izquierda y la derecha para capturar todas.
    Complejidad esperada: O(log n + k) donde k = número de coincidencias.
    """
    # TODO
    pass


# =============================================================================
# PARTE 2: ESTADÍSTICAS RECURSIVAS
# =============================================================================

def suma_recursiva(nums):
    """
    Calcula la suma de `nums` usando recursión (sin usar sum()).
    Caso base: lista vacía → 0
    Complejidad: O(n).
    """
    # TODO
    pass


def maximo_recursivo(nums):
    """
    Encuentra el máximo de `nums` usando recursión (sin usar max()).
    Caso base: lista de un elemento → ese elemento.
    Complejidad: O(n).
    """
    # TODO
    pass


def cuenta_mayores_recursivo(nums, umbral, i=0):
    """
    Cuenta cuántos elementos de nums[i:] son estrictamente mayores que umbral.
    Usa recursión de cola.
    Complejidad: O(n).
    """
    # TODO
    pass


# =============================================================================
# PARTE 3: POTENCIAS Y EXPONENCIACIÓN RÁPIDA
# =============================================================================

def potencia_lenta(base, exp):
    """
    Calcula base^exp multiplicando una a una (O(n)).
    Ya implementada — úsala como referencia.
    """
    if exp == 0:
        return 1
    return base * potencia_lenta(base, exp - 1)


def potencia_rapida(base, exp):
    """
    Calcula base^exp con exponenciación por cuadrado.
    Observación clave: base^exp = (base^(exp//2))^2  si exp es par
                                  base * base^(exp-1) si exp es impar
    Complejidad: O(log n) — reduce el exponent a la mitad en cada paso.
    """
    if exp == 0:
        return 1
    # TODO: implementa los casos par e impar
    pass


# =============================================================================
# PARTE 4: PROBLEMA INTEGRADOR — TOP-K PRODUCTOS
# =============================================================================
# Dado un catálogo de productos con precios, encontrar los K más baratos
# de forma eficiente.

CATALOGO = [
    {"nombre": "Audífonos BT",     "precio": 45.99},
    {"nombre": "Cargador USB-C",   "precio": 12.50},
    {"nombre": "Funda celular",    "precio": 8.99},
    {"nombre": "Teclado inalám.",  "precio": 35.00},
    {"nombre": "Mouse ergonómico", "precio": 28.75},
    {"nombre": "Webcam HD",        "precio": 55.00},
    {"nombre": "Hub USB 4 puertos","precio": 18.00},
    {"nombre": "Soporte laptop",   "precio": 22.50},
    {"nombre": "Cable HDMI 2m",    "precio": 9.99},
    {"nombre": "Parlante portátil","precio": 39.00},
]


def top_k_baratos(catalogo, k):
    """
    Retorna los k productos más baratos del catálogo, ordenados de menor
    a mayor precio.
    PISTA: ordena primero y luego usa rebanado de lista.
    Complejidad: O(n log n + k).
    """
    # TODO
    pass


def rango_precio(catalogo_ordenado, precio_min, precio_max):
    """
    Usando el catálogo YA ORDENADO por precio, retorna todos los
    productos cuyo precio está en [precio_min, precio_max].
    Usa búsqueda binaria para encontrar los extremos del rango.
    Complejidad: O(log n + k).
    """
    # TODO: usa bisect o tu propia búsqueda binaria sobre los precios
    # Tip: extrae una lista de solo precios para facilitar la búsqueda binaria
    pass


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":

    # ---- PARTE 1 ----
    print("=" * 60)
    print("PARTE 1: Agenda de Contactos")
    print("=" * 60)

    ordenados = ordenar_contactos(CONTACTOS_EJEMPLO)
    if ordenados:
        print("Contactos ordenados:")
        for c in ordenados:
            print(f"  {c['apellido']:15} {c['nombre']:10} {c['telefono']}")

        encontrados = buscar_por_apellido(ordenados, "Morales")
        print(f"\nBúsqueda 'Morales': {len(encontrados) if encontrados else 0} resultado(s)")
        for c in (encontrados or []):
            print(f"  {c['nombre']} {c['apellido']} — {c['telefono']}")

        no_encontrado = buscar_por_apellido(ordenados, "García")
        print(f"Búsqueda 'García': {no_encontrado}")  # esperado: [] o None

    # ---- PARTE 2 ----
    print("\n" + "=" * 60)
    print("PARTE 2: Estadísticas Recursivas")
    print("=" * 60)
    nums = [4, 7, 2, 9, 1, 5]
    print(f"Lista: {nums}")
    print(f"  suma_recursiva:           {suma_recursiva(nums)}  (esperado: 28)")
    print(f"  maximo_recursivo:         {maximo_recursivo(nums)}  (esperado: 9)")
    print(f"  cuenta_mayores(umbral=4): {cuenta_mayores_recursivo(nums, 4)}  (esperado: 3)")
    print(f"  suma_recursiva([]):       {suma_recursiva([])}  (esperado: 0)")

    # ---- PARTE 3 ----
    print("\n" + "=" * 60)
    print("PARTE 3: Potencias")
    print("=" * 60)
    pares_prueba = [(2, 10), (3, 5), (5, 0), (7, 3)]
    for base, exp in pares_prueba:
        lenta = potencia_lenta(base, exp)
        rapida = potencia_rapida(base, exp)
        estado = "OK" if lenta == rapida else "ERROR"
        print(f"  [{estado}] {base}^{exp} = {lenta} (rápida={rapida})")

    print("\nComparación de tiempos (base=2, exp=1000):")
    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_lenta(2, 1000)
    t_lenta = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_rapida(2, 1000)
    t_rapida = time.perf_counter() - t0

    print(f"  Lenta O(n):        {t_lenta:.4f}s")
    print(f"  Rápida O(log n):   {t_rapida:.4f}s")

    # ---- PARTE 4 ----
    print("\n" + "=" * 60)
    print("PARTE 4: Top-K Productos")
    print("=" * 60)
    baratos = top_k_baratos(CATALOGO, 3)
    print("Top-3 más baratos:")
    for p in (baratos or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    cat_ord = sorted(CATALOGO, key=lambda p: p['precio'])
    rango = rango_precio(cat_ord, 10.0, 30.0)
    print("\nProductos entre $10 y $30:")
    for p in (rango or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    # ---- REFLEXIÓN ----
    print("\n" + "=" * 60)
    print("REFLEXIÓN FINAL")
    print("=" * 60)
    print("""
[ANÁLISIS] Responde en el docstring o en un comentario:

1. ¿Qué algoritmo de ordenación elegiste en la Parte 1 y por qué
   es apropiado para ordenar una lista de dicts por apellido?

2. ¿Cuántas comparaciones haría la búsqueda binaria en una agenda
   de 1 000 contactos en el peor caso?

3. ¿Cuántas llamadas recursivas hace potencia_rapida(2, 64)?
   Dibuja el árbol de llamadas.
""")
