# Módulo 8 — Construir algo real

Ya conoces los componentes básicos. Ahora vas a construir algo.

En este módulo eliges uno de cuatro proyectos y lo terminas. No tiene que ser perfecto — pero sí debe funcionar. Y que funcione es la única medida que importa.

---

## Elige tu proyecto

Elige el proyecto que más te interese.

---

### Proyecto A — Quiz

Un quiz que hace preguntas y lleva la cuenta de cuántas acertaste.

**Qué hace:**
- Hace 3 preguntas o más
- Acepta una respuesta del usuario
- Indica si fue correcta o incorrecta
- Da la puntuación total al final

**Punto de partida:**
```javascript
let puntuacion = 0;

function hacerPregunta(pregunta, respuestaCorrecta) {
    let respuesta = prompt(pregunta);
    if (respuesta.toLowerCase() === respuestaCorrecta.toLowerCase()) {
        alert("¡Correcto!");
        puntuacion++;
    } else {
        alert("Lástima. La respuesta correcta era: " + respuestaCorrecta);
    }
}

hacerPregunta("¿Cuál es la capital de los Países Bajos?", "Ámsterdam");
hacerPregunta("¿Cuánto es 7 por 8?", "56");
hacerPregunta("¿Quién escribió el primer algoritmo para una máquina?", "Ada Lovelace");

alert("Tu puntuación: " + puntuacion + " de 3");
```

**Amplíalo:**
- Añade más preguntas
- Da retroalimentación por pregunta
- Haz que las preguntas sean aleatorias con `Math.random()`

---

### Proyecto B — Calculadora

Una calculadora que opera con dos números y una operación.

**Qué hace:**
- Pide dos números
- Pregunta qué operación (+, -, *, /)
- Da el resultado

**Punto de partida:**
```javascript
function calcular(a, b, operacion) {
    if (operacion === "+") return a + b;
    if (operacion === "-") return a - b;
    if (operacion === "*") return a * b;
    if (operacion === "/") {
        if (b === 0) return "No se puede dividir entre cero";
        return a / b;
    }
    return "Operación desconocida";
}

let numero1 = Number(prompt("Primer número:"));
let numero2 = Number(prompt("Segundo número:"));
let operacion = prompt("Operación (+, -, *, /):");

let resultado = calcular(numero1, numero2, operacion);
alert(numero1 + " " + operacion + " " + numero2 + " = " + resultado);
```

**Amplíalo:**
- Deja que el usuario haga varios cálculos seguidos
- Añade la raíz cuadrada (`Math.sqrt()`)
- Guarda un historial de todos los cálculos

---

### Proyecto C — Procesador de texto

Un programa que hace algo con el texto que introduces.

**Qué hace:**
- Cuenta el número de palabras de un texto
- Cuenta cuántas veces aparece una palabra determinada
- Convierte el texto a mayúsculas o minúsculas

**Punto de partida:**
```javascript
let texto = prompt("Introduce un texto:");

let palabras = texto.split(" ");
alert("Número de palabras: " + palabras.length);

let palabraBuscada = prompt("¿Qué palabra quieres buscar?");
let contador = 0;
for (let i = 0; i < palabras.length; i++) {
    if (palabras[i].toLowerCase() === palabraBuscada.toLowerCase()) {
        contador++;
    }
}
alert("'" + palabraBuscada + "' aparece " + contador + " veces");
```

**Amplíalo:**
- Sustituye una palabra por otra palabra
- Invierte el orden de las palabras
- Cuenta el número de frases (pista: busca los puntos)

---

### Proyecto D — Adivina el número

Un juego en el que el ordenador elige un número y tú debes adivinarlo.

**Qué hace:**
- El ordenador elige un número aleatorio entre 1 y 100
- El jugador hace una suposición
- El programa dice "demasiado alto", "demasiado bajo" o "acertaste"
- Cuenta cuántos intentos necesitó el jugador

**Punto de partida:**
```javascript
let secreto = Math.floor(Math.random() * 100) + 1;
let intentos = 0;
let acertado = false;

while (!acertado) {
    let intento = Number(prompt("Adivina un número entre 1 y 100:"));
    intentos++;

    if (intento < secreto) {
        alert("¡Demasiado bajo! Prueba con uno más alto.");
    } else if (intento > secreto) {
        alert("¡Demasiado alto! Prueba con uno más bajo.");
    } else {
        alert("¡Acertaste! Necesitaste " + intentos + " intentos.");
        acertado = true;
    }
}
```

**Amplíalo:**
- Añade un número máximo de intentos
- Da una valoración según el número de intentos
- Deja que el jugador vuelva a jugar sin recargar la página

---

## Cómo abordarlo

**Paso 1 — Elige y comprende el punto de partida**
Lee el código línea por línea. ¿Puedes explicar qué hace cada línea?

**Paso 2 — Haz que funcione tal cual está**
Copia el punto de partida en la consola del navegador y ejecútalo. ¿Funciona?

**Paso 3 — Ajusta una cosa**
Cambia un valor pequeño o añade una línea. Vuelve a ejecutarlo.

**Paso 4 — Amplíalo paso a paso**
Añade una ampliación a la vez. Prueba después de cada adición.

**Paso 5 — Rómpelo deliberadamente**
Cambia algo para que falle. Lee el mensaje de error. Arréglalo.

---

## ¿Qué hace bueno a un programa?

- Hace lo que se supone que debe hacer
- Da una retroalimentación clara al usuario
- No falla ante una entrada inesperada
- Puedes explicarle a otros cómo funciona

El perfeccionismo es el enemigo de terminar algo. Haz que funcione — luego podrás mejorarlo.
