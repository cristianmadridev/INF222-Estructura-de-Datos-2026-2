"""
Lab 2 — Pila Enlazada, Cola y Simulador de Impresión
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""


# =============================================================================
# PARTE 1: NODO (base para la pila enlazada y la cola)
# =============================================================================

class Nodo:
    """Nodo básico con un dato y una referencia al siguiente nodo."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # referencia al próximo nodo


# =============================================================================
# PARTE 2: PILA ENLAZADA
# =============================================================================

class PilaEnlazada:
    """
    Pila implementada con nodos enlazados.
    El tope de la pila es la cabeza de la lista de nodos.
    """

    def __init__(self):
        self._cabeza = None  # nodo del tope (None si la pila está vacía)
        self._tamanio = 0

    def push(self, dato):
        """Inserta dato en el tope. Complejidad: O(1)."""
        # TODO: crea un nuevo Nodo, ponlo como nueva cabeza
        pass

    def pop(self):
        """Elimina y retorna el dato del tope. Lanza IndexError si está vacía."""
        # TODO: guarda el dato de la cabeza, avanza la cabeza al siguiente
        pass

    def peek(self):
        """Retorna (sin eliminar) el dato del tope. Lanza IndexError si está vacía."""
        # TODO
        pass

    def is_empty(self):
        """Retorna True si la pila está vacía."""
        return self._cabeza is None

    def size(self):
        """Retorna el número de elementos."""
        return self._tamanio

    def __str__(self):
        """Representación: tope → ... → base"""
        # TODO
        pass


# =============================================================================
# PARTE 3: VERIFICADOR DE PARÉNTESIS BALANCEADOS
# =============================================================================

def parentesis_balanceados(cadena):
    """
    Retorna True si todos los pares de paréntesis, corchetes y llaves
    en `cadena` están correctamente balanceados; False en caso contrario.
    Usa la clase PilaEnlazada.

    Ejemplos:
        parentesis_balanceados("({[]})")  → True
        parentesis_balanceados("([)]")    → False
        parentesis_balanceados("{[")      → False
    """
    # TODO: implementa el algoritmo con una PilaEnlazada
    # Tip: define un diccionario de pares cierre→apertura
    pares = {')': '(', ']': '[', '}': '{'}
    aperturas = set(pares.values())
    pass


# =============================================================================
# PARTE 4: COLA (QUEUE)
# =============================================================================

class Cola:
    """
    Cola implementada con nodos enlazados.
    - enqueue agrega al final (cola)
    - dequeue saca del frente (cabeza)
    """

    def __init__(self):
        self._frente = None  # nodo del frente (primer en salir)
        self._final = None   # nodo del final (último en entrar)
        self._tamanio = 0

    def enqueue(self, dato):
        """Agrega dato al final de la cola. Complejidad: O(1)."""
        # TODO
        pass

    def dequeue(self):
        """Elimina y retorna el dato del frente. Lanza IndexError si está vacía."""
        # TODO
        pass

    def front(self):
        """Retorna (sin eliminar) el dato del frente. Lanza IndexError si está vacía."""
        # TODO
        pass

    def is_empty(self):
        return self._frente is None

    def size(self):
        return self._tamanio

    def __str__(self):
        """Representación: frente → ... → final"""
        # TODO
        pass


# =============================================================================
# PARTE 5: SIMULADOR DE COLA DE IMPRESIÓN (mini-proyecto)
# =============================================================================

class TrabajoImpresion:
    """Representa un trabajo en la cola de impresión."""

    def __init__(self, nombre, paginas):
        self.nombre = nombre
        self.paginas = paginas

    def __str__(self):
        return f"'{self.nombre}' ({self.paginas} pág.)"


def simulador_impresion(trabajos):
    """
    Simula una cola de impresión. Recibe una lista de tuplas (nombre, páginas).
    Imprime en orden de llegada (FIFO) el nombre de cada trabajo y cuántas páginas tiene.
    Al final muestra el total de páginas impresas.

    Ejemplo de uso:
        trabajos = [("Tesis cap1", 12), ("Factura", 1), ("Informe", 8)]
        simulador_impresion(trabajos)
    """
    # TODO: encola todos los trabajos, luego deséncola uno por uno mostrando el progreso
    pass


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 2: Pila Enlazada")
    print("=" * 55)
    # TODO: prueba push, pop, peek, is_empty, size, __str__

    print("\n" + "=" * 55)
    print("PARTE 3: Verificador de Paréntesis Balanceados")
    print("=" * 55)
    casos = [
        ("({[]})", True),
        ("([)]", False),
        ("{[", False),
        ("", True),          # cadena vacía: balanceada por vacío
        ("3 + (4 * [2])", True),
    ]
    for cadena, esperado in casos:
        resultado = parentesis_balanceados(cadena)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] '{cadena}' → {resultado} (esperado: {esperado})")

    print("\n" + "=" * 55)
    print("PARTE 4: Cola")
    print("=" * 55)
    # TODO: prueba enqueue, dequeue, front, is_empty, size

    print("\n" + "=" * 55)
    print("PARTE 5: Simulador de Impresión")
    print("=" * 55)
    trabajos = [("Tesis cap1", 12), ("Factura", 1), ("Informe anual", 8), ("CV", 2)]
    simulador_impresion(trabajos)
