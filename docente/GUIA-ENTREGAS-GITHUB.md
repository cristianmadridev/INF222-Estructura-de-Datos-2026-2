# Guía docente — Entregas por GitHub (sin GitHub Classroom)

GitHub Classroom está en transición hacia soluciones de terceros y no está disponible para configurar
asignaciones nuevas en este momento. En vez de depender de ese servicio, este curso usa **la función
nativa de plantillas de GitHub** ("Template repository"), que ya está activada en los dos repositorios
del curso y no depende de ningún servicio externo:

| Repositorio | Tipo | URL |
|---|---|---|
| Laboratorios (individual) | 1 copia por estudiante | `https://github.com/avila-fiec-up/INF222-Estructura-de-Datos-2026-2` |
| Proyecto final (equipo) | 1 copia por equipo de 3-4 | `https://github.com/avila-fiec-up/INF222-Proyecto-Final-2026-2` |

Ambos son **privados** y están marcados como plantilla (*Template repository* activo).

---

## 1. Cómo obtiene su copia cada estudiante (instrucciones para ellos)

Comparte esto tal cual con la clase — también está en `README.md` de cada repo:

1. Entra a la URL del repo de laboratorios (arriba).
2. Botón verde **"Use this template"** → **"Create a new repository"**.
3. **Owner**: tu propia cuenta de GitHub (no hace falta pertenecer a ninguna organización).
4. **Repository name**: puedes dejar el mismo nombre o poner `INF222-<tu-nombre>-2026-2`.
5. **Visibility**: **Private**.
6. Click **Create repository from template** — en segundos tienes tu propia copia completa (los 15 módulos, exámenes, políticas, Docker) bajo tu cuenta.
7. En **Settings → Collaborators** de tu repo nuevo, agrega al docente (`profangelavila671-spec`) con acceso de lectura como mínimo.
8. Clona tu copia y trabaja como siempre: `git clone`, `git add`, `git commit`, `git push`.

Para el **proyecto final** (equipo): un solo integrante repite los mismos pasos con el repo de proyecto, y luego agrega como colaboradores a sus compañeros de equipo **y** al docente desde **Settings → Collaborators**.

## 2. Cómo tú (docente) ves y sigues todas las entregas

No hay un tablero central como el de Classroom, pero no necesitas uno: en cuanto un estudiante te agrega como colaborador, su repo aparece en tu propia cuenta. Para listarlos todos de una vez (con la GitHub CLI, `gh`, ya instalada y autenticada en esta máquina):

```bash
# Todos los repos donde eres colaborador (no propietario) — es decir, todas las entregas
gh api /user/repos --paginate -X GET -f affiliation=collaborator --jq '.[] | select(.name | test("INF222")) | .full_name'
```

Recomendación práctica: pide que cada estudiante te agregue **en las primeras 48 horas** de la semana 1 y usa ese mismo comando como pase de lista de quién ya se puso al día.

Para clonar/descargar todas las entregas antes de calificar:

```bash
gh api /user/repos --paginate -X GET -f affiliation=collaborator --jq '.[] | select(.name | test("INF222")) | .clone_url' \
  | xargs -n1 git clone
```

## 3. Autocalificación

Cada copia hereda `.github/workflows/autograding.yml`, que corre `pytest` automáticamente en cada
`git push` del propio estudiante (ver la pestaña **Actions** de su repo) — funciona igual que antes,
no depende de Classroom para nada. GitHub Actions da 2,000 minutos gratis al mes en cuentas
personales, más que suficiente para este curso.

## 4. Si más adelante GitHub Classroom vuelve a estar disponible

Los dos repos ya cumplen todos los requisitos para usarlo (marcados como plantilla, en una
organización). Si quieres retomarlo, solo faltaría: entrar a classroom.github.com, vincular la
organización `avila-fiec-up`, y crear una asignación individual y una grupal apuntando a estos mismos
repos — el resto del curso no cambia.
