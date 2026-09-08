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
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Crear dos nodos
nodo1 = Nodo(10)
nodo2 = Nodo(20)

# Conectar los nodos
nodo1.siguiente = nodo2


# Mostrar los datos
print("Primer nodo:", nodo1.dato)
print("Segundo nodo:", nodo1.siguiente.dato)

# =============================================================================
# PARTE 2: PILA ENLAZADA
# ==========================================================
class PilaEnlazada:
    """
    Pila implementada con nodos enlazados.
    El tope de la pila es la cabeza de la lista de nodos.
    """

    class Nodo:
     """Nodo básico."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """Pila implementada con nodos enlazados."""

    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self):
        if self.tope is None:
            raise IndexError("Pila vacía")

        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato


# Prueba
pila = Pila()

pila.push(10)
pila.push(20)

print("Sale:", pila.pop())
print("Sale:", pila.pop())

# =============================================================================
# PARTE 3: VERIFICADOR DE PARÉNTESIS BALANCEADOS
# =============================================================================

def parentesis_balanceados(cadena):
    pares = {')': '(', ']': '[', '}': '{'}
    aperturas = set(pares.values())

    pila = PilaEnlazada()

    for caracter in cadena:

        if caracter in aperturas:
            pila.push(caracter)

        elif caracter in pares:
            if pila.is_empty():
                return False

            if pila.pop() != pares[caracter]:
                return False

    return pila.is_empty()


# =============================================================================
# PARTE 4: COLA (QUEUE)
# =============================================================================

class Nodo:
    """Nodo básico."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    """Cola implementada con nodos enlazados."""

    def __init__(self):
        self.frente = None
        self.final = None

    def enqueue(self, dato):
        nuevo = Nodo(dato)

        if self.final is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def dequeue(self):
        if self.frente is None:
            raise IndexError("Cola vacía")

        dato = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        return dato


# Prueba
cola = Cola()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

print(cola.dequeue())
print(cola.dequeue())


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
    Simula una cola de impresión.
    Recibe una lista de tuplas (nombre, páginas).
    Imprime los trabajos en orden FIFO.
    """

    cola = Cola()
    total = 0

    # Encolar los trabajos
    for nombre, paginas in trabajos:
        trabajo = TrabajoImpresion(nombre, paginas)
        cola.enqueue(trabajo)

    # Desencolar e imprimir
    while not cola.is_empty():
        trabajo = cola.dequeue()

        print("Imprimiendo:", trabajo)

        total = total + trabajo.paginas

    print("Total de páginas impresas:", total)


# Prueba
trabajos = [
    ("Tesis cap1", 12),
    ("Factura", 1),
    ("Informe", 8)
]

simulador_impresion(trabajos)

# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("PARTE 2: Pila Enlazada")
    print("=" * 55)

    pila = PilaEnlazada()

    pila.push(10)
    pila.push(20)
    pila.push(30)

    print("Tope:", pila.peek())
    print("Sale:", pila.pop())
    print("Tope:", pila.peek())
    print("¿Está vacía?:", pila.is_empty())


    print("\n" + "=" * 55)
    print("PARTE 3: Verificador de Paréntesis Balanceados")
    print("=" * 55)

    casos = [
        ("({[]})", True),
        ("([)]", False),
        ("{[", False),
        ("", True),
        ("3 + (4 * [2])", True),
    ]

    for cadena, esperado in casos:
        resultado = parentesis_balanceados(cadena)
        estado = "OK" if resultado == esperado else "ERROR"

        print(f"  [{estado}] '{cadena}' → {resultado} "
              f"(esperado: {esperado})")


    print("\n" + "=" * 55)
    print("PARTE 4: Cola")
    print("=" * 55)

    cola = Cola()

    cola.enqueue(10)
    cola.enqueue(20)
    cola.enqueue(30)

    print("Frente:", cola.peek())
    print("Sale:", cola.dequeue())
    print("Frente:", cola.peek())
    print("¿Está vacía?:", cola.is_empty())


    print("\n" + "=" * 55)
    print("PARTE 5: Simulador de Impresión")
    print("=" * 55)

    trabajos = [
        ("Tesis cap1", 12),
        ("Factura", 1),
        ("Informe anual", 8),
        ("CV", 2)
    ]

    simulador_impresion(trabajos)