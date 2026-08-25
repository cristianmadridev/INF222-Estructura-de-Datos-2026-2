"""
Lab 1 — Implementación de la clase Pila (Stack)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________
"""


class Pila:
    """
    Implementación de una pila (stack) usando una lista de Python como
    contenedor interno. Principio LIFO: el último elemento insertado es
    el primero en salir.
    """

    def __init__(self):
        """Inicializa una pila vacía."""
        self._datos = []  # el tope de la pila está en el índice -1

    def push(self, dato):
        """
        Agrega `dato` al tope de la pila.
        Complejidad: O(1) amortizado.
        """
        # TODO: implementa este método
        pass

    def pop(self):
        """
        Elimina y retorna el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1) amortizado.
        """
        # TODO: implementa este método
        # Recuerda verificar si la pila está vacía antes de operar
        pass

    def peek(self):
        """
        Retorna (sin eliminar) el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        pass

    def is_empty(self):
        """
        Retorna True si la pila no contiene elementos, False en caso contrario.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        pass

    def size(self):
        """
        Retorna el número de elementos en la pila.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        pass

    def __str__(self):
        """
        Retorna una representación legible de la pila.
        Formato sugerido: Pila (tope -> base): [3, 2, 1]
        Complejidad: O(n).
        """
        # TODO: implementa este método
        pass


# =============================================================================
# CASOS DE PRUEBA
# Agrega aquí al menos 5 casos de prueba. Usa print() para mostrar resultados
# y verifica que cada caso produce la salida esperada.
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Pruebas de la clase Pila")
    print("=" * 50)

    # Caso 1: Pila vacía
    # TODO: crea una pila vacía y verifica is_empty()

    # Caso 2: push de 3 elementos
    # TODO: agrega 3 elementos y verifica size()

    # Caso 3: peek sin modificar la pila
    # TODO: verifica que peek retorna el tope y la pila no cambia

    # Caso 4: pop retorna el tope
    # TODO: haz pop y verifica el valor retornado

    # Caso 5: pop en pila vacía lanza IndexError
    # TODO: usa try/except para verificar que se lanza IndexError

    # Caso 6 en adelante: agrega tus propios casos de prueba
    # ...
