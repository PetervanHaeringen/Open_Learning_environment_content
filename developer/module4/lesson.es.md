# Módulo 4 — Comparando lenguajes

Existen cientos de lenguajes de programación. No necesitas conocerlos todos.
Pero sí necesitas entender por qué hay tantos — y cómo elegir.

---

## 1. El mismo problema, tres lenguajes

Empecemos con un algoritmo sencillo: determinar si un número es par o impar.

**Pseudocódigo** — no es un lenguaje real, solo la idea escrita:
```
si número es divisible por 2:
    imprimir "par"
si no:
    imprimir "impar"
```

**Python:**
```python
numero = 7
if numero % 2 == 0:
    print("par")
else:
    print("impar")
```

**JavaScript:**
```javascript
let numero = 7;
if (numero % 2 === 0) {
    console.log("par");
} else {
    console.log("impar");
}
```

La idea es idéntica. La ortografía es distinta.

Fíjate: Python usa la indentación (los espacios en blanco) para delimitar bloques. JavaScript usa llaves `{}`. Ambos funcionan — son simplemente elecciones distintas de quienes diseñaron el lenguaje.

---

## 2. Los grandes nombres y para qué sirven

| Lenguaje | Punto fuerte | Uso típico |
|------|----------|-----------------------|
| Python | legibilidad, datos, IA | scripts, análisis de datos, backend, educación |
| JavaScript | navegador, interactividad | sitios web, frontend, también backend (Node.js) |
| Java | estabilidad, sistemas grandes | software empresarial, Android |
| C / C++ | velocidad, control del hardware | sistemas operativos, motores de videojuegos, embebido |
| SQL | consultar bases de datos | cualquier aplicación con base de datos |
| HTML/CSS | estructura y estilo | páginas web (no es un lenguaje de programación, pero sí es código) |
| PHP | servidores web | WordPress, muchos sitios web ya existentes |
| Swift / Kotlin | móvil | iOS (Swift), Android (Kotlin) |

No existe el lenguaje "mejor". Cada lenguaje es una herramienta. Eliges según el problema.

---

## 3. ¿Cómo se lee código desconocido?

A lo largo de tu carrera, te vas a encontrar constantemente con código que nunca has visto antes.
Eso es normal. La habilidad no consiste en saberlo todo — consiste en poder leer la idea general.

**Estrategia:**
1. Busca la estructura: ¿dónde empiezan los bloques? ¿Dónde terminan?
2. Busca la intención: ¿qué está intentando hacer este código?
3. Busca la entrada y la salida: ¿qué entra, qué sale?
4. Busca patrones conocidos: if/else, bucles, funciones — se ven parecidos en todos los lenguajes

**Ejemplo — lenguaje desconocido (Ruby):**
```ruby
numero = 7
if numero % 2 == 0
  puts "par"
else
  puts "impar"
end
```

Puede que no conozcas Ruby. Pero reconoces `if`, `else`, `% 2`, y la idea de una salida.
Entiendes lo que hace este código, aunque nunca hayas aprendido Ruby.

---

## 4. JavaScript en el navegador — pruébalo tú mismo

JavaScript tiene una ventaja especial: cualquier ordenador con un navegador ya tiene un entorno de JavaScript integrado.

**Así lo abres:**
1. Abre Chrome, Firefox o Edge
2. Pulsa F12 (o clic derecho → "Inspeccionar")
3. Haz clic en la pestaña "Console" (Consola)
4. Escribe JavaScript aquí y pulsa Enter

Prueba:
```javascript
console.log("Hola mundo");
```

Y luego:
```javascript
let x = 5;
let y = 3;
console.log(x + y);
```

El navegador lo ejecuta al instante. Sin instalación, sin configuración.

---

## 5. Python — el lenguaje que se lee como inglés

Python fue diseñado con un objetivo claro: **la legibilidad**.

Su creador, Guido van Rossum, escribió en 1991 un lenguaje en el que los espacios en blanco tienen significado, en el que no necesitas punto y coma, y en el que el código se lee casi como prosa.

```python
nombres = ["Ali", "Fatima", "Jonas"]

for nombre in nombres:
    print("Hola, " + nombre)
```

Esto hace exactamente lo que dice: para cada nombre de la lista, imprime un saludo.

Python es popular en la educación, el análisis de datos, la IA y los scripts. Es el lenguaje que eliges cuando quieres construir algo rápido y la legibilidad importa.

---

## 6. ¿Qué lenguaje aprender primero?

La respuesta honesta: importa menos de lo que crees.

Si aprendes JavaScript, después entenderás Python más rápido. Si aprendes Python, después entenderás JavaScript más rápido. Los conceptos fundamentales — variables, condiciones, bucles, funciones — están presentes en todos los lenguajes.

Elige según:
- **Qué quieres construir** — ¿un sitio web? JavaScript. ¿Analizar datos? Python. ¿Una app? Swift o Kotlin.
- **Qué usa tu entorno** — si tus compañeros escriben Python, empieza con Python.
- **Qué te motiva** — aprendes más rápido con el lenguaje que te entusiasma.

En este curso usamos JavaScript para los ejercicios en el navegador (sin necesidad de instalación) y Python para los conceptos de backend.
