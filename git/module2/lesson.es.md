# Módulo 5 — Trabajar en local

Has visto Git, lo has sentido y lo has dibujado.
Ahora vas a hacerlo tú mismo. En la terminal, sobre un repositorio real.

---

## Preparación: instalación y configuración

**Instala Git**
- Windows: [git-scm.com/download/win](https://git-scm.com/download/win)
- Mac: abre la Terminal, escribe `git --version` (se instala automáticamente o te da instrucciones)
- Linux: `sudo apt install git`

**Configura tu nombre y correo electrónico** (esto aparece en cada commit que hagas):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

Comprueba tu configuración:

```bash
git config --list
```

---

## El repositorio de práctica

Para este itinerario de aprendizaje usamos un repositorio de práctica aparte:

**`git-garden-playground`**

Tu profesor te dará la URL exacta.
Empieza con `https://github.com/...`

Este repositorio está pensado específicamente para practicar — no puedes romper nada.

---

## Paso 1: Clonar

Clonar significa descargar un repositorio a tu propio ordenador.

```bash
git clone https://github.com/...url.../git-garden-playground
```

Después de clonar:

```bash
cd git-garden-playground
ls
```

Verás los archivos del repositorio. Y hay una carpeta oculta `.git` — la máquina del tiempo.

---

## Paso 2: Ver el estado

`git status` es tu brújula. Úsalo con frecuencia.

```bash
git status
```

Verás en qué rama estás y si hay archivos que han cambiado.

---

## Paso 3: Hacer un cambio

Abre la carpeta en tu editor (o usa la terminal).
Crea un archivo nuevo en la carpeta `deelnemers/`:

```bash
mkdir -p deelnemers
echo "Naam: [tu nombre]" > deelnemers/[tu-nombre].txt
```

Después, comprueba el estado:

```bash
git status
```

Git indica que el nuevo archivo está "sin seguimiento" (untracked) — existe, pero Git todavía no lo está rastreando.

---

## Paso 4: Preparar (staging)

Preparar (stage) significa decir: "quiero incluir este archivo en el próximo commit".

```bash
git add deelnemers/[tu-nombre].txt
```

O añade todo de una vez:

```bash
git add .
```

Vuelve a comprobar el estado. El archivo ahora está en el "área de preparación" (staging area) — listo para el commit.

![Flujo de trabajo: directorio de trabajo → área de preparación → repositorio](images/werkstroom.png)

---

## Paso 5: Hacer el commit

Ahora creas la instantánea.

```bash
git commit -m "Añade a [tu nombre] a la lista de participantes"
```

Un buen mensaje de commit:
- empieza con un verbo: "Añade", "Corrige", "Actualiza", "Elimina"
- describe *qué* cambió, no *cómo*
- es breve (máximo ~72 caracteres)

---

## Paso 6: Ver el historial

```bash
git log
```

Verás todos los commits: hash, autor, fecha, mensaje.

Para una vista compacta:

```bash
git log --oneline
```

Para una vista visual con ramas:

```bash
git log --oneline --graph --all
```

---

## Paso 7: Ver las diferencias

¿Quieres ver qué cambió antes de hacer commit?

```bash
git diff
```

Después de preparar (stage), pero antes del commit:

```bash
git diff --staged
```

---

## Resumen: el flujo de trabajo diario

```
[hacer un cambio]
      ↓
git add .
      ↓
git commit -m "..."
      ↓
git push   (lo veremos en el módulo 6)
```

Repite este patrón decenas de veces al día.
Se convierte en algo automático.
