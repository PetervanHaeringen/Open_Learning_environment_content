# Módulo 4 — El juego de Git

Solo entiendes Git de verdad cuando lo has *sentido*.
En este juego, el grupo mismo se convierte en un sistema de control de versiones.
Sin terminal. Sin comandos. Pero con una experiencia real de lo que ocurre dentro de Git.

---

## Material

- Notas adhesivas (post-its) o tarjetas (mínimo 30)
- Rotuladores (mínimo 2 colores)
- Una mesa o pared como "línea de tiempo"
- 1 rollo de cinta adhesiva o cinta de pintor para las líneas
- Participantes: de 3 a 8 personas

---

## Roles

| Rol | Tarea |
|-----|------|
| **Maintainer** | Gestiona la rama `main`. Aprueba las fusiones (merges). |
| **Developer A** | Trabaja en su propia rama. |
| **Developer B** | Trabaja en otra rama (al mismo tiempo que A). |
| **Reviewer** | Revisa las ramas antes de que se fusionen. |

En grupos pequeños, una persona puede asumir varios roles.

---

## El "proyecto"

El proyecto es un archivo de texto ficticio: `README.txt`
La versión inicial tiene tres líneas:

```
Projectnaam: Git Garden
Versie: 1.0
Beschrijving: Een oefenproject.
```

Escribe esta versión inicial en un post-it. Esto es el **commit A** — el origen.
Pégalo en el extremo izquierdo de la línea de tiempo.

---

## Ronda 1 — Línea de tiempo recta

**Objetivo:** experimentar cómo los commits se suceden uno tras otro.

1. Developer A escribe un pequeño cambio en un post-it nuevo.
   Ejemplo: `Versie: 1.1`
   Escribe arriba: `Commit B — Developer A — "versión actualizada"`
2. Pega el commit B a la derecha de A, conectado con una flecha.
3. Developer A hace otro cambio → commit C.
4. Developer B hace lo mismo → commit D, E.

Después de cinco commits tienes una línea de tiempo. Comenten:
- ¿Quién cambió qué?
- ¿Puedes volver al commit B?

---

## Ronda 2 — Ramificar (branching)

**Objetivo:** experimentar que dos personas pueden trabajar en el mismo proyecto al mismo tiempo.

1. Con cinta adhesiva, traza dos líneas desde el commit C — una hacia arriba, otra recta.
2. Developer A sigue trabajando en la línea superior: commit D (su versión del archivo).
3. Developer B trabaja en la línea inferior: commit D' (su versión — cambios distintos).
4. Ambos escriben sus post-its y los pegan en su propia línea.

Ahora tienen dos ramas. Comenten:
- ¿Qué hay en la línea de A? ¿Qué hay en la línea de B?
- ¿Son ambas válidas? Sí. Git lleva el registro de las dos.

---

## Ronda 3 — Fusionar (merge)

**Objetivo:** experimentar qué es una fusión — y cuándo puede salir mal.

**Escenario A: sin conflicto**
Developer A cambió la descripción.
Developer B cambió la versión.
→ Sin conflicto. El Reviewer combina ambos cambios en un nuevo post-it: **commit de fusión M**.
Pega M a la derecha de las dos líneas, con dos flechas apuntando hacia él.

**Escenario B: conflicto**
Developer A escribe: `Versie: 2.0`
Developer B también escribe: `Versie: 1.5`
→ ¡Conflicto! La misma línea, dos valores distintos.
El Reviewer se detiene. Comenten: ¿quién tiene razón? ¿Qué eligen?
Escriban la decisión en el commit de fusión.

Esto es exactamente lo que hace Git: fusiona automáticamente cuando puede, y se detiene cuando no puede.

---

## Ronda 4 — Volver atrás en el tiempo

**Objetivo:** comprender que Git nunca olvida nada.

1. Miren la línea de tiempo.
2. El Maintainer pregunta: "¿Cómo era el archivo en el commit B?"
3. Todos miran el post-it del commit B — y pueden dar la respuesta.

Git hace exactamente esto: cada commit contiene el estado completo del proyecto.
Siempre puedes volver atrás.

---

## Puesta en común

Comenten en grupo:

1. ¿Cuál fue el momento más difícil del juego?
2. ¿Cuándo surgió el conflicto — y cómo lo resolvieron?
3. ¿Qué mensaje de commit podría haber sido mejor?
4. ¿Cómo se relaciona esto con vuestro trabajo diario con archivos?

---

## Conexión con la terminal real

Después de este juego, conoces los conceptos desde dentro:

| Lo que hiciste en el juego | Comando de Git |
|--------------------------|--------------|
| Escribir un post-it (registrar un cambio) | `git commit -m "..."` |
| Trazar una nueva línea (crear una rama) | `git branch nombre` |
| Cambiar a otra línea | `git switch nombre` |
| Combinar dos líneas | `git merge nombre` |
| Mirar un post-it anterior | `git log` / `git checkout` |

En el próximo módulo harás exactamente esto — pero en la terminal.
