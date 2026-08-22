# Módulo 5 – Exploratory Testing

El Exploratory Testing es una de las formas más potentes y más divertidas de probar software.

Te embarcas en un viaje de descubrimiento a través del software, tal como lo haría un usuario real:
con curiosidad, creatividad y sin pasos predefinidos.

Aquí es donde los testers aportan un valor real.

---

## 1. ¿Qué es el Exploratory Testing?

El Exploratory Testing significa que pruebas **descubriendo**:

al mismo tiempo:
- piensas qué quieres probar
- lo ejecutas
- y aprendes mientras vas probando

Es lo opuesto a un guion rígido.

> Sigues tus ojos, tu intuición y las señales que te da el software.

### Características

- Piensas como un usuario
- Haces clic, pruebas y experimentas
- Sigues fallos extraños o situaciones inesperadas
- Investigas sin una lista fija de pasos

---

## 2. ¿Por qué es importante el Exploratory Testing?

El exploratory testing suele encontrar errores que nunca aparecen en ningún documento ni caso de prueba.

### Problemas que a menudo solo encuentras explorando

- Comportamiento extraño al hacer clic rápidamente
- Comportamiento en móvil distinto al de escritorio
- Flujos ilógicos
- Transiciones de pantalla confusas
- Pequeños problemas de maquetación o de texto

Por eso, el exploratory testing es un complemento perfecto para el scripted testing (pruebas con guion).

---

## 3. Session-Based Test Management (SBTM)

Durante el exploratory testing, sueles trabajar en sesiones cortas.

Una sesión de este tipo suele tener tres partes:

- **Charter** — ¿qué vas a investigar?
- **Temporizador (Timer)** — normalmente entre 30 y 60 minutos
- **Toma de notas** — ¿qué ves y qué te llama la atención?

### Ejemplo de Charter

> Investiga la página de registro en busca de flujos ilógicos, mensajes de error y su uso en móvil.

---

## 4. ¿Cómo se hace el Exploratory Testing?

Algunas pautas prácticas:

- Empieza con un objetivo claro
- Piensa como un usuario
- Hazte preguntas:
  - "¿Qué pasa si…?"
- Sigue las situaciones inesperadas
- Anota todo lo que te llame la atención
- Prueba tanto rápido como despacio
- Prueba en móvil, tablet y otros navegadores

> El exploratory testing no es caos.
> Trabajas con un propósito, pero dejas espacio para el descubrimiento.

---

## 5. Session Report

Usa un breve informe durante o después de tu sesión.

```text
Session Report – [componente] – [fecha]

Charter:
  ¿Cuál era tu objetivo?

Duración:
  ¿Cuánto tiempo estuviste probando?

Observaciones:
  - ¿Qué viste?
  - ¿Qué situaciones extrañas aparecieron?

Incidencias encontradas:
  - Bug 1: descripción + ¿reproducible?
  - Bug 2: descripción + ¿reproducible?
  - Bug 3: descripción + ¿reproducible?

Comentarios:
  Preguntas, ideas, dudas
```

---

## 6. Ejercicio práctico: Sesión exploratoria de 60 minutos

Ahora vas a realizar tú mismo una sesión de exploratory testing.

### Ejercicio

1. Elige un componente:
   - registro
   - inicio de sesión
   - carrito de compra
   - u otro componente

2. Escribe un charter de una sola frase.

3. Pon un temporizador de 60 minutos.

4. Prueba de forma exploratoria y anota todo lo que te llame la atención.

5. Escribe un session report.

6. Entrega al menos 3 bugs como informes de errores independientes.

> Pregúntate con regularidad:
> "¿Dónde podría confundirse un usuario?"

---

## 7. Reflexión

Piensa de nuevo en tu sesión:

- ¿Qué te sorprendió?
- ¿Qué error nunca habrías encontrado solo con casos de prueba?
- ¿Qué habilidades te resultaron útiles?
- ¿Qué harías de forma diferente la próxima vez?
