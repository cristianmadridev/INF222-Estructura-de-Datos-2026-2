# Herramientas, Recursos y Guía de IA

**Estructura de Datos (INF 222) — Semestre 2026-2**

---

## 1. Stack tecnológico del curso

| Herramienta | Rol en el curso |
|---|---|
| **Python 3** (versión estable más reciente) | Lenguaje de programación principal, en actualización coherente con la bibliografía oficial (ver justificación en `01-Syllabus-actualizado.md`). |
| **Visual Studio Code** | Entorno de desarrollo integrado recomendado; se sugieren extensiones de Python, linting (p. ej. Pylint/Flake8) y control de versiones integrado. |
| **Git** | Sistema de control de versiones utilizado desde el primer laboratorio para todo el trabajo individual y grupal. |
| **GitHub** | Plataforma de alojamiento de repositorios y canal oficial de entrega de laboratorios y proyecto final, mediante una copia privada del repositorio que el docente crea para cada estudiante/equipo a partir de una plantilla. |
| **Python Tutor** (pythontutor.com) | Visualizador de ejecución paso a paso de código Python, incluyendo el modelo de memoria (referencias, objetos, pila de llamadas). Uso intensivo en los temas de punteros/referencias (semana 4) y recursividad (semana 8). |
| **VisuAlgo** (visualgo.net) | Visualizador de estructuras de datos y algoritmos (pilas, colas, listas enlazadas, árboles, grafos, ordenación, búsqueda). Uso recomendado como apoyo de estudio en prácticamente todas las semanas del curso. |
| **Replit** | Entorno de desarrollo en la nube, alternativa/respaldo para estudiantes con limitaciones de instalación local o para demostraciones rápidas en clase. |

---

## 2. Asistentes de inteligencia artificial generativa

El curso integra formalmente tres asistentes de IA como herramientas de apoyo a la programación, bajo la política de uso descrita en `05-Reglas-del-juego-politicas-aula.md`.

| Asistente | Rol pedagógico sugerido |
|---|---|
| **GitHub Copilot** | Asistente de autocompletado dentro de VS Code; útil para acelerar la escritura de código ya diseñado por el estudiante (boilerplate de clases, pruebas repetitivas), no para diseñar la solución algorítmica desde cero. |
| **Claude** (Anthropic) | Asistente conversacional útil para explicaciones conceptuales extendidas, generación de trazados de ejecución (como en el laboratorio de recursividad de la semana 8), y revisión crítica de código propio ("¿qué le pasaría a mi función si el árbol está vacío?"). |
| **ChatGPT** (OpenAI) | Asistente conversacional alternativo, con usos pedagógicos equivalentes a Claude: aclaración conceptual, generación de ejercicios de práctica adicionales, y apoyo en la depuración de errores. |

### Principio pedagógico común a los tres asistentes

En todos los casos, la IA se enseña y se usa como **par de programación supervisado**: el estudiante debe mantener el control del diseño de la solución, usar la IA para acelerar tareas mecánicas o para verificar/explicar razonamiento propio, y declarar su uso según los niveles establecidos en la política de IA del curso. Ningún asistente de IA sustituye la comprensión de los fundamentos algorítmicos que el curso busca desarrollar.

---

## 3. Recursos complementarios modernos

| Recurso | Tipo | Uso sugerido |
|---|---|---|
| **freeCodeCamp** (freecodecamp.org) | Plataforma de cursos gratuitos | Módulos de Python y de estructuras de datos y algoritmos como refuerzo autónomo fuera de clase. |
| **NeetCode** (neetcode.io) | Plataforma de práctica de algoritmos | Ejercicios categorizados por estructura de datos (pilas, listas enlazadas, árboles, grafos), útiles como banco de problemas adicionales, especialmente de cara al proyecto final y a la preparación de parciales. |
| **GeeksforGeeks** (geeksforgeeks.org) | Portal de referencia técnica | Artículos de referencia rápida sobre cada estructura de datos, con ejemplos de implementación en múltiples lenguajes, útil para consulta puntual de dudas conceptuales. |
| **Hoja de referencia de complejidad Big-O** (Big-O Cheat Sheet, bigocheatsheet.com) | Recurso de consulta | Tabla resumen de la complejidad temporal y espacial de las estructuras de datos y algoritmos vistos en el curso; se recomienda tenerla a mano desde la semana 1 y durante todo el semestre. |
| **VisuAlgo y Python Tutor** | (ver sección 1) | Recursos ya integrados como parte del stack oficial del curso. |

---

## 4. Bibliografía oficial

La siguiente es la bibliografía oficial del programa sintético de la asignatura, sin modificaciones:

- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). *Data Structures and Algorithms in Python*. Wiley.
- Yang Hu. (2021). *Easy Learning Data Structures & Algorithms Python* (2ª ed.).
- Russell, R. *Estructura de datos y algoritmos. Una introducción sencilla*. CreateSpace.
- Miller, B., & Ranum, D. (2005). *Problem Solving with Algorithms and Data Structures using Python*. Franklin, Beedle & Associates.
- Zelle, J. (2004). *Python Programming: an introduction to computer science*. Franklin, Beedle & Associates.
- Wilkinson, C. (2020). *Ciencia de Datos Python*.
- Williams, E. (2019). *Ciencia de Datos con Python*.

### 4.1 Correspondencia sugerida bibliografía-módulo (orientativa, no exclusiva)

| Módulo | Referencias más pertinentes |
|---|---|
| Módulo 1 (lineales: pilas, colas) | Goodrich et al.; Miller & Ranum; Yang Hu |
| Módulo 2 (dinámicas lineales: punteros/referencias, listas enlazadas) | Goodrich et al.; Zelle; Yang Hu; Russell |
| Módulo 3 (recursividad, ordenación, búsqueda) | Goodrich et al.; Miller & Ranum; Zelle |
| Módulo 4 (árboles, grafos) | Goodrich et al.; Miller & Ranum; Yang Hu |
| Transversal (fundamentos de Python y ciencia de datos) | Zelle; Wilkinson; Williams |

---

## 5. Nota sobre actualización de recursos

Los recursos complementarios listados en la sección 3 (freeCodeCamp, NeetCode, GeeksforGeeks, hoja de referencia Big-O) y los asistentes de IA de la sección 2 son **añadidos de actualización pedagógica** para el semestre 2026-2 y no sustituyen ni alteran la bibliografía oficial del programa sintético (sección 4), la cual se mantiene íntegra como referencia formal de la asignatura. La adopción de Python 3 como lenguaje principal (en reemplazo instrumental de la referencia original a "Software Dev C") se justifica en detalle en `01-Syllabus-actualizado.md`.

---

*Documento elaborado para el semestre 2026-2. Forma parte del conjunto de 6 documentos del Plan 2026-2 de Estructura de Datos (INF 222).*
