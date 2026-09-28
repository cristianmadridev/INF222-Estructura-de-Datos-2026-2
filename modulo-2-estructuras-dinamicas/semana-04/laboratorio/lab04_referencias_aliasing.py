"""
Lab 4 — Referencias y Aliasing en Python
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: _________________________
Grupo: ______________________________
Fecha: ______________________________

Instrucciones:
    Para cada fragmento de código, PRIMERO escribe tu predicción en el comentario
    "PREDICCIÓN:", LUEGO ejecuta y registra el resultado real en "RESULTADO:".
    Usa Python Tutor para visualizar el estado de la memoria.
"""

# Listas (mutables): MISMO objeto
a = [1, 2, 3]
b = a            # b no copia nada, apunta a la misma lista
b[0] = 99        # mutas a través de b
print(a)         # [99, 2, 3]  <- a también cambió
print(a is b)    # True

# Números (inmutables): no se pueden mutar
x = 42
y = x
y = y + 1        # crea un int nuevo (43) y y pasa a apuntar a él
print(x)         # 42  <- x no cambió
print(x is y)    # False