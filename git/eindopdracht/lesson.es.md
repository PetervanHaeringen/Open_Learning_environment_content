# Trabajo final — Flujo de trabajo completo de Git

Ya has pasado por la teoría, las visualizaciones y los pasos prácticos.
Ahora lo unirás todo: un flujo de trabajo profesional completo sobre el repositorio de práctica.

---

## Qué vas a hacer

Vas a seguir los pasos que un tester realiza a diario en un equipo real:

```
Crear un issue
      ↓
Crear una rama
      ↓
Escribir un archivo de prueba + commit
      ↓
Push a GitHub
      ↓
Abrir una pull request
      ↓
Recibir y procesar la revisión
      ↓
Merge (por el profesor o un compañero)
      ↓
Cerrar el issue
```

---

## El ejercicio

### Paso 1 — Crear un issue

Crea un issue en el repositorio `git-garden-playground`.

El escenario: has descubierto que en la carpeta `handleidingen/` faltan las instrucciones sobre el tema que has aprendido.

Escribe un issue con:
- un título claro
- una descripción de lo que falta
- etiqueta: `documentation`
- milestone: `Git Garden v1.0` (si existe; si no, déjalo vacío)

Anota el número del issue — lo necesitarás más adelante.

---

### Paso 2 — Crear una rama

```bash
git switch main
git pull
git switch -c docs/handleiding-[tu-nombre]
```

Usa un nombre de rama descriptivo que empiece con `docs/`.

---

### Paso 3 — Escribir un archivo

Crea un archivo en la carpeta `handleidingen/`:

**`handleidingen/[tu-nombre]-samenvatting.md`**

Escribe en él un breve resumen de lo que has aprendido en este itinerario de Git.
Como mínimo:
- 3 cosas que ahora entiendes y que antes no entendías
- 1 comando que te parece el más útil
- 1 situación de tu propio trabajo en la que te gustaría usar Git

---

### Paso 4 — Hacer commit

```bash
git add handleidingen/[tu-nombre]-samenvatting.md
git commit -m "Añade resumen de Git para [tu nombre] (Closes #[número-de-issue])"
```

---

### Paso 5 — Push

```bash
git push origin docs/handleiding-[tu-nombre]
```

---

### Paso 6 — Abrir una pull request

Ve a GitHub y abre una pull request.

**Requisitos para la descripción de la PR:**
- ¿Qué has añadido?
- ¿Por qué es útil para los demás?
- Referencia al issue: `Closes #[número]`
- Un punto que el revisor debería comprobar específicamente

---

### Paso 7 — Procesar la revisión

Tu profesor o un compañero revisará tu PR.
Si hay comentarios:
1. Ajusta el archivo en tu rama local
2. Haz commit del cambio con un mensaje claro
3. Sube (push) el cambio — la PR se actualiza automáticamente

---

### Paso 8 — Merge

Tras la aprobación, la PR se fusiona por parte del profesor o por ti mismo (si los permisos lo permiten).

Después, comprueba:
```bash
git switch main
git pull
ls handleidingen/
```

Tu archivo ya está en `main`. Forma parte del repositorio oficial.

---

## Criterios de evaluación

| Elemento | Bien |
|-----------|------|
| Issue | Título claro, descripción, etiqueta correcta |
| Nombre de la rama | Descriptivo, empieza con `docs/` |
| Mensaje de commit | Descriptivo, hace referencia al número de issue |
| Archivo | Cumple los requisitos, texto propio |
| Descripción de la PR | Completa, incluye Closes #número |
| Procesar los comentarios | Nuevo commit con un mensaje claro |

---

## ¿Terminado?

Si todo se ha fusionado, has demostrado que puedes:
- llevar a cabo de forma autónoma un flujo de trabajo completo en Git
- comunicarte de forma profesional en issues y pull requests
- saber cómo procesar comentarios sin interrumpir el flujo de trabajo

Eso no es un truco con cuatro comandos — eso es trabajar como un profesional.
