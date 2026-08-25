# Semana 10 — Búsqueda y Checkpoint 1 del Proyecto Final

**Módulo 3: Recursividad, ordenación y búsqueda**

---

## Objetivos de aprendizaje

- Implementar búsqueda secuencial (lineal) en su versión iterativa.
- Implementar búsqueda binaria en sus versiones **iterativa** y **recursiva**.
- Comparar la eficiencia de ambos métodos: O(n) vs. O(log n).
- Comprender la precondición de la búsqueda binaria (datos ordenados).
- Presentar el **Checkpoint 1 del proyecto final** con retroalimentación del docente.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Búsqueda secuencial:
   - Recorre elemento por elemento hasta encontrar el objetivo
   - Funciona en arreglos no ordenados
   - Complejidad: O(n) en todos los casos útiles
2. Búsqueda binaria:
   - **Precondición**: el arreglo DEBE estar ordenado
   - Divide el espacio de búsqueda a la mitad en cada paso
   - Complejidad: O(log n)
   - Versión iterativa: mantiene punteros `izquierda` y `derecha`
   - Versión recursiva: llama con el subarreglo correspondiente

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Implementar `busqueda_secuencial` e `busqueda_binaria` (ambas versiones)
2. Comparar tiempos en arreglos de distintos tamaños
3. **Checkpoint 1 del proyecto final**: el docente revisa el avance de cada equipo

---

## Entregable de la semana

**Laboratorio 9** — Búsqueda secuencial y binaria

- Archivo: `modulo-3-recursividad-ordenacion-busqueda/semana-10/laboratorio/lab10_busqueda.py`

**Checkpoint 1 del proyecto final** (en equipo):

- Archivo: `proyecto-final/checkpoint-1/PLANTILLA-checkpoint-1.md` → renombrar a `checkpoint-1.md`
- El docente revisará el código en `proyecto-final/src/`

---

## Checkpoint 1 del Proyecto Final — ¿Qué debes tener?

Al menos **una estructura de datos correctamente implementada** y **en uso** dentro del proyecto:
- No basta con tener la clase definida; debe estar integrada en la lógica del sistema
- El código debe ejecutarse sin errores
- El README del proyecto debe estar actualizado con el alcance actual

---

## Trazado de búsqueda binaria

Buscar el valor 40 en: `[5, 10, 20, 30, 40, 50, 60, 70, 80]` (índices 0-8)

```
Iteración 1:  izq=0, der=8, mid=4 → arr[4]=40 == 40 → ¡ENCONTRADO en pos 4!

Buscar 35 en el mismo arreglo:
Iteración 1:  izq=0, der=8, mid=4 → arr[4]=40 > 35 → buscar en la mitad izquierda
Iteración 2:  izq=0, der=3, mid=1 → arr[1]=10 < 35 → buscar en la mitad derecha
Iteración 3:  izq=2, der=3, mid=2 → arr[2]=20 < 35 → buscar en la mitad derecha
Iteración 4:  izq=3, der=3, mid=3 → arr[3]=30 < 35 → buscar en la mitad derecha
              izq=4 > der=3 → NO ENCONTRADO
```

---

## Tarea / trabajo autónomo

En el repositorio del proyecto, redactar una **bitácora de avance** (`proyecto-final/checkpoint-1/checkpoint-1.md`) con:
- Qué estructura(s) de datos implementaron hasta ahora
- Decisiones de diseño tomadas y por qué
- Problemas encontrados y cómo los resolvieron
- Qué falta para el checkpoint 2
