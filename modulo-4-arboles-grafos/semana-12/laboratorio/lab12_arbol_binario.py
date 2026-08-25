"""
Lab 12 — Árbol Binario y Recorridos
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""

from collections import deque  # para el recorrido por niveles (tarea)


class NodoArbol:
    """Nodo de un árbol binario."""

    def __init__(self, dato):
        self.dato = dato
        self.hijo_izq = None
        self.hijo_der = None

    def __str__(self):
        return str(self.dato)


class ArbolBinario:
    """
    Árbol binario con recorridos implementados de forma recursiva.
    La inserción es manual (no BST): el usuario construye el árbol
    asignando directamente hijo_izq e hijo_der a los nodos.
    """

    def __init__(self):
        self.raiz = None

    # ------------------------------------------------------------------
    # RECORRIDOS RECURSIVOS
    # ------------------------------------------------------------------

    def inorden(self, nodo=None, primera_llamada=True):
        """
        Recorrido inorden: izquierda → raíz → derecha.
        Retorna una lista con los datos en el orden visitado.
        """
        if primera_llamada:
            nodo = self.raiz
        # TODO: implementa la recursividad
        # Caso base: nodo is None → retornar []
        # Caso recursivo: inorden(izq) + [nodo.dato] + inorden(der)
        pass

    def preorden(self, nodo=None, primera_llamada=True):
        """
        Recorrido preorden: raíz → izquierda → derecha.
        Retorna una lista con los datos en el orden visitado.
        """
        if primera_llamada:
            nodo = self.raiz
        # TODO
        pass

    def postorden(self, nodo=None, primera_llamada=True):
        """
        Recorrido postorden: izquierda → derecha → raíz.
        Retorna una lista con los datos en el orden visitado.
        """
        if primera_llamada:
            nodo = self.raiz
        # TODO
        pass

    def por_niveles(self):
        """
        Recorrido por niveles (BFS): visita los nodos de arriba hacia abajo,
        izquierda a derecha dentro de cada nivel. Usa una cola.
        TAREA (trabajo autónomo): implementa este método.
        Retorna una lista con los datos en el orden visitado.
        """
        # TODO (tarea): usa una deque como cola
        # Agrega la raíz a la cola
        # Mientras la cola no esté vacía:
        #   - Saca el nodo del frente
        #   - Agrega su dato a la lista de resultado
        #   - Agrega sus hijos (no None) a la cola
        pass

    # ------------------------------------------------------------------
    # UTILIDADES
    # ------------------------------------------------------------------

    def altura(self, nodo=None, primera_llamada=True):
        """
        Retorna la altura del árbol (número de niveles - 1).
        Árbol vacío → -1. Solo la raíz → 0.
        """
        if primera_llamada:
            nodo = self.raiz
        if nodo is None:
            return -1
        # TODO: altura = 1 + max(altura(izq), altura(der))
        pass

    def contar_nodos(self, nodo=None, primera_llamada=True):
        """Retorna el número de nodos en el árbol."""
        if primera_llamada:
            nodo = self.raiz
        if nodo is None:
            return 0
        # TODO
        pass


# =============================================================================
# CONSTRUCCIÓN MANUAL DEL ÁRBOL DE EJEMPLO
# =============================================================================

def construir_arbol_ejemplo():
    """
    Construye el árbol:
            10
           /  \
          5    20
         / \     \
        3   7    30
    """
    arbol = ArbolBinario()

    # raíz
    arbol.raiz = NodoArbol(10)

    # nivel 1
    arbol.raiz.hijo_izq = NodoArbol(5)
    arbol.raiz.hijo_der = NodoArbol(20)

    # nivel 2
    arbol.raiz.hijo_izq.hijo_izq = NodoArbol(3)
    arbol.raiz.hijo_izq.hijo_der = NodoArbol(7)
    arbol.raiz.hijo_der.hijo_der = NodoArbol(30)

    return arbol


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    arbol = construir_arbol_ejemplo()

    print("Árbol de ejemplo:")
    print("        10")
    print("       /  \\")
    print("      5    20")
    print("     / \\     \\")
    print("    3   7    30")
    print()

    inorden   = arbol.inorden()
    preorden  = arbol.preorden()
    postorden = arbol.postorden()
    niveles   = arbol.por_niveles()

    print(f"Inorden    (izq-raíz-der): {inorden}")
    print(f"  Esperado:                [3, 5, 7, 10, 20, 30]")
    print(f"  {'OK' if inorden == [3, 5, 7, 10, 20, 30] else 'ERROR'}")

    print(f"\nPreorden   (raíz-izq-der): {preorden}")
    print(f"  Esperado:                [10, 5, 3, 7, 20, 30]")
    print(f"  {'OK' if preorden == [10, 5, 3, 7, 20, 30] else 'ERROR'}")

    print(f"\nPostorden  (izq-der-raíz): {postorden}")
    print(f"  Esperado:                [3, 7, 5, 30, 20, 10]")
    print(f"  {'OK' if postorden == [3, 7, 5, 30, 20, 10] else 'ERROR'}")

    print(f"\nPor niveles (tarea):       {niveles}")
    print(f"  Esperado:                [10, 5, 20, 3, 7, 30]")

    print(f"\nAltura del árbol: {arbol.altura()} (esperado: 2)")
    print(f"Número de nodos:  {arbol.contar_nodos()} (esperado: 6)")

    # Árbol vacío
    vacio = ArbolBinario()
    print(f"\nÁrbol vacío — altura: {vacio.altura()} (esperado: -1)")
    print(f"Árbol vacío — nodos:  {vacio.contar_nodos()} (esperado: 0)")
    print(f"Árbol vacío — inorden: {vacio.inorden()} (esperado: [])")
