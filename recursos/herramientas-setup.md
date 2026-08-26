# Guía de Instalación y Configuración de Herramientas — INF 222

**Haz esto en la primera semana del semestre.**

---

## 1. Python 3

### Windows
1. Descarga el instalador desde python.org/downloads (versión estable más reciente, 3.12 o superior).
2. Ejecuta el instalador. **Marca "Add Python to PATH"** antes de continuar.
3. Verifica en la terminal (PowerShell o CMD):
   ```
   python --version
   ```

### macOS
```bash
# Con Homebrew (recomendado)
brew install python
python3 --version
```

### Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt install python3 python3-pip
python3 --version
```

---

## 2. Visual Studio Code

1. Descarga desde code.visualstudio.com.
2. Instala las siguientes extensiones (busca en la pestaña Extensions, ícono de bloques):
   - **Python** (Microsoft)
   - **Pylance** (Microsoft)
   - **GitLens** (GitKraken) — opcional pero muy útil

---

## 3. Git

### Windows
Descarga desde git-scm.com e instala con las opciones predeterminadas.

### macOS
```bash
brew install git
```

### Linux
```bash
sudo apt install git
```

### Configuración inicial (obligatoria para todos)
```bash
git config --global user.name "Tu Nombre Apellido"
git config --global user.email "tu-email@up.ac.pa"
git config --global core.editor "code --wait"
```

---

## 4. GitHub — cuenta y tu copia del repositorio

1. Si no tienes cuenta, crea una en github.com. Usa un nombre de usuario profesional (tu nombre o variante).
2. Responde la pregunta de Google Classroom de la semana 1 con tu **usuario de GitHub** (no tu correo).
3. El docente te creará tu propia copia privada del repositorio y te agregará como colaborador — recibirás un correo de invitación de GitHub. Acéptala.
4. Clona tu copia (no la plantilla del docente):

```bash
git clone https://github.com/<tu-usuario>/<nombre-del-repo>.git
```

---

## 5. Flujo de trabajo semanal (Git básico)

Cada vez que trabajes:

```bash
# Actualiza tu copia local si el docente publicó cambios
git pull

# Después de trabajar, guarda tu progreso
git add modulo-1-estructuras-lineales/semana-01/laboratorio/lab01_pila.py
git commit -m "semana-01: implemento push, pop, peek en clase Pila"
git push
```

**Comandos que usarás frecuentemente:**

| Comando | Qué hace |
|---------|---------|
| `git status` | Ver qué archivos cambiaste |
| `git add <archivo>` | Preparar un archivo para el commit |
| `git commit -m "mensaje"` | Guardar snapshot con mensaje descriptivo |
| `git push` | Subir al repositorio en GitHub |
| `git pull` | Bajar los últimos cambios de GitHub |
| `git log --oneline` | Ver historial de commits |

---

## 6. Python Tutor — visualizador de ejecución

Herramienta en línea, no requiere instalación.  
URL: **pythontutor.com**

Pega cualquier fragmento de código Python y ejecuta paso a paso para ver el estado de las variables y la pila de llamadas. Fundamental para entender recursividad (semana 8) y punteros/referencias (semana 4).

---

## 7. VisuAlgo — visualizador de algoritmos y estructuras

URL: **visualgo.net/en**

Módulos relevantes para este curso:
- Stack / Queue (semanas 1-3)
- Linked List (semanas 4-7)
- Sorting (semana 9)
- Binary Search Tree (semana 13)
- Graph Traversal (semana 14)

---

## 8. Replit — entorno alterno en la nube

URL: **replit.com**

Útil si tienes problemas con la instalación local. Crea un proyecto Python y conecta tu repositorio de GitHub para sincronizar tu trabajo. No reemplaza el entorno local, pero es un respaldo válido.

---

## 9. Docker — entorno reproducible (opcional)

Si prefieres no instalar Python localmente, o quieres eliminar por completo el riesgo de "en mi máquina sí funciona", el repositorio incluye un entorno Docker ya configurado en `docker/`:

```bash
docker compose -f docker/docker-compose.yml run --rm lab
```

Ver `docker/README.md` para el detalle. Es el mismo entorno que usa la autocalificación por GitHub Actions, así que si tus pruebas pasan ahí, van a pasar en la corrección automática. **No es obligatorio** — instalar Python 3 localmente (opción 1) es suficiente para todo el curso.

---

## Verificación final

Antes de llegar al primer laboratorio, verifica que todo funciona:

```python
# Guarda esto como test_setup.py y ejecútalo
print("Python OK:", __import__("sys").version)
print("Git disponible desde Python Tutor: manual")
print("Configuración lista para INF 222 – 2026-2")
```

```bash
python test_setup.py
```

Si ves los tres mensajes sin errores, estás listo para el curso.
