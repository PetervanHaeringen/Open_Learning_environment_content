# Módulo 3 — Lenguajes y abstracción

Cuando escribes Python, en realidad no le estás hablando al ordenador.
Le hablas a Python. Python le habla a C. C le habla al ensamblador. El ensamblador le habla al procesador.

Cada capa oculta la complejidad de la capa que tiene debajo. A eso se le llama **abstracción** — y es una de las ideas más poderosas de la informática.

---

## 1. El ordenador solo habla ceros y unos

En el nivel más profundo, un ordenador entiende una sola cosa: hay corriente o no la hay. Encendido o apagado. 1 o 0.

Todo el código que llegues a escribir termina convirtiéndose en una larga secuencia de 1s y 0s — **lenguaje máquina**.

Una simple suma en lenguaje máquina se ve así:
```
10110000 01100001
00000101 00000001
10100010 01100001
```

Esto es, literalmente, lo que ejecuta el procesador. Los humanos no pueden escribir ni leer esto sin cometer errores. Por eso se inventó la siguiente capa.

---

## 2. Ensamblador — nombres para las instrucciones

En los años 50, los programadores pensaron: ¿por qué no le damos nombre a las instrucciones más usadas?

En lugar de `10110000 01100001` escribes:
```asm
MOV AL, 1
ADD AL, 1
MOV memoria, AL
```

`MOV` significa "mover un valor". `ADD` significa "sumar".
Son exactamente las mismas instrucciones que los ceros y unos — pero legibles para los humanos.

Un **ensamblador (assembler)** convierte el código ensamblador en lenguaje máquina.

El ensamblador fue un enorme paso adelante. Pero seguía muy cerca del hardware — todavía tenías que saber exactamente cuánta memoria tenías, qué registros estaban disponibles, cómo estaba construido el procesador.

---

## 3. Lenguajes de alto nivel — escribir para humanos

En los años 50 y 60 surgió una nueva idea: ¿y si escribes código que se parezca más al lenguaje humano?

**FORTRAN** (1957) — para cálculos científicos:
```fortran
X = A + B * C
```

**COBOL** (1959) — para aplicaciones empresariales:
```cobol
ADD SALARY TO TOTAL-WAGES
```

**C** (1972) — compacto, potente, cercano al hardware pero legible:
```c
int suma = a + b;
```

**Python** (1991) — tan legible que casi parece inglés:
```python
suma = a + b
```

Cada generación de lenguajes se volvió más legible. Y cada paso ocultó más complejidad.

![Capas de abstracción en los lenguajes de programación](/instructions/content-images/developer/module3/lagen_abstractie.svg)

---

## 4. Compiladores e intérpretes — los traductores

¿Cómo llega el código legible hasta el procesador?

A través de un **compilador** o un **intérprete**.

**Compilador** — traduce todo el código de una sola vez a lenguaje máquina antes de que el programa se ejecute.
Ventaja: el programa es rápido.
Desventaja: tienes que recompilar con cada cambio.
Ejemplos: C, C++, Rust.

**Intérprete** — traduce el código línea por línea mientras el programa se está ejecutando.
Ventaja: ves el resultado de un cambio de inmediato.
Desventaja: es algo más lento.
Ejemplos: Python, JavaScript, Ruby.

La mayoría de los lenguajes con los que te encontrarás como developer son interpretados — tanto Python como JavaScript lo son. Eso resulta muy práctico para aprender: escribes una línea, y ves lo que pasa.

---

## 5. ¿Por qué es tan poderosa la abstracción?

Imagina que cada vez que construyeras un sitio web, tuvieras que escribir el código completo en lenguaje máquina solo para mostrar texto en una pantalla. Nunca pasarías de "Hola mundo".

La abstracción permite **construir sobre lo que otros ya han construido**.

Python está escrito en C.
C está escrito en ensamblador.
El ensamblador está escrito en lenguaje máquina.
El lenguaje máquina es ejecutado por transistores.
Los transistores están diseñados por ingenieros electrónicos.

No necesitas saber nada de todo eso para escribir un programa que haga algo útil. Usas las capas que otros ya han construido.

Esa es también la filosofía detrás del código abierto (open source): compartir código para que la siguiente persona pueda seguir construyendo.

---

## 6. El precio de la abstracción

Pero la abstracción también tiene un precio.

Cuanto más alta es la capa de abstracción, menos control tienes sobre lo que ocurre exactamente.
Un programador de C puede determinar con exactitud cuánta memoria usa un programa.
Un programador de Python delega eso en Python.

Para la mayoría de las aplicaciones, eso no importa en absoluto. Pero para los sistemas donde cada milisegundo cuenta — sistemas operativos, motores de videojuegos, hardware embebido — se elige una capa más baja.

Como developer, aprendes a elegir qué capa se adapta mejor a tu problema.
