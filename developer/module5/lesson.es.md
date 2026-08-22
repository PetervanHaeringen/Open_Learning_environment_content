# Módulo 5 — Programar sin ordenador

No entiendes el código leyéndolo. Lo entiendes *haciéndolo*.
En este módulo vas a representar algoritmos — con tarjetas, roles y tu propio cuerpo.

---

## Material

- Tarjetas o post-its (mínimo 20)
- Rotuladores
- Participantes: de 3 a 8 personas
- Opcional: cinta adhesiva en el suelo para marcar "espacios de memoria"

---

## Roles del juego

| Rol | Tarea |
|-----|------|
| **Procesador** | Ejecuta las instrucciones — una por una |
| **Memoria** | Sostiene tarjetas con valores (variables) |
| **Entrada** | Proporciona nuevos valores cuando el programa los pide |
| **Salida** | Escribe lo que el programa "imprime" |
| **Programa** | Lee las instrucciones en voz alta, una por una |

---

## Juego 1 — Variables y suma

**El programa:**
```
1. Guarda el valor 5 como "x"
2. Guarda el valor 3 como "y"
3. Calcula x + y
4. Guarda el resultado como "suma"
5. Imprime "suma"
```

**Desarrollo del juego:**
- Memoria escribe "x = 5" en una tarjeta y la sostiene
- Memoria escribe "y = 3" en una tarjeta y la sostiene
- Procesador le pregunta a Memoria: "¿Qué es x?" → Memoria muestra la tarjeta
- Procesador pregunta: "¿Qué es y?" → Memoria muestra la tarjeta
- Procesador calcula 5 + 3 = 8
- Memoria escribe "suma = 8" en una tarjeta nueva
- Salida escribe "8" en la pizarra

**Puesta en común:** ¿Qué pasa si en el paso 1 cambias "x = 5" por "x = 10"? ¿Quién ajusta qué?

---

## Juego 2 — Condición (if/else)

**El programa:**
```
1. Pregunta un número al usuario → guárdalo como "numero"
2. Si numero es mayor que 10:
       imprime "grande"
   Si no:
       imprime "pequeño"
```

**Desarrollo del juego:**
- Entrada elige un número (por ejemplo, 7) y lo escribe en una tarjeta
- Memoria lo guarda como "numero = 7"
- Procesador pregunta: "¿Es 7 mayor que 10?" → No
- Procesador va a la rama "Si no"
- Salida escribe "pequeño"

Juégalo tres veces con números distintos. ¿Qué cambia en el comportamiento del Procesador?

---

## Juego 3 — Bucle (repetición)

**El programa:**
```
1. Guarda el valor 1 como "contador"
2. Mientras contador sea menor o igual que 5:
       imprime contador
       aumenta contador en 1
3. Listo
```

**Desarrollo del juego:**
- Memoria empieza con "contador = 1"
- Procesador comprueba: ¿1 ≤ 5? Sí → salida escribe "1", contador pasa a 2
- Procesador comprueba: ¿2 ≤ 5? Sí → salida escribe "2", contador pasa a 3
- ... (continúa hasta que contador = 6)
- Procesador comprueba: ¿6 ≤ 5? No → se detiene

**Puesta en común:** ¿Qué pasaría si hubiéramos olvidado el paso 3 — "aumenta contador en 1"? Pruébalo.

*(Esto es un **bucle infinito** — el programa nunca se detiene. Es un error muy común.)*

---

## Juego 4 — Ordenar (representar un algoritmo)

Este es un clásico: **Bubble Sort** (ordenamiento de burbuja).

**Preparación:**
- Escribe 5 números al azar en tarjetas: por ejemplo, 4, 1, 7, 2, 9
- Colócalos en fila sobre la mesa

**El algoritmo:**
```
Repite hasta que ya no cambie nada:
    Para cada par de números contiguos:
        Si el número de la izquierda es mayor que el de la derecha:
            Intercámbialos
```

**Desarrollo del juego:**
- Ronda 1: compara 4 y 1 → 4 > 1, intercambia → [1, 4, 7, 2, 9]
- Compara 4 y 7 → 4 < 7, no intercambies
- Compara 7 y 2 → 7 > 2, intercambia → [1, 4, 2, 7, 9]
- Compara 7 y 9 → 7 < 9, no intercambies
- Ronda 2: vuelve a empezar desde el principio...
- Continúa hasta que una ronda completa no produzca ningún intercambio

**Puesta en común:**
- ¿Cuántas rondas necesitaste?
- ¿Cuál es el "peor caso" — qué orden requiere más pasos?
- ¿Se te ocurre un enfoque más rápido?

---

## Conexión con código real

Después de estos juegos, reconocerás los conceptos cuando te los encuentres en código:

| Lo que hiciste en el juego | En código |
|--------------------------|---------|
| Sostener una tarjeta con un valor | `x = 5` (variable) |
| "Si esto, entonces aquello" | `if / else` |
| Repetir hasta que una condición deja de cumplirse | bucle `while` |
| Recorrer una fila | bucle `for` |
| Olvidar un paso, provocando que no se detenga | bucle infinito (bug) |

En el próximo módulo escribirás todo esto tú mismo — pero en un lenguaje real.
