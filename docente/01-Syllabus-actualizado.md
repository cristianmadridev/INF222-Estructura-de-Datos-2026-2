# Syllabus — Estructura de Datos (INF 222)

**Universidad de Panamá — Facultad de Informática, Electrónica y Comunicación**
**Licenciatura en Desarrollo de Aplicaciones Tecnológicas**
**Semestre 2026-2**

---

## 1. Datos generales

| Campo | Detalle |
|---|---|
| Denominación de la asignatura | ESTRUCTURA DE DATOS |
| Código | INF 222 |
| Carrera | Licenciatura en Desarrollo de Aplicaciones Tecnológicas |
| Ubicación en el plan de estudios | Segundo año, segundo semestre |
| Créditos | 4 |
| Horas totales | 90 horas (15 semanas) |
| Horas semanales | 6 (3 teóricas + 3 de laboratorio) |
| Horario de clases | Teoría (grupos A y B): martes, 8:45 p.m. – 10:30 p.m., y miércoles, 6:00 p.m. – 6:50 p.m. · Laboratorio Grupo A: miércoles, 6:55 p.m. – 9:35 p.m. (a continuación de la teoría del miércoles) · Laboratorio Grupo B: viernes, 7:50 p.m. – 10:30 p.m. (grupo B por división de capacidad de aula) |
| Prerrequisito | Programación I |
| Modalidad | Presencial, con apoyo de plataforma virtual y repositorio Git |
| Lenguaje de programación del curso | Python 3 |
| Semestre académico | 2026-2 |

---

## 2. Justificación

Estructura de Datos es una asignatura núcleo de la formación en desarrollo de software: provee el vocabulario técnico y las herramientas conceptuales (pilas, colas, listas enlazadas, árboles, grafos, recursividad, ordenación y búsqueda) que sostienen prácticamente cualquier sistema de software posterior, desde bases de datos hasta modelos de inteligencia artificial. Sin un dominio sólido de estas estructuras, el estudiante no puede razonar correctamente sobre eficiencia, memoria ni escalabilidad de un programa.

El contexto profesional de 2026 exige, además, dos competencias que este syllabus incorpora explícitamente:

1. **Uso crítico y ético de asistentes de inteligencia artificial generativa** (GitHub Copilot, Claude, ChatGPT). El mercado laboral ya no evalúa si un desarrollador usa IA, sino si sabe usarla con criterio: verificar su salida, entender por qué un algoritmo funciona y no limitarse a copiar código generado. Un estudiante que no entiende una pila o un árbol binario tampoco puede evaluar si el código que una IA le sugirió es correcto o eficiente. Por ello el curso enseña a usar la IA como par de programación supervisado, nunca como sustituto del razonamiento algorítmico.
2. **Control de versiones profesional (Git/GitHub)** como práctica estándar de la industria para trabajo individual y en equipo, integrado desde el primer laboratorio.

### Actualización de recursos declarada

El programa sintético original de la asignatura menciona "Software Dev C" como entorno de referencia. Toda la bibliografía oficial vigente del curso (Goodrich et al., Yang Hu, Miller & Ranum, Zelle, entre otros) está escrita en **Python**. En consecuencia, y para mantener coherencia entre el material didáctico y la bibliografía oficial sin alterar el contenido temático ni el sistema de evaluación aprobados, este syllabus **adopta Python 3 como lenguaje principal del curso**, complementado con Visual Studio Code como entorno de desarrollo y Git/GitHub como sistema de control de versiones. Esta actualización es puramente instrumental: los conceptos, la síntesis modular, la carga horaria y la ponderación de evaluación se mantienen exactamente como en el programa oficial.

---

## 3. Competencias

### 3.1 Competencias genéricas

- Capacidad de análisis y síntesis para resolver problemas computacionales.
- Capacidad de aprendizaje autónomo y actualización tecnológica continua.
- Capacidad de trabajo en equipo y comunicación efectiva de soluciones técnicas.
- Compromiso ético en el ejercicio profesional, incluyendo el uso responsable de herramientas de inteligencia artificial.
- Capacidad de razonamiento crítico frente a soluciones generadas automáticamente (por IA o por terceros), evaluando su corrección, eficiencia y pertinencia antes de adoptarlas.

### 3.2 Competencias específicas

- Comprende los fundamentos teóricos de las estructuras de datos lineales y no lineales, estáticas y dinámicas.
- Selecciona la estructura de datos apropiada para un problema dado, justificando la decisión en términos de complejidad temporal y espacial (notación Big-O).
- Implementa en Python pilas, colas, listas enlazadas (simples, circulares, con nodo cabeza y doblemente enlazadas), árboles binarios y grafos.
- Diseña e implementa algoritmos recursivos, de ordenación y de búsqueda, evaluando su eficiencia comparativa.
- Aplica control de versiones (Git/GitHub) en el desarrollo individual y colaborativo de software.
- Utiliza asistentes de inteligencia artificial generativa como herramientas de apoyo a la programación, de manera declarada, verificable y éticamente responsable.
- Desarrolla, documenta y sustenta un proyecto de software que integra múltiples estructuras de datos para resolver un problema real.

---

## 4. Síntesis modular

| Módulo | Contenido | Horas | Semanas |
|---|---|---|---|
| 1 | Estructuras de datos lineales (introducción, pilas, colas) | 18 | 3 |
| 2 | Estructuras de datos dinámicas lineales (punteros/referencias, listas enlazadas simples, circulares, circulares con nodo cabeza, doblemente enlazadas) | 24 | 4 |
| 3 | Recursividad, ordenación y búsqueda | 24 | 4 |
| 4 | Estructura avanzada de datos (árboles y grafos) | 24 | 4 |
| **Total** | | **90** | **15** |

El detalle semana por semana de contenidos, actividades y evidencias se desarrolla en el documento `02-Plan-trabajo-15-semanas.md`.

---

## 5. Metodología

El curso se desarrolla bajo un enfoque de **aprendizaje activo centrado en el estudiante**, con distribución equilibrada 50/50 entre teoría y práctica de laboratorio, según la carga horaria oficial (3h teóricas + 3h de laboratorio semanales). Los principios metodológicos son:

1. **Clase teórica participativa**: exposición dialogada, resolución de problemas en pizarra/proyector, trazado manual de algoritmos antes de programarlos, y discusión de casos reales.
2. **Laboratorio práctico obligatorio**: implementación guiada y luego autónoma en Python, con retroalimentación inmediata del docente.
3. **Aprendizaje basado en proyectos (ABP)**: desde la semana 3 los estudiantes trabajan en equipo en un proyecto final que integra progresivamente los contenidos del semestre, con hitos de revisión (propuesta, dos checkpoints, sustentación).
4. **Pair programming con IA supervisada**: se enseña a los estudiantes a usar asistentes de IA generativa como "par de programación" en laboratorios y proyecto, bajo la condición explícita de declarar su uso y de poder explicar, sin apoyo de la IA, cualquier línea de código entregado. El uso de IA está prohibido en evaluaciones presenciales (parciales).
5. **Visualización algorítmica**: uso de herramientas como Python Tutor y VisuAlgo para hacer tangible la ejecución de estructuras de datos (punteros, memoria, recorridos).
6. **Control de versiones desde el primer laboratorio**: todos los laboratorios y el proyecto final se entregan mediante repositorios Git (GitHub Classroom), fomentando buenas prácticas de commits, ramas y documentación.
7. **Evaluación formativa continua**: quices cortos, checkpoints de proyecto y retroalimentación semanal, complementando la evaluación sumativa oficial.

---

## 6. Recursos y herramientas

| Categoría | Recurso |
|---|---|
| Lenguaje de programación | Python 3 (versión estable más reciente) |
| Entorno de desarrollo | Visual Studio Code |
| Control de versiones | Git y GitHub (GitHub Classroom para laboratorios y proyecto) |
| Asistentes de IA generativa | GitHub Copilot, Claude, ChatGPT (uso declarado y supervisado — ver `05-Reglas-del-juego-politicas-aula.md`) |
| Visualizadores algorítmicos | Python Tutor, VisuAlgo |
| Entorno alterno / respaldo | Replit |
| Plataforma de gestión académica | Aula virtual institucional |
| Bibliografía | Ver sección 8 y detalle ampliado en `06-Herramientas-recursos-IA.md` |

---

## 7. Sistema de evaluación

Ponderación oficial según el programa sintético de la asignatura:

| Rubro | Porcentaje |
|---|---|
| Exámenes Parciales (3) | 30% |
| Prácticas / Laboratorios | 30% |
| Proyecto Final | 40% |
| **Total** | **100%** |

**Nota mínima de aprobación: 71%**, conforme al Estatuto de la Universidad de Panamá (artículos 280-283).

El detalle de rúbricas, criterios de desempeño y cálculo de promedios se desarrolla en `03-Sistema-evaluacion-rubricas.md`. La especificación de los tres parciales y del proyecto final se desarrolla en `04-Examenes-parciales-y-proyecto-final.md`.

---

## 8. Bibliografía

### 8.1 Bibliografía oficial

- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). *Data Structures and Algorithms in Python*. Wiley.
- Yang Hu. (2021). *Easy Learning Data Structures & Algorithms Python* (2ª ed.).
- Russell, R. *Estructura de datos y algoritmos. Una introducción sencilla*. CreateSpace.
- Miller, B., & Ranum, D. (2005). *Problem Solving with Algorithms and Data Structures using Python*. Franklin, Beedle & Associates.
- Zelle, J. (2004). *Python Programming: an introduction to computer science*. Franklin, Beedle & Associates.
- Wilkinson, C. (2020). *Ciencia de Datos Python*.
- Williams, E. (2019). *Ciencia de Datos con Python*.

### 8.2 Recursos complementarios de actualización (2026)

Ver listado ampliado, con enlaces y uso pedagógico sugerido, en `06-Herramientas-recursos-IA.md`.

---

## 9. Datos del docente

| Campo | Detalle |
|---|---|
| Docente | Angel R. Avila G. |
| Correo institucional | angel.avila@up.ac.pa |
| Horario de atención | (completar) |
| Sección / grupo | (completar) |

---

*Documento elaborado para el semestre 2026-2. Forma parte del conjunto de 6 documentos del Plan 2026-2 de Estructura de Datos (INF 222).*
