# Módulo 2 — De Lovelace a Turing

La idea de que una máquina puede seguir instrucciones no es evidente por sí misma.
Alguien tuvo que idearla. Y antes de eso, alguien tuvo que atreverse a pensarla.

Esta es la historia de las personas que lo hicieron — mucho antes de que existiera una pantalla.

---
![La Máquina Diferencial de Babbage, Science Museum de Londres](/instructions/content-images/developer/module2/difference_engine.jpg)

*Foto: Science Museum de Londres — Creative Commons*

## 1. Charles Babbage — la máquina que nunca se terminó (década de 1820)

Charles Babbage era un matemático británico con una obsesión: los errores en las tablas de cálculo.

En su época, las tablas matemáticas — para la navegación, la artillería, los impuestos — se calculaban a mano, por personas. Y las personas cometen errores. Babbage quería una máquina que no los cometiera.

Diseñó la **Difference Engine** (Máquina Diferencial): una calculadora mecánica de engranajes y palancas. Y más tarde la **Analytical Engine** (Máquina Analítica): una máquina que no solo podía calcular, sino que también podía programarse mediante tarjetas perforadas.

La Analytical Engine tenía todo lo que tiene un ordenador moderno:
- un "mill" (el procesador)
- un "store" (la memoria)
- entrada mediante tarjetas perforadas
- salida mediante una impresora

Babbage nunca terminó de construirla. La tecnología de su época no era lo bastante precisa. Pero la idea ya estaba ahí.

![La Analytical Engine de Babbage — esquema](/instructions/content-images/developer/module2/analytical_engine.svg)

---

## 2. Ada Lovelace — la primera programadora (1843)

Ada Lovelace era hija del poeta Lord Byron y de una madre con formación matemática.
Conoció a Babbage cuando tenía 17 años y quedó fascinada por sus máquinas.

En 1843 tradujo del francés al inglés un artículo sobre la Analytical Engine. Pero añadió mucho más que una traducción — escribió notas extensas que hicieron el texto original tres veces más largo.

En esas notas describió:
- cómo la máquina podía usarse para algo más que calcular
- cómo se podía hacer que la máquina repitiera las mismas instrucciones una y otra vez (el primer bucle)
- un plan paso a paso para calcular los números de Bernoulli — el primer algoritmo jamás escrito para una máquina

Pero lo que realmente la distinguió fue su intuición: la máquina procesa *símbolos*, no solo números. Escribió que la Analytical Engine incluso podría componer música — siempre que la música se tradujera en símbolos.

Esa intuición es la base de todos los ordenadores modernos.

> "La máquina solo puede hacer lo que le ordenamos que haga."
> — Ada Lovelace

Murió a los 36 años. Su trabajo no se redescubrió hasta un siglo después.

---

## 3. Alan Turing — ¿puede pensar una máquina? (1936)

Alan Turing era un matemático británico que planteó una pregunta que cambió el mundo:

**¿Cuáles son los límites de lo que puede calcular una máquina?**

En 1936 — antes de que existiera ningún ordenador — describió una máquina imaginaria: la **máquina de Turing**. Una cinta infinitamente larga con símbolos, un cabezal de lectura que lee y escribe símbolos, y un conjunto de reglas que determina qué sucede a continuación.

Este modelo abstracto podía realizar cualquier cálculo que fuera posible realizar.
Con él, Turing demostró que existen cálculos que *nunca* podrán resolverse mediante una máquina — sin importar lo potente que sea.

Durante la Segunda Guerra Mundial, Turing y su equipo descifraron el código Enigma de los nazis — acortando la guerra, según se estima, en dos años.

Después de la guerra, planteó la pregunta que aún hoy sigue ocupando a los programadores:

**¿Puede pensar una máquina?**

Diseñó el **test de Turing**: si una persona, comunicándose por texto, no puede distinguir si está hablando con un humano o con una máquina, la máquina ha "aprobado" la prueba de inteligencia.

Turing fue procesado por el gobierno británico debido a su homosexualidad y murió en 1954, probablemente por suicidio. En 2013 recibió un indulto póstumo por parte de la monarquía británica.

---

## 4. La línea de Babbage hasta hoy

```
Babbage (década de 1820)     → la idea: una máquina que sigue instrucciones
Lovelace (1843)                → el primer algoritmo, el primer bucle
Turing (1936)                  → la teoría: ¿qué puede calcular una máquina?
ENIAC (1945)                   → el primer ordenador electrónico real
transistor (1947)              → más pequeño, más rápido, más barato
circuito integrado             → aún más pequeño
ordenador personal             → en cada salón
internet                       → conectados
smartphone                     → en cada bolsillo
IA (ahora)                     → máquinas que aprenden patrones por sí mismas
```

Cada paso se construyó sobre el anterior. Y cada paso empezó con alguien que se hizo una pregunta.

---

## 5. ¿Qué significa esto para ti?

Tú te encuentras al final de esa línea — y, al mismo tiempo, al principio de algo nuevo.

Las herramientas que vas a usar son el resultado de ochenta años de trabajo de personas que se hicieron preguntas fascinantes. Lovelace se preguntó: ¿qué más puede hacer una máquina, además de calcular? Turing se preguntó: ¿cuáles son los límites? Los creadores de Python se preguntaron: ¿cómo escribimos código que las personas puedan leer?

Como developer, tú harás tus propias preguntas. Y las respuestas que escribas pasarán a formar parte de esa misma línea.
