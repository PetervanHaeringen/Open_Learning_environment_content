# Módulo 6 — Ramas y colaboración

Ya conoces el flujo de trabajo básico. Ahora vas a añadir la colaboración.
Colaborar en Git gira en torno a las ramas (branches) y las pull requests — las dos herramientas que permiten a los equipos trabajar en el mismo proyecto al mismo tiempo, sin caos.

---

## 1. Crear una rama

Crea siempre una rama para una nueva tarea.
Nunca trabajes directamente en `main`.

```bash
git branch mi-rama
git switch mi-rama
```

O en un solo paso:

```bash
git switch -c mi-rama
```

Comprueba en qué rama estás:

```bash
git branch
```

La rama con un `*` delante es la rama actual.

Los buenos nombres de rama son descriptivos y cortos:
- `agregar-readme`
- `corregir-typo-introduccion`
- `actualizar-numero-version`

---

## 2. Hacer commit de los cambios en la rama

Trabaja igual que en el módulo 5:

```bash
# hacer un cambio en un archivo
git add .
git commit -m "Descripción del cambio"
```

Tus commits ahora están en tu rama — no en `main`.
`main` permanece sin cambios.

---

## 3. Subir (push) a GitHub

Ahora envías tu rama a GitHub:

```bash
git push origin mi-rama
```

La primera vez, Git te pedirá que confirmes tu cuenta de GitHub.
Después de hacer push, la rama estará en GitHub — visible para los demás.

---

## 4. Abrir una pull request

Una **pull request (PR)** es una propuesta: "quiero fusionar mi rama con main."

En GitHub:
1. Ve al repositorio `git-garden-playground`
2. Verás una barra amarilla: "mi-rama — Compare & pull request"
3. Haz clic en ella
4. Escribe una descripción:
   - ¿Qué cambiaste?
   - ¿Por qué?
   - ¿Hay algo que el revisor deba saber?
5. Haz clic en **"Create pull request"**

![Crear una pull request en GitHub](images/pull_request_aanmaken.png)

Una pull request es una conversación, no un formulario.
Cuanto mejor sea la descripción, más fluida será la revisión.

---

## 5. El flujo de trabajo de la colaboración

```
main (estable)
 |
 ├── rama A (Developer A trabaja aquí)
 |        → commits → push → PR → revisión → merge
 |
 ├── rama B (Developer B trabaja aquí)
 |        → commits → push → PR → revisión → merge
 |
main (actualizado tras los merges)
```

Cada persona trabaja en su propia rama.
`main` solo se actualiza mediante pull requests aprobadas.
Así, `main` se mantiene siempre estable.

---

## 6. Obtener los cambios de otras personas

Si la rama de otra persona ha sido fusionada, tú también querrás esos cambios.

```bash
git switch main
git pull
```

`git pull` descarga la versión más reciente de `main` desde GitHub.

¿Quieres saber qué hay en GitHub sin cambiar tus archivos locales?

```bash
git fetch
git status
```

`git fetch` descarga la información. `git pull` descarga la información *y además* actualiza tus archivos.

---

## 7. Ejercicio práctico

1. Clona el repositorio `git-garden-playground` (si aún no lo has hecho).
2. Crea una rama con tu nombre: `contribucion-[tu-nombre]`
3. Crea un archivo en la carpeta `bijdragen/`: `[tu-nombre].md`
4. Escribe en él:
   - Qué esperas aprender de Git
   - Una pregunta que aún tengas
5. Haz commit del archivo con un mensaje claro.
6. Sube (push) la rama a GitHub.
7. Abre una pull request con una breve descripción.

Después del ejercicio: tu profesor o un compañero revisará la PR.
