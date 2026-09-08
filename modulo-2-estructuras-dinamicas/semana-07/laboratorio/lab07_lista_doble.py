"""
Lab 7 — Lista Doblemente Enlazada
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""


class NodoDoble:
    """Nodo con referencias al nodo anterior y al siguiente."""

    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDoblementeEnlazada:
    """
    Lista doblemente enlazada.
    Permite inserción y eliminación en ambos extremos en O(1).
    Permite recorrido en ambas direcciones.
    """

    def __init__(self):
        self._cabeza = None  # primer nodo
        self._cola = None    # último nodo
        self._tamanio = 0

    # ------------------------------------------------------------------
    # INSERCIÓN
    # ------------------------------------------------------------------

    def insertar_inicio(self, dato):
        """Inserta dato al inicio. O(1)."""
        nuevo = NodoDoble(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo
            self._cabeza = nuevo
        self._tamanio += 1

    def insertar_final(self, dato):
        """Inserta dato al final. O(1)."""
        # TODO
        pass

    def insertar_en_posicion(self, posicion, dato):
        """Inserta en la posición dada (0-indexed). O(n)."""
        # TODO: casos: posición 0 → insertar_inicio, posición >= tamaño → insertar_final
        pass

    # ------------------------------------------------------------------
    # ELIMINACIÓN
    # ------------------------------------------------------------------

    def eliminar_inicio(self):
        """Elimina y retorna el dato del inicio. Lanza IndexError si vacía."""
        if self._cabeza is None:
            raise IndexError("lista vacía")
        dato = self._cabeza.dato
        if self._cabeza == self._cola:  # único elemento
            self._cabeza = None
            self._cola = None
        else:
            self._cabeza = self._cabeza.siguiente
            self._cabeza.anterior = None
        self._tamanio -= 1
        return dato

    def eliminar_final(self):
        """Elimina y retorna el dato del final. O(1)."""
        # TODO: usa self._cola; ajusta self._cola.anterior
        pass

    def eliminar(self, dato):
        """Elimina la primera ocurrencia de dato. Retorna True si se encontró."""
        # TODO: recorre desde la cabeza buscando el dato;
        #       al encontrarlo, desconecta ajustando anterior y siguiente del nodo vecino
        pass

    # ------------------------------------------------------------------
    # RECORRIDO
    # ------------------------------------------------------------------

    def recorrer_adelante(self):
        """Retorna lista con datos desde la cabeza hasta la cola."""
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def recorrer_atras(self):
        """Retorna lista con datos desde la cola hasta la cabeza."""
        resultado = []
        actual = self._cola
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.anterior
        return resultado

    # ------------------------------------------------------------------
    # UTILIDADES
    # ------------------------------------------------------------------

    def tamanio(self):
        return self._tamanio

    def es_vacia(self):
        return self._cabeza is None

    def __str__(self):
        datos = self.recorrer_adelante()
        return "None ← " + " ⇄ ".join(str(d) for d in datos) + " → None"


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Pruebas de ListaDoblementeEnlazada")
    print("=" * 55)

    lista = ListaDoblementeEnlazada()

    print("\n--- Insertar al inicio y al final ---")
    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    lista.insertar_final(30)
    lista.insertar_final(40)
    print(lista)
    print(f"Hacia atrás: {lista.recorrer_atras()}")

    print("\n--- Insertar en posición 2 ---")
    lista.insertar_en_posicion(2, 25)
    print(lista)

    print(f"\n--- Tamaño: {lista.tamanio()} ---")

    print("\n--- Eliminar inicio ---")
    print(f"  Eliminado: {lista.eliminar_inicio()}")
    print(lista)

    print("\n--- Eliminar final ---")
    print(f"  Eliminado: {lista.eliminar_final()}")
    print(lista)

    print("\n--- Eliminar 25 (del medio) ---")
    print(f"  ¿Encontrado? {lista.eliminar(25)}")
    print(lista)

    print("\n--- Eliminar 99 (no existe) ---")
    print(f"  ¿Encontrado? {lista.eliminar(99)}")

    print(f"\n--- Recorrido final hacia atrás: {lista.recorrer_atras()} ---")

    print("\n--- Verificación de consistencia ---")
    adelante = lista.recorrer_adelante()
    atras = lista.recorrer_atras()
    print(f"  Adelante: {adelante}")
    print(f"  Atrás:    {atras}")
    print(f"  ¿Consistente? {adelante == list(reversed(atras))}")
