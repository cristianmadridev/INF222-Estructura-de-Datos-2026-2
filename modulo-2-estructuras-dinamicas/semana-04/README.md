# Semana 4 — Punteros, Memoria Dinámica y Referencias en Python

**Módulo 2: Estructuras de datos dinámicas lineales**

---

## Objetivos de aprendizaje

- Comprender el concepto clásico de **puntero** y asignación dinámica de memoria (heap vs. stack de ejecución).
- Relacionar los punteros de C con el **modelo de referencias a objetos** de Python.
- Explicar el fenómeno de **aliasing** y sus consecuencias al mutar estructuras de datos.
- Predecir el comportamiento de código con referencias compartidas usando `id()`.

---

## Contenidos de la semana

### Teoría (martes + miércoles)

1. Punteros (contexto histórico y conceptual):
   - Dirección de memoria como "dónde está el dato en el heap"
   - Puntero = variable que almacena una dirección
   - Desreferencia: acceder al dato a través del puntero
2. Modelo de Python (equivalente moderno):
   - Toda variable es una referencia a un objeto en el heap
   - `id(x)` retorna la identidad del objeto (equivalente a la dirección)
   - Mutabilidad vs. inmutabilidad: `list` es mutable, `int`/`str`/`tuple` son inmutables
3. Aliasing:
   - `lista_b = lista_a` NO crea una copia — ambas apuntan al mismo objeto
   - Mutar a través de una referencia afecta todas las referencias al mismo objeto
   - Cómo copiar correctamente: `lista.copy()`, `list(original)`, `copy.deepcopy()`

### Laboratorio (miércoles Gr. A / viernes Gr. B)

1. Ejercicios con `id()` para observar cuándo dos variables referencian el mismo objeto
2. Experimentos de aliasing: mutar a través de una segunda referencia
3. Implementar una función que decida si mutar in situ o retornar una copia
4. Predicciones previas + verificación con Python Tutor

---

## Entregable de la semana

**Laboratorio 3** *(numeración del plan de trabajo)* — Referencias y Aliasing

- Archivo: `modulo-2-estructuras-dinamicas/semana-04/laboratorio/lab04_referencias_aliasing.py`
- Herramienta clave: **Python Tutor** para visualizar el estado de la memoria

---

## Tarea / trabajo autónomo

Predecir la salida de los fragmentos de código del archivo `lab04_referencias_aliasing.py` **antes** de ejecutarlos. Luego verifica con Python Tutor y documenta si tu predicción fue correcta y por qué.

---

## Diagrama mental: puntero vs. referencia Python

```
C (puntero):                    Python (referencia):
int x = 42;                     x = 42
int *p = &x;    ───────────>    p = x         # p referencia el mismo int 42
*p = 99;                        # pero 42 es inmutable, no puedes cambiarlo
                                # x sigue siendo 42

Con listas (mutables):
int arr[] = {1,2,3};            arr = [1, 2, 3]
int *p = arr;                   p = arr          # MISMO objeto
p[0] = 99;    ──────────>       p[0] = 99        # arr[0] también es 99
```

---

## Recurso imprescindible esta semana

**Python Tutor** — pythontutor.com — Ejecuta paso a paso el código de aliasing y observa las flechas (referencias) en el diagrama de memoria.
