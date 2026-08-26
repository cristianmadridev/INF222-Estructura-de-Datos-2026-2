# Guía docente — Entregas por GitHub (repos privados, sin GitHub Classroom)

GitHub Classroom está en transición hacia soluciones de terceros y no está disponible para configurar
asignaciones nuevas. Los repos del curso se mantienen **privados** (incluyen guías de examen), así que
el autoservicio con "Use this template" no funciona: un estudiante sin acceso no puede ni ver la
plantilla. En su lugar, **el docente (o Claude, con `gh` ya autenticado) crea una copia privada por
estudiante** a partir de la plantilla y lo agrega como colaborador de su propia copia — el estudiante
nunca necesita acceso a la plantilla en sí.

| Repositorio (plantilla, privado) | Tipo | URL |
|---|---|---|
| Laboratorios (individual) | 1 copia privada por estudiante | `https://github.com/avila-fiec-up/INF222-Estructura-de-Datos-2026-2` |
| Proyecto final (equipo) | 1 copia privada por equipo de 3-4 | `https://github.com/avila-fiec-up/INF222-Proyecto-Final-2026-2` |

---

## 1. Recolectar el roster (nombre + usuario de GitHub)

La forma más simple: en Google Classroom, publica en la semana 1 una **Pregunta** de respuesta corta
("¿Cuál es tu usuario de GitHub? Créalo antes de responder si no tienes uno") — Classroom ya asocia
cada respuesta al nombre real del estudiante, así que obtienes el roster completo en una sola lista,
sin depender de que te escriban por correo. Detalle en `GUIA-GOOGLE-CLASSROOM.md`.

Para el proyecto (equipos), necesitas además el nombre del equipo y sus 3-4 integrantes — puede ser la
misma pregunta reformulada en la semana 3, después del kickoff.

## 2. Crear un repo privado por estudiante (individual)

Con el roster en mano (una lista de usuarios de GitHub), esto se hace con `gh` — pégamelo en el chat y
lo corro, o hazlo tú mismo:

```bash
export PATH="$HOME/.local/bin:$PATH"

# Por cada estudiante:
USUARIO="usuario-del-estudiante"
NOMBRE_REPO="inf222-$USUARIO-2026-2"

gh repo create "avila-fiec-up/$NOMBRE_REPO" \
  --private \
  --template "avila-fiec-up/INF222-Estructura-de-Datos-2026-2"

gh api -X PUT "repos/avila-fiec-up/$NOMBRE_REPO/collaborators/$USUARIO" -f permission=push
```

El script `scripts/crear-repos-estudiantes.sh` de este repositorio automatiza esto para una lista
completa (un usuario de GitHub por línea) — ver la cabecera del script para el uso exacto.

GitHub le manda automáticamente al estudiante una **invitación por correo** a su propio repo en cuanto
lo agregas como colaborador — no hace falta que tú le pases el link a mano, ni que Classroom lo cargue.
El estudiante la acepta, clona su copia, y trabaja como siempre.

## 3. Crear un repo privado por equipo (proyecto final)

Igual que el paso 2, pero desde la plantilla de proyecto y agregando a **todos** los integrantes del
equipo como colaboradores del mismo repo:

```bash
NOMBRE_REPO="inf222-proyecto-equipo-01-2026-2"

gh repo create "avila-fiec-up/$NOMBRE_REPO" \
  --private \
  --template "avila-fiec-up/INF222-Proyecto-Final-2026-2"

for USUARIO in usuario1 usuario2 usuario3; do
  gh api -X PUT "repos/avila-fiec-up/$NOMBRE_REPO/collaborators/$USUARIO" -f permission=push
done
```

## 4. Cómo el docente ve y sigue todas las entregas

```bash
# Todos los repos donde eres colaborador Y propietario que empiecen con "inf222" — o sea, todo lo creado
gh repo list avila-fiec-up --limit 200 --json name,pushedAt,isPrivate --jq '.[] | select(.name | test("(?i)inf222"))'
```

Como tú (el docente) eres quien crea cada repo, ya son tuyos — no necesitas el paso extra de "todos los
repos donde soy colaborador" que sí haría falta con el modelo de autoservicio.

## 5. Autocalificación

Cada copia hereda `.github/workflows/autograding.yml`, que corre `pytest` automáticamente en cada
`git push` del propio estudiante (pestaña **Actions** de su repo) — no depende de Classroom ni de
ninguna acción de terceros.

## 6. Si más adelante GitHub Classroom vuelve a estar disponible

Los dos repos plantilla ya cumplen los requisitos (marcados como plantilla, en una organización). Si
retomas Classroom, solo faltaría vincular la organización `avila-fiec-up` y crear las asignaciones —
el resto del curso no cambia.
