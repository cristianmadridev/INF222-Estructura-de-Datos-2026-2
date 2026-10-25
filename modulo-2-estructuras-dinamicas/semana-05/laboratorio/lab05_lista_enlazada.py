"""Lab 5 — Lista Enlazada Simple.

INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""

import time


class Nodo:
    """Nodo de una lista enlazada simple: guarda un dato y la referencia al siguiente."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """Lista enlazada simple con referencia a la cabeza, a la cola y un contador."""

    def __init__(self):
        self.cabeza = None
        self.cola = None      # permite insertar al final en O(1)
        self._tamano = 0      # permite obtener la longitud en O(1)

    # ---------------- Insercion ----------------
    def insertar_inicio(self, dato):
        """O(1): el nuevo nodo apunta a la antigua cabeza y pasa a ser la cabeza."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        if self.cola is None:         # la lista estaba vacia
            self.cola = nuevo
        self._tamano += 1

    def insertar_final(self, dato):
        """O(1) gracias al puntero a la cola (O(n) si hubiera que recorrer)."""
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self._tamano += 1

    def insertar_en_posicion(self, pos, dato):
        """O(n): inserta de modo que el nuevo dato quede en el indice `pos`.
        Lanza IndexError si pos < 0 o pos > longitud."""
        if pos < 0 or pos > self._tamano:
            raise IndexError(f"Posicion {pos} fuera de rango (0..{self._tamano})")
        if pos == 0:
            self.insertar_inicio(dato)
            return
        if pos == self._tamano:
            self.insertar_final(dato)
            return
        anterior = self.cabeza
        for _ in range(pos - 1):          # llegar al nodo anterior a la posicion
            anterior = anterior.siguiente
        nuevo = Nodo(dato)
        nuevo.siguiente = anterior.siguiente
        anterior.siguiente = nuevo
        self._tamano += 1

    # ---------------- Eliminacion ----------------
    def eliminar(self, dato):
        """O(n): elimina la primera aparicion de `dato`. Retorna True/False."""
        anterior = None
        actual = self.cabeza
        while actual is not None and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if actual is None:                # no existe
            return False
        self._desenlazar(anterior, actual)
        return True

    def eliminar_en_posicion(self, pos):
        """O(n): elimina el nodo en el indice `pos` y retorna su dato."""
        if pos < 0 or pos >= self._tamano:
            raise IndexError(f"Posicion {pos} fuera de rango (0..{self._tamano - 1})")
        anterior = None
        actual = self.cabeza
        for _ in range(pos):
            anterior = actual
            actual = actual.siguiente
        dato = actual.dato
        self._desenlazar(anterior, actual)
        return dato

    def _desenlazar(self, anterior, actual):
        """Quita `actual` de la lista (casos: primero, intermedio, ultimo)."""
        if anterior is None:              # era la cabeza
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        if actual is self.cola:           # era la cola
            self.cola = anterior
        self._tamano -= 1

    # ---------------- Consulta ----------------
    def buscar(self, dato):
        """O(n): retorna el indice de la primera aparicion o -1."""
        actual, i = self.cabeza, 0
        while actual is not None:
            if actual.dato == dato:
                return i
            actual = actual.siguiente
            i += 1
        return -1

    def obtener(self, indice):
        """O(n): retorna el dato en `indice` (admite negativos como Python)."""
        if indice < 0:
            indice += self._tamano
        if indice < 0 or indice >= self._tamano:
            raise IndexError("Indice fuera de rango")
        actual = self.cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.dato

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        """O(1) gracias al contador."""
        return self._tamano

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def recorrer(self):
        """O(n): imprime cada elemento."""
        for dato in self:
            print(dato)

    def __str__(self):
        return " -> ".join(str(d) for d in self) + " -> None" if self.cabeza else "None"

    # ---------------- Tarea ----------------
    def invertir(self):
        """O(n) tiempo, O(1) espacio: invierte la lista in situ, sin crear nodos."""
        anterior = None
        actual = self.cabeza
        self.cola = self.cabeza           # la antigua cabeza sera la nueva cola
        while actual is not None:
            siguiente = actual.siguiente  # 1. guardar el resto
            actual.siguiente = anterior   # 2. invertir el enlace
            anterior = actual             # 3. avanzar
            actual = siguiente
        self.cabeza = anterior


# ======================================================================
# Pruebas (casos borde)
# ======================================================================
def pruebas():
    # Lista vacia
    l = ListaEnlazada()
    assert len(l) == 0 and l.esta_vacia() and str(l) == "None"
    assert l.buscar(1) == -1
    assert l.eliminar(1) is False
    l.invertir()
    assert str(l) == "None"
    try:
        l.obtener(0); assert False
    except IndexError:
        pass

    # Un solo elemento
    l.insertar_inicio(10)
    assert l.cabeza is l.cola and len(l) == 1
    l.invertir()
    assert list(l) == [10]
    assert l.eliminar(10) is True
    assert l.cabeza is None and l.cola is None and len(l) == 0

    # Inserciones
    for x in (20, 10):
        l.insertar_inicio(x)             # 10, 20
    l.insertar_final(30)                 # 10, 20, 30
    l.insertar_en_posicion(1, 15)        # 10, 15, 20, 30
    l.insertar_en_posicion(0, 5)         # 5, 10, 15, 20, 30
    l.insertar_en_posicion(5, 99)        # 5, 10, 15, 20, 30, 99
    assert list(l) == [5, 10, 15, 20, 30, 99] and len(l) == 6

    # Posicion fuera de rango
    for pos in (-1, 7):
        try:
            l.insertar_en_posicion(pos, 0); assert False
        except IndexError:
            pass

    # Eliminar: primero, intermedio, ultimo, inexistente
    assert l.eliminar(5) and list(l) == [10, 15, 20, 30, 99]
    assert l.eliminar(20) and list(l) == [10, 15, 30, 99]
    assert l.eliminar(99) and list(l) == [10, 15, 30] and l.cola.dato == 30
    assert l.eliminar(1234) is False
    assert l.eliminar_en_posicion(1) == 15 and list(l) == [10, 30]

    # Buscar y obtener
    assert l.buscar(30) == 1 and l.buscar(7) == -1
    assert l.obtener(0) == 10 and l.obtener(-1) == 30

    # Invertir
    for x in (40, 50):
        l.insertar_final(x)              # 10, 30, 40, 50
    ids_antes = {id(n) for n in nodos(l)}
    l.invertir()
    assert list(l) == [50, 40, 30, 10]
    assert {id(n) for n in nodos(l)} == ids_antes     # mismos nodos
    assert l.cola.dato == 10
    l.insertar_final(0)                  # la cola sigue valida
    assert list(l) == [50, 40, 30, 10, 0]
    print("Todas las pruebas pasaron correctamente.")


def nodos(lista):
    actual = lista.cabeza
    while actual:
        yield actual
        actual = actual.siguiente


# ======================================================================
# Comparacion empirica: insertar al inicio
# ======================================================================
def comparar_tiempos(tamanos=(1_000, 5_000, 10_000, 20_000, 40_000)):
    print(f"{'n':>8} | {'list.insert(0)':>15} | {'insertar_inicio':>16}")
    print("-" * 46)
    resultados = []
    for n in tamanos:
        py = []
        t0 = time.perf_counter()
        for i in range(n):
            py.insert(0, i)
        t_py = time.perf_counter() - t0

        le = ListaEnlazada()
        t0 = time.perf_counter()
        for i in range(n):
            le.insertar_inicio(i)
        t_le = time.perf_counter() - t0

        resultados.append((n, t_py, t_le))
        print(f"{n:>8} | {t_py:>13.5f} s | {t_le:>14.5f} s")
    return resultados


if __name__ == "__main__":
    pruebas()
    comparar_tiempos()