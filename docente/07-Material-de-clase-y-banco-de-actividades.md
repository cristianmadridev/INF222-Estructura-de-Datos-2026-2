# Material de Clase y Banco de Actividades

**Estructura de Datos (INF 222) — Semestre 2026-2**
**Docente: Angel R. Avila G. — angel.avila@up.ac.pa**

Este documento complementa a `02-Plan-trabajo-15-semanas.md`. Mientras aquel describe **qué** se hace cada semana, este desarrolla **el contenido listo para usar en clase**: guiones breves de mini-clase, ejemplos resueltos con código, técnicas de aprendizaje activo específicas por sesión, preguntas de cierre (exit ticket) y un banco adicional de ejercicios con solución por módulo. El objetivo es maximizar el aprendizaje dentro de las 6 horas semanales (3 teóricas + 3 de laboratorio) sin necesidad de improvisar contenido el mismo día.

**Horario real del curso**: Teoría, martes 8:45 p.m. – 10:30 p.m. y miércoles 6:00 p.m. – 6:50 p.m. (grupos A y B juntos en ambos bloques). Laboratorio Grupo A, miércoles 6:55 p.m. – 9:35 p.m. (a continuación del bloque teórico del miércoles). Laboratorio Grupo B, viernes 7:50 p.m. – 10:30 p.m.

---

## 0. Rutina de clase recomendada (aplicar cada sesión teórica)

| Bloque | Duración sugerida | Propósito |
|---|---|---|
| **Warm-up / pregunta detonante** | 5 min | Activar conocimiento previo o generar curiosidad antes de exponer el tema nuevo. |
| **Mini-clase dialogada** | 20-25 min | Exponer el concepto nuevo con preguntas intercaladas (no exposición pasiva de 45 min). |
| **Ejemplo resuelto en vivo** | 15-20 min | Trazar/codificar el ejemplo junto con el grupo, pidiendo que predigan el siguiente paso antes de mostrarlo. |
| **Técnica de aprendizaje activo** | 10-15 min | Ver técnica sugerida por semana (sección 2). Consolida antes de pasar al laboratorio. |
| **Exit ticket** | 3-5 min | Pregunta de cierre que cada estudiante responde en papel o en el aula virtual; permite detectar quién necesita refuerzo antes del laboratorio. |

La teoría real del curso se reparte en dos bloques semanales: martes 8:45–10:30 p.m. (1h45) y miércoles 6:00–6:50 p.m. (50 min, inmediatamente antes del laboratorio del Grupo A). Se recomienda usar el bloque del martes para warm-up + mini-clase + ejemplo resuelto, y el bloque del miércoles para la técnica de aprendizaje activo + exit ticket, ya que este último conecta directamente con el laboratorio que sigue a continuación para el Grupo A.

---

## 1. Banco de técnicas de aprendizaje activo (usar de forma rotativa)

| Técnica | Cómo aplicarla | Cuándo funciona mejor |
|---|---|---|
| **Piensa-Compara-Comparte** (Think-Pair-Share) | El estudiante responde solo (2 min), compara con un compañero (3 min), se comparte con la clase (5 min). | Preguntas conceptuales o de trazado corto. |
| **Predicción antes de ejecutar** | Antes de correr código en el proyector, la clase predice la salida por escrito o a mano alzada. | Cualquier demo de código en vivo. |
| **El punto más confuso** (Muddiest Point) | Al cierre, cada estudiante escribe en una tarjeta/formulario qué fue lo menos claro de la sesión. | Cierre de temas densos (recursividad, punteros, árboles). |
| **Codificación coral guiada** (Call-and-response coding) | El docente escribe una línea, la clase decide en voz alta la siguiente. | Implementación guiada de estructuras nuevas (pila, lista enlazada). |
| **Analogía física / kinestésica** | Estudiantes actúan la estructura de datos con su cuerpo o con objetos (ver sección 3). | Introducción de una estructura nueva, especialmente al inicio de cada módulo. |
| **Depuración en parejas** (Pair debugging) | Se entrega código con un error intencional; en parejas deben encontrarlo y corregirlo antes que el resto de la clase. | Repaso previo a parciales, cierre de laboratorios. |
| **Traza en cadena** (Round-robin trace) | Cada estudiante traza un paso del algoritmo en la pizarra y pasa el marcador al siguiente. | Trazado de algoritmos de ordenación, búsqueda, recorridos. |
| **Uno verdadero, uno falso** | El docente presenta dos afirmaciones sobre el tema; la clase vota cuál es falsa y explica por qué. | Repaso rápido de conceptos antes de un parcial. |

---

## 2. Guion de clase por semana

### MÓDULO 1 — Estructuras lineales

**Semana 1 — Complejidad y pilas**
- *Warm-up*: "¿Cuál de estos dos programas creen que tarda más si `n` crece mucho?" (mostrar un bucle simple vs. uno anidado).
- *Mini-clase*: definición de estructura de datos → clasificación → notación Big-O con ejemplos progresivos O(1), O(n), O(n²), O(log n), usando conteo de instrucciones, no fórmulas abstractas de entrada.
- *Ejemplo resuelto*: analizar línea por línea la complejidad de una función que busca el máximo en una lista.
- *Técnica activa*: **analogía física** — apilar y desapilar libros/cuadernos frente al grupo, verbalizando `push`/`pop`/`peek` en cada paso.
- *Exit ticket*: "Si tengo una pila vacía y hago push(5), push(3), pop(), push(8), ¿qué contiene la pila y qué devolvió cada operación?"

**Semana 2 — Pilas avanzadas y colas**
- *Warm-up*: mostrar la cadena `"(a+b)*(c-d)"` y preguntar cómo verificarían a mano que los paréntesis están balanceados.
- *Mini-clase*: algoritmo de paréntesis balanceados con pila (idea antes que código). Introducción de colas con analogía de fila del banco.
- *Ejemplo resuelto (código)*:
```python
def parentesis_balanceados(expresion):
    pila = []
    apertura = {')': '(', ']': '[', '}': '{'}
    for caracter in expresion:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila or pila.pop() != apertura[caracter]:
                return False
    return not pila
```
- *Técnica activa*: **codificación coral guiada** para construir la función junto con la clase, prediciendo cada línea.
- *Exit ticket*: "¿Por qué esta función no funcionaría correctamente si usáramos una cola en vez de una pila?"

**Semana 3 — Variantes de colas y taller integrador**
- *Warm-up*: "Uno verdadero, uno falso" con dos afirmaciones sobre colas circulares vs. colas simples.
- *Mini-clase*: cola circular, cola de prioridad (concepto), deque, con ejemplos de uso real (buffer de audio, impresora, sistema operativo).
- *Ejemplo resuelto*: trazar en pizarra el llenado y vaciado de una cola circular de tamaño 5, mostrando el reciclaje de posiciones.
- *Técnica activa*: **Piensa-Compara-Comparte** sobre "¿en qué situación usarían una pila y en cuál una cola para resolver el mismo problema (por ejemplo, deshacer una acción vs. procesar tickets de soporte)?"
- *Exit ticket*: quiz formativo 1 (ver `03-Sistema-evaluacion-rubricas.md`).

### MÓDULO 2 — Estructuras dinámicas lineales

**Semana 4 — Punteros y memoria dinámica**
- *Warm-up*: mostrar `a = [1,2,3]; b = a; b.append(4); print(a)` y pedir predicción de la salida antes de ejecutar.
- *Mini-clase*: diagramas de caja y flecha para memoria; heap vs. pila de ejecución; `id()` en Python.
- *Ejemplo resuelto*: comparar `lista_b = lista_a` (alias) vs. `lista_b = lista_a.copy()` (copia), mostrando `id()` de cada una.
- *Técnica activa*: **predicción antes de ejecutar**, con 4-5 fragmentos cortos de aliasing en dificultad creciente.
- *Exit ticket*: "Dibuja el diagrama de caja y flecha después de `x = [1,2]; y = x; y.append(3)`."

**Semana 5 — Listas enlazadas simples**
- *Warm-up*: preguntar "¿qué pasa si quiero insertar un elemento al inicio de una lista de Python nativa con un millón de elementos? ¿Es gratis?"
- *Mini-clase*: estructura de nodo, por qué insertar al inicio es O(1) en lista enlazada vs. O(n) en arreglo.
- *Ejemplo resuelto (código)*:
```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
```
- *Técnica activa*: **codificación coral guiada** para `insertar_final` y `eliminar`, discutiendo primero los casos borde (lista vacía) antes de escribir código.
- *Exit ticket*: "¿Qué referencia hay que actualizar para eliminar el segundo nodo de una lista enlazada de 4 nodos?"

**Semana 6 — Listas circulares y con nodo cabeza**
- *Warm-up*: plantear el problema de Josephus en términos simples ("n personas en círculo, se elimina cada k-ésima persona") sin mencionar aún la solución.
- *Mini-clase*: por qué el último nodo apunta al primero; el nodo centinela como forma de eliminar casos especiales del código.
- *Ejemplo resuelto*: trazado en pizarra del problema de Josephus con n=7, k=3 usando un círculo dibujado (tiza/marcador), antes de programarlo.
- *Técnica activa*: **analogía física** — el grupo se sienta en círculo y simula el problema de Josephus eliminando compañeros según la regla, para "sentir" el algoritmo antes de codificarlo.
- *Exit ticket*: "Menciona una aplicación real de una lista circular distinta a las vistas en clase."

**Semana 7 — Listas doblemente enlazadas, repaso y Parcial 1**
- *Warm-up*: "Uno verdadero, uno falso" mezclando afirmaciones de pilas, colas, listas enlazadas y listas circulares como repaso rápido.
- *Mini-clase*: repaso integrador dirigido por preguntas guía (no exposición de contenido nuevo extenso, dado que hay parcial en la misma sesión).
- *Técnica activa*: **traza en cadena** sobre un ejercicio combinado (por ejemplo, insertar y eliminar en una lista doblemente enlazada), cada estudiante pasa al frente a resolver un paso.
- *Exit ticket*: no aplica (se sustituye por el Parcial 1).

### MÓDULO 3 — Recursividad, ordenación y búsqueda

**Semana 8 — Recursividad**
- *Warm-up*: preguntar "¿cómo explicarían a alguien qué es la recursividad sin usar la palabra 'recursividad'?"
- *Mini-clase*: caso base y caso recursivo con el ejemplo de factorial; luego Fibonacci ingenuo mostrando el crecimiento del árbol de llamadas.
- *Ejemplo resuelto (código)*:
```python
def factorial(n):
    if n == 0:          # caso base
        return 1
    return n * factorial(n - 1)   # caso recursivo
```
- *Técnica activa*: **predicción antes de ejecutar** con Python Tutor proyectado, prediciendo el valor de retorno en cada nivel de la pila de llamadas de `factorial(4)` antes de avanzar el visualizador.
- *Exit ticket*: "¿Cuál es el caso base de una función que calcula la suma de los elementos de una lista de forma recursiva?"

**Semana 9 — Ordenación**
- *Warm-up*: repartir a 6-8 estudiantes un número en una tarjeta y pedirles que se ordenen físicamente frente a la clase; cronometrar y contar "intercambios" (cambios de posición).
- *Mini-clase*: burbuja, selección e inserción, comparando el número de comparaciones/intercambios sobre el mismo arreglo pequeño.
- *Ejemplo resuelto*: trazado comparativo en pizarra de los tres algoritmos sobre `[5, 2, 8, 1, 9]`, contando operaciones de cada uno.
- *Técnica activa*: **traza en cadena** — cada fila de estudiantes traza una pasada completa de un algoritmo distinto sobre el mismo arreglo, y se comparan resultados al final.
- *Exit ticket*: "¿Cuál de los tres algoritmos básicos harías menos comparaciones si el arreglo ya está casi ordenado? ¿Por qué?"

**Semana 10 — Búsqueda y Checkpoint 1**
- *Warm-up*: proponer buscar un nombre en una guía telefónica física (o su equivalente digital) y preguntar cómo lo harían sin leer todos los nombres uno por uno.
- *Mini-clase*: búsqueda binaria, precondición de arreglo ordenado, reducción del espacio de búsqueda a la mitad en cada paso.
- *Ejemplo resuelto*: trazado en pizarra de búsqueda binaria sobre un arreglo ordenado de 15 elementos, marcando el rango `[inicio, fin]` en cada iteración.
- *Técnica activa*: **Piensa-Compara-Comparte**: "¿Por qué la búsqueda binaria no funciona si el arreglo no está ordenado? Den un contraejemplo."
- *Exit ticket*: no aplica (se sustituye por el Checkpoint 1 del proyecto en laboratorio).

**Semana 11 — Taller integrador y Parcial 2**
- *Warm-up*: "Uno verdadero, uno falso" combinando recursividad, ordenación y búsqueda.
- *Mini-clase*: repaso dirigido por preguntas guía como preparación directa al parcial.
- *Técnica activa*: **depuración en parejas** con una función recursiva y un algoritmo de ordenación que contienen errores intencionales (off-by-one, caso base incorrecto).
- *Exit ticket*: no aplica (se sustituye por el Parcial 2).

### MÓDULO 4 — Estructura avanzada de datos

**Semana 12 — Árboles generales y binarios**
- *Warm-up*: dibujar en la pizarra el árbol genealógico de una familia y preguntar qué términos (raíz, hijo, hoja) reconocen de forma intuitiva.
- *Mini-clase*: terminología de árboles; recorridos inorden/preorden/postorden con el mismo árbol de ejemplo, mostrando el orden distinto de visita.
- *Ejemplo resuelto (código)*:
```python
def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izquierdo)
        print(nodo.dato, end=" ")
        inorden(nodo.derecho)
```
- *Técnica activa*: **traza en cadena** — tres estudiantes distintos trazan inorden, preorden y postorden del mismo árbol dibujado en la pizarra, comparando resultados en vivo.
- *Exit ticket*: "Dibuja un árbol binario de 5 nodos y escribe su recorrido postorden."

**Semana 13 — BST y árboles balanceados**
- *Warm-up*: insertar en la pizarra la secuencia 10, 5, 15, 3, 7 en un árbol vacío, paso a paso, preguntando a la clase dónde va cada valor antes de dibujarlo.
- *Mini-clase*: propiedad de orden del BST; qué pasa si se insertan valores ya ordenados (árbol degenerado); idea general de rotación AVL (sin implementarla).
- *Ejemplo resuelto*: comparar la altura resultante de insertar `[10,5,15,3,7,12,20]` (balanceado) vs. `[1,2,3,4,5,6,7]` (degenerado) en un BST.
- *Técnica activa*: **Piensa-Compara-Comparte**: "¿Qué le pasa a la complejidad de la búsqueda si el BST se degenera en una lista? Comparen con la complejidad de una lista enlazada."
- *Exit ticket*: "Inserta 8, 3, 10, 1, 6 en un BST vacío y dibuja el árbol resultante."

**Semana 14 — Grafos y Checkpoint 2**
- *Warm-up*: proyectar un mapa simplificado de rutas entre 5 ciudades de Panamá (nodos y líneas) y preguntar cómo encontrarían la ruta más corta "a ojo".
- *Mini-clase*: terminología de grafos; matriz vs. lista de adyacencia; BFS con cola vs. DFS con pila/recursión, conectando con los módulos 1 y 3.
- *Ejemplo resuelto*: trazado en pizarra de BFS y DFS sobre el mismo grafo de 6 nodos, mostrando el orden de visita y la estructura auxiliar (cola/pila) en cada paso.
- *Técnica activa*: **analogía física** — los estudiantes se colocan en el patio/aula representando nodos de un grafo (con cinta o cuerdas como aristas) y "propagan" BFS pasando una señal (aplauso, pelota) nivel por nivel.
- *Exit ticket*: "¿En qué se diferencia el orden de visita de BFS y DFS sobre el mismo grafo? Den un ejemplo breve."

**Semana 15 — Cierre, Parcial 3 y sustentación**
- *Warm-up*: "Uno verdadero, uno falso" integrando árboles y grafos como repaso final.
- *Mini-clase*: no aplica (sesión dedicada a Parcial 3 y sustentaciones).
- *Técnica activa*: **coevaluación estructurada** durante las sustentaciones (ver rúbrica en `04-Examenes-parciales-y-proyecto-final.md`).
- *Exit ticket*: encuesta de cierre de semestre (ver `02-Plan-trabajo-15-semanas.md`, semana 15).

---

## 3. Ideas adicionales de actividades kinestésicas (uso opcional, refuerzo)

| Actividad | Estructura que refuerza | Materiales |
|---|---|---|
| "Cadena de personas" | Lista enlazada / lista doblemente enlazada | Cada estudiante sostiene un papel con su "dato" y toma de la mano (o señala) al "siguiente"; se simula inserción/eliminación moviendo personas físicamente. |
| "Círculo de Josephus" | Lista circular | Estudiantes en círculo, eliminación por conteo (ver semana 6). |
| "Torre humana de platos" | Pila | Objetos apilables (vasos, libros) para simular push/pop frente al grupo. |
| "Fila del comedor" | Cola | Estudiantes simulan una fila y se discuten variantes: fila normal (FIFO), fila con prioridad (alguien con "ticket VIP"), fila circular (buffer). |
| "Árbol genealógico viviente" | Árboles | Grupos pequeños se organizan en niveles (raíz al frente) para visualizar altura y profundidad. |
| "Mapa de rutas con cuerdas" | Grafos | Nodos marcados en el piso/pizarra, cuerdas o cinta como aristas, simulación de BFS/DFS con una señal que se propaga. |

---

## 4. Banco de ejercicios adicionales por módulo (con solución breve)

Uso sugerido: ejercicios de repaso para antes de cada parcial, tarea corta adicional, o comodín para clases que terminan antes de lo previsto.

### Módulo 1 (pilas y colas)

1. **Enunciado**: Escriba una función que, usando una pila, invierta el orden de los elementos de una cola sin usar una segunda cola.
   **Solución (idea)**: extraer todos los elementos de la cola con `dequeue()` y apilarlos con `push()`; luego, extraer de la pila con `pop()` y volver a insertarlos en la cola con `enqueue()`.

2. **Enunciado**: ¿Cuál es la complejidad de encontrar el elemento mínimo en una pila de `n` elementos sin estructuras auxiliares?
   **Solución**: O(n), porque en el peor caso hay que desapilar todos los elementos para inspeccionarlos.

3. **Enunciado**: Diseñe (en pseudocódigo) un simulador de "deshacer" con capacidad máxima de 10 acciones. ¿Qué estructura usaría y qué pasa al llegar al límite?
   **Solución esperada**: pila con tamaño máximo; al superar 10 elementos, se descarta la acción más antigua (la del fondo de la pila), lo cual requiere discutir la limitación de una pila pura para este caso (puente hacia deque).

### Módulo 2 (listas enlazadas)

4. **Enunciado**: Escriba una función que detecte si una lista enlazada tiene un ciclo (sin usar un conjunto/lista auxiliar para marcar nodos visitados).
   **Solución (idea)**: algoritmo de "tortuga y liebre" (dos punteros, uno avanza de a uno y otro de a dos; si se encuentran, hay ciclo).

5. **Enunciado**: Dada una lista enlazada simple, escriba una función que retorne el valor del nodo en la posición media, recorriendo la lista una sola vez.
   **Solución (idea)**: dos punteros, uno avanza de a uno (lento) y otro de a dos (rápido); cuando el rápido llega al final, el lento está en la posición media.

6. **Enunciado**: ¿Por qué una lista circular con nodo cabeza simplifica el código de inserción al inicio en comparación con una lista circular sin nodo cabeza?
   **Solución**: porque el nodo cabeza siempre existe, evitando el caso especial de "lista vacía" al insertar/eliminar.

### Módulo 3 (recursividad, ordenación, búsqueda)

7. **Enunciado**: Escriba una función recursiva `es_palindromo(cadena)` que determine si una cadena es un palíndromo.
   **Solución (idea)**: caso base: cadena de longitud 0 o 1 → `True`; caso recursivo: comparar primer y último carácter, y llamar recursivamente sobre la subcadena intermedia.

8. **Enunciado**: Dado el arreglo `[8, 3, 5, 1, 9, 2]`, trace manualmente la primera pasada completa de selection sort (selección) indicando qué intercambio ocurre.
   **Solución**: se busca el mínimo (1) y se intercambia con el primer elemento → `[1, 3, 5, 8, 9, 2]`.

9. **Enunciado**: ¿Cuántas comparaciones como máximo requiere la búsqueda binaria sobre un arreglo de 1000 elementos ordenados?
   **Solución**: aproximadamente ⌈log₂(1000)⌉ = 10 comparaciones.

### Módulo 4 (árboles y grafos)

10. **Enunciado**: Dado un árbol binario con recorrido preorden `[8, 3, 1, 6, 10, 14]` e inorden `[1, 3, 6, 8, 10, 14]`, reconstruya el árbol.
    **Solución (idea)**: el primer elemento del preorden (8) es la raíz; en el inorden, todo lo que está a la izquierda de 8 (`[1,3,6]`) es el subárbol izquierdo y todo lo que está a la derecha (`[10,14]`) es el subárbol derecho; se repite recursivamente.

11. **Enunciado**: Represente el siguiente grafo no dirigido como lista de adyacencia: aristas A-B, A-C, B-D, C-D.
    **Solución**: `{A: [B, C], B: [A, D], C: [A, D], D: [B, C]}`.

12. **Enunciado**: ¿En qué escenario conviene más una matriz de adyacencia que una lista de adyacencia?
    **Solución**: cuando el grafo es denso (muchas aristas respecto al número de vértices) y se requieren consultas rápidas de "¿existe arista entre A y B?" en O(1).

---

## 5. Plantillas rápidas de "ticket de salida" (exit ticket) genéricas

Para semanas sin exit ticket específico arriba, o como alternativa, usar cualquiera de estas tres preguntas genéricas adaptadas al tema del día:

1. "Explica el concepto de hoy en una sola oración, como si se lo explicaras a un compañero que faltó a clase."
2. "¿Qué fue lo más confuso de la sesión de hoy?" (Muddiest Point)
3. "Da un ejemplo de la vida real (fuera de la programación) que se parezca a la estructura/algoritmo visto hoy."

---

*Documento elaborado para el semestre 2026-2. Complementa el conjunto de documentos del Plan 2026-2 de Estructura de Datos (INF 222). Docente: Angel R. Avila G. — angel.avila@up.ac.pa.*
