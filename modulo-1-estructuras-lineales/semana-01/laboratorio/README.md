# Lab 1 — Implementación de la clase Pila

**Semana 1 · INF 222 · Semestre 2026-2**

---

## Objetivo

Implementar una clase `Pila` (stack) en Python usando una lista como contenedor interno, aplicando el principio LIFO.

---

## Instrucciones

Abre el archivo `lab01_pila.py` que ya está en esta carpeta. Verás un esqueleto con la clase `Pila` y comentarios que indican qué implementar en cada método.

### Métodos a implementar

| Método | Descripción | Complejidad esperada |
|--------|-------------|---------------------|
| `push(dato)` | Agrega `dato` al tope de la pila | O(1) |
| `pop()` | Elimina y retorna el dato del tope; lanza `IndexError` si está vacía | O(1) |
| `peek()` | Retorna (sin eliminar) el dato del tope; lanza `IndexError` si está vacía | O(1) |
| `is_empty()` | Retorna `True` si la pila no tiene elementos | O(1) |
| `size()` | Retorna el número de elementos | O(1) |
| `__str__()` | Retorna una representación legible de la pila, tope a la izquierda | O(n) |

### Casos de prueba mínimos a incluir

En el bloque `if __name__ == "__main__":` al final del archivo, debes agregar **al menos los siguientes 5 casos de prueba**, más los que consideres necesarios:

1. Crear una pila vacía y verificar `is_empty()`.
2. Hacer `push` de 3 elementos y verificar que `size()` retorna 3.
3. Verificar que `peek()` retorna el elemento correcto sin modificar la pila.
4. Hacer `pop()` y verificar que retorna el último elemento insertado.
5. Intentar `pop()` en una pila vacía y verificar que lanza `IndexError`.

---

## Criterios de evaluación

| Criterio | Puntos |
|---------|--------|
| Métodos correctamente implementados (6 métodos × 10 pts) | 60 |
| Casos de prueba: mínimo 5, bien redactados y con verificación del resultado | 25 |
| Código legible (nombres descriptivos, lógica clara) | 10 |
| Commit con mensaje descriptivo y push en fecha | 5 |
| **Total** | **100** |

---

## Entrega

```bash
git add modulo-1-estructuras-lineales/semana-01/laboratorio/lab01_pila.py
git commit -m "semana-01: lab1 implementación de la clase Pila"
git push
```

---

## Herramientas permitidas

- Python 3 + VS Code
- Python Tutor (para verificar el estado interno de la pila)
- VisuAlgo módulo Stack (para visualizar las operaciones)
- Libros de la bibliografía oficial

**No se permite** entregar código generado íntegramente por IA sin declaración de uso. Ver `politicas/politica-ia.md`.
