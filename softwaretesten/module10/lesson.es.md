# Módulo 10 — Técnicas de prueba de caja negra (Black-box)

Hasta ahora has aprendido sobre todo *que* pruebas. Este módulo trata de *cómo* eliges de forma inteligente *qué* pruebas. Porque es imposible probarlo todo — normalmente hay infinitas entradas posibles. El arte consiste en encontrar los errores con un conjunto pequeño y bien elegido de casos de prueba.

---

## 1. Caja negra: probar sin mirar el código

En las **pruebas de caja negra (black-box)** tratas el programa como una caja negra: sabes qué entra y qué debería salir, pero no miras el código de dentro. Compruebas si el comportamiento coincide con lo prometido — la especificación.

Lo contrario son las **pruebas de caja blanca (white-box)**, donde sí miras el código interno para determinar qué pruebas. Ambas tienen su lugar. La caja negra es potente porque tus casos de prueba siguen funcionando aunque el código interno se reescriba por completo — mientras el comportamiento prometido siga siendo el mismo.

En este módulo veremos cuatro técnicas de caja negra muy usadas:
- Clases de equivalencia
- Análisis de valores límite
- Tablas de decisión
- Transiciones de estado

---

## 2. Clases de equivalencia: grupos que se tratan igual

Imagina: un sitio web solo permite crear una cuenta a personas de 18 años o más. La edad puede ir de 0 a unos 120. ¿Tienes que probar las 121 edades? No.

La idea detrás de las **clases de equivalencia** es que el programa trata grandes grupos de entrada exactamente de la misma manera. Para la comprobación de edad, en realidad solo hay dos grupos:
- **demasiado joven**: de 0 a 17 (se rechaza)
- **suficientemente mayor**: de 18 a 120 (se acepta)

Dentro de cada grupo, no importa qué valor elijas — si 25 funciona, 40 probablemente también. Así que pruebas un valor por grupo. Por ejemplo, edad 10 (demasiado joven) y edad 30 (suficientemente mayor). Dos casos de prueba en lugar de 121.

Una **clase válida** contiene valores que deberían aceptarse, una **clase no válida** contiene valores que deberían rechazarse. Importante: no olvides las clases no válidas. Un programa que gestiona bien las entradas correctas pero falla con las incorrectas sigue estando roto.

---

## 3. Análisis de valores límite: los errores viven en los bordes

Los programadores no suelen cometer la mayoría de sus errores en medio de un grupo, sino en los **límites** entre ellos. ¿Es `>= 18` o `> 18`? Esa diferencia de un año es precisamente donde suele fallar.

El **análisis de valores límite (BVA)** se centra, por tanto, en los bordes de una clase de equivalencia. En el límite de edad de 18, los valores interesantes son:
- **17** — justo demasiado joven (último valor del grupo rechazado)
- **18** — justo suficientemente mayor (primer valor del grupo aceptado)

Al probar exactamente estos dos valores, detectas el clásico error de "justo sí / justo no". Un programador que escribió por error `> 18` en lugar de `>= 18` rechazaría injustamente a alguien de 18 años — y tu prueba con edad 18 lo detecta.

Algunos testers también incluyen el valor un paso más allá (16, 17, 18 o 17, 18, 19) para estar aún más seguros. Cuantos más valores límite incluyas, más exhaustivo será — pero también más trabajo. Es una decisión de equilibrio.

Ten en cuenta: el análisis de valores límite solo funciona con entradas **ordenadas**, donde "mayor que" y "menor que" tienen sentido — números, fechas, importes. Con entradas no ordenadas (como elegir entre rojo, verde o azul) no existe ningún límite.

---

## 4. Tablas de decisión: cuando varias condiciones se combinan

A veces el comportamiento de un programa depende de una combinación de condiciones. Una tienda online, por ejemplo, da un descuento según estas reglas:
- ¿Es miembro del club de clientes? **y**
- ¿El pedido supera los 50 euros?

Con dos condiciones, cada una de las cuales puede ser verdadera o falsa, hay cuatro combinaciones. Una **tabla de decisión** las organiza claramente:

| ¿Miembro? | ¿Más de 50 euros? | Descuento |
|------|----------------|---------|
| sí   | sí             | 10%     |
| sí   | no             | 5%      |
| no   | sí             | ninguno |
| no   | no             | ninguno |

Cada columna (o fila, según cómo lo organices) es una regla independiente que pruebas. La fuerza de una tabla de decisión es que recorres sistemáticamente *todas* las combinaciones — incluida la que de otro modo quizás olvidarías. Además, el hecho de elaborarla te obliga a comprobar si las reglas son realmente completas y sin contradicciones.

Con dos condiciones hay cuatro combinaciones, con tres ya son ocho, con cuatro dieciséis — se va duplicando siempre. Con muchas condiciones esto se vuelve inmanejable, y eliges las combinaciones más importantes según el riesgo.

---

## 5. Transiciones de estado: comportamiento que depende de la historia

Algunos sistemas se comportan de forma distinta según en qué punto se encuentren en ese momento — su **estado**. Piensa en un semáforo sencillo: rojo → verde → ámbar → rojo. O en un pedido online: *borrador → realizado → enviado → entregado*.

Con las **pruebas de transición de estados**, compruebas si el sistema pasa correctamente de un estado a otro cuando ocurre algo (un *evento*), y — igual de importante — si *no* cambia de estado ante acciones prohibidas.

Ejemplo: un pedido que ya ha sido enviado no debería poder cancelarse. Esa es una **transición no válida**. Un buen tester precisamente prueba esos pasos prohibidos, porque ahí suelen estar los bugs más peligrosos: un sistema que permite cancelar un paquete ya enviado puede provocar problemas reales.

Así que pruebas dos cosas:
- las **transiciones válidas**: ¿ocurren todas correctamente?
- las **transiciones no válidas**: ¿se rechazan todas correctamente?

---

## 6. ¿Qué técnica usar, y cuándo?

Ninguna técnica es "la mejor" — se complementan entre sí:
- **Clases de equivalencia** cuando hay grupos de entrada que se tratan de la misma manera.
- **Análisis de valores límite** en cuanto entran en juego límites ordenados (edades, importes, fechas).
- **Tablas de decisión** cuando el comportamiento depende de combinaciones de condiciones.
- **Transiciones de estado** cuando el comportamiento depende de en qué punto se encuentra el sistema.

En la práctica, las combinas. Para la comprobación de edad, usas clases de equivalencia y valores límite juntos. Un tester experimentado siente qué técnica encaja con qué problema — y ese instinto se desarrolla con la práctica.

---

> **¿Camino a una certificación?**
> Estas técnicas forman el núcleo de las certificaciones de testing de nivel inicial reconocidas internacionalmente, como ISTQB Foundation. TestGarden te prepara en los conceptos; el examen oficial lo realizas a través de un organismo reconocido (en los Países Bajos y Bélgica, el BNTQB). Habla con tu tutor y en casa sobre si y cuándo ese paso es adecuado para ti.
