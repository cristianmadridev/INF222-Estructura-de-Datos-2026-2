"""
Lab 13 — Árbol Binario de Búsqueda (BST)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""

import random


# =============================================================================
# NODO DEL BST
# =============================================================================

class NodoBST:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


# =============================================================================
# ÁRBOL BINARIO DE BÚSQUEDA
# =============================================================================

class BST:
    """
    Árbol Binario de Búsqueda (Binary Search Tree).
    Invariante: para todo nodo n:
      - todos los nodos del subárbol izquierdo tienen dato < n.dato
      - todos los nodos del subárbol derecho tienen dato > n.dato
    No se almacenan duplicados.
    """

    def __init__(self):
        self._raiz = None

    # ------------------------------------------------------------------
    # INSERCIÓN
    # ------------------------------------------------------------------

    def insertar(self, dato):
        """Inserta `dato` en el BST. Ignora duplicados. O(h)."""
        self._raiz = self._insertar_rec(self._raiz, dato)

    def _insertar_rec(self, nodo, dato):
        """
        Retorna el nodo raíz del subárbol actualizado.
        Caso base: nodo es None → crear hoja nueva.
        Si dato < nodo.dato: insertar en subárbol izquierdo.
        Si dato > nodo.dato: insertar en subárbol derecho.
        Si dato == nodo.dato: no hacer nada (sin duplicados).
        """
        # TODO
        pass

    # ------------------------------------------------------------------
    # BÚSQUEDA
    # ------------------------------------------------------------------

    def buscar(self, dato):
        """Retorna True si `dato` está en el BST, False si no. O(h)."""
        return self._buscar_rec(self._raiz, dato)

    def _buscar_rec(self, nodo, dato):
        """
        Caso base 1: nodo es None → no encontrado.
        Caso base 2: nodo.dato == dato → encontrado.
        Si dato < nodo.dato: buscar en subárbol izquierdo.
        Si dato > nodo.dato: buscar en subárbol derecho.
        """
        # TODO
        pass

    # ------------------------------------------------------------------
    # MÍNIMO Y MÁXIMO
    # ------------------------------------------------------------------

    def minimo(self):
        """Retorna el dato mínimo del BST. Lanza ValueError si está vacío."""
        if self._raiz is None:
            raise ValueError("árbol vacío")
        return self._minimo_nodo(self._raiz).dato

    def _minimo_nodo(self, nodo):
        """Navega hacia el nodo más a la izquierda (mínimo del subárbol)."""
        # TODO: recorre hacia la izquierda hasta que izquierdo sea None
        pass

    def maximo(self):
        """Retorna el dato máximo del BST."""
        if self._raiz is None:
            raise ValueError("árbol vacío")
        # TODO: recorre hacia la derecha hasta que derecho sea None
        pass

    # ------------------------------------------------------------------
    # ELIMINACIÓN
    # ------------------------------------------------------------------

    def eliminar(self, dato):
        """Elimina `dato` del BST si existe. O(h)."""
        self._raiz = self._eliminar_rec(self._raiz, dato)

    def _eliminar_rec(self, nodo, dato):
        """
        Retorna el nodo raíz del subárbol actualizado.

        Hay 3 casos para el nodo a eliminar:
          CASO 1 — Es una hoja (sin hijos):
            → Retornar None (eliminar el nodo).

          CASO 2 — Tiene un solo hijo:
            → Retornar el hijo que existe (el nodo desaparece).

          CASO 3 — Tiene dos hijos:
            → Encontrar el SUCESOR INORDEN (mínimo del subárbol derecho).
            → Copiar el dato del sucesor al nodo actual.
            → Eliminar el sucesor del subárbol derecho.
        """
        if nodo is None:
            return None  # dato no estaba en el árbol

        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar_rec(nodo.derecho, dato)
        else:
            # Encontrado — aplicar los 3 casos
            # TODO: implementa CASO 1, CASO 2 y CASO 3
            pass

        return nodo

    # ------------------------------------------------------------------
    # ALTURA Y TAMAÑO
    # ------------------------------------------------------------------

    def altura(self):
        """Altura del árbol (0 si vacío, 1 si solo raíz). O(n)."""
        return self._altura_rec(self._raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_rec(nodo.izquierdo),
                       self._altura_rec(nodo.derecho))

    def tamanio(self):
        """Número de nodos en el árbol. O(n)."""
        return self._tamanio_rec(self._raiz)

    def _tamanio_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._tamanio_rec(nodo.izquierdo) + self._tamanio_rec(nodo.derecho)

    # ------------------------------------------------------------------
    # RECORRIDOS
    # ------------------------------------------------------------------

    def inorden(self):
        """Retorna lista con los datos en orden ascendente. O(n)."""
        resultado = []
        self._inorden_rec(self._raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorden_rec(nodo.derecho, resultado)

    # ------------------------------------------------------------------
    # ÁRBOL DEGENERADO (comparación)
    # ------------------------------------------------------------------

    def construir_bst_degenerado(self, datos_ordenados):
        """
        Inserta datos_ordenados en orden → produce un árbol como lista enlazada.
        Útil para comparar el caso promedio vs. el peor caso de un BST.
        """
        bst = BST()
        for d in datos_ordenados:
            bst.insertar(d)
        return bst


# =============================================================================
# FUNCIONES DE VISUALIZACIÓN (no modificar)
# =============================================================================

def imprimir_arbol(nodo, prefijo="", es_derecho=True):
    """Imprime el árbol de forma visual rotada 90° (subárbol derecho arriba)."""
    if nodo is not None:
        imprimir_arbol(nodo.derecho, prefijo + ("│   " if es_derecho else "    "), True)
        print(prefijo + ("└── " if es_derecho else "┌── ") + str(nodo.dato))
        imprimir_arbol(nodo.izquierdo, prefijo + ("    " if es_derecho else "│   "), False)


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Construcción e inserción")
    print("=" * 55)
    bst = BST()
    valores = [50, 30, 70, 20, 40, 60, 80, 35, 45]
    for v in valores:
        bst.insertar(v)

    print("Árbol construido:")
    imprimir_arbol(bst._raiz)
    print(f"\nInorden (debe ser ascendente): {bst.inorden()}")
    print(f"Altura: {bst.altura()}  |  Tamaño: {bst.tamanio()}")

    print("\n" + "=" * 55)
    print("Búsqueda")
    print("=" * 55)
    for v, esperado in [(40, True), (55, False), (80, True), (1, False)]:
        resultado = bst.buscar(v)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] buscar({v}) = {resultado} (esperado: {esperado})")

    print("\n" + "=" * 55)
    print("Mínimo y máximo")
    print("=" * 55)
    print(f"  Mínimo: {bst.minimo()}  (esperado: 20)")
    print(f"  Máximo: {bst.maximo()}  (esperado: 80)")

    print("\n" + "=" * 55)
    print("Eliminación — CASO 1: hoja (20)")
    print("=" * 55)
    bst.eliminar(20)
    print(f"  Inorden: {bst.inorden()}")
    imprimir_arbol(bst._raiz)

    print("\n" + "=" * 55)
    print("Eliminación — CASO 2: un hijo (60, si tiene solo 1 hijo)")
    print("=" * 55)
    bst.insertar(55)   # 60 queda con solo hijo izquierdo 55
    bst.eliminar(60)
    print(f"  Inorden: {bst.inorden()}")

    print("\n" + "=" * 55)
    print("Eliminación — CASO 3: dos hijos (30)")
    print("=" * 55)
    bst.eliminar(30)
    print(f"  Inorden: {bst.inorden()}")
    imprimir_arbol(bst._raiz)

    print("\n" + "=" * 55)
    print("Árbol degenerado vs. balanceado")
    print("=" * 55)
    datos = list(range(1, 16))  # 1..15

    # BST con inserción ordenada (degenerado)
    bst_deg = BST()
    for d in datos:
        bst_deg.insertar(d)
    print(f"BST degenerado (insertos en orden 1..15):")
    print(f"  Altura: {bst_deg.altura()}  (esperado: 15 — lista enlazada)")

    # BST con inserción en orden aleatorio (balanceado en promedio)
    random.shuffle(datos)
    bst_bal = BST()
    for d in datos:
        bst_bal.insertar(d)
    print(f"BST mezclado (insertos en orden aleatorio):")
    print(f"  Altura: {bst_bal.altura()}  (esperado: ~4-5 en promedio)")
    print(f"  ¿Por qué la diferencia? [ANÁLISIS — responde en tu entrega]")
