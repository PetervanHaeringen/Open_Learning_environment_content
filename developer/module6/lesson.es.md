# Módulo 6 — Los componentes de un programa

Has sentido los algoritmos con tus propias manos. Ahora vas a escribirlos.
Abre la consola del navegador (F12 → Console) y escribe a medida que vas leyendo.

---

## 1. Variables — poner nombre a los valores

Una variable es un nombre que guarda un valor.

```javascript
let nombre = "Ali";
let edad = 23;
let activo = true;
```

- `let` crea una nueva variable
- `nombre`, `edad`, `activo` son los nombres
- Los valores a la derecha del `=` se almacenan

Escribe esto en la consola y pulsa Enter después de cada línea.
Luego escribe `nombre` y pulsa Enter — la consola muestra "Ali".

**Tres tipos de valores:**
- Texto (string): `"Ali"` — siempre entre comillas
- Número (number): `23` — sin comillas
- Verdadero/falso (boolean): `true` o `false`

---

## 2. Condiciones — tomar decisiones

```javascript
let temperatura = 22;

if (temperatura > 25) {
    console.log("Calor — lleva agua");
} else {
    console.log("Fresco — una chaqueta viene bien");
}
```

Escribe esto en la consola. Luego cambia `22` por `30` y ejecútalo de nuevo.

La estructura siempre es:
```javascript
if (condicion) {
    // haz esto si la condición es verdadera
} else {
    // haz esto si la condición no es verdadera
}
```

**Operadores de comparación:**
| Operador | Significado |
|----------|-----------|
| `>` | mayor que |
| `<` | menor que |
| `>=` | mayor o igual que |
| `<=` | menor o igual que |
| `===` | exactamente igual a |
| `!==` | distinto de |

---

## 3. Bucles — repetir

**Bucle for** — cuando sabes cuántas veces quieres repetir algo:

```javascript
for (let i = 1; i <= 5; i++) {
    console.log("Paso " + i);
}
```

Esto imprime "Paso 1" hasta "Paso 5".

Las tres partes entre paréntesis:
1. `let i = 1` — empieza en 1
2. `i <= 5` — continúa mientras i sea menor o igual que 5
3. `i++` — aumenta i en 1 después de cada paso

**Bucle while** — cuando no sabes cuántas veces:

```javascript
let contador = 1;

while (contador <= 5) {
    console.log("El contador ahora es: " + contador);
    contador++;
}
```

Mismo resultado, forma distinta de escribirlo. Usa `while` cuando la condición de parada dependa de algo que cambia durante la ejecución del programa.

---

## 4. Funciones — bloques reutilizables

Una función es un bloque de código con un nombre. Lo escribes una vez y lo usas muchas veces.

```javascript
function saludar(nombre) {
    console.log("Hola, " + nombre + "!");
}

saludar("Ali");
saludar("Fatima");
saludar("Jonas");
```

La función `saludar` espera un **parámetro** — `nombre`.
Cada vez que llamas a la función, le pasas un valor distinto.

**Funciones que devuelven un valor:**

```javascript
function cuadrado(numero) {
    return numero * numero;
}

let resultado = cuadrado(4);
console.log(resultado);
```

`return` devuelve un valor. Puedes guardarlo o usarlo directamente.

---

## 5. Todo junto — un mini programa

```javascript
function calificar(puntuacion) {
    if (puntuacion >= 90) {
        return "Excelente";
    } else if (puntuacion >= 70) {
        return "Bien";
    } else if (puntuacion >= 55) {
        return "Suficiente";
    } else {
        return "Insuficiente";
    }
}

let puntuaciones = [88, 42, 95, 67, 55];

for (let i = 0; i < puntuaciones.length; i++) {
    let calificacion = calificar(puntuaciones[i]);
    console.log("Puntuación " + puntuaciones[i] + ": " + calificacion);
}
```

Copia esto en la consola. Observa lo que ocurre.
Luego cambia una puntuación y ejecútalo de nuevo.

Esto es un programa real: tiene entrada, procesamiento y salida.

---

## 6. Ejercicios

Prueba estos ejercicios en la consola del navegador:

**Ejercicio 1:** Escribe una función `esPar` que devuelva `true` si un número es par, y `false` si es impar. Pruébala con los números 4, 7, 12 y 9.

**Ejercicio 2:** Escribe un bucle que imprima la tabla del 3 (3, 6, 9, ... hasta el 30 incluido).

**Ejercicio 3:** Crea una lista con cinco nombres. Recorre la lista e imprime cada nombre con "¡Bienvenido, [nombre]!".

*Consejo: usa `let nombres = ["nombre1", "nombre2", ...]` para una lista (array).*
