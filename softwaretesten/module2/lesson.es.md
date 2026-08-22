# Módulo 2 — Niveles de prueba y Smoke Testing

En este módulo descubrirás cómo se prueba el software en distintas capas, y cuál es el papel del conocido **smoke test**.

Iremos de la visión general a la práctica, para que entiendas cómo tu trabajo de testing encaja en el conjunto más amplio.

---

## 1. ¿Qué son los niveles de prueba?

El software no se prueba de una sola vez. Cada parte se comprueba en un nivel distinto.

A estos niveles los llamamos **niveles de prueba (test levels)**.

- **Pruebas unitarias (Unit Testing)** — pequeños fragmentos de código, probados por los developers
- **Pruebas de integración** — ¿funciona todo junto como debería?
- **Pruebas de sistema** — ¿funciona toda la aplicación en su conjunto?
- **Pruebas de aceptación** — ¿funciona para el usuario y para el cliente?

### Ejemplo

En una tienda online:

- prueba unitaria → ¿funciona el cálculo del descuento?
- prueba de integración → ¿funcionan juntos el carrito de compra y el inventario?
- prueba de sistema → ¿funciona el proceso de pedido de principio a fin?
- prueba de aceptación → ¿le resulta al cliente lógico y utilizable el flujo?

---

## 2. Tipos de prueba: funcionales y no funcionales

Además de los niveles de prueba, también existen los **tipos de prueba**.

Esto describe *qué* estás probando.

- **Pruebas funcionales** — ¿hace la función lo que se supone que debe hacer?
- **Pruebas no funcionales** — velocidad, seguridad, facilidad de uso, estabilidad

En TestGarden nos centramos principalmente en las pruebas funcionales, como los smoke tests y el exploratory testing.

---

## 3. ¿Qué es un Smoke Test?

Un smoke test es una **comprobación breve y rápida** para ver si el sistema está "más o menos sano" después de un nuevo release, actualización o despliegue.

Es el equivalente digital de:

> "¿está sonando la alarma de humo?"

Si algo fundamental está roto, quieres saberlo de inmediato.

### ¿Por qué hacer smoke tests?

- Son rápidos y dan claridad inmediata
- Evitan perder tiempo en builds rotas
- Dan un GO / NO-GO para seguir probando

### Ejemplo de un smoke test

- ¿Carga la aplicación?
- ¿Puede el usuario iniciar sesión?
- ¿Funciona el flujo principal?
- ¿No hay errores 404 o 500?

---

## 4. Ejemplo de checklist de Smoke Test

- [ ] ¿Es accesible el sitio web?
- [ ] ¿Puede un usuario de prueba iniciar sesión?
- [ ] ¿Funciona la funcionalidad principal?
- [ ] ¿Funcionan los enlaces y botones principales?
- [ ] ¿No se ven errores importantes?
- [ ] ¿Funciona también en móvil o en otro navegador?

Cierras un smoke test con:

**GO / NO-GO**

---

## 5. Ejercicio práctico

1. Elige una web app de demostración
2. Crea una checklist de smoke test
3. Ejecuta la checklist
4. Anota Pass / Fail
5. Escribe una conclusión

> Un smoke test no es una prueba completa.
> Es un escaneo rápido de salud.

---

## 6. Reflexión

Piensa en:

- ¿Cuál comprobación fue la más importante?
- ¿Qué problema representaba el mayor riesgo?
- ¿Cómo mejorarías tu checklist?
