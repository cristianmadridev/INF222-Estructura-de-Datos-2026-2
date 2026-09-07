"""
Lab 1 — Implementación de la clase Pila (Stack)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: __________cristian Madrid_______________
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
        self._datos.append(dato)
        if self.is_empty():
            raise IndexError("No se puede hacer pop de una pila vacía")

        return self._datos.pop()

def peek(self):
    """
    Retorna (sin eliminar) el elemento del tope de la pila.
    Lanza IndexError si la pila está vacía.
    Complejidad: O(1).
    """
    # TODO: implementa este método
    if self.is_empty():
        raise IndexError("No se puede hacer peek de una pila vacía")

    return self._datos[-1]



    def is_empty(self):
     """
    Retorna True si la pila no contiene elementos, False en caso contrario.
    Complejidad: O(1).
    """
    # TODO: implementa este método
    return len(self._datos) == 0

    def size(self):
     """
    Retorna el número de elementos en la pila.
    Complejidad: O(1).
    """
    # TODO: implementa este método
    return len(self._datos)

    def __str__(self):
     """
    Retorna una representación legible de la pila.
    Formato sugerido: Pila (tope -> base): [3, 2, 1]
    Complejidad: O(n).
    """
    # TODO: implementa este método
    return f"Pila (tope -> base): {list(reversed(self._datos))}"



#CASOS DE PRUEBA
# Agrega aquí al menos 5 casos de prueba. Usa print() para mostrar resultados
# y verifica que cada caso produce la salida esperada.


# Caso 1: Pila vacía
# TODO: crea una pila vacía y verifica is_empty()

    pila = Pila()

    if pila.is_empty():
     print("Caso 1: OK - la pila está vacía")
    else:
     print("Caso 1: ERROR - la pila debería estar vacía")


# Caso 2: push de 3 elementos
# TODO: agrega 3 elementos y verifica size()
    pila.push(1)
    pila.push(2)
    pila.push(3)

    if pila.size() == 3:
     print("Caso 2: OK - la pila tiene 3 elementos")
    else:
     print("Caso 2: ERROR - la pila debería tener 3 elementos")

     # Caso 3: peek sin modificar la pila
# TODO: verifica que peek retorna el tope y la pila no cambiatamaño_antes = pila.size()
    tope = pila.peek()
    tamaño_despues = pila.size()

    print("Elemento del tope:", tope)

    if tope == 3 and tamaño_antes == tamaño_despues:
     print("Caso 3: OK - peek() funciona correctamente")
    else:
     print("Caso 3: ERROR - peek() no funciona correctamente")

     # Caso 4: pop retorna el tope
# TODO: haz pop y verifica el valor retornado

    elemento = pila.pop()

    print("Elemento eliminado:", elemento)

    if elemento == 3:
     print("Caso 4: OK - pop() retornó el tope")
    else:
     print("Caso 4: ERROR - pop() no retornó el elemento correcto")

     # Caso 5: pop en pila vacía lanza IndexError
# TODO: usa try/except para verificar que se lanza IndexError

pila_vacia = Pila()

try:
    pila_vacia.pop()
    print("Caso 5: ERROR - no se lanzó IndexError")
except IndexError:
    print("Caso 5: OK - se lanzó IndexError correctamente")





if __name__ == "__main__":
    print("=" * 50)
    print("Pruebas de la clase Pila")
    print("=" * 50)

   
