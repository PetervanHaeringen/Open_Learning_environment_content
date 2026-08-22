# Módulo 3 – Plan de pruebas y análisis de riesgos

En este módulo aprenderás lo básico de un plan de pruebas ligero.

No documentos extensos, sino un resumen práctico de:

**¿qué vamos a probar, por qué, cómo y cuándo es suficientemente bueno?**

---

## 1. ¿Qué es un plan de pruebas?

Un plan de pruebas es un documento breve que da dirección al testing.

Describe:

- qué hay que probar
- qué riesgos son importantes
- qué enfoque se elige

En proyectos modernos, y desde luego en TestGarden, mantenemos los planes de prueba lo más sencillos posible.

A menudo, una sola página ya es suficiente.

### Un plan de pruebas suele contener

- Alcance (scope) — ¿qué probamos y qué no?
- Riesgos principales
- Enfoque — smoke tests, casos de prueba, exploratory testing
- Entorno de pruebas
- Criterios de entrada y salida (Entry & Exit criteria)
- Roles — ¿quién hace qué?

---

## 2. ¿Qué es el testing basado en riesgos?

Los riesgos te ayudan a decidir qué partes son más importantes de probar.

Un riesgo surge cuando un **posible error** se combina con su **impacto**.

Usamos una fórmula sencilla:

> **Riesgo = probabilidad × impacto**

Cuanto mayor sea el riesgo, más atención necesita esa parte en tu plan de pruebas.

### Ejemplo de una tienda online

- Página "Ver producto" → impacto bajo
- Página "Pagar" (Checkout) → impacto alto

Por eso, el proceso de pago recibe pruebas más numerosas y más profundas.

---

## 3. Ejemplo de un plan de pruebas de 1 página

Usa esto como base cuando escribas tu propio plan de pruebas.

```text
Título: Plan de pruebas para [componente/app]
Fecha:
Autor:

1. Alcance (Scope):
   - ¿Qué probamos?
   - ¿Qué no probamos?

2. Riesgos principales:
   - R1: [riesgo + motivo]
   - R2: [riesgo + motivo]

3. Enfoque:
   - Smoke tests
   - Casos de prueba
   - Exploratory testing

4. Entorno de pruebas:
   - URL, datos, cuentas

5. Criterios de entrada:
   - El build funciona
   - Hay datos de prueba disponibles

6. Criterios de salida:
   - No hay bugs P1/P0 abiertos
   - El smoke test ha pasado

7. Roles:
   - Tester(s)
   - Coach / Product owner
```

---

## 4. Ejercicio práctico: Crea tu propio mini plan de pruebas

Ahora vas a escribir, por primera vez, tu propio plan de pruebas para una pequeña parte de la app de demostración.

### Ejercicio

1. Elige una parte de la app de demostración, por ejemplo el registro.
2. Identifica 3 riesgos usando probabilidad × impacto.
3. Describe qué vas a probar (*scope*).
4. Elige tu enfoque:
   - smoke testing
   - casos de prueba
   - exploratory testing
5. Rellena por completo la plantilla de plan de pruebas de 1 página.

> **Consejo:**
> Mantenlo corto, claro y práctico.
> Un plan de pruebas no es un informe — es tu brújula.

---

## 5. Reflexión

Piensa en tu plan de pruebas:

- ¿Qué riesgos fueron los más importantes?
- ¿Qué dejaste *fuera* del alcance, y por qué?
- ¿Añadirías más o menos detalle?

Intenta averiguar:

- qué decisiones fueron conscientes
- qué partes recibieron atención extra
- y cómo cambiaría tu enfoque con una aplicación más grande
