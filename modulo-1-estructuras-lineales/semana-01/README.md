# Semana 1 — Introducción al curso, Complejidad y Pilas

**Módulo 1: Estructuras de datos lineales**

---

## Objetivos de aprendizaje

Al finalizar esta semana debes ser capaz de:

- Explicar qué es una estructura de datos y por qué importa en el desarrollo de software.
- Clasificar estructuras de datos (lineales/no lineales, estáticas/dinámicas).
- Analizar la eficiencia de un algoritmo usando notación Big-O (O(1), O(n), O(n²), O(log n)).
- Definir el concepto de **pila (stack)**, su principio LIFO y sus operaciones fundamentales.
- Implementar una clase `Pila` básica en Python usando una lista como contenedor.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Presentación del syllabus, sistema de evaluación y política de uso de IA
2. Estructuras de datos: definición y clasificación
3. Análisis de complejidad:
   - Notación Big-O — qué mide y cómo leerla
   - Comparativo: O(1) · O(log n) · O(n) · O(n²)
   - Cómo estimar la complejidad de un fragmento de código
4. Pilas (Stack):
   - Principio **LIFO** (Last In, First Out)
   - Operaciones: `push(dato)`, `pop()`, `peek()` / `top()`, `is_empty()`
   - Casos de uso reales: pila de llamadas del sistema, deshacer/rehacer, navegación

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Configuración del entorno: Python 3, VS Code, cuenta de GitHub, entrega de tu usuario de GitHub en Google Classroom para recibir tu copia privada del repositorio
2. Implementación de la clase `Pila` con lista de Python
3. Pruebas con casos simples

---

## Entregable de la semana

**Laboratorio 1** — Implementación de la clase `Pila`

- Archivo: `modulo-1-estructuras-lineales/semana-01/laboratorio/lab01_pila.py`
- Subir con `git commit` y `git push` antes de la fecha límite indicada en el aula virtual

---

## Tarea / trabajo autónomo

- Leer el capítulo introductorio de Goodrich et al. sobre análisis de algoritmos.
- Completar la implementación de `Pila` iniciada en laboratorio, agregando **al menos 5 casos de prueba propios** al final del archivo (como funciones o bloque `if __name__ == "__main__":`).

---

## Recursos de la semana

| Recurso | Propósito |
|---------|-----------|
| VisuAlgo → Stack | Ver animación del push/pop |
| Python Tutor | Visualizar el estado de la pila durante la ejecución |
| Goodrich et al., cap. 1-3 | Fundamentos teóricos de Big-O |
| `politicas/politica-ia.md` | Leer antes del primer laboratorio |

---

## Notas importantes

- Esta semana **no se requiere declarar uso de IA** (no es una semana de uso guiado), pero sí debes haber leído la política antes del lab.
- Si tienes problemas instalando Python o Git, revisa `recursos/herramientas-setup.md` y abre un issue en el foro del aula virtual con captura de pantalla del error.
- Tu primer commit debe tener el mensaje: `semana-01: configuración inicial del entorno`
