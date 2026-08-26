# Guía del estudiante — INF 222 Estructura de Datos (2026-2)

Qué hacer, en orden, desde el primer día hasta la sustentación final. Si tienes prisa, esto es lo
único que necesitas leer para saber qué se espera de ti cada semana.

---

## Antes de la primera clase

- [ ] Crea una cuenta en [github.com](https://github.com) si no tienes una (usa un nombre profesional, no un apodo).
- [ ] Instala Python 3, VS Code y Git — pasos exactos en [`recursos/herramientas-setup.md`](recursos/herramientas-setup.md).
- [ ] Entra a Google Classroom y responde la pregunta **"Tu usuario de GitHub"** de la semana 1 con tu usuario exacto.

## Cómo obtienes tu copia del repositorio

Hay dos caminos válidos — tu docente te indicará cuál aplica, pero ambos funcionan porque este
repositorio es público:

1. **El docente te crea una copia** a partir de tu respuesta en Classroom. Te llega un correo de
   GitHub invitándote a un repositorio con tu nombre — acéptalo, ya está listo.
2. **Tú mismo creas tu copia**: entra a [este repositorio](https://github.com/avila-fiec-up/INF222-Estructura-de-Datos-2026-2), botón verde **"Use this template" → "Create a new repository"**, Owner: tu cuenta, Visibility: Private, y agrega a tu docente (`profangelavila671-spec`) en **Settings → Collaborators**.

En cualquiera de los dos casos, clona **tu propia copia** (nunca la plantilla) y trabaja ahí:

```bash
git clone https://github.com/<tu-usuario>/<nombre-de-tu-repo>.git
cd <nombre-de-tu-repo>
```

## El ritmo de cada semana

1. En Google Classroom, cada **Tema** ("Semana 01", "Semana 02"...) corresponde exactamente a una
   carpeta de tu repositorio (`modulo-X/semana-XX/`).
2. Antes de la clase, lee el `README.md` de esa carpeta — tiene los objetivos, el contenido y el
   entregable exacto de la semana. La tarea de Classroom ya trae el enlace directo.
3. Trabaja el laboratorio dentro de `semana-XX/laboratorio/`.
4. Antes de la fecha límite: `git add`, `git commit` (con un mensaje descriptivo), `git push`.
5. **No se aceptan entregas por correo ni por ningún otro canal.** Si no está en tu repositorio antes
   de la fecha límite, no cuenta — mejor entregar algo incompleto (con una nota explicando qué falta)
   que no entregar nada.

## Cómo se califica

| Rubro | Peso |
|---|---|
| Exámenes Parciales (3, 10% c/u) | 30% |
| Laboratorios | 30% |
| Proyecto Final | 40% |

Nota mínima de aprobación: **71%**. Rúbrica completa (cómo se reparten los puntos de cada
laboratorio, parcial y del proyecto): [`docente/03-Sistema-evaluacion-rubricas.md`](docente/03-Sistema-evaluacion-rubricas.md). Guías de estudio de los 3 parciales: [`examenes/`](examenes/).

## Uso de inteligencia artificial

Resumen (política completa en [`politicas/politica-ia.md`](politicas/politica-ia.md)):

- **Libre, sin declarar**: dudas conceptuales, práctica adicional no calificada.
- **Permitido, con declaración obligatoria**: laboratorios y proyecto final — di qué herramienta
  usaste, para qué, y qué verificaste tú mismo. Debes poder explicar cualquier línea que entregues.
- **Prohibido**: los 3 parciales presenciales y los quices evaluados en el momento.

Usarla sin declararla se trata como plagio.

## El proyecto final

- Equipos de 3-4, formados en la semana 3 (kickoff).
- Vive en un repositorio **aparte**: [`INF222-Proyecto-Final-2026-2`](https://github.com/avila-fiec-up/INF222-Proyecto-Final-2026-2) — mismo mecanismo de acceso que el repositorio individual, pero un solo repo por equipo.
- Hitos: Propuesta formal (semana 7, 10%) · Checkpoint 1 (semana 10, 10%) · Checkpoint 2 (semana 14, 10%) · Entrega final y sustentación (semana 15, 70%).
- Especificación completa, opciones de tema y rúbrica: `README.md` de ese repositorio.

## Entorno de trabajo (Docker, opcional)

Si prefieres no instalar Python localmente, el repositorio incluye un entorno Docker listo en
[`docker/`](docker/) — ver `docker/README.md`. No es obligatorio.

## Dudas

- **Técnicas sobre el contenido**: foro del aula virtual (así tus compañeros también ven la respuesta).
- **Personales o de calificación**: angel.avila@up.ac.pa, asunto `[INF222]` + tu grupo. Respuesta en 48h hábiles.
- No se resuelven entregas por WhatsApp ni redes sociales.

---

*Reglas completas del aula, integridad académica e inclusión: [`politicas/reglas-del-aula.md`](politicas/reglas-del-aula.md).*
