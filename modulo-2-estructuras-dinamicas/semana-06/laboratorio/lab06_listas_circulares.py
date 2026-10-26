"""
Lab 6 — Listas Circulares y Problema de Josephus
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# =============================================================================
# PARTE 1: LISTA ENLAZADA CIRCULAR
# El último nodo apunta al primero (no a None).
# =============================================================================
class ListaCircular:
    """
    Lista enlazada circular. El atributo `_cola` apunta al ÚLTIMO nodo
    (cuyo `siguiente` es el primer nodo). Esto permite insertar al
    inicio y al final en O(1).
    """

    def __init__(self):
        self._cola = None   # nodo del final; _cola.siguiente = primer nodo
        self._tamanio = 0

    def insertar_inicio(self, dato):
        """Inserta dato al inicio de la lista. O(1)."""
        nuevo = Nodo(dato)
        if self._cola is None:
            nuevo.siguiente = nuevo  # apunta a sí mismo (único nodo)
            self._cola = nuevo
        else:
            nuevo.siguiente = self._cola.siguiente  # nuevo → primero
            self._cola.siguiente = nuevo            # cola → nuevo (ahora es el primero)
        self._tamanio += 1

    def insertar_final(self, dato):
        """Inserta dato al final de la lista. O(1)."""
        self.insertar_inicio(dato)         # inserta al inicio...
        self._cola = self._cola.siguiente  # ...y avanza la cola: el nuevo es el último

    def eliminar_inicio(self):
        """Elimina y retorna el dato del inicio. Lanza IndexError si está vacía."""
        if self._cola is None:
            raise IndexError("eliminar en lista circular vacía")
        primero = self._cola.siguiente
        if primero is self._cola:    # solo un nodo
            self._cola = None
        else:
            self._cola.siguiente = primero.siguiente
        self._tamanio -= 1
        return primero.dato

    def recorrer(self):
        """Retorna una lista con todos los datos en orden desde el inicio."""
        resultado = []
        if self._cola is None:
            return resultado
        actual = self._cola.siguiente  # primero
        for _ in range(self._tamanio):
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def es_vacia(self):
        return self._cola is None

    def tamanio(self):
        return self._tamanio

    def __str__(self):
        datos = self.recorrer()
        if not datos:
            return "Lista circular vacía"
        return " → ".join(str(d) for d in datos) + " → (inicio)"


# =============================================================================
# PARTE 2: LISTA CIRCULAR CON NODO CABEZA (SENTINELA)
# Hay un nodo fijo (centinela) que no contiene dato útil.
# La lista está vacía cuando centinela.siguiente == centinela.
# =============================================================================

class ListaCircularConCabeza:
    """
    Lista enlazada circular con nodo centinela.
    El centinela siempre existe (no puede eliminarse).
    La lista vacía: centinela.siguiente = centinela.
    """

    def __init__(self):
        self._centinela = Nodo(None)
        self._centinela.siguiente = self._centinela
        self._tamanio = 0

    def insertar_inicio(self, dato):
        """Inserta dato justo después del centinela (al inicio lógico). O(1)."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self._centinela.siguiente
        self._centinela.siguiente = nuevo
        self._tamanio += 1

    def insertar_final(self, dato):
        """Inserta dato justo antes del centinela (al final). O(n) sin puntero al final."""
        anterior = self._centinela
        while anterior.siguiente is not self._centinela:  # buscar el último nodo
            anterior = anterior.siguiente
        nuevo = Nodo(dato)
        nuevo.siguiente = self._centinela   # el nuevo cierra el círculo
        anterior.siguiente = nuevo
        self._tamanio += 1

    def eliminar(self, dato):
        """Elimina la primera ocurrencia de dato. Retorna True si se encontró."""
        anterior = self._centinela
        actual = self._centinela.siguiente
        while actual is not self._centinela:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente   # saltar el nodo
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def recorrer(self):
        """Retorna lista con todos los datos desde el inicio hasta antes del centinela."""
        resultado = []
        actual = self._centinela.siguiente
        while actual is not self._centinela:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def es_vacia(self):
        return self._centinela.siguiente is self._centinela

    def __str__(self):
        datos = self.recorrer()
        if not datos:
            return "[C] → [C] (vacía)"
        return "[C] → " + " → ".join(str(d) for d in datos) + " → [C]"


# =============================================================================
# PARTE 3: PROBLEMA DE JOSEPHUS
# n personas en círculo, contar hasta k, eliminar, repetir.
# =============================================================================

def josephus(n, k):
    """
    Resuelve el problema de Josephus usando ListaCircular.
    n: número de personas (numeradas del 1 al n)
    k: cuenta hasta k para eliminar a alguien
    Retorna: el número de la persona que sobrevive.
    """
    if n <= 0 or k <= 0:
        raise ValueError("Para Josephus se requieren n > 0 y k > 0.")

    lista = ListaCircular()
    for i in range(1, n + 1):
        lista.insertar_final(i)

    anterior = lista._cola          # nodo anterior al primero (la persona 1)
    while lista.tamanio() > 1:
        for _ in range(k - 1):      # avanzar hasta el nodo anterior al k-ésimo
            anterior = anterior.siguiente
        eliminado = anterior.siguiente
        anterior.siguiente = eliminado.siguiente   # sacar al k-ésimo del círculo
        lista._tamanio -= 1
        lista._cola = anterior      # mantener la lista consistente

    return lista._cola.dato         # único sobreviviente


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 1: Lista Circular")
    print("=" * 55)
    lc = ListaCircular()
    lc.insertar_final(1)
    lc.insertar_final(2)
    lc.insertar_final(3)
    lc.insertar_inicio(0)
    print(lc)           # 0 → 1 → 2 → 3 → (inicio)
    print(f"Tamaño: {lc.tamanio()}")
    dato = lc.eliminar_inicio()
    print(f"Eliminado del inicio: {dato}")
    print(lc)           # 1 → 2 → 3 → (inicio)

    print("\n" + "=" * 55)
    print("PARTE 2: Lista Circular con Nodo Cabeza")
    print("=" * 55)
    lcc = ListaCircularConCabeza()
    print(f"¿Vacía? {lcc.es_vacia()}")
    lcc.insertar_inicio(10)
    lcc.insertar_inicio(20)
    lcc.insertar_final(5)
    print(lcc)           # [C] → 20 → 10 → 5 → [C]
    lcc.eliminar(10)
    print(f"Después de eliminar 10: {lcc}")

    print("\n" + "=" * 55)
    print("PARTE 3: Problema de Josephus")
    print("=" * 55)
    print(f"josephus(7, 3) = {josephus(7, 3)}  (esperado: 4)")
    print(f"josephus(5, 2) = {josephus(5, 2)}  (esperado: 3)")
    print(f"josephus(1, 5) = {josephus(1, 5)}  (esperado: 1)")