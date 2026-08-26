/**
 * INF 222 — Estructura de Datos (2026-2)
 * Script de configuración automática de Google Classroom.
 *
 * Crea (o reutiliza) el curso, los 15 temas semanales, la pregunta de
 * recolección del usuario de GitHub, el material de bienvenida, y las tareas
 * de las 15 semanas + parciales + hitos del proyecto final — con los mismos
 * nombres, pesos y estructura que docente/02-Plan-trabajo-15-semanas.md y
 * docente/03-Sistema-evaluacion-rubricas.md.
 *
 * Cada tarea/material queda enlazado al archivo real correspondiente en los
 * repositorios públicos de GitHub (avila-fiec-up/INF222-Estructura-de-Datos-2026-2
 * y avila-fiec-up/INF222-Proyecto-Final-2026-2) — el README de la semana, la
 * guía del parcial, o la plantilla del hito del proyecto — en vez de solo
 * texto genérico.
 *
 * Si un tema/tarea/material ya existe (por título), el script lo ACTUALIZA
 * (agrega/reemplaza los enlaces y la descripción) en vez de duplicarlo —
 * así, si ya corriste una versión anterior de este script sin enlaces, con
 * volver a correr esta versión les agrega los enlaces sin crear nada de más.
 *
 * NO crea las "categorías de calificación ponderadas" (Ajustes → Calificación):
 * el soporte de esa función en la API pública de Classroom es limitado/no
 * confirmado. Configúrala una sola vez a mano — 2 minutos, ver
 * docente/GUIA-GOOGLE-CLASSROOM.md §5. Los puntos de cada tarea de esta
 * plantilla ya están fijados para que, si activas esa función, el promedio
 * salga correcto sin ajustar nada más (Propuesta 10 / Checkpoint 10 / Checkpoint 10 /
 * Entrega final 70, dentro de la categoría Proyecto Final).
 *
 * ============================== CÓMO USARLO ==============================
 * 1. Ve a script.google.com → Nuevo proyecto. Borra el contenido de
 *    Code.gs y pega este archivo completo.
 * 2. En el panel izquierdo, "Servicios" (ícono +) → busca "Google Classroom
 *    API" → Agregar. (Esto habilita el objeto `Classroom` usado abajo.)
 * 3. Arriba, cambia la función seleccionada (donde dice "Seleccionar función")
 *    a `main` y presiona Ejecutar (▶). La primera vez te pedirá autorizar
 *    el acceso a tu propia cuenta de Google — acéptalo (no comparte nada
 *    conmigo ni con nadie más, corre enteramente en tu cuenta).
 * 4. Revisa el registro de ejecución (Ver → Registros, o Ctrl+Enter). Con
 *    DRY_RUN en true (el valor por defecto abajo) el script solo IMPRIME lo
 *    que haría, sin crear ni modificar nada todavía — revísalo con calma.
 * 5. Cuando el registro se vea bien, cambia DRY_RUN a false y ejecuta `main`
 *    de nuevo. Es seguro volver a ejecutarlo cuantas veces quieras: no
 *    duplica temas/tareas que ya existan, solo actualiza sus enlaces.
 * 6. Si tu cuenta no puede crear el curso por API (error CourseStateDenied),
 *    créalo a mano en classroom.google.com, corre la función `listMyCourses`
 *    para obtener su ID numérico real (¡no el de la URL del navegador!), y
 *    pégalo en CONFIG.EXISTING_COURSE_ID.
 * ===========================================================================
 */

// ---------------------------------------------------------------------------
// CONFIGURACIÓN — ajusta esto antes de correr el script
// ---------------------------------------------------------------------------
const CONFIG = {
  DRY_RUN: true, // true = solo simula e imprime en el registro. Cambia a false para crear/actualizar de verdad.

  // ID numérico del curso (NO la URL del navegador — usa listMyCourses() para
  // obtenerlo si tienes dudas). Vacío = el script intenta crear el curso por
  // API (falla con CourseStateDenied en la mayoría de cuentas personales).
  EXISTING_COURSE_ID: "869257559169",

  COURSE_NAME: "INF 222 — Estructura de Datos (2026-2)",
  COURSE_SECTION: "Grupo A / Grupo B",
  COURSE_ROOM: "FIEC — Universidad de Panamá",
  COURSE_DESCRIPTION:
    "Licenciatura en Desarrollo de Aplicaciones Tecnológicas. Docente: Angel R. Avila G. " +
    "Entregas por GitHub — ver docente/GUIA-ENTREGAS-GITHUB.md.",
};

// ---------------------------------------------------------------------------
// Repositorios (ya públicos) — bases para construir los enlaces directos
// ---------------------------------------------------------------------------
const REPO_ROOT = "https://github.com/avila-fiec-up/INF222-Estructura-de-Datos-2026-2";
const REPO_BLOB = REPO_ROOT + "/blob/main/";
const PROJECT_REPO_ROOT = "https://github.com/avila-fiec-up/INF222-Proyecto-Final-2026-2";
const PROJECT_REPO_BLOB = PROJECT_REPO_ROOT + "/blob/main/";

// ---------------------------------------------------------------------------
// DATOS DE LAS 15 SEMANAS (título, tema, carpeta del repo, ítems con
// categoría, puntos, y enlace adicional opcional cuando aplica)
// Categorías: "Laboratorios" (30%) · "Exámenes Parciales" (30%) · "Proyecto Final" (40%)
// ---------------------------------------------------------------------------
const WEEKS = [
  { w: 1, topic: "Semana 01", path: "modulo-1-estructuras-lineales/semana-01", items: [
    { title: "Semana 01 — Introducción, Big-O y Pilas (Lab 1: Pila con lista)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 2, topic: "Semana 02", path: "modulo-1-estructuras-lineales/semana-02", items: [
    { title: "Semana 02 — Pilas avanzadas y colas (Lab 2)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 3, topic: "Semana 03", path: "modulo-1-estructuras-lineales/semana-03", items: [
    { title: "Semana 03 — Variantes de colas · Quiz formativo · Taller · Kickoff proyecto", cat: "Laboratorios", points: 100 },
  ]},
  { w: 4, topic: "Semana 04", path: "modulo-2-estructuras-dinamicas/semana-04", items: [
    { title: "Semana 04 — Punteros y memoria dinámica (Lab 3)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 5, topic: "Semana 05", path: "modulo-2-estructuras-dinamicas/semana-05", items: [
    { title: "Semana 05 — Listas enlazadas simples (Lab 4)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 6, topic: "Semana 06", path: "modulo-2-estructuras-dinamicas/semana-06", items: [
    { title: "Semana 06 — Listas circulares (Lab 5)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 7, topic: "Semana 07", path: "modulo-2-estructuras-dinamicas/semana-07", items: [
    { title: "Semana 07 — Listas doblemente enlazadas (Lab 6)", cat: "Laboratorios", points: 100 },
    { title: "Parcial 1 (Módulos 1 y 2)", cat: "Exámenes Parciales", points: 100,
      link: { url: REPO_BLOB + "examenes/guia-parcial-1.md", title: "Guía de estudio — Parcial 1" } },
    { title: "Proyecto final — Propuesta formal", cat: "Proyecto Final", points: 10,
      link: { url: PROJECT_REPO_BLOB + "propuesta/PLANTILLA-propuesta.md", title: "Plantilla — Propuesta formal" } },
  ]},
  { w: 8, topic: "Semana 08", path: "modulo-3-recursividad-ordenacion-busqueda/semana-08", items: [
    { title: "Semana 08 — Recursividad (Lab 7, con declaración de uso de IA)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 9, topic: "Semana 09", path: "modulo-3-recursividad-ordenacion-busqueda/semana-09", items: [
    { title: "Semana 09 — Algoritmos de ordenación (Lab 8)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 10, topic: "Semana 10", path: "modulo-3-recursividad-ordenacion-busqueda/semana-10", items: [
    { title: "Semana 10 — Búsqueda (Lab 9)", cat: "Laboratorios", points: 100 },
    { title: "Proyecto final — Checkpoint 1", cat: "Proyecto Final", points: 10,
      link: { url: PROJECT_REPO_BLOB + "checkpoint-1/PLANTILLA-checkpoint-1.md", title: "Plantilla — Checkpoint 1" } },
  ]},
  { w: 11, topic: "Semana 11", path: "modulo-3-recursividad-ordenacion-busqueda/semana-11", items: [
    { title: "Semana 11 — Taller integrador", cat: "Laboratorios", points: 100 },
    { title: "Parcial 2 (Módulo 3)", cat: "Exámenes Parciales", points: 100,
      link: { url: REPO_BLOB + "examenes/guia-parcial-2.md", title: "Guía de estudio — Parcial 2" } },
  ]},
  { w: 12, topic: "Semana 12", path: "modulo-4-arboles-grafos/semana-12", items: [
    { title: "Semana 12 — Árboles generales y binarios (Lab 10)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 13, topic: "Semana 13", path: "modulo-4-arboles-grafos/semana-13", items: [
    { title: "Semana 13 — BST: inserción, búsqueda, eliminación (Lab 11)", cat: "Laboratorios", points: 100 },
  ]},
  { w: 14, topic: "Semana 14", path: "modulo-4-arboles-grafos/semana-14", items: [
    { title: "Semana 14 — Grafos, BFS y DFS (Lab 12)", cat: "Laboratorios", points: 100 },
    { title: "Proyecto final — Checkpoint 2", cat: "Proyecto Final", points: 10,
      link: { url: PROJECT_REPO_BLOB + "checkpoint-2/PLANTILLA-checkpoint-2.md", title: "Plantilla — Checkpoint 2" } },
  ]},
  { w: 15, topic: "Semana 15", path: "modulo-4-arboles-grafos/semana-15", items: [
    { title: "Parcial 3 (Módulo 4)", cat: "Exámenes Parciales", points: 100,
      link: { url: REPO_BLOB + "examenes/guia-parcial-3.md", title: "Guía de estudio — Parcial 3" } },
    { title: "Proyecto final — Entrega final y sustentación", cat: "Proyecto Final", points: 70,
      link: { url: PROJECT_REPO_BLOB + "entrega-final/PLANTILLA-readme-proyecto.md", title: "Plantilla — Entrega final" } },
  ]},
];

const INSTRUCCIONES_GENERICAS =
  "Consulta el README de la semana (enlazado abajo) para los objetivos y el entregable exacto. " +
  "Tu copia de trabajo puede ser privada (el docente te la crea a partir del repositorio) o tu " +
  "propia copia con \"Use this template\" — ver docente/GUIA-ENTREGAS-GITHUB.md. Haz commit y push " +
  "antes de la fecha límite indicada en el aula virtual.";

// ---------------------------------------------------------------------------
// PUNTO DE ENTRADA
// ---------------------------------------------------------------------------
function main() {
  Logger.log("=== INF 222 — configuración de Google Classroom (DRY_RUN=%s) ===", CONFIG.DRY_RUN);

  const courseId = getOrCreateCourse_();
  Logger.log("Curso: %s", courseId);

  const existingTopics = listExistingTopics_(courseId);
  const topicIdByName = {};
  const allTopicNames = WEEKS.map(function (w) { return w.topic; });
  allTopicNames.forEach(function (name) {
    topicIdByName[name] = getOrCreateTopic_(courseId, name, existingTopics);
  });

  const existingWork = listExistingCourseWork_(courseId);
  const existingMaterials = listExistingMaterials_(courseId);

  createOrUpdateWelcomeMaterial_(courseId, topicIdByName["Semana 01"], existingMaterials);
  createGithubUsernameQuestion_(courseId, topicIdByName["Semana 01"], existingWork);

  WEEKS.forEach(function (week) {
    const topicId = topicIdByName[week.topic];
    const weekReadmeUrl = REPO_BLOB + week.path + "/README.md";
    week.items.forEach(function (item) {
      createOrUpdateAssignment_(courseId, topicId, item, weekReadmeUrl, existingWork);
    });
  });

  Logger.log("=== Listo. Revisa el registro completo arriba antes de confiar en el resultado. ===");
}

// ---------------------------------------------------------------------------
// Curso
// ---------------------------------------------------------------------------
function getOrCreateCourse_() {
  if (CONFIG.EXISTING_COURSE_ID) {
    // Acepta tanto el ID solo ("869257559169") como una URL completa pegada
    // por error (".../c/ALGO"), para que ese error no vuelva a romper nada.
    const match = String(CONFIG.EXISTING_COURSE_ID).match(/\/c\/([^/?#]+)/);
    const id = match ? match[1] : CONFIG.EXISTING_COURSE_ID;
    Logger.log("Usando EXISTING_COURSE_ID: %s", id);
    return id;
  }
  if (CONFIG.DRY_RUN) {
    Logger.log('[DRY_RUN] Crearía el curso "%s"', CONFIG.COURSE_NAME);
    return "DRY_RUN_COURSE_ID";
  }
  // No se fija courseState aquí a propósito: pedir "ACTIVE" directamente falla
  // con CourseStateDenied en la mayoría de cuentas personales (no Workspace for
  // Education). Sin el campo, la API crea el curso en estado PROVISIONED.
  let course;
  try {
    course = Classroom.Courses.create({
      name: CONFIG.COURSE_NAME,
      section: CONFIG.COURSE_SECTION,
      room: CONFIG.COURSE_ROOM,
      description: CONFIG.COURSE_DESCRIPTION,
      ownerId: "me",
    });
  } catch (e) {
    throw new Error(
      "No se pudo crear el curso por API (" + e.message + "). " +
      "Tu cuenta probablemente no tiene permiso para crear cursos de Classroom por API — " +
      "esto es normal en cuentas de Google personales. Solución: crea el curso a mano en " +
      "classroom.google.com (+ → Crear clase, 30 segundos), corre listMyCourses() para obtener " +
      "su ID numérico real, y pégalo en CONFIG.EXISTING_COURSE_ID arriba. Luego vuelve a " +
      "ejecutar main()."
    );
  }
  Logger.log('Curso creado en estado PROVISIONED: "%s" (id %s)', course.name, course.id);
  Logger.log(
    "IMPORTANTE: entra a classroom.google.com — este curso recién creado por API pedirá que " +
    "lo confirmes/actives desde la interfaz antes de que sea visible y usable con normalidad."
  );
  return course.id;
}

// ---------------------------------------------------------------------------
// Temas
// ---------------------------------------------------------------------------
function listExistingTopics_(courseId) {
  if (CONFIG.DRY_RUN && courseId === "DRY_RUN_COURSE_ID") return {};
  const byName = {};
  let pageToken;
  do {
    const resp = Classroom.Courses.Topics.list(courseId, { pageToken: pageToken });
    (resp.topic || []).forEach(function (t) { byName[t.name] = t.topicId; });
    pageToken = resp.nextPageToken;
  } while (pageToken);
  return byName;
}

function getOrCreateTopic_(courseId, name, existingTopics) {
  if (existingTopics[name]) {
    Logger.log('Tema "%s" ya existe, se reutiliza', name);
    return existingTopics[name];
  }
  if (CONFIG.DRY_RUN) {
    Logger.log('[DRY_RUN] Crearía el tema "%s"', name);
    return "DRY_RUN_TOPIC_" + name;
  }
  const topic = Classroom.Courses.Topics.create({ name: name }, courseId);
  Logger.log('Tema creado: "%s"', name);
  return topic.topicId;
}

// ---------------------------------------------------------------------------
// CourseWork / Materiales existentes (id por título, para actualizar en vez
// de duplicar si se corre el script más de una vez)
// ---------------------------------------------------------------------------
function listExistingCourseWork_(courseId) {
  const byTitle = {};
  if (CONFIG.DRY_RUN && courseId === "DRY_RUN_COURSE_ID") return byTitle;
  let pageToken;
  do {
    const resp = Classroom.Courses.CourseWork.list(courseId, { pageToken: pageToken });
    (resp.courseWork || []).forEach(function (cw) { byTitle[cw.title] = cw.id; });
    pageToken = resp.nextPageToken;
  } while (pageToken);
  return byTitle;
}

function listExistingMaterials_(courseId) {
  const byTitle = {};
  if (CONFIG.DRY_RUN && courseId === "DRY_RUN_COURSE_ID") return byTitle;
  let pageToken;
  do {
    const resp = Classroom.Courses.CourseWorkMaterials.list(courseId, { pageToken: pageToken });
    (resp.courseWorkMaterial || []).forEach(function (m) { byTitle[m.title] = m.id; });
    pageToken = resp.nextPageToken;
  } while (pageToken);
  return byTitle;
}

// ---------------------------------------------------------------------------
// Material de bienvenida (semana 1) — crea o actualiza sus enlaces
// ---------------------------------------------------------------------------
function createOrUpdateWelcomeMaterial_(courseId, topicId, existingMaterials) {
  const title = "Bienvenida, syllabus y recursos del curso";
  const body = {
    title: title,
    description:
      "Empieza por 'Guía del estudiante' (primer enlace abajo): qué hacer antes de la primera " +
      "clase, cómo obtener tu copia del repositorio, el ritmo de cada semana, cómo se califica, y " +
      "la política de IA — todo en una sola página. El resto de los enlaces son la fuente original " +
      "de cada tema por si quieres el detalle completo. No se aceptan entregas por correo.",
    materials: [
      { link: { url: REPO_BLOB + "GUIA-ESTUDIANTE.md", title: "📌 Guía del estudiante — empieza aquí" } },
      { link: { url: REPO_ROOT, title: "Repositorio del curso — INF 222" } },
      { link: { url: REPO_BLOB + "syllabus/syllabus-oficial-inf222.md", title: "Syllabus oficial" } },
      { link: { url: REPO_BLOB + "docente/03-Sistema-evaluacion-rubricas.md", title: "Sistema de evaluación y rúbricas" } },
      { link: { url: REPO_ROOT + "/tree/main/examenes", title: "Guías de estudio de los 3 parciales" } },
      { link: { url: REPO_BLOB + "politicas/reglas-del-aula.md", title: "Reglas del aula" } },
      { link: { url: REPO_BLOB + "politicas/politica-ia.md", title: "Política de uso de IA" } },
      { link: { url: REPO_BLOB + "recursos/herramientas-setup.md", title: "Guía de instalación de herramientas" } },
      { link: { url: PROJECT_REPO_ROOT, title: "Repositorio del proyecto final" } },
      { link: { url: "https://claude.ai/code/artifact/b139c519-9b3f-4474-8888-e4682df32d79", title: "Presentación de clase — INF 222" } },
      { link: { url: "https://claude.ai/code/artifact/653b3e29-08d9-4336-aed3-2a46b717fd4f", title: "Panel del semestre 2026-2" } },
    ],
    topicId: topicId,
    state: "PUBLISHED",
  };

  const existingId = existingMaterials[title];
  if (CONFIG.DRY_RUN) {
    Logger.log(existingId
      ? '[DRY_RUN] Actualizaría los enlaces del material "%s"'
      : '[DRY_RUN] Crearía el material "%s"', title);
    return;
  }
  if (existingId) {
    Classroom.Courses.CourseWorkMaterials.patch(body, courseId, existingId, { updateMask: "materials,description" });
    Logger.log('Material actualizado: "%s"', title);
  } else {
    Classroom.Courses.CourseWorkMaterials.create(body, courseId);
    Logger.log('Material creado: "%s"', title);
  }
}

// ---------------------------------------------------------------------------
// Pregunta para recolectar el usuario de GitHub
// ---------------------------------------------------------------------------
function createGithubUsernameQuestion_(courseId, topicId, existingWork) {
  const title = "Tu usuario de GitHub";
  if (existingWork[title]) {
    Logger.log('Pregunta "%s" ya existe, se omite', title);
    return;
  }
  const body = {
    title: title,
    description:
      "Crea una cuenta en github.com si no tienes una (usa un nombre profesional). Escribe aquí tu " +
      "usuario exacto — lo voy a usar para darte acceso a tu copia del repositorio del curso.",
    workType: "SHORT_ANSWER_QUESTION",
    topicId: topicId,
    state: "PUBLISHED",
    maxPoints: 0,
  };
  if (CONFIG.DRY_RUN) {
    Logger.log('[DRY_RUN] Crearía la pregunta "%s"', title);
    return;
  }
  Classroom.Courses.CourseWork.create(body, courseId);
  Logger.log('Pregunta creada: "%s"', title);
}

// ---------------------------------------------------------------------------
// Tareas semanales / parciales / hitos del proyecto — crea o actualiza enlaces
// ---------------------------------------------------------------------------
function createOrUpdateAssignment_(courseId, topicId, item, weekReadmeUrl, existingWork) {
  const materials = [
    { link: { url: weekReadmeUrl, title: "README de la semana en GitHub" } },
  ];
  if (item.link) {
    materials.push({ link: { url: item.link.url, title: item.link.title } });
  }

  const body = {
    title: item.title,
    description: INSTRUCCIONES_GENERICAS + "\n\nCategoría: " + item.cat + " (ver docente/03-Sistema-evaluacion-rubricas.md).",
    workType: "ASSIGNMENT",
    maxPoints: item.points,
    materials: materials,
    topicId: topicId,
    state: "PUBLISHED", // cambia a "DRAFT" si prefieres revisar/publicar cada una a mano
  };

  const existingId = existingWork[item.title];
  if (CONFIG.DRY_RUN) {
    Logger.log(existingId
      ? '[DRY_RUN] Actualizaría los enlaces de "%s" (%s, %s pts)'
      : '[DRY_RUN] Crearía la tarea "%s" (%s, %s pts)', item.title, item.cat, item.points);
    return;
  }
  if (existingId) {
    Classroom.Courses.CourseWork.patch(body, courseId, existingId, { updateMask: "materials,description" });
    Logger.log('Tarea actualizada: "%s" (%s, %s pts)', item.title, item.cat, item.points);
  } else {
    Classroom.Courses.CourseWork.create(body, courseId);
    Logger.log('Tarea creada: "%s" (%s, %s pts)', item.title, item.cat, item.points);
  }
}

// ---------------------------------------------------------------------------
// Utilidad: lista tus cursos existentes y sus IDs (para llenar EXISTING_COURSE_ID)
// ---------------------------------------------------------------------------
function listMyCourses() {
  const resp = Classroom.Courses.list({ teacherId: "me" });
  (resp.courses || []).forEach(function (c) {
    Logger.log("%s — id: %s — estado: %s", c.name, c.id, c.courseState);
  });
}
