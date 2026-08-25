# Sistema de Evaluación y Rúbricas

**Estructura de Datos (INF 222) — Semestre 2026-2**

---

## 1. Ponderación oficial

| Rubro | Porcentaje |
|---|---|
| Exámenes Parciales (3) | 30% |
| Prácticas / Laboratorios | 30% |
| Proyecto Final | 40% |
| **Total** | **100%** |

**Nota mínima de aprobación: 71%**, conforme al Estatuto de la Universidad de Panamá, artículos 280-283. Todo estudiante con nota final inferior a 71% no aprueba la asignatura, independientemente del desempeño parcial en algún rubro específico.

---

## 2. Cálculo de la nota final

```
Nota final = (Promedio de Parciales × 0.30) + (Promedio de Laboratorios × 0.30) + (Nota de Proyecto Final × 0.40)
```

### 2.1 Promedio de Exámenes Parciales (30%)

El curso contempla tres exámenes parciales, distribuidos según el cierre de cada bloque temático:

| Parcial | Semana | Cobertura |
|---|---|---|
| Parcial 1 | 7 | Módulos 1 y 2 (lineales + dinámicas lineales) |
| Parcial 2 | 11 | Módulo 3 (recursividad, ordenación, búsqueda) |
| Parcial 3 | 15 | Módulo 4 (árboles y grafos) |

El promedio de parciales se calcula como el promedio simple de los tres:

```
Promedio de Parciales = (Parcial 1 + Parcial 2 + Parcial 3) / 3
```

No se promedian pesos distintos entre parciales: los tres valen igual dentro de este rubro. El detalle de alcance y formato de cada parcial se desarrolla en `04-Examenes-parciales-y-proyecto-final.md`.

### 2.2 Promedio de Laboratorios (30%)

Incluye todas las entregas de laboratorio semanal (12 laboratorios prácticos), los talleres integradores (semanas 3 y 11) y los quices formativos (semana 3 y los que el docente decida aplicar adicionalmente). El promedio de laboratorios se calcula como el promedio simple de todas las entregas calificadas de este rubro durante el semestre. Se recomienda que el docente publique en el aula virtual, desde la primera semana, la lista completa de entregas de laboratorio que compondrán este promedio.

### 2.3 Proyecto Final (40%)

Nota única integrada que combina los hitos de seguimiento (propuesta, checkpoints 1 y 2, considerados de forma formativa/complementaria) y la evaluación sumativa final (funcionalidad, código, documentación, sustentación oral y coevaluación de pares), según la rúbrica detallada en `04-Examenes-parciales-y-proyecto-final.md`.

---

## 3. Rúbrica de laboratorios semanales

Cada laboratorio se califica sobre 100 puntos (o su equivalente porcentual), distribuidos en los siguientes criterios:

| Criterio | Peso | Descripción |
|---|---|---|
| Corrección funcional | 40% | El código implementa correctamente las operaciones solicitadas y pasa los casos de prueba propuestos, incluyendo casos borde. |
| Uso apropiado de la estructura de datos | 20% | Se utiliza la estructura de datos correspondiente al tema de la semana de forma adecuada, no una solución alternativa que evite el aprendizaje buscado. |
| Calidad y legibilidad del código | 15% | Nombres de variables claros, código organizado en funciones/clases, ausencia de duplicación innecesaria, cumplimiento de convenciones básicas de estilo Python (PEP 8). |
| Documentación mínima | 10% | Comentarios donde son necesarios, docstrings en funciones/clases principales, README breve si el laboratorio lo requiere. |
| Uso declarado de herramientas de IA (cuando aplique) | 10% | Cuando el laboratorio involucra IA (p. ej. semana 8), se declara su uso y se demuestra comprensión propia del resultado. En laboratorios donde no se usó IA, este criterio se reasigna proporcionalmente a corrección funcional. |
| Entrega puntual vía Git/GitHub | 5% | Commit y push dentro del plazo establecido, con historial de commits razonable (no un único commit masivo). |

### Niveles de desempeño (escala general aplicable a cada criterio)

| Nivel | Rango | Descripción |
|---|---|---|
| Excelente | 90-100% | Cumple todos los requisitos, sin errores, con buenas prácticas evidentes y comprensión demostrada. |
| Satisfactorio | 75-89% | Cumple los requisitos principales con errores menores que no afectan la funcionalidad central. |
| Aceptable | 60-74% | Cumple parcialmente; hay errores que afectan algunos casos o funcionalidades secundarias. |
| Insuficiente | 40-59% | Implementación incompleta o con errores que afectan la funcionalidad central. |
| No logrado | 0-39% | No se entrega, no compila/ejecuta, o no corresponde al tema solicitado (incluye copia no declarada o plagio). |

---

## 4. Rúbrica de quices formativos

Los quices formativos (p. ej. semana 3) tienen como propósito principal diagnosticar el nivel de comprensión antes de una evaluación sumativa, no penalizar severamente el error. Se recomienda ponderarlos dentro del rubro de laboratorios con un peso menor a una entrega de laboratorio estándar (por ejemplo, la mitad).

| Criterio | Peso | Descripción |
|---|---|---|
| Respuestas conceptuales correctas | 60% | Definiciones y explicaciones correctas de los conceptos evaluados. |
| Trazado/resolución correcta | 30% | Resolución correcta de ejercicios cortos de trazado manual o código breve. |
| Claridad y orden de la respuesta | 10% | La respuesta es legible y sigue el razonamiento solicitado. |

Se retroalimenta el mismo día o en la siguiente sesión de clase, priorizando el valor formativo sobre el punitivo.

---

## 5. Rúbrica de participación

Aunque la participación no constituye un rubro independiente en la ponderación oficial, se recomienda integrarla como un componente transversal dentro del rubro de laboratorios (por ejemplo, hasta un 10% adicional distribuido en varias sesiones, o como criterio de desempate). Criterios sugeridos:

| Criterio | Descripción |
|---|---|
| Participación en clase teórica | Interviene con preguntas o respuestas pertinentes durante la exposición dialogada. |
| Participación en laboratorio | Colabora activamente en la resolución de ejercicios guiados, no solo copia la solución final. |
| Contribución en trabajo de equipo | Evidencia de aporte individual dentro del repositorio Git del proyecto (commits propios, no solo presencia nominal en el equipo). |
| Actitud y respeto | Mantiene un ambiente de aula respetuoso y colaborativo, conforme a las normas de convivencia del curso. |

| Nivel | Descripción |
|---|---|
| Alta | Participación frecuente, pertinente y constructiva en la mayoría de las sesiones. |
| Media | Participación ocasional, generalmente pertinente. |
| Baja | Participación mínima o solo cuando se le solicita directamente. |
| Nula | Sin evidencia de participación en el periodo evaluado. |

---

## 6. Cómo se promedian los tres parciales

1. Cada parcial se califica sobre 100 puntos, siguiendo la estructura descrita en `04-Examenes-parciales-y-proyecto-final.md` (combinación de teoría conceptual, trazado de código y resolución de problemas).
2. Al finalizar el semestre, se obtiene el promedio simple de los tres parciales.
3. Este promedio se pondera al 30% de la nota final, según la fórmula de la sección 2.
4. No se elimina el parcial de menor nota ni se aplica ponderación diferenciada entre parciales; los tres tienen el mismo peso relativo dentro del rubro.
5. En caso de ausencia justificada a un parcial (según reglamento institucional), el docente aplicará el mecanismo de reposición que corresponda conforme a la normativa vigente de la Universidad de Panamá, documentado en `05-Reglas-del-juego-politicas-aula.md`.

---

## 7. Transparencia y publicación de notas

- Todas las notas de laboratorio se publican en el aula virtual dentro de una semana posterior a la entrega, con retroalimentación específica por criterio de rúbrica.
- Las notas de parciales se publican junto con la hoja de respuestas o retroalimentación general del examen.
- El estudiante puede solicitar revisión de nota siguiendo el proceso descrito en `05-Reglas-del-juego-politicas-aula.md`.

---

*Documento elaborado para el semestre 2026-2. Forma parte del conjunto de 6 documentos del Plan 2026-2 de Estructura de Datos (INF 222).*
