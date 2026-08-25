# Guía docente — Configurar INF 222 en GitHub Classroom

Este curso usa **dos asignaciones separadas** en GitHub Classroom porque Classroom no permite mezclar
trabajo individual y trabajo en equipo dentro de una misma asignación: cada asignación crea **un repo
por estudiante** o **un repo por equipo**, nunca ambos a la vez.

| Asignación | Tipo | Repo plantilla (este árbol de carpetas) | Cuándo se abre |
|---|---|---|---|
| Laboratorios semanales | Individual | `INF222-Estructura-de-Datos-2026-2` | Semana 1 |
| Proyecto final | Grupal (equipos de 3-4) | `INF222-Proyecto-Final-2026-2` | Semana 3 (kickoff) |

---

## 1. Requisitos previos (una sola vez por semestre)

1. Tener una **organización de GitHub** para la universidad/facultad (o usar una personal si aún no hay una institucional). GitHub Classroom se conecta a una organización, no a una cuenta personal.
2. Activar [GitHub Classroom](https://classroom.github.com) con tu cuenta docente y conectarla a esa organización.
3. Crear el "classroom" del semestre, por ejemplo: `INF222-2026-2`.
4. Importar el roster de estudiantes (CSV con nombres/carné, o vincular a Google Classroom/Canvas si tu facultad lo usa) — permite que Classroom identifique quién entrega qué sin depender solo del username de GitHub.

## 2. Subir los repos plantilla

Para cada uno de los dos repos (`INF222-Estructura-de-Datos-2026-2` y `INF222-Proyecto-Final-2026-2`):

```bash
cd INF222-Estructura-de-Datos-2026-2      # o INF222-Proyecto-Final-2026-2
git init
git add .
git commit -m "Plantilla inicial INF 222 — semestre 2026-2"
git branch -M main
git remote add origin https://github.com/<tu-organizacion>/<nombre-del-repo>.git
git push -u origin main
```

Luego, en GitHub → *Settings* del repo → activa **"Template repository"**. Esto es obligatorio: Classroom solo permite crear asignaciones a partir de un repo marcado como plantilla.

## 3. Crear la asignación de laboratorios (individual)

En Classroom → *New assignment*:

- **Nombre**: `Laboratorios y Modulos — INF 222`
- **Tipo**: *Individual assignment*
- **Repositorio plantilla**: `INF222-Estructura-de-Datos-2026-2`
- **Visibilidad**: *Private* (solo el estudiante y el docente ven el repo)
- **Deadline**: opcional por asignación general; las fechas reales de cada laboratorio se comunican en el aula virtual y en cada `semana-XX/README.md` (Classroom no soporta 15 deadlines distintos dentro de una sola asignación — para eso está la wiki/aula virtual).
- **Autograding (opcional pero recomendado)**: el repo ya incluye `.github/workflows/classroom.yml`, que corre automáticamente `pytest` en cada `git push` y reporta el resultado en la pestaña *Actions* de cada repo de estudiante. Los tests de la semana 1 (`test_lab01_pila.py`) ya están incluidos como ejemplo; agrega `test_labXX_*.py` junto a cada laboratorio a medida que lo asignas (ver el archivo de la semana 1 como plantilla del patrón).
- Genera el **enlace de invitación** y publícalo en el aula virtual la semana 1.

## 4. Crear la asignación del proyecto final (grupal)

En Classroom → *New assignment*:

- **Nombre**: `Proyecto Final — INF 222`
- **Tipo**: *Group assignment*
- **Tamaño de equipo**: 3-4 integrantes (fija el máximo en la configuración)
- **Grouping**: crea un "grouping" nuevo llamado por ejemplo `Equipos-Proyecto-INF222` — así, si reutilizas Classroom en otro semestre, los equipos no se mezclan con los de otro grupo.
- **Repositorio plantilla**: `INF222-Proyecto-Final-2026-2`
- **Visibilidad**: *Private*
- **Autograding**: mismo mecanismo (`pytest` sobre `src/tests/`), útil para verificar que el proyecto al menos ejecuta y pasa las pruebas mínimas antes de la sustentación.
- Genera el enlace de invitación y publícalo **en la semana 3** (kickoff), después de que los equipos estén formados. Los estudiantes que se unen con el mismo nombre de equipo comparten automáticamente un solo repo.

## 5. Flujo semanal del docente

1. Cada semana, revisa *Classroom → assignment → ver todos los repos* para ver de un vistazo quién ha hecho push y el estado del autograder (✅/❌) sin clonar cada repo manualmente.
2. Para retroalimentación puntual, usa comentarios directamente en el commit o abre un *Issue* en el repo del estudiante/equipo — queda como registro permanente.
3. Descarga masiva de todos los repos (útil antes de calificar): `gh classroom clone student-repos` (requiere la extensión `gh-classroom` de la GitHub CLI: `gh extension install github/gh-classroom`).

## 6. Notas importantes

- **No** es necesario que los estudiantes tengan Git avanzado: `git clone`, `git add`, `git commit`, `git push` (ya cubierto en `recursos/herramientas-setup.md §5`) es suficiente para todo el semestre.
- El repo de laboratorios y el del proyecto final son **independientes**: un estudiante puede tener el de laboratorios al día y el de proyecto atrasado, o viceversa — revísalos por separado.
- Si un estudiante cambia de equipo a mitad de semestre (caso excepcional), debe hacerse manualmente desde Classroom (*Manage repository access*); Classroom no reasigna repos de proyecto automáticamente.
