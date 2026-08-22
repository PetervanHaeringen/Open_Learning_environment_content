# Módulo 1 — Origen y filosofía

Git es hoy el sistema de control de versiones más utilizado del mundo.
Pero no siempre existió. Y no surgió por casualidad: detrás había un problema serio.

---

## 1. El problema: crear software en equipo

Imagina que trabajas con diez personas en el mismo proyecto.
Todos tienen los mismos archivos. Todos hacen cambios.

¿Cómo sabes entonces:
- quién cambió qué?
- cuándo se introdujo un error?
- cómo volver al estado de ayer?

Sin control de versiones, la respuesta es: no lo sabes.
Envías archivos por correo, sobrescribes el trabajo de los demás, pierdes código.

Eso es exactamente lo que ocurría antes en los equipos de software.

---

## 2. Control de versiones centralizado: la generación anterior

Antes de Git existían sistemas como SVN y CVS.
Funcionaban de forma **centralizada**: un único servidor central guardaba todo el historial.

Eso tenía desventajas:
- el servidor se cae → todos se quedan parados
- no puedes trabajar sin conexión de red
- un error en el servidor = todo perdido

![Control de versiones centralizado frente a distribuido](/instructions/content-images/git/module1/centralized_vs_distributed.svg)

---

## 3. Linus Torvalds y el conflicto de 2005

Linus Torvalds es el creador del núcleo de Linux, el corazón de muchos sistemas operativos.
Miles de desarrolladores colaboraban en él.

Usaban un sistema comercial: **BitKeeper**.
Gratuito para proyectos de código abierto, hasta que en 2005 se retiró la licencia.

Linus tenía una opción: cambiar a un sistema existente o construir algo él mismo.
Ninguna de las herramientas existentes hacía lo que necesitaba.

En **dos semanas** escribió la base de Git.

> "I'm an egotistical bastard, and I name all my projects after myself.
> First Linux, now Git."
> — Linus Torvalds

---

## 4. La filosofía de Git

Git se basa en tres ideas fundamentales:

**Distribuido**
Cada persona tiene el historial completo en su propio ordenador.
Puedes trabajar sin internet. El servidor no es sagrado.

**Seguro**
Cada commit recibe un código único (hash) basado en su contenido.
Cualquier cambio en el historial se detecta de inmediato.

**Rápido**
Git funciona localmente. Casi todo ocurre en tu propia máquina.
Sin tiempos de espera, sin depender de un servidor.

---

## 5. Git no es GitHub

Esta es una confusión habitual.

**Git** es el sistema de control de versiones: un programa que instalas localmente.
**GitHub** es un sitio web donde puedes almacenar y compartir proyectos de Git.

Git fue inventado por Linus Torvalds.
GitHub es una empresa, fundada en 2008, comprada por Microsoft en 2018.

Puedes usar Git sin GitHub.
Pero GitHub sin Git no tiene sentido.

---

## 6. ¿Por qué es relevante para ti como tester?

Como tester trabajas con código, scripts de prueba, informes de errores y documentación.
Todos esos archivos cambian con el tiempo.

Git te ofrece:
- un historial completo de cada archivo
- conocer quién cambió qué y cuándo
- la posibilidad de volver atrás cuando algo sale mal
- colaboración sin caos

No necesitas saber programar para que Git te resulte útil.
