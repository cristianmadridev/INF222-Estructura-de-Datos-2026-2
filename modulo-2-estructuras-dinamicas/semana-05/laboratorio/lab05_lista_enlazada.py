"""
Lab 5 — Lista Enlazada Simple
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""


class Nodo:
    """Nodo de una lista enlazada simple."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """
    Lista enlazada simple con referencia a la cabeza.
    Los nodos NO son accesibles directamente desde el exterior;
    toda operación se hace a través de los métodos de esta clase.
    """

    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    # ------------------------------------------------------------------
    # INSERCIÓN
    # ------------------------------------------------------------------

    def insertar_inicio(self, dato):
        """Inserta dato al inicio de la lista. O(1)."""
        # TODO
        pass

    def insertar_final(self, dato):
        """Inserta dato al final de la lista. O(n)."""
        # TODO: recorre hasta el último nodo, luego enlaza el nuevo
        pass

    def insertar_en_posicion(self, posicion, dato):
        """
        Inserta dato en la posición indicada (0-indexed).
        posición 0 equivale a insertar_inicio.
        Si posición >= tamaño, inserta al final.
        O(n).
        """
        # TODO
        pass

    # ------------------------------------------------------------------
    # ELIMINACIÓN
    # ------------------------------------------------------------------

    def eliminar(self, dato):
        """
        Elimina la primera ocurrencia de dato en la lista.
        Retorna True si se encontró y eliminó, False si no existe.
        Casos borde: eliminar la cabeza, eliminar un nodo intermedio,
                     eliminar el único nodo, dato no existe.
        O(n).
        """
        # TODO
        pass

    def eliminar_en_posicion(self, posicion):
        """
        Elimina el nodo en la posición indicada (0-indexed).
        Lanza IndexError si la posición está fuera de rango.
        O(n).
        """
        # TODO
        pass

    # ------------------------------------------------------------------
    # BÚSQUEDA Y ACCESO
    # ------------------------------------------------------------------

    def buscar(self, dato):
        """
        Retorna True si dato está en la lista, False si no.
        O(n).
        """
        # TODO
        pass

    def obtener(self, indice):
        """
        Retorna el dato en la posición `indice` (0-indexed).
        Lanza IndexError si el índice está fuera de rango.
        O(n).
        """
        # TODO (tarea / trabajo autónomo)
        pass

    # ------------------------------------------------------------------
    # OTROS
    # ------------------------------------------------------------------

    def invertir(self):
        """
        Invierte la lista in situ (sin crear nuevos nodos, solo re-enlaza).
        O(n).
        Ejemplo: [1→2→3] queda como [3→2→1]
        """
        # TODO (tarea / trabajo autónomo)
        # Pista: necesitas tres punteros: anterior, actual, siguiente
        pass

    def tamanio(self):
        """Retorna el número de elementos. O(1)."""
        return self._tamanio

    def es_vacia(self):
        """Retorna True si la lista no tiene elementos."""
        return self._cabeza is None

    def __str__(self):
        """Representación: cabeza → [1] → [2] → [3] → None"""
        nodos = []
        actual = self._cabeza
        while actual is not None:
            nodos.append(str(actual.dato))
            actual = actual.siguiente
        return "cabeza → " + " → ".join(nodos) + " → None"

    def __len__(self):
        return self._tamanio


# =============================================================================
# COMPARACIÓN EMPÍRICA DE TIEMPOS
# =============================================================================

def comparar_tiempos_insercion_inicio(n=10_000):
    """
    Compara el tiempo de insertar n elementos al inicio:
    - Lista de Python (insert(0, dato)) → O(n) por operación → O(n²) total
    - ListaEnlazada (insertar_inicio(dato)) → O(1) por operación → O(n) total
    """
    import time

    # Lista de Python
    lista_python = []
    t0 = time.perf_counter()
    for i in range(n):
        lista_python.insert(0, i)
    t1 = time.perf_counter()
    tiempo_python = t1 - t0

    # Lista Enlazada
    lista_enlazada = ListaEnlazada()
    t0 = time.perf_counter()
    for i in range(n):
        lista_enlazada.insertar_inicio(i)
    t1 = time.perf_counter()
    tiempo_enlazada = t1 - t0

    print(f"\nInserción al inicio de {n:,} elementos:")
    print(f"  Lista de Python:  {tiempo_python:.4f} s")
    print(f"  Lista Enlazada:   {tiempo_enlazada:.4f} s")
    if tiempo_python > 0:
        print(f"  Razón:            {tiempo_python / tiempo_enlazada:.1f}× más rápida la enlazada")


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Pruebas de ListaEnlazada")
    print("=" * 55)

    lista = ListaEnlazada()

    print("\n--- Insertar al inicio ---")
    lista.insertar_inicio(30)
    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    print(lista)  # esperado: cabeza → [10] → [20] → [30] → None

    print("\n--- Insertar al final ---")
    lista.insertar_final(40)
    lista.insertar_final(50)
    print(lista)  # esperado: ... → [40] → [50] → None

    print("\n--- Insertar en posición 2 ---")
    lista.insertar_en_posicion(2, 25)
    print(lista)  # esperado: [10] → [20] → [25] → [30] → [40] → [50]

    print(f"\n--- Tamaño: {len(lista)} (esperado: 6) ---")

    print("\n--- Buscar ---")
    print(f"  buscar(25): {lista.buscar(25)}  (esperado: True)")
    print(f"  buscar(99): {lista.buscar(99)}  (esperado: False)")

    print("\n--- Eliminar el primero (10) ---")
    lista.eliminar(10)
    print(lista)

    print("\n--- Eliminar del medio (30) ---")
    lista.eliminar(30)
    print(lista)

    print("\n--- Eliminar el último (50) ---")
    lista.eliminar(50)
    print(lista)

    print("\n--- Eliminar valor inexistente (99) ---")
    print(f"  resultado: {lista.eliminar(99)}  (esperado: False)")
    print(lista)

    print("\n--- Invertir lista ---")
    lista.invertir()
    print(lista)  # el orden debe haberse invertido

    print("\n--- Comparación de tiempos ---")
    comparar_tiempos_insercion_inicio(n=50_000)
