# Semana 12 — Árboles Generales y Binarios

**Módulo 4: Estructura avanzada de datos**

---

## Objetivos de aprendizaje

- Definir la terminología de árboles: raíz, nodo, hoja, padre, hijo, nivel, altura, profundidad, subárbol.
- Distinguir árboles generales de árboles binarios.
- Implementar los tres recorridos fundamentales de un árbol binario: **inorden**, **preorden** y **postorden**.
- Conectar la recursividad del Módulo 3 con el recorrido de árboles.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Árboles generales:
   - Colección jerárquica de nodos; cada nodo tiene un padre (excepto la raíz)
   - Terminología: raíz, nodo interno, hoja, nivel (profundidad), altura del árbol
2. Árboles binarios:
   - Cada nodo tiene a lo sumo 2 hijos: izquierdo y derecho
   - Implementación: clase `NodoArbol` (dato, hijo_izq, hijo_der)
3. Recorridos recursivos:
   - **Preorden**: raíz → izquierda → derecha (útil para copiar/serializar el árbol)
   - **Inorden**: izquierda → raíz → derecha (en BST produce los elementos ordenados)
   - **Postorden**: izquierda → derecha → raíz (útil para eliminar el árbol, calcular tamaño)

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar `NodoArbol` y `ArbolBinario`
2. Implementar los 3 recorridos de forma recursiva
3. Visualizar y comparar las 3 salidas sobre el mismo árbol

---

## Entregable de la semana

**Laboratorio 10** — Árbol binario con tres recorridos

- Archivo: `modulo-4-arboles-grafos/semana-12/laboratorio/lab12_arbol_binario.py`

---

## Tarea / trabajo autónomo

Implementar el **recorrido por niveles** (BFS sobre árbol, usando una cola) como puente conceptual hacia los grafos de la semana 14.

---

## Árbol de ejemplo — trazado de los 3 recorridos

```
        10
       /  \
      5    20
     / \     \
    3   7    30

Inorden    (izq-raíz-der): 3, 5, 7, 10, 20, 30
Preorden   (raíz-izq-der): 10, 5, 3, 7, 20, 30
Postorden  (izq-der-raíz): 3, 7, 5, 30, 20, 10
Por niveles (BFS):          10, 5, 20, 3, 7, 30
```

---

## Terminología clave

| Término | Definición |
|---------|-----------|
| Raíz | Nodo sin padre (punto de entrada al árbol) |
| Nodo interno | Nodo con al menos un hijo |
| Hoja | Nodo sin hijos |
| Nivel / profundidad | Distancia desde la raíz (raíz = nivel 0) |
| Altura del árbol | Máximo nivel de cualquier hoja |
| Subárbol | Un nodo con todos sus descendientes |
