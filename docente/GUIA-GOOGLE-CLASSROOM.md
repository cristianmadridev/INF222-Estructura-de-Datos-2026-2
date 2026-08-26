# Guía docente — Google Classroom para INF 222 (Estructura de Datos)

Google Classroom es el LMS del curso: agenda, materiales, recolección del usuario de GitHub de cada
estudiante, y libro de calificaciones. El código y las entregas viven en GitHub (ver
`GUIA-ENTREGAS-GITHUB.md`) — Classroom no aloja ni corrige código, solo organiza el curso alrededor de
esos repositorios.

Todo esto se hace a mano en classroom.google.com (no tiene una CLI equivalente a `gh`; si quieres
automatizar la creación de las 15 tareas semanales más adelante, se puede con un script de Google Apps
Script que llama a la API de Classroom — pregúntame si lo quieres y te lo escribo).

---

## 1. Crear la clase

1. classroom.google.com → **+** (arriba a la derecha) → **Crear clase**.
2. Nombre: `INF 222 — Estructura de Datos (2026-2)`.
3. Sección: `Grupo A` o `Grupo B` (crea una clase por grupo si los gestionas por separado, o una sola con ambos si prefieres un solo tablero).
4. Asignatura: `Estructura de Datos`. Aula: el horario de teoría/laboratorio.
5. Classroom genera un **código de clase** — lo compartes en la primera sesión para que los estudiantes se unan (o los invitas por correo institucional desde **Personas → Invitar estudiantes**, más confiable si tienes la lista oficial).

## 2. Crear los Temas (uno por semana, igual que el repositorio)

**Trabajo de clase → Crear → Tema**. Crea 15 temas con el mismo nombre que las carpetas del repo, para que la organización sea idéntica en ambos lados:

```
Semana 01 · Semana 02 · Semana 03 · Semana 04 · Semana 05 · Semana 06 · Semana 07 ·
Semana 08 · Semana 09 · Semana 10 · Semana 11 · Semana 12 · Semana 13 · Semana 14 · Semana 15
```

## 3. Recolectar el usuario de GitHub de cada estudiante (semana 1, antes de todo)

**Trabajo de clase → Crear → Pregunta**:

- Título: `Tu usuario de GitHub`
- Tema: `Semana 01`
- Tipo de pregunta: **Respuesta corta**
- Instrucciones: *"Crea una cuenta en github.com si no tienes una (usa un nombre profesional). Escribe aquí tu usuario exacto — lo voy a usar para darte acceso a tu repositorio privado del curso."*
- Fecha límite: antes de tu primera sesión de laboratorio.

Cuando respondan, entra a la pregunta → **Ver todas las respuestas**: verás el nombre real de cada
estudiante junto a su respuesta. Copia la lista de usuarios (uno por línea) a un archivo de texto y
dámelo, o úsalo tú mismo con `scripts/crear-repos-estudiantes.sh` (ver `GUIA-ENTREGAS-GITHUB.md`).

Repite esta misma pregunta en la **semana 3** pidiendo además el **nombre del equipo** del proyecto
final, para alimentar `scripts/crear-repos-equipos.sh`.

## 4. Publicar el material de bienvenida

**Trabajo de clase → Crear → Material** (tema: `Semana 01`):

- Adjunta el syllabus (`docente/01-Syllabus-actualizado.md`, expórtalo a PDF o pégalo como Google Doc).
- Adjunta el enlace de la presentación de clase (artifact ya publicado).
- Adjunta el enlace del [Panel del semestre](https://claude.ai/code/artifact/653b3e29-08d9-4336-aed3-2a46b717fd4f).
- Un párrafo explicando el flujo: *"Tu trabajo se entrega en un repositorio privado de GitHub que te crearé después de que respondas la pregunta de esta semana. No se aceptan entregas por correo."*

## 5. Configurar las categorías de calificación (para que el promedio respete los pesos oficiales)

**Ajustes (⚙️) → Calificación**:

1. Sistema de calificación: **Categorías de calificación ponderadas**.
   > Si tu cuenta no muestra esta opción, es una función de Google Workspace for Education — con una
   > cuenta personal puedes lograr el mismo resultado asignando los puntos de cada tarea para que ya
   > sumen proporcionalmente (p. ej. cada parcial vale 100 pts y hay 3, cada laboratorio vale ~8-9 pts
   > para sumar 100 entre los 12+2, y el proyecto se registra aparte).
2. Agrega 3 categorías, con el mismo peso que `docente/03-Sistema-evaluacion-rubricas.md`:
   - **Exámenes Parciales** — 30%
   - **Laboratorios** — 30%
   - **Proyecto Final** — 40%

## 6. Crear una Tarea por cada semana

**Trabajo de clase → Crear → Tarea**, una por semana (usa `docente/02-Plan-trabajo-15-semanas.md` o
el `semana-XX/README.md` correspondiente para copiar objetivos/entregable):

| Campo | Qué poner |
|---|---|
| Título | `Semana XX — <título de la semana>` (p. ej. "Semana 01 — Pilas y complejidad") |
| Tema | El tema `Semana XX` creado en el paso 2 |
| Instrucciones | Objetivos + entregable, copiados del README de esa semana |
| Categoría de calificación | `Laboratorios` (semanas normales), `Exámenes Parciales` (semanas 7, 11, 15), o `Proyecto Final` (hitos de propuesta/checkpoints) |
| Puntos | Según la rúbrica de esa semana |
| Fecha de entrega | La que definas en el aula virtual |
| Adjuntos | Ninguno — el repo es privado y personal, no hace falta enlazar nada. En las instrucciones basta con: "Tu entregable está en tu propio repositorio (revisa tu correo de invitación de GitHub). Haz push antes de la fecha límite." |

Los estudiantes no "suben" ningún archivo en Classroom — su trabajo real vive en GitHub. Pueden marcar
la tarea como **"Entregado"** manualmente para que te quede un segundo indicador visual en el
libro de calificaciones, además de lo que veas con `gh` (ver `GUIA-ENTREGAS-GITHUB.md` §4).

**Semanas con evento especial** (según el calendario del curso):

- **Semana 7**: Parcial 1 + Propuesta formal del proyecto → 2 tareas ese tema (una en cada categoría).
- **Semana 10**: Checkpoint 1 del proyecto.
- **Semana 11**: Parcial 2 + Taller integrador.
- **Semana 14**: Checkpoint 2 del proyecto.
- **Semana 15**: Parcial 3 + Sustentación final + Coevaluación.

## 7. Ritmo semanal sugerido

Cada semana, antes de la clase de teoría: **Trabajo de clase → Crear → Anuncio** recordando el tema,
la actividad de laboratorio, y la fecha límite. Toma 2 minutos y mantiene a la clase orientada sin
depender de que revisen el repositorio por su cuenta.

## 8. Automatizar esto con Apps Script (ya está escrito)

`docente/apps-script-classroom.gs` automatiza los pasos 1-6 completos: crea (o reutiliza) el curso,
los 15 temas, la pregunta del usuario de GitHub, el material de bienvenida, y las 15 tareas semanales
+ parciales + hitos del proyecto — con los mismos títulos, categorías y puntos de esta guía. Corre
enteramente en tu cuenta de Google, sin compartir ninguna credencial conmigo.

**Cómo usarlo** (instrucciones completas dentro del propio archivo):

1. script.google.com → Nuevo proyecto → pega el contenido de `apps-script-classroom.gs`.
2. Servicios (+) → agrega **Google Classroom API**.
3. Ejecuta la función `main` — la primera vez te pedirá autorizar el acceso, acéptalo.
4. Por defecto corre en modo `DRY_RUN` (solo imprime en el registro lo que haría, sin crear nada).
   Revisa el registro con calma.
5. Cuando se vea bien, cambia `DRY_RUN` a `false` dentro del script y ejecútalo de nuevo. Es seguro
   volver a correrlo si algo falla a la mitad — no duplica lo que ya existe.

**Lo único que el script NO hace** es activar "Categorías de calificación ponderadas" en Ajustes →
Calificación (§5) — el soporte de esa función específica en la API pública de Classroom no está
confirmado, así que se deja como el único paso manual (2 minutos). Los puntos de cada tarea ya están
fijados para que, activada esa función, el promedio salga correcto sin ajustar nada más.
