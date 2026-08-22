# Módulo 3 — El control de versiones, visualizado

Antes de escribir un comando, necesitas poder *verlo*.
En este módulo construimos el modelo mental: ¿cómo se ve Git si lo dibujas?

---

## 1. La línea de tiempo: commits en fila

La situación más simple en Git es una línea recta de commits.
Cada commit es una instantánea. Cada commit apunta hacia atrás, a su predecesor.

```
○ — ○ — ○ — ○ — ○
A   B   C   D   E
```

- **A** es el primer commit (el origen)
- **E** es el último commit (el estado actual)
- Las flechas apuntan hacia el pasado

Lee la línea de tiempo de izquierda a derecha: así es como creció la historia.

![Línea de tiempo de Git — commits en fila](images/tijdlijn_lineair.png)

---

## 2. Una rama (branch): un camino paralelo

Imagina que quieres probar algo sin tocar la línea principal.
Creas una **rama** — un camino paralelo que empieza en un commit ya existente.

```
○ — ○ — ○ — ○ — ○       (main)
              |
              ○ — ○       (experiment)
```

- `main` simplemente continúa
- `experiment` empieza en el commit D y crece de forma independiente
- Ambas existen al mismo tiempo, sin afectarse mutuamente

En Git, una rama no es más que un nombre que apunta a un commit.
Eso es todo. Sin copia de archivos, sin carpeta duplicada — solo una etiqueta.

![Una rama como camino paralelo de la línea de tiempo](images/branch_zijtak.png)

---

## 3. Fusionar (merge): unir dos ramas

Cuando el experimento está terminado, quieres incorporarlo de nuevo en `main`.
A eso se le llama **merge** (fusión).

```
○ — ○ — ○ — ○ — ○ — ○   (main, tras el merge)
              |       |
              ○ — ○ ——   (experiment, fusionado)
```

Git observa el ancestro común (commit D) y los dos extremos.
Combina los cambios y crea un nuevo **commit de fusión** (el último ○ en main).

Si las mismas líneas fueron cambiadas en ambas ramas → conflicto.
Si no → fusión automática.

![Fusión de dos ramas](images/merge_visueel.png)

---

## 4. HEAD: tú estás aquí

`HEAD` es una etiqueta que muestra dónde te encuentras ahora dentro del grafo.

```
○ — ○ — ○ — ○ — ○
                 ↑
                HEAD (main)
```

Cuando cambias a otra rama (`git switch experiment`), la etiqueta se mueve contigo:

```
○ — ○ — ○ — ○ — ○       (main)
              |
              ○ — ○
                   ↑
                  HEAD (experiment)
```

Todo lo que hagas commit ahora irá a la rama en la que se encuentre HEAD.

---

## 5. Volver atrás en el tiempo

Supón que el commit C contenía un error que ahora quieres investigar.
Puedes mover HEAD temporalmente a C (`git checkout C`).

```
○ — ○ — ○ — ○ — ○
         ↑
        HEAD (detached)
```

Tus archivos se verán entonces tal como estaban en ese momento.
Git llama a esto "detached HEAD" (HEAD desconectado) — no estás en una rama, sino directamente sobre un commit.

Útil para mirar. Peligroso para hacer commit sin crear antes una nueva rama.

---

## 6. Ejercicio: dibújalo tú mismo

Toma lápiz y papel.

1. Dibuja una línea recta con cinco círculos (commits A hasta E).
2. Dibuja una rama que empiece en C, con dos commits adicionales.
3. Dibuja una fusión de vuelta a la línea principal después de E.
4. Coloca la etiqueta HEAD en el lugar correcto.

Este dibujo es exactamente lo que Git guarda internamente.
En el próximo módulo representarás esto de nuevo, pero con tarjetas.
