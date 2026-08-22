# Módulo 7 — Conflictos y calidad

Colaborar no siempre va sobre ruedas.
A veces intentas fusionar algo y Git te dice: "esto no puedo resolverlo solo."
Eso no es un error — es una pregunta dirigida a ti.

---

## 1. ¿Qué es un conflicto de fusión (merge conflict)?

Un conflicto de fusión ocurre cuando dos ramas **han cambiado la misma línea de forma distinta**.

Git no puede decidir por sí solo cuál versión es la correcta.
Marca las líneas en conflicto y espera tu decisión.

Ejemplo: en `main`, la primera línea de `README.md` es:
```
Versie: 1.0
```

En tu rama, la cambiaste a:
```
Versie: 2.0
```

Y en la otra rama dice:
```
Versie: 1.5
```

¿Quién tiene razón? Git no lo sabe. Tú sí.

---

## 2. ¿Cómo se ve un conflicto?

Git abre el archivo e inserta marcadores:

```
<<<<<<< HEAD
Versie: 2.0
=======
Versie: 1.5
>>>>>>> otra-rama
```

- Todo lo que hay entre `<<<<<<< HEAD` y `=======` es tu versión
- Todo lo que hay entre `=======` y `>>>>>>>` es la versión de la otra rama
- Tú decides qué se queda

---

## 3. Resolver un conflicto: paso a paso

```bash
# Intentas fusionar
git merge otra-rama

# Git informa: CONFLICT (content) in README.md
# Abre el archivo en tu editor
```

**En el editor:**
1. Busca los marcadores de conflicto (`<<<<<<<`, `=======`, `>>>>>>>`)
2. Decide qué versión es la correcta — o combínalas
3. Elimina todos los marcadores
4. Guarda el archivo

**De vuelta en la terminal:**
```bash
git add README.md
git commit -m "Conflicto resuelto: número de versión establecido en 2.0"
```

El conflicto está resuelto. Se ha creado el commit de fusión.

---

## 4. Prevenir conflictos

La mejor forma de evitar conflictos: **commits y fusiones pequeños y frecuentes**.

Cuanto más esperes para fusionar, mayor es la probabilidad de que otra persona haya cambiado las mismas líneas.

Buenos hábitos:
- Mantén las ramas de corta duración — trabaja en días, no en semanas
- Haz pull con regularidad: `git pull origin main` en tu rama para mantenerte al día
- Comenten quién trabaja en qué parte

---

## 5. Revisión de código: calidad antes de la fusión

Una **revisión de código (code review)** consiste en examinar el trabajo de otra persona antes de que se fusione.

Como revisor, presta atención a:
- ¿Se entiende el cambio?
- ¿Tiene consecuencias inesperadas?
- ¿Son claros los mensajes de commit?
- ¿Hay errores tipográficos o inconsistencias?

Como tester, se te da muy bien revisar — ya piensas en casos límite y riesgos.

**Buena etiqueta de revisión:**
- Haz preguntas en lugar de imponer exigencias: "¿Has pensado en...?" en vez de "Esto está mal."
- Menciona también lo que está bien
- Deja tu ego fuera de la revisión — se trata del producto

![Revisión de una pull request en GitHub](images/code_review.png)

---

## 6. Etiquetas (tags) y releases

Una **etiqueta (tag)** es un nombre que le das a un commit específico.
Útil para los números de versión: `v1.0`, `v2.3.1`.

```bash
# Crear una etiqueta ligera
git tag v1.0

# Crear una etiqueta anotada (con descripción)
git tag -a v1.0 -m "Primera versión estable"

# Subir la etiqueta a GitHub
git push origin v1.0
```

En GitHub puedes crear un **release** a partir de una etiqueta.
Un release contiene:
- el código en ese momento
- notas de la versión (qué hay de nuevo, qué se ha corregido)
- opcionalmente, archivos adjuntos (instaladores)

Para un tester, un release es el punto de partida de una ronda de pruebas.
