# Exámenes Parciales y Proyecto Final

**Estructura de Datos (INF 222) — Semestre 2026-2**

---

## Parte 1 — Exámenes Parciales

Los tres exámenes parciales son evaluaciones **presenciales, individuales, sin uso de asistentes de IA generativa** (ver política en `05-Reglas-del-juego-politicas-aula.md`). Cada uno se estructura combinando tres tipos de reactivos: teoría conceptual, trazado de código y resolución de problemas, según la distribución que se detalla a continuación.

---

### Parcial 1 — Semana 7

**Alcance temático exacto**: Módulo 1 completo (introducción a estructuras de datos, notación Big-O, pilas y sus operaciones/implementaciones/aplicaciones, colas y sus operaciones/implementaciones/variantes) y Módulo 2 completo (punteros/referencias y aliasing en Python, listas enlazadas simples, listas circulares, listas circulares con nodo cabeza, listas doblemente enlazadas).

**Formato** (100 puntos):

| Componente | Peso | Descripción |
|---|---|---|
| Teoría conceptual | 30% | Preguntas de selección múltiple, verdadero/falso justificado y respuesta corta sobre definiciones, propiedades y diferencias entre estructuras. |
| Trazado de código | 35% | Se entrega código Python (pila, cola o lista enlazada) y el estudiante debe indicar el estado de la estructura y/o la salida en distintos puntos de ejecución. |
| Resolución de problemas | 35% | Ejercicios de diseño/implementación parcial de código: completar una función, corregir un error en una implementación dada, o diseñar el algoritmo para un caso nuevo. |

**Ejemplos ilustrativos de tipos de pregunta** (no constituyen un examen completo):

- Teoría conceptual: "Explique la diferencia entre una lista enlazada circular y una lista enlazada circular con nodo cabeza. ¿Qué problema resuelve el nodo cabeza?"
- Trazado de código: "Dado el siguiente fragmento que usa una pila con push(1), push(2), pop(), push(3), peek(), indique el contenido de la pila después de cada operación."
- Resolución de problemas: "Complete el método `eliminar(valor)` de la clase `ListaEnlazada`, considerando los casos: el valor está en el primer nodo, en un nodo intermedio, en el último nodo, o no existe en la lista."

---

### Parcial 2 — Semana 11

**Alcance temático exacto**: Módulo 3 completo (naturaleza de la recursividad, funciones recursivas, casos base, recursividad directa e indirecta, casos a evitar; algoritmos de ordenación burbuja/selección/inserción y su análisis de complejidad, con referencia conceptual a merge sort/quick sort; búsqueda secuencial y binaria, iterativa y recursiva).

**Formato** (100 puntos):

| Componente | Peso | Descripción |
|---|---|---|
| Teoría conceptual | 25% | Definiciones y comparaciones (p. ej. complejidad de cada algoritmo de ordenación, condiciones para aplicar búsqueda binaria). |
| Trazado de código | 40% | Trazado manual de una función recursiva (pila de llamadas) o de una pasada de un algoritmo de ordenación/búsqueda sobre un conjunto de datos dado. |
| Resolución de problemas | 35% | Escribir o completar una función recursiva, o justificar la elección de un algoritmo de ordenación/búsqueda para un escenario dado en términos de complejidad. |

**Ejemplos ilustrativos de tipos de pregunta**:

- Teoría conceptual: "¿Por qué la búsqueda binaria requiere que el arreglo esté ordenado? ¿Cuál es su complejidad en el peor caso?"
- Trazado de código: "Trace la pila de llamadas de `factorial(4)` indicando el valor de retorno en cada nivel."
- Resolución de problemas: "Escriba una función recursiva `suma_digitos(n)` que retorne la suma de los dígitos de un número entero positivo, indicando claramente el caso base."

---

### Parcial 3 — Semana 15

**Alcance temático exacto**: Módulo 4 completo (árboles generales, árboles binarios, terminología, recorridos inorden/preorden/postorden, operaciones de inserción/eliminación/búsqueda en BST, mención de árboles balanceados AVL; grafos: concepto, definiciones, representación por matriz y lista de adyacencia, recorridos BFS y DFS).

**Formato** (100 puntos):

| Componente | Peso | Descripción |
|---|---|---|
| Teoría conceptual | 25% | Terminología de árboles y grafos, diferencias entre representaciones, comparación BFS vs. DFS. |
| Trazado de código | 40% | Dado un árbol o grafo dibujado, indicar el orden de recorrido resultante de aplicar inorden/preorden/postorden o BFS/DFS. |
| Resolución de problemas | 35% | Insertar una secuencia de valores en un BST y dibujar el árbol resultante; o completar el pseudocódigo/código de BFS o DFS. |

**Ejemplos ilustrativos de tipos de pregunta**:

- Teoría conceptual: "Explique la diferencia entre representar un grafo con matriz de adyacencia y con lista de adyacencia. ¿Cuándo conviene cada una?"
- Trazado de código: "Dado el árbol binario de la figura, escriba la secuencia de nodos visitados en recorrido inorden, preorden y postorden."
- Resolución de problemas: "Inserte los valores 50, 30, 70, 20, 40, 60, 80 en un árbol binario de búsqueda vacío y dibuje el árbol resultante. Indique su altura."

---

## Parte 2 — Proyecto Final

### 2.1 Especificación general

El proyecto final es un trabajo en equipo (3-4 integrantes) que debe **aplicar correctamente al menos tres estructuras de datos distintas** trabajadas durante el semestre (por ejemplo: pila, lista enlazada y árbol; o cola, grafo y BST; entre otras combinaciones válidas) para resolver un problema real o realista, implementado en Python 3, versionado en Git/GitHub (repositorio plantilla del proyecto), y documentado con declaración explícita del uso de herramientas de IA generativa durante su desarrollo.

### 2.2 Requisitos mínimos

- Aplicación funcional, ejecutable, con interfaz de al menos línea de comandos (se admite interfaz gráfica o web como valor agregado, no como requisito).
- Uso justificado (no arbitrario) de al menos tres estructuras de datos del curso.
- Repositorio Git con historial de commits que refleje el trabajo de todos los integrantes.
- README con: descripción del problema, instrucciones de ejecución, estructuras de datos utilizadas y por qué, y declaración de uso de IA (qué se usó, para qué, y qué se hizo con criterio propio).
- Pruebas mínimas (casos de prueba manuales o automatizados) que demuestren el funcionamiento correcto.
- Sustentación oral en la semana 15.

### 2.3 Opciones de tema propuestas

Los equipos pueden elegir una de las siguientes opciones o proponer una alternativa equivalente, sujeta a aprobación del docente en la semana 3:

1. **Gestor de tareas con deshacer/rehacer**: aplicación de lista de tareas (to-do) que use una pila para deshacer/rehacer acciones, una lista enlazada o cola para el orden de tareas pendientes, y opcionalmente un árbol para categorías/subtareas jerárquicas.
2. **Sistema de rutas (estilo GPS simplificado)**: modelado de una red de ciudades/nodos como grafo, con cálculo de rutas mediante BFS/DFS (o una extensión con costos), uso de una cola de prioridad o pila para el algoritmo de recorrido, y una lista enlazada para el historial de rutas consultadas.
3. **Red social simplificada**: representación de usuarios y conexiones como grafo, búsqueda de conexiones (amigos en común, grados de separación) mediante BFS, uso de pilas o colas para un feed de publicaciones, y listas enlazadas para el manejo de publicaciones o comentarios.
4. **Buscador de palabras / diccionario con árbol**: implementación de un árbol (binario de búsqueda o estructura tipo trie simplificada) para almacenar y buscar palabras, con una pila o cola auxiliar para el procesamiento de texto, y una lista enlazada para el historial de búsquedas.
5. **Sistema de gestión de inventario**: manejo de productos mediante listas enlazadas (o doblemente enlazadas) para el catálogo, una pila o cola para el registro de movimientos (entradas/salidas), y un árbol binario de búsqueda para búsquedas rápidas por código o nombre de producto.

Cualquier tema alternativo propuesto por un equipo debe demostrar el mismo nivel de exigencia (mínimo tres estructuras de datos aplicadas de forma justificada) y ser aprobado por el docente antes del fin de la semana 3.

### 2.4 Cronograma de hitos

| Hito | Semana | Descripción | Naturaleza |
|---|---|---|---|
| Anuncio del proyecto y formación de equipos | 3 | Presentación de opciones de tema y conformación de equipos. | Administrativo |
| Propuesta formal | 7 | Entrega de documento breve: tema elegido, estructuras de datos a usar, alcance funcional, roles del equipo. | Evaluativo (parte de la nota de proceso) |
| Checkpoint 1 | 10 | Avance funcional con al menos una estructura de datos correctamente implementada y en uso. | Formativo/evaluativo |
| Checkpoint 2 | 14 | Avance funcional avanzado, integrando al menos dos de las tres estructuras requeridas. | Formativo/evaluativo |
| Entrega final y sustentación | 15 | Entrega del repositorio completo y presentación/exposición oral ante el docente y compañeros, más coevaluación de pares. | Evaluativo (sumativo) |

Distribución fijada para 2026-2 (dentro del rango recomendado de 20-30% para el proceso / 70-80% para la entrega final): propuesta formal 10%, checkpoint 1 10%, checkpoint 2 10% (30% en conjunto, calificados de forma formativa/complementaria), y entrega final + sustentación 70%. Esta es la misma tabla publicada en `INF222-Proyecto-Final-2026-2/README.md` — cualquier ajuste debe actualizarse en ambos lugares.

### 2.5 Rúbrica de evaluación del proyecto final

| Criterio | Peso sugerido | Descripción |
|---|---|---|
| Funcionalidad | 25% | El sistema cumple con los requisitos funcionales propuestos, ejecuta sin errores críticos y resuelve el problema planteado de forma completa. |
| Uso correcto de estructuras de datos | 25% | Se aplican correctamente al menos tres estructuras de datos del curso, con una justificación técnica coherente de por qué se eligió cada una (no un uso forzado o superficial). |
| Eficiencia y complejidad | 15% | El equipo puede explicar la complejidad (Big-O) de las operaciones clave de su sistema y ha tomado decisiones de diseño razonables en términos de eficiencia. |
| Calidad y documentación del código | 15% | Código organizado, legible, con nombres significativos, comentarios/docstrings donde corresponde, y README completo. |
| Uso ético y declarado de IA | 10% | Declaración clara y verificable de qué partes del proyecto tuvieron apoyo de IA generativa, y evidencia de que el equipo comprende y puede explicar todo el código entregado, incluido el generado con asistencia de IA. |
| Trabajo en equipo | 5% | Evidencia de contribución equilibrada en el historial de Git y en la coevaluación de pares; resolución adecuada de conflictos de equipo. |
| Presentación oral | 5% | Claridad de la exposición, dominio del tema por todos los integrantes, capacidad de responder preguntas técnicas sobre las estructuras de datos utilizadas. |

**Niveles de desempeño por criterio** (aplicable a cada fila de la tabla anterior):

| Nivel | Rango | Descripción general |
|---|---|---|
| Excelente | 90-100% | El criterio se cumple plenamente, con evidencia clara y de alta calidad. |
| Satisfactorio | 75-89% | El criterio se cumple en su mayoría, con detalles menores por mejorar. |
| Aceptable | 60-74% | El criterio se cumple parcialmente; hay debilidades notorias pero no incapacitantes. |
| Insuficiente | 40-59% | El criterio se cumple de forma mínima o con errores significativos. |
| No logrado | 0-39% | El criterio no se cumple, no hay evidencia, o existe incumplimiento de integridad académica (p. ej. uso de IA no declarado, código no comprendido por el equipo). |

### 2.6 Coevaluación de pares (semana 15)

Cada integrante completa un instrumento breve donde valora, de forma anónima para sus compañeros, aspectos como: cumplimiento de compromisos, calidad del aporte técnico, comunicación y actitud colaborativa. El resultado agregado de la coevaluación se utiliza como insumo directo para ajustar (dentro de un rango razonable, p. ej. ±10%) la nota individual del criterio "Trabajo en equipo" cuando existan diferencias significativas de contribución dentro de un mismo equipo, evitando que un integrante con aporte mínimo reciba la misma nota que el resto del equipo.

---

*Documento elaborado para el semestre 2026-2. Forma parte del conjunto de 6 documentos del Plan 2026-2 de Estructura de Datos (INF 222).*
