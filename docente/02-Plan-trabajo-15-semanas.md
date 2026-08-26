# Plan de Trabajo — 15 Semanas

**Estructura de Datos (INF 222) — Semestre 2026-2**

Este documento desarrolla, semana por semana, el plan de trabajo del curso, siguiendo estrictamente la síntesis modular oficial (Módulo 1: semanas 1-3; Módulo 2: semanas 4-7; Módulo 3: semanas 8-11; Módulo 4: semanas 12-15). Cada semana incluye objetivos de aprendizaje, contenidos, actividad teórica, actividad de laboratorio, tarea/trabajo autónomo, herramientas (incluyendo IA) y evidencia de evaluación.

**Horario de clases**: la sesión "Actividad teórica" de cada semana se imparte en dos bloques comunes a los grupos A y B: **martes, 8:45 p.m. – 10:30 p.m.** y **miércoles, 6:00 p.m. – 6:50 p.m.** La sesión "Actividad de laboratorio" corresponde a la clase de laboratorio de cada grupo: **Grupo A, miércoles 6:55 p.m. – 9:35 p.m.** (inmediatamente después del bloque teórico del miércoles); **Grupo B, viernes 7:50 p.m. – 10:30 p.m.** (el grupo B existe por división de capacidad de aula). Ambos grupos avanzan por el mismo contenido semanal.

---

## MÓDULO 1 — Estructuras de datos lineales (semanas 1 a 3, 18 horas)

### Semana 1 — Introducción al curso, complejidad y pilas

**Objetivos de aprendizaje**
- Comprender el propósito del curso, el sistema de evaluación y la política de uso de IA.
- Explicar qué es una estructura de datos y por qué es relevante para el desarrollo de software.
- Analizar la eficiencia de un algoritmo mediante la notación Big-O (casos mejor, promedio y peor).
- Definir el concepto de pila (stack) y sus operaciones fundamentales.

**Contenidos**
- Presentación del syllabus, reglas del juego y política de uso de IA generativa.
- Introducción a estructuras de datos: definición, clasificación (lineales/no lineales, estáticas/dinámicas).
- Análisis de complejidad: notación Big-O, ejemplos comparativos (O(1), O(n), O(n²), O(log n)).
- Pilas: concepto, principio LIFO, operaciones (push, pop, peek/top, isEmpty).

**Actividad teórica**
Exposición dialogada sobre estructuras de datos y complejidad computacional. Ejercicio en pizarra: estimar la complejidad de fragmentos de código sencillos. Demostración conceptual de una pila con objetos físicos (analogía de platos apilados) y trazado manual de push/pop.

**Actividad de laboratorio**
Configuración del entorno (Python 3, VS Code, cuenta de GitHub, entrega del usuario de GitHub en Google Classroom para recibir tu copia privada del repositorio). Implementación de una clase `Pila` usando una lista de Python como contenedor, con métodos `push`, `pop`, `peek` e `is_empty`. Pruebas con casos simples (pila vacía, desbordamiento lógico).

**Tarea / trabajo autónomo**
Lectura: capítulo introductorio de Goodrich et al. sobre análisis de algoritmos. Completar y subir a tu copia del repositorio en GitHub la implementación de la pila iniciada en laboratorio, con al menos 5 casos de prueba propios.

**Herramientas / IA**
Python 3, VS Code, Git/GitHub. Se presenta formalmente la política de uso de IA (sin uso obligatorio esta semana).

**Evidencia de evaluación**
Entrega de laboratorio 1 (implementación de pila) — rubro Laboratorios.

---

### Semana 2 — Pilas avanzadas y colas

**Objetivos de aprendizaje**
- Implementar una pila usando una lista ligada (nodos enlazados) y comparar ventajas frente a la implementación basada en arreglo.
- Aplicar pilas a problemas reales: verificación de paréntesis balanceados, evaluación de notación postfija/prefija, mecanismos de deshacer/rehacer.
- Definir el concepto de cola (queue) y sus operaciones fundamentales.

**Contenidos**
- Pilas: implementación con lista ligada (nodo con dato y referencia al siguiente).
- Aplicaciones de pilas: paréntesis balanceados, conversión y evaluación de notación postfija/prefija, historial de deshacer/rehacer.
- Colas: concepto, principio FIFO, operaciones (enqueue, dequeue, front, isEmpty).

**Actividad teórica**
Trazado en pizarra del algoritmo de verificación de paréntesis balanceados usando una pila. Discusión de la diferencia entre implementación con arreglo (acceso O(1) pero tamaño fijo o redimensionable) y con lista ligada (tamaño dinámico). Introducción del concepto de cola con analogía de fila de atención al cliente.

**Actividad de laboratorio**
Implementación de `PilaEnlazada` con clase `Nodo`. Implementación de un verificador de paréntesis balanceados usando la pila propia. Implementación de la clase `Cola` con métodos `enqueue`, `dequeue`, `front`, `is_empty`. Mini-proyecto de laboratorio: simulador de cola de impresión (cada trabajo tiene nombre y número de páginas; se procesan en orden FIFO).

**Tarea / trabajo autónomo**
Implementar la evaluación de una expresión en notación postfija utilizando la pila propia. Documentar en el README del repositorio el razonamiento del algoritmo.

**Herramientas / IA**
Python Tutor para visualizar la ejecución paso a paso del verificador de paréntesis. Git/GitHub para el commit y push de los avances.

**Evidencia de evaluación**
Entrega de laboratorio 2 (pila enlazada + verificador de paréntesis + cola + simulador de impresión) — rubro Laboratorios.

---

### Semana 3 — Cierre del módulo 1: variantes de colas y taller integrador

**Objetivos de aprendizaje**
- Distinguir variantes de la estructura cola: cola circular, cola de prioridad y deque (cola doblemente terminada).
- Integrar pilas y colas en la solución de un problema combinado.
- Formar equipos de trabajo y comprender los lineamientos del proyecto final.

**Contenidos**
- Colas circulares (evitar desperdicio de espacio en implementación con arreglo).
- Colas de prioridad (concepto general, sin profundizar en heaps, que se retoman en el módulo 4).
- Deque: inserción y eliminación en ambos extremos.
- Taller integrador: combinación de pilas y colas.

**Actividad teórica**
Comparación de las variantes de cola con ejemplos de uso real (cola circular en buffers, cola de prioridad en sistemas operativos, deque en algoritmos de ventana deslizante). Presentación formal del proyecto final: modalidad, opciones de tema, cronograma de hitos y formación de equipos (ver `04-Examenes-parciales-y-proyecto-final.md`).

**Actividad de laboratorio**
Taller integrador: construir un simulador de historial de navegador web usando dos pilas (atrás/adelante) y, opcionalmente, una cola para el historial de pestañas recientes. Quiz formativo corto (10-15 minutos) sobre pilas y colas, de carácter diagnóstico y de retroalimentación inmediata.

**Tarea / trabajo autónomo**
Formar equipos de proyecto final (3-4 integrantes) y comenzar a explorar las opciones de tema propuestas. Repasar los conceptos del módulo 1 con apoyo de VisuAlgo (módulos de Stack y Queue).

**Herramientas / IA**
VisuAlgo para repaso visual. Se recuerda la política de IA: en el quiz formativo no se permite el uso de asistentes de IA.

**Evidencia de evaluación**
Quiz formativo 1 (pilas y colas) — rubro Laboratorios/formativo. Taller integrador — rubro Laboratorios. Registro de formación de equipos de proyecto final (sin nota, insumo administrativo).

---

## MÓDULO 2 — Estructuras de datos dinámicas lineales (semanas 4 a 7, 24 horas)

### Semana 4 — Punteros y memoria dinámica

**Objetivos de aprendizaje**
- Comprender el concepto de puntero y asignación dinámica de memoria.
- Relacionar el concepto clásico de puntero con el modelo de referencias y objetos de Python.
- Explicar el fenómeno de aliasing y sus implicaciones al mutar estructuras de datos.

**Contenidos**
- Punteros: concepto clásico, asignación dinámica de memoria (heap vs. stack de ejecución).
- Variables puntero: declaración, asignación, desreferencia (contextualizado en lenguajes como C).
- Equivalente en Python: modelo de referencias a objetos, la función `id()`, mutabilidad vs. inmutabilidad, aliasing.
- Ejemplos: por qué `lista_b = lista_a` no copia la lista, y cómo copiarla correctamente (`copy`, `deepcopy`).

**Actividad teórica**
Explicación con diagramas de memoria (caja y flecha) de cómo un puntero clásico apunta a una dirección de memoria, y cómo una variable de Python es una referencia a un objeto en el heap. Comparación explícita entre el modelo de C (punteros explícitos) y el modelo de Python (referencias implícitas), para dar contexto a la bibliografía histórica del curso.

**Actividad de laboratorio**
Ejercicios prácticos con `id()` para observar cuándo dos variables referencian el mismo objeto. Ejercicios de aliasing: mutar una lista a través de una segunda referencia y observar el efecto en la primera. Implementación de una función que reciba una lista y decida explícitamente si debe mutarla in situ o retornar una copia.

**Tarea / trabajo autónomo**
Ejercicio escrito: predecir la salida de fragmentos de código con aliasing antes de ejecutarlos, y luego verificar con Python Tutor.

**Herramientas / IA**
Python Tutor (visualización de memoria y referencias, pieza central de esta semana). Se autoriza el uso de IA para generar ejercicios adicionales de práctica personal, declarando su uso (no aplica a la entrega calificada).

**Evidencia de evaluación**
Entrega de laboratorio 3 (ejercicios de referencias y aliasing) — rubro Laboratorios.

---

### Semana 5 — Listas enlazadas simples

**Objetivos de aprendizaje**
- Explicar la estructura y motivación de una lista enlazada simple frente a una lista basada en arreglo.
- Implementar las operaciones fundamentales: inserción (inicio, final, posición), eliminación, búsqueda y recorrido.
- Analizar la complejidad de cada operación.

**Contenidos**
- Listas enlazadas: introducción, estructura de nodo (dato + referencia al siguiente).
- Operaciones: inserción al inicio, al final, en posición; eliminación por valor y por posición; búsqueda; recorrido; cálculo de longitud.
- Implementación completa con clases `Nodo` y `ListaEnlazada` en Python.

**Actividad teórica**
Trazado en pizarra de las operaciones de inserción y eliminación, mostrando el reacomodo de referencias (siguiente) en cada caso, incluyendo casos borde (lista vacía, inserción al inicio, eliminación del único nodo).

**Actividad de laboratorio**
Implementación guiada, paso a paso, de la clase `ListaEnlazada` con métodos `insertar_inicio`, `insertar_final`, `insertar_en_posicion`, `eliminar`, `buscar`, `recorrer` (o `__str__`/`__iter__`). Comparación empírica de tiempos de inserción al inicio en una lista de Python nativa vs. una lista enlazada propia.

**Tarea / trabajo autónomo**
Ampliar la implementación con un método `invertir()` que invierta la lista in situ, y un método `obtener(indice)`.

**Herramientas / IA**
VisuAlgo (módulo Linked List) para reforzar el trazado visual. Git/GitHub para el control de versiones del código.

**Evidencia de evaluación**
Entrega de laboratorio 4 (lista enlazada simple completa) — rubro Laboratorios.

---

### Semana 6 — Listas circulares y circulares con nodo cabeza

**Objetivos de aprendizaje**
- Distinguir una lista enlazada circular de una lista enlazada simple.
- Implementar algoritmos sobre listas circulares y sobre listas circulares con nodo cabeza (centinela).
- Identificar aplicaciones reales de listas circulares.

**Contenidos**
- Listas enlazadas circulares: el último nodo apunta al primero; algoritmos de inserción, eliminación y recorrido controlado (evitar bucles infinitos).
- Listas enlazadas circulares con nodo cabeza (sentinel node): simplificación de casos borde mediante un nodo centinela fijo.
- Aplicaciones: turnos rotativos (problema de Josephus), buffers circulares, reproducción de listas en bucle.

**Actividad teórica**
Discusión del problema de Josephus como caso motivador de listas circulares. Comparación de la complejidad y simplicidad del código con y sin nodo cabeza.

**Actividad de laboratorio**
Implementación de `ListaCircular` con recorrido controlado por conteo de nodos (no por referencia nula). Implementación de `ListaCircularConCabeza`. Resolución del problema de Josephus usando la lista circular propia.

**Tarea / trabajo autónomo**
Documentar en el repositorio, con un diagrama (puede ser ASCII o imagen), la diferencia estructural entre lista simple, circular y circular con nodo cabeza.

**Herramientas / IA**
VisuAlgo. Se permite consultar un asistente de IA para aclarar dudas conceptuales sobre el problema de Josephus, siempre que el estudiante documente la consulta y explique la solución con sus propias palabras en el README (ver política de IA en `05-Reglas-del-juego-politicas-aula.md`).

**Evidencia de evaluación**
Entrega de laboratorio 5 (lista circular + lista circular con nodo cabeza + problema de Josephus) — rubro Laboratorios.

---

### Semana 7 — Cierre del módulo 2: listas doblemente enlazadas, repaso y PARCIAL 1

**Objetivos de aprendizaje**
- Implementar una lista doblemente enlazada y sus operaciones (inserción y eliminación en ambos extremos y en posición intermedia).
- Reconocer aplicaciones de las listas doblemente enlazadas (navegación bidireccional, deque eficiente).
- Consolidar e integrar los contenidos de los módulos 1 y 2 para la evaluación parcial.

**Contenidos**
- Listas doblemente enlazadas: nodo con referencias al anterior y al siguiente; operaciones de inserción, eliminación y recorrido en ambos sentidos.
- Aplicaciones: implementación eficiente de un deque, navegación adelante/atrás, listas de reproducción editables.
- Repaso integrador de pilas, colas, punteros/referencias y listas enlazadas (todas sus variantes).

**Actividad teórica**
Repaso general dirigido por preguntas guía y resolución de dudas. Sesión de preguntas y respuestas sobre los temas de los módulos 1 y 2 como preparación directa para el parcial.

**Actividad de laboratorio**
Implementación de `ListaDoblementeEnlazada` con métodos de inserción/eliminación en ambos extremos y recorrido en ambos sentidos. **PARCIAL 1** (evaluación escrita/práctica que cubre módulos 1 y 2, ver detalle en `04-Examenes-parciales-y-proyecto-final.md`). Entrega de la propuesta formal de proyecto final por equipo.

**Tarea / trabajo autónomo**
Estudio dirigido para el parcial 1 con guía de repaso entregada por el docente.

**Herramientas / IA**
Ninguna herramienta de IA permitida durante el parcial (evaluación presencial). Git/GitHub para la entrega de la propuesta de proyecto.

**Evidencia de evaluación**
Entrega de laboratorio 6 (lista doblemente enlazada) — rubro Laboratorios. **PARCIAL 1** — rubro Exámenes Parciales. Propuesta formal de proyecto final — hito del rubro Proyecto Final.

---

## MÓDULO 3 — Recursividad, ordenación y búsqueda (semanas 8 a 11, 24 horas)

### Semana 8 — Recursividad

**Objetivos de aprendizaje**
- Explicar la naturaleza de una función recursiva: caso base y caso recursivo.
- Distinguir recursividad directa e indirecta.
- Identificar casos en los que la recursividad debe evitarse (ineficiencia, riesgo de desbordamiento de pila).
- Usar un asistente de IA de forma crítica para trazar y depurar código recursivo, explicando el resultado sin depender de la IA.

**Contenidos**
- Naturaleza de las funciones recursivas: caso base, caso recursivo, pila de llamadas.
- Recursividad directa (una función se llama a sí misma) e indirecta (A llama a B, B llama a A).
- Casos a evitar: recursividad sin caso base claro, recursividad ineficiente (p. ej. Fibonacci recursivo ingenuo) frente a alternativas iterativas o memoizadas.
- Ejemplos clásicos: factorial, Fibonacci, Torres de Hanoi.

**Actividad teórica**
Trazado manual en pizarra de la pila de llamadas para el cálculo recursivo de un factorial y de Fibonacci, evidenciando el crecimiento exponencial de llamadas en el caso de Fibonacci ingenuo. Explicación de Torres de Hanoi con demostración física o animada.

**Actividad de laboratorio — Lab con IA**
Implementación de las funciones recursivas de factorial, Fibonacci y Torres de Hanoi. Actividad especial: los estudiantes usan un asistente de IA (Claude, ChatGPT o Copilot) para generar un trazado paso a paso de la ejecución recursiva de una función dada (por ejemplo, Fibonacci(5)). **Requisito obligatorio (antiplagio):** cada estudiante debe reescribir y explicar, en sus propias palabras y sin apoyo de la IA, el trazado obtenido, incluyendo un diagrama de la pila de llamadas dibujado por el propio estudiante. Se evalúa la comprensión demostrada, no la copia del texto generado.

**Tarea / trabajo autónomo**
Resolver Torres de Hanoi para n=4 y n=5 mediante trazado manual, y comparar con la salida del programa.

**Herramientas / IA**
Uso declarado y obligatorio de un asistente de IA únicamente para el trazado (no para escribir el código de solución). Python Tutor como alternativa/complemento de verificación del trazado.

**Evidencia de evaluación**
Entrega de laboratorio 7 (funciones recursivas + trazado explicado con IA declarada) — rubro Laboratorios.

---

### Semana 9 — Ordenación

**Objetivos de aprendizaje**
- Implementar los algoritmos de ordenación burbuja, selección e inserción.
- Analizar y comparar la complejidad temporal de estos algoritmos.
- Reconocer, a nivel introductorio, los algoritmos de ordenación por división (merge sort y quick sort) como ampliación moderna más eficiente.

**Contenidos**
- Concepto de ordenación (in situ vs. no in situ, estable vs. inestable).
- Algoritmos básicos: burbuja (bubble sort), selección (selection sort), inserción (insertion sort).
- Análisis comparativo de complejidad: O(n²) en los tres algoritmos básicos, mejores y peores casos.
- Introducción breve a merge sort y quick sort: idea de "dividir y vencer" y complejidad O(n log n) (sin implementación exhaustiva, como ampliación moderna del contenido oficial).

**Actividad teórica**
Trazado comparativo en pizarra de los tres algoritmos básicos sobre el mismo arreglo de ejemplo, contando comparaciones e intercambios. Presentación conceptual de merge sort y quick sort mediante diagramas de división recursiva.

**Actividad de laboratorio**
Implementación de burbuja, selección e inserción en Python. Medición empírica de tiempos de ejecución (módulo `time`) sobre arreglos de distintos tamaños (por ejemplo, 100, 1000, 5000 elementos) y arreglos ya ordenados, invertidos y aleatorios. Elaboración de una tabla/gráfico comparativo de resultados.

**Tarea / trabajo autónomo**
Investigar e implementar, de forma opcional/ampliación, una versión básica de merge sort o quick sort, comparando sus tiempos con los algoritmos O(n²).

**Herramientas / IA**
VisuAlgo (módulo Sorting) para visualizar cada algoritmo. Hoja de referencia de complejidad Big-O (ver `06-Herramientas-recursos-IA.md`).

**Evidencia de evaluación**
Entrega de laboratorio 8 (algoritmos de ordenación + comparación de tiempos) — rubro Laboratorios.

---

### Semana 10 — Búsqueda y Checkpoint 1 del proyecto final

**Objetivos de aprendizaje**
- Implementar búsqueda secuencial y búsqueda binaria, en sus versiones iterativa y recursiva.
- Comparar la eficiencia de ambos métodos de búsqueda.
- Presentar un avance funcional verificable del proyecto final.

**Contenidos**
- Búsqueda secuencial: concepto, implementación, complejidad O(n).
- Búsqueda binaria: precondición de arreglo ordenado, implementación iterativa y recursiva, complejidad O(log n).
- Comparación de escenarios de uso apropiados para cada método.

**Actividad teórica**
Trazado en pizarra de la búsqueda binaria sobre un arreglo ordenado, mostrando la reducción del espacio de búsqueda en cada iteración. Discusión de por qué la búsqueda binaria requiere datos ordenados y su relación con los algoritmos de ordenación de la semana anterior.

**Actividad de laboratorio**
Implementación de búsqueda secuencial y búsqueda binaria (iterativa y recursiva). **Checkpoint 1 del proyecto final**: cada equipo presenta al docente un avance funcional del proyecto (al menos una estructura de datos correctamente implementada y en uso), recibiendo retroalimentación formativa para ajustar el rumbo antes de la entrega final.

**Tarea / trabajo autónomo**
Redactar, en el repositorio del proyecto, un registro de avance (bitácora) que documente decisiones de diseño tomadas hasta la fecha.

**Herramientas / IA**
VisuAlgo (módulo Binary Search). Git/GitHub para la entrega del checkpoint del proyecto.

**Evidencia de evaluación**
Entrega de laboratorio 9 (búsqueda secuencial y binaria) — rubro Laboratorios. Checkpoint 1 de proyecto — hito formativo del rubro Proyecto Final (retroalimentación, con posible ponderación menor según rúbrica de proyecto).

---

### Semana 11 — Cierre del módulo 3: taller integrador y PARCIAL 2

**Objetivos de aprendizaje**
- Integrar recursividad, ordenación y búsqueda en la resolución de un problema combinado.
- Demostrar dominio de los contenidos del módulo 3 en una evaluación sumativa.

**Contenidos**
- Repaso integrador: recursividad, algoritmos de ordenación y algoritmos de búsqueda.
- Relación entre los tres temas: por ejemplo, ordenar un conjunto de datos (iterativa o recursivamente) para luego aplicar búsqueda binaria eficiente.

**Actividad teórica**
Sesión de repaso dirigido por preguntas guía, resolución de dudas y ejercicios tipo examen (sin resolver el examen real) como preparación para el parcial 2.

**Actividad de laboratorio**
Taller integrador: dado un conjunto de datos desordenado, implementar una solución que lo ordene (usando uno de los algoritmos vistos) y luego permita búsquedas eficientes repetidas, incluyendo al menos una función recursiva auxiliar. **PARCIAL 2** (evaluación que cubre el módulo 3 completo: recursividad, ordenación y búsqueda; ver detalle en `04-Examenes-parciales-y-proyecto-final.md`).

**Tarea / trabajo autónomo**
Estudio dirigido para el parcial 2 con guía de repaso entregada por el docente.

**Herramientas / IA**
Ninguna herramienta de IA permitida durante el parcial (evaluación presencial).

**Evidencia de evaluación**
Taller integrador — rubro Laboratorios. **PARCIAL 2** — rubro Exámenes Parciales.

---

## MÓDULO 4 — Estructura avanzada de datos (semanas 12 a 15, 24 horas)

### Semana 12 — Árboles generales y binarios

**Objetivos de aprendizaje**
- Definir la terminología fundamental de árboles (raíz, nodo, hoja, altura, profundidad, subárbol).
- Distinguir árboles generales de árboles binarios.
- Implementar los recorridos fundamentales de un árbol binario: inorden, preorden y postorden.

**Contenidos**
- Árboles generales: definición, terminología (raíz, padre, hijo, hoja, nivel, altura).
- Árboles binarios: definición, estructura de nodo (dato, hijo izquierdo, hijo derecho).
- Recorridos: inorden, preorden, postorden (recursivos e introducción a la versión iterativa con pila).

**Actividad teórica**
Trazado en pizarra de los tres recorridos sobre un mismo árbol binario de ejemplo, evidenciando el orden distinto en que se visitan los nodos. Analogía entre recorrido de árboles y recursividad (módulo 3), reforzando la conexión entre contenidos.

**Actividad de laboratorio**
Implementación de la clase `NodoArbol` y `ArbolBinario`. Implementación de los tres recorridos de forma recursiva. Visualización de resultados comparando las tres salidas sobre el mismo árbol.

**Tarea / trabajo autónomo**
Implementar el recorrido por niveles (BFS sobre árbol, usando una cola) como puente conceptual hacia el tema de grafos de la semana 14.

**Herramientas / IA**
VisuAlgo (módulo Binary Tree). Python Tutor para visualizar la pila de llamadas de los recorridos recursivos.

**Evidencia de evaluación**
Entrega de laboratorio 10 (árbol binario + tres recorridos) — rubro Laboratorios.

---

### Semana 13 — Operaciones con árboles binarios (BST) y árboles balanceados

**Objetivos de aprendizaje**
- Implementar las operaciones de inserción, búsqueda y eliminación en un árbol binario de búsqueda (BST).
- Reconocer el problema de desbalance en un BST y su efecto en la complejidad.
- Identificar el concepto de árbol AVL como solución moderna al problema de desbalance.
- Relacionar los árboles binarios con aplicaciones reales.

**Contenidos**
- Árbol binario de búsqueda (BST): propiedad de orden, inserción, búsqueda, eliminación (casos: nodo hoja, un hijo, dos hijos).
- Complejidad de las operaciones BST: O(log n) en árbol balanceado, O(n) en árbol degenerado.
- Árboles balanceados (AVL): concepto general de factor de balance y rotaciones, como ampliación moderna (sin exigir implementación completa de rotaciones).
- Aplicaciones reales: índices de bases de datos, autocompletado, diccionarios ordenados.

**Actividad teórica**
Trazado en pizarra de inserciones sucesivas en un BST hasta llegar a un caso degenerado (equivalente a una lista enlazada), y discusión de cómo un árbol AVL evitaría ese problema mediante rotaciones. Presentación de casos reales de uso de árboles (autocompletado de buscadores, índices de bases de datos).

**Actividad de laboratorio**
Implementación de `ArbolBinarioBusqueda` con métodos `insertar`, `buscar`, `eliminar` (los tres casos). Prueba con conjuntos de datos que generen árboles balanceados y desbalanceados, midiendo la profundidad resultante.

**Tarea / trabajo autónomo**
Investigar (lectura corta, con o sin apoyo de IA declarado) el concepto de rotación simple en AVL y explicarlo con un diagrama propio en el repositorio.

**Herramientas / IA**
VisuAlgo (módulo BST y AVL Tree) para visualizar inserciones, eliminaciones y rotaciones.

**Evidencia de evaluación**
Entrega de laboratorio 11 (BST completo) — rubro Laboratorios.

---

### Semana 14 — Grafos y Checkpoint 2 del proyecto final

**Objetivos de aprendizaje**
- Definir el concepto de grafo y su terminología (vértice, arista, dirigido/no dirigido, ponderado).
- Representar un grafo mediante matriz de adyacencia y lista de adyacencia.
- Implementar los recorridos BFS y DFS.
- Presentar un avance funcional avanzado (casi completo) del proyecto final.

**Contenidos**
- Grafos: concepto, definiciones (vértice, arista, grado, camino, ciclo, grafo dirigido/no dirigido, ponderado/no ponderado).
- Representación: matriz de adyacencia y lista de adyacencia (ventajas y desventajas de cada una).
- Recorridos: BFS (recorrido en anchura, con cola) y DFS (recorrido en profundidad, con pila o recursividad).
- Aplicaciones actuales: sistemas de rutas (GPS), redes sociales (conexiones entre usuarios), sistemas de recomendación.

**Actividad teórica**
Trazado en pizarra de BFS y DFS sobre un mismo grafo de ejemplo, mostrando la diferencia en el orden de visita y la estructura de datos auxiliar usada en cada caso (cola vs. pila/recursión). Conexión explícita con los contenidos de los módulos 1 (pilas y colas) y 3 (recursividad).

**Actividad de laboratorio**
Implementación de la clase `Grafo` con representación por lista de adyacencia. Implementación de BFS y DFS. **Checkpoint 2 del proyecto final**: cada equipo presenta un avance funcional avanzado (integración de al menos dos de las tres estructuras de datos requeridas), recibiendo retroalimentación previa a la sustentación final de la semana 15.

**Tarea / trabajo autónomo**
Modelar como grafo un problema del dominio del proyecto final (si aplica) o un caso propuesto por el docente (por ejemplo, red de rutas entre ciudades de Panamá), y ejecutar BFS/DFS sobre dicho modelo.

**Herramientas / IA**
VisuAlgo (módulo Graph: BFS/DFS). Git/GitHub para la entrega del checkpoint del proyecto.

**Evidencia de evaluación**
Entrega de laboratorio 12 (grafo + BFS + DFS) — rubro Laboratorios. Checkpoint 2 de proyecto — hito formativo/evaluativo del rubro Proyecto Final.

---

### Semana 15 — Cierre del módulo 4: PARCIAL 3, sustentación del proyecto final y cierre del curso

**Objetivos de aprendizaje**
- Demostrar dominio de los contenidos del módulo 4 (árboles y grafos) en una evaluación sumativa.
- Sustentar oralmente el proyecto final ante el docente y los compañeros, demostrando el uso correcto de al menos tres estructuras de datos.
- Ejercer la coevaluación de pares de forma constructiva y objetiva.
- Reflexionar críticamente sobre el propio proceso de aprendizaje del semestre.

**Contenidos**
- Repaso integrador de árboles y grafos.
- Presentación y defensa del proyecto final.
- Coevaluación de pares.
- Cierre y retroalimentación general del curso.

**Actividad teórica**
**PARCIAL 3** (evaluación que cubre el módulo 4: árboles y grafos; ver detalle en `04-Examenes-parciales-y-proyecto-final.md`).

**Actividad de laboratorio**
**Sustentación/exposición del proyecto final**: cada equipo presenta su proyecto (demostración funcional en vivo, explicación de las estructuras de datos utilizadas y de las decisiones de diseño, declaración explícita del uso de IA durante el desarrollo) ante el docente y el resto de la clase. **Coevaluación de pares**: cada estudiante evalúa el desempeño de sus compañeros de equipo mediante un instrumento breve y estructurado. Cierre del curso: retroalimentación general, encuesta de fin de semestre y espacio abierto de comentarios sobre la experiencia con Python, Git/GitHub e IA generativa a lo largo del curso.

**Tarea / trabajo autónomo**
Entrega final del repositorio del proyecto (código, documentación, README con declaración de uso de IA) antes de la sustentación.

**Herramientas / IA**
Ninguna herramienta de IA permitida durante el parcial 3 (evaluación presencial). Declaración obligatoria y documentada del uso de IA durante todo el desarrollo del proyecto, presentada en la sustentación.

**Evidencia de evaluación**
**PARCIAL 3** — rubro Exámenes Parciales. **Sustentación y entrega final del proyecto** — rubro Proyecto Final. Coevaluación de pares — insumo para el componente de trabajo en equipo de la rúbrica de proyecto.

---

## Resumen de evidencias de evaluación por semana

| Semana | Evidencia principal | Rubro |
|---|---|---|
| 1 | Laboratorio 1: pila con lista | Laboratorios |
| 2 | Laboratorio 2: pila enlazada + cola | Laboratorios |
| 3 | Quiz formativo 1 + taller integrador | Laboratorios |
| 4 | Laboratorio 3: referencias y aliasing | Laboratorios |
| 5 | Laboratorio 4: lista enlazada simple | Laboratorios |
| 6 | Laboratorio 5: listas circulares | Laboratorios |
| 7 | Laboratorio 6: lista doblemente enlazada + **PARCIAL 1** + propuesta de proyecto | Laboratorios / Parciales / Proyecto |
| 8 | Laboratorio 7: recursividad con IA declarada | Laboratorios |
| 9 | Laboratorio 8: algoritmos de ordenación | Laboratorios |
| 10 | Laboratorio 9: búsqueda + Checkpoint 1 | Laboratorios / Proyecto |
| 11 | Taller integrador + **PARCIAL 2** | Laboratorios / Parciales |
| 12 | Laboratorio 10: árbol binario y recorridos | Laboratorios |
| 13 | Laboratorio 11: BST | Laboratorios |
| 14 | Laboratorio 12: grafos + Checkpoint 2 | Laboratorios / Proyecto |
| 15 | **PARCIAL 3** + sustentación de proyecto + coevaluación | Parciales / Proyecto |

---

*Documento elaborado para el semestre 2026-2. Forma parte del conjunto de 6 documentos del Plan 2026-2 de Estructura de Datos (INF 222).*
