# Módulo 7 — Cometer y leer errores

Todo programa que escribas fallará en algún momento.
Eso no es grave — es inevitable. La pregunta no es *si* cometerás errores, sino con qué rapidez los encuentras y los solucionas.

Los buenos developers no son personas que no cometen errores. Son personas que leen los errores rápido.

---

## 1. Tres tipos de errores

**Error de sintaxis (SyntaxError)**
El código es gramaticalmente incorrecto — el lenguaje no lo entiende.

```javascript
console.log("Hola"   // falta el paréntesis de cierre
```
```
Uncaught SyntaxError: Unexpected end of input
```

El intérprete ni siquiera puede empezar a ejecutar el código. Busca paréntesis, comillas o llaves que falten.

---

**Error en tiempo de ejecución (Runtime error)**
El código es gramaticalmente correcto, pero falla durante la ejecución.

```javascript
let numero = null;
console.log(numero.toString());
```
```
Uncaught TypeError: Cannot read properties of null
```

El código parece válido pero intenta hacer algo que no es posible — en este caso, llamar a un método sobre `null`.

---

**Error lógico**
El código se ejecuta sin ningún mensaje de error, pero no hace lo que pretendías.

```javascript
function promedio(a, b) {
    return a + b / 2;   // error: solo divide b entre 2
}

console.log(promedio(4, 6));  // da 7, no 5
```

Este es el tipo de error más difícil — el ordenador no se queja. Tienes que descubrir tú mismo qué está mal.

---

## 2. Leer mensajes de error

Un mensaje de error no es un ataque. Es información.

```
Uncaught TypeError: nombres.push is not a function
    at <anonymous>:3:7
```

Léelo en tres pasos:

1. **Tipo de error** — `TypeError`: algo tiene el tipo equivocado
2. **Descripción** — `nombres.push is not a function`: la variable `nombres` no tiene un método `push`
3. **Ubicación** — `at <anonymous>:3:7`: línea 3, carácter 7

Empieza siempre por el primer mensaje de error. A veces un solo error desencadena una cascada de otros mensajes.

---

## 3. Depurar como proceso de pensamiento

Depurar (debugging) es pensamiento científico: formular una hipótesis, probarla, sacar una conclusión.

**Paso 1 — Reproduce el problema**
¿Puedes hacer que el problema ocurra de forma fiable? Si no sabes cuándo falla, no puedes solucionarlo.

**Paso 2 — Aísla el problema**
Reduce el código hasta que tengas la versión más pequeña que siga fallando. Cuanto menos código, más fácil de entender.

**Paso 3 — Formula una hipótesis**
"Creo que falla porque la variable x está vacía en este punto."

**Paso 4 — Comprueba la hipótesis**
Añade `console.log` para ver cuáles son los valores:

```javascript
function calcularDescuento(precio, porcentaje) {
    console.log("precio:", precio);           // comprobar entrada
    console.log("porcentaje:", porcentaje);  // comprobar entrada
    let descuento = precio * porcentaje / 100;
    console.log("descuento:", descuento);        // comprobar cálculo
    return precio - descuento;
}
```

**Paso 5 — Ajusta y prueba de nuevo**
¿Era correcta tu hipótesis? Si no, formula una nueva.

---

## 4. Errores comunes y cómo solucionarlos

| Error | Causa | Solución |
|------|---------|-----------|
| `is not defined` | La variable no existe o el nombre está mal escrito | Comprueba el nombre y si se usó `let` |
| `is not a function` | Se llama a algo que no es una función | Comprueba el tipo de la variable |
| `Cannot read properties of null` | Se llama a un método sobre null/undefined | Comprueba si la variable tiene un valor |
| `SyntaxError` | Falta un paréntesis, comilla o llave | Cuenta los paréntesis — ¿están cerrados? |
| Bucle infinito | La condición de parada nunca se vuelve falsa | Comprueba si la variable de la condición cambia |

---

## 5. Reparar programas rotos

A continuación hay tres fragmentos de código roto. Encuentra el error y arréglalo.

**Programa roto 1:**
```javascript
function saludar(nombre) {
    console.log("Hola, " + nombre)
}

saludar("Ali"
```

**Programa roto 2:**
```javascript
let puntuacion = "95";

if (puntuacion >= 90) {
    console.log("Aprobado");
}
```
*(Pista: `puntuacion` es un string, no un número. ¿Qué hace `>=` con un string?)*

**Programa roto 3:**
```javascript
function multiplicar(a, b) {
    return a + b;
}

console.log(multiplicar(3, 4));  // se espera 12, da 7
```

---

## 6. La mentalidad de quien depura

Los mejores developers no se enfadan con los errores — sienten curiosidad.

Un error significa: *el ordenador te está diciendo algo sobre tu propio código que aún no sabías.*

Eso es valioso. Cada error que solucionas te hace mejor a la hora de evitar ese mismo error la próxima vez.

> "Depurar es como ser el detective de una historia policiaca en la que tú también eres el asesino."
