# Módulo 8 — Git para testers

Como tester, es posible que uses Git de forma distinta a un developer.
Tú trabajas con scripts de prueba, informes de errores, hallazgos y documentación.
En este módulo verás cómo Git y GitHub apoyan directamente tu trabajo como tester.

---

## 1. GitHub Issues: el corazón del flujo de trabajo

Un **issue** es una tarea, un informe de error o una pregunta que se registra en GitHub.

Como tester, creas issues para:
- errores que has encontrado
- preguntas de pruebas para el equipo
- solicitudes de datos de prueba adicionales
- propuestas de mejora para los scripts de prueba

**Un buen informe de error como issue contiene:**

```markdown
## Descripción
Al hacer clic en el botón "Guardar" del formulario, aparece un error 500.

## Pasos para reproducir
1. Ve a /formulier
2. Rellena todos los campos
3. Haz clic en "Guardar"

## Comportamiento esperado
El formulario se guarda y recibes una confirmación.

## Comportamiento real
Mensaje de error: Internal Server Error (500)

## Entorno
- Navegador: Chrome 124
- SO: Windows 11
- Entorno de prueba: staging
```

---

## 2. Etiquetas (labels): añadir estructura

Las etiquetas categorizan los issues.
Etiquetas predeterminadas en GitHub:

| Etiqueta | Uso |
|-------|---------|
| `bug` | Algo no funciona como se espera |
| `enhancement` | Propuesta de mejora |
| `question` | Pregunta para el equipo |
| `documentation` | Falta documentación o es incorrecta |
| `duplicate` | Ya se había reportado antes |
| `won't fix` | Decisión deliberada de no solucionarlo |

También puedes crear tus propias etiquetas:
- `prioridad: alta`
- `test: regresión`
- `entorno: staging`

---

## 3. Milestones: vincular a una versión o sprint

Un **milestone** agrupa los issues que pertenecen a una versión o sprint.

Ejemplo:
- Milestone `Sprint 4 — Release 2.1`
- Issues: 12 errores, 3 solicitudes de prueba
- Progreso: 7 de 15 cerrados

Como tester, un milestone te da una visión general: ¿qué debe estar listo antes del release?

---

## 4. Gestionar scripts de prueba en Git

Los scripts de prueba son simplemente archivos normales (YAML, txt, Python, etc.).
Como están en un repositorio Git, obtienes:

- **Historial**: ¿quién modificó este script de prueba y cuándo?
- **Reversión**: ¿un error en un script de prueba? Vuelve a la versión anterior.
- **Colaboración**: un compañero puede revisar los scripts de prueba mediante una pull request.
- **Trazabilidad**: puedes vincular un script de prueba a un issue.

**Buena estructura de carpetas para scripts de prueba:**

```
testscripts/
  regressie/
    module1_login.yaml
    module2_formulieren.yaml
  smoke/
    dagelijkse_check.yaml
  exploratory/
    notities_sprint4.md
```

---

## 5. Vincular un informe de error a un commit

En un mensaje de commit puedes hacer referencia a un issue:

```bash
git commit -m "Fix login validatie (#42)"
```

GitHub reconoce `#42` y crea automáticamente un enlace al issue 42.
Usa `Closes #42` para cerrar el issue automáticamente al hacer merge:

```bash
git commit -m "Fix: botón de guardar roto en el formulario (Closes #58)"
```

---

## 6. El flujo de trabajo de pruebas en Git

Un ciclo típico para un tester:

```
1. Escribir o modificar un script de prueba
       ↓
2. Crear una rama: test/sprint4-regressie
       ↓
3. Commits: cambios pequeños con mensajes claros
       ↓
4. Pull request → revisada por un compañero
       ↓
5. ¿Se encontró un error? → Crear un issue con los pasos para reproducirlo
       ↓
6. El developer soluciona el error → tú vuelves a probar en la rama de la PR
       ↓
7. PR fusionada → milestone actualizado
```

Git no es una capa extra de administración.
Es el lugar donde tu trabajo se vuelve visible y trazable.
