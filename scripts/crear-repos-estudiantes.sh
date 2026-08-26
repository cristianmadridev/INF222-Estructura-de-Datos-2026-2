#!/usr/bin/env bash
# Crea un repositorio privado por estudiante a partir de la plantilla del curso
# y agrega a cada estudiante como colaborador de SU propia copia (nunca de la
# plantilla). GitHub le envía automáticamente al estudiante una invitación por
# correo — no hace falta compartir ningún enlace a mano.
#
# Uso:
#   ./crear-repos-estudiantes.sh roster.txt
#
# roster.txt: un usuario de GitHub por línea (uno por estudiante), por ejemplo:
#   maria-dev
#   juanperez22
#
# Requiere: gh autenticado (gh auth status) con acceso de escritura a la
# organización avila-fiec-up.

set -euo pipefail

ORG="avila-fiec-up"
TEMPLATE="INF222-Estructura-de-Datos-2026-2"
PREFIJO="inf222"

ROSTER="${1:?Uso: $0 roster.txt (un usuario de GitHub por línea)}"

while IFS= read -r USUARIO; do
  [ -z "$USUARIO" ] && continue
  REPO="${PREFIJO}-${USUARIO}-2026-2"

  echo "=== $USUARIO -> $ORG/$REPO ==="

  if gh repo view "$ORG/$REPO" >/dev/null 2>&1; then
    echo "  ya existe, se omite la creación"
  else
    gh repo create "$ORG/$REPO" --private --template "$ORG/$TEMPLATE"
  fi

  gh api -X PUT "repos/$ORG/$REPO/collaborators/$USUARIO" -f permission=push
  echo "  invitación enviada a $USUARIO"
done < "$ROSTER"

echo "Listo. Cada estudiante recibirá un correo de GitHub para aceptar su repo."
