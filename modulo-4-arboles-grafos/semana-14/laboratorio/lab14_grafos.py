"""
Lab 14 — Grafos: representación, BFS y DFS
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""

from collections import deque


class Grafo:
    """
    Grafo no dirigido representado con lista de adyacencia.
    Los vértices pueden ser cualquier valor hashable (entero, string, etc.).
    """

    def __init__(self):
        self._lista_adyacencia = {}  # {vértice: [vecinos]}

    def agregar_vertice(self, v):
        """Agrega el vértice v si no existe. O(1)."""
        if v not in self._lista_adyacencia:
            self._lista_adyacencia[v] = []

    def agregar_arista(self, v1, v2):
        """
        Agrega una arista NO DIRIGIDA entre v1 y v2.
        Agrega los vértices si no existen.
        O(1).
        """
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)
        # TODO: agrega v2 a la lista de v1 Y v1 a la lista de v2
        pass

    def vecinos(self, v):
        """Retorna la lista de vecinos del vértice v."""
        return self._lista_adyacencia.get(v, [])

    def vertices(self):
        """Retorna la lista de todos los vértices."""
        return list(self._lista_adyacencia.keys())

    def __str__(self):
        """Representación legible de la lista de adyacencia."""
        lineas = []
        for v, vecinos in self._lista_adyacencia.items():
            lineas.append(f"  {v} → {vecinos}")
        return "Grafo:\n" + "\n".join(lineas)

    # ------------------------------------------------------------------
    # RECORRIDOS
    # ------------------------------------------------------------------

    def bfs(self, inicio):
        """
        Recorrido en anchura (Breadth-First Search) desde el vértice `inicio`.
        Usa una cola (deque).
        Retorna una lista con los vértices en el orden en que fueron visitados.
        """
        visitados = set()
        orden_visita = []
        cola = deque()

        # TODO: implementa BFS
        # 1. Agrega `inicio` a la cola y al set de visitados
        # 2. Mientras la cola no esté vacía:
        #    a. Saca el vértice del frente (popleft)
        #    b. Agrégalo a orden_visita
        #    c. Para cada vecino no visitado: márcalo como visitado y agrégalo a la cola

        return orden_visita

    def dfs_iterativo(self, inicio):
        """
        Recorrido en profundidad (Depth-First Search) desde `inicio`.
        Versión iterativa: usa una pila (list de Python).
        Retorna la lista de vértices en orden de visita.
        """
        visitados = set()
        orden_visita = []
        pila = [inicio]

        # TODO: implementa DFS iterativo con pila
        # Nota: la pila produce un orden diferente al DFS recursivo;
        # ambos son DFS válidos.

        return orden_visita

    def dfs_recursivo(self, inicio):
        """
        Recorrido en profundidad desde `inicio` usando recursividad.
        Retorna la lista de vértices en orden de visita.
        """
        visitados = set()
        orden_visita = []

        def _dfs(v):
            # TODO: marca v como visitado, agrégalo a orden_visita
            # luego llama _dfs recursivamente sobre sus vecinos no visitados
            pass

        _dfs(inicio)
        return orden_visita

    def camino_bfs(self, inicio, fin):
        """
        Retorna el camino más corto (en número de aristas) de `inicio` a `fin`
        usando BFS. Retorna una lista de vértices que forman el camino,
        o None si no existe camino.
        """
        # TODO: modifica BFS para registrar el predecesor de cada vértice
        # Luego reconstruye el camino desde `fin` hasta `inicio` usando el mapa de predecesores
        pass


# =============================================================================
# CONSTRUCCIÓN DE GRAFO DE EJEMPLO
# =============================================================================

def grafo_ejemplo_1():
    """
    Grafo:  A - B - D
            |   |
            C   E
    """
    g = Grafo()
    for arista in [("A","B"), ("A","C"), ("B","D"), ("B","E")]:
        g.agregar_arista(*arista)
    return g


def grafo_ciudades_panama():
    """
    Red simplificada de ciudades de Panamá conectadas por rutas.
    """
    g = Grafo()
    rutas = [
        ("Ciudad de Panamá", "La Chorrera"),
        ("Ciudad de Panamá", "Colón"),
        ("Ciudad de Panamá", "Chepo"),
        ("La Chorrera", "Arraiján"),
        ("La Chorrera", "Penonomé"),
        ("Penonomé", "Santiago"),
        ("Santiago", "Chitré"),
        ("Chitré", "Las Tablas"),
        ("Colón", "Portobelo"),
    ]
    for v1, v2 in rutas:
        g.agregar_arista(v1, v2)
    return g


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Grafo de ejemplo 1")
    print("=" * 55)
    g1 = grafo_ejemplo_1()
    print(g1)

    print(f"\nBFS desde A:           {g1.bfs('A')}")
    print(f"DFS iterativo desde A: {g1.dfs_iterativo('A')}")
    print(f"DFS recursivo desde A: {g1.dfs_recursivo('A')}")

    print("\n" + "=" * 55)
    print("Red de ciudades de Panamá")
    print("=" * 55)
    g2 = grafo_ciudades_panama()
    print(g2)

    inicio = "Ciudad de Panamá"
    print(f"\nBFS desde '{inicio}':")
    for v in g2.bfs(inicio):
        print(f"  {v}")

    print(f"\nCamino más corto de 'Ciudad de Panamá' a 'Las Tablas':")
    camino = g2.camino_bfs("Ciudad de Panamá", "Las Tablas")
    if camino:
        print("  " + " → ".join(camino))
    else:
        print("  No existe camino")
