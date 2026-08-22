# Módulo 6 – Informes de errores (Bug Reporting)

Los informes de errores son una de las habilidades más importantes de un tester.

Un buen informe de error es:
- claro
- reproducible
- completo
- útil para los developers

En este módulo aprenderás a escribir informes de errores profesionales.

---

## 1. ¿Qué es un bug?

Un **bug** es una situación en la que el software no hace lo que se espera.

Esto puede tratarse de:

- errores funcionales
- problemas de maquetación
- mensajes de error incorrectos
- comportamiento inesperado
- problemas de seguridad
- problemas de rendimiento

Un bug es, por tanto, la diferencia entre:

> el comportamiento esperado ↔ el comportamiento real

---

## 2. ¿Qué hace bueno a un informe de error?

Un buen informe de error es:

- **Claro** — todo el mundo entiende el problema
- **Reproducible** — otra persona puede volver a provocarlo
- **Completo** — contiene toda la información relevante
- **Neutral** — objetivo, sin culpas ni emociones

### Ejemplo

#### Informe de error malo

> "La web no funciona. Arreglarlo pls."

#### Informe de error bueno

> "Al hacer clic en 'Guardar' aparece un error 500 y el formulario no se guarda."

---

## 3. Severidad y Prioridad (Severity & Priority)

Los testers suelen añadir etiquetas a los bugs.

### Severidad (Severity)

¿Qué tan grave es el problema para el sistema?

### Prioridad (Priority)

¿Con qué rapidez hay que solucionarlo?

### Ejemplos

#### Severidad alta, prioridad baja
Un fallo (crash) en una función que casi nadie usa.

#### Severidad baja, prioridad alta
Una falta de ortografía en la página de inicio de un cliente importante.

---

## 4. Plantilla de informe de error

Usa esta plantilla al escribir informes de errores.

```text
Título:
  Descripción breve y clara

Entorno:
  Navegador, SO, versión, dispositivo

Severidad:
Prioridad:

Pasos para reproducir:
  1. ...
  2. ...
  3. ...

Resultado esperado:
  ¿Qué debería ocurrir?

Resultado real:
  ¿Qué ocurrió en su lugar?

Captura de pantalla / log:
  (opcional pero recomendado)

Comentarios adicionales:
  frecuencia, impacto, detalles
```

---

## 5. Ejercicio práctico: escribe 3 informes de errores

Ahora vas a escribir tres informes de errores basados en fallos que encontraste antes durante el exploratory testing.

### Ejercicio

1. Elige tres incidencias de tu session report.
2. Escribe un informe de error completo para cada incidencia.
3. Usa la plantilla anterior.
4. Comprueba si el bug es reproducible.
5. Pide a un compañero de clase que pruebe tu informe.

> Un informe de error solo es bueno cuando otra persona puede reproducir exactamente el mismo problema.

---

## 6. Reflexión

Piensa de nuevo en tus informes de errores:

- ¿Cuál fue el más claro?
- ¿Qué información se te olvidó al principio?
- ¿Cómo reaccionó tu compañero de clase?
- ¿Qué harías de forma diferente la próxima vez?
