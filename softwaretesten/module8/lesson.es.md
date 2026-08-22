# Módulo 8 – Automatización y Testing de IA

En este módulo conocerás dos grandes desarrollos dentro del testing de software moderno:

- la automatización de pruebas
- el testing asistido por IA (AI-assisted testing)

El desarrollo de software cambia rápidamente.
Los sistemas de IA escriben código, generan pruebas, analizan logs y apoyan a los testers en su trabajo.

Pero, al mismo tiempo, surge un nuevo desafío:

> ¿Cómo controlas sistemas que no siempre responden exactamente de la misma manera?

Por eso, el papel del tester se está desplazando poco a poco de:
- solo comprobar
hacia:
- observar
- evaluar
- interpretar
- pensar de forma crítica

---

## 1. ¿Qué es la automatización de pruebas?

La automatización de pruebas significa que las pruebas se ejecutan automáticamente mediante scripts o herramientas.

En lugar de realizar repetidamente los mismos pasos a mano, dejas que el software los repita.

A menudo automatizas:

- smoke tests
- pruebas de regresión
- comprobaciones de API
- flujos end-to-end
- comprobaciones de rendimiento

### ¿Por qué automatizar?

La automatización ayuda a:
- obtener feedback más rápido
- probar de forma repetible
- reducir los errores humanos
- probar con más frecuencia

### ¿Qué normalmente no se automatiza?

Algunas formas de testing siguen siendo fuertemente humanas:

- exploratory testing
- usabilidad
- creatividad
- empatía
- comprender el contexto
- reconocer situaciones inesperadas

> La automatización refuerza a los testers.
> No sustituye su criterio.

---

## 2. Herramientas modernas para la automatización

Las herramientas más utilizadas son:

- **Playwright**
- **Cypress**
- **Selenium**
- **Postman**
- pipelines de CI/CD como GitHub Actions

### Ejemplo de automatización

Un script puede, automáticamente:

1. abrir un sitio web
2. iniciar sesión
3. rellenar formularios
4. comprobar si algo es visible
5. reportar errores

Eso hace posibles pruebas de regresión rápidas en cada nuevo release.

---

## 3. Testing asistido por IA

La IA se usa cada vez más como apoyo en el testing.

Por ejemplo, para:

- generar casos de prueba
- resumir logs
- reconocer patrones de errores
- predecir riesgos de regresión
- crear datos de prueba
- escribir documentación automática

### Pero ten cuidado

La salida (output) de una IA suena a menudo convincente.

Eso no significa automáticamente que sea correcta.

Una IA puede:
- hacer suposiciones erróneas
- inventar detalles
- pasar por alto escenarios importantes
- dar respuestas inconsistentes

Por eso, el control humano sigue siendo esencial.

> Los buenos testers no confían ciegamente en la IA.
> La usan de forma crítica.

---

## 4. Sistemas deterministas frente a probabilistas

El software tradicional suele funcionar de forma determinista.

Eso significa:

```text
misma entrada → misma salida
```

En los sistemas de IA, esto suele funcionar de otra manera.

Un modelo de lenguaje grande (LLM) o un sistema de recomendaciones puede responder con:

```text
misma entrada → distintas salidas posibles
```

A esto lo llamamos comportamiento probabilista.

### ¿Por qué es importante esto?

Porque cambia la forma de probar.

Con el software clásico, sueles comprobar:

- el resultado exacto
- reglas fijas
- resultados predecibles

Con los sistemas de IA, sueles evaluar más bien:

- calidad
- consistencia
- razonabilidad
- seguridad
- sesgo (bias)
- sensibilidad al contexto

---

## 5. Evaluar de forma crítica la salida de la IA

Los sistemas de IA pueden sonar convincentes y aun así cometer errores.

Por eso, como tester compruebas:

- ¿es correcta la información?
- ¿se mantiene el sistema dentro de la tarea asignada?
- ¿aparecen alucinaciones?
- ¿es segura la salida?
- ¿responde el sistema de forma estable?
- ¿trata a los usuarios de forma justa?

### Alucinaciones

Una IA puede generar información que:
- suena creíble
- pero es factualmente incorrecta

Por ejemplo:
- fuentes inventadas
- funciones que no existen
- conclusiones erróneas
- resúmenes incorrectos

Por eso, un tester debe aprender:

> "Suena lógico" no es lo mismo que "es correcto".

---

## 6. Riesgos importantes en los sistemas de IA

### Sesgo (Bias)

¿Trata el sistema a los distintos grupos de usuarios de forma justa?

### Deriva (Drift)

¿Cambia el comportamiento poco a poco debido a nuevos datos?

### Sensibilidad al prompt (Prompt sensitivity)

¿Un pequeño cambio en la redacción produce, de repente, respuestas totalmente distintas?

### Seguridad

¿Qué ocurre con:
- entradas extrañas
- prompts manipuladores
- situaciones extremas?

### Explicabilidad (Explainability)

¿Puedes entender por qué el sistema hace algo?

---

## 7. Probar IA en la práctica

El testing de IA se parece a menudo más a hacer investigación que a un control clásico.

Trabajas con:
- hipótesis
- observaciones
- comparación de salidas
- reconocimiento de patrones

### Ejemplos de pruebas de IA

- ¿Da el sistema respuestas consistentes?
- ¿Cómo reacciona ante información contradictoria?
- ¿Puede manejar entradas incompletas?
- ¿Surgen patrones discriminatorios?
- ¿Responde de forma segura ante el mal uso?

---

## 8. Ejercicio práctico: investigar una función de IA

Ahora vas a investigar de forma crítica un sistema de IA.

### Ejercicio

1. Elige una función de IA:
   - chatbot
   - reconocedor de imágenes
   - sistema de recomendaciones
   - asistente de IA

2. Idea al menos 5 pruebas:
   - 2 escenarios normales
   - 2 casos límite
   - 1 prueba de equidad/sesgo (fairness/bias)

3. Anota para cada prueba:
   - entrada (input)
   - comportamiento esperado
   - comportamiento real

4. Analiza:
   - previsibilidad
   - consistencia
   - seguridad
   - equidad

---

## 9. Reflexión

Piensa en:

- ¿Qué respuesta de la IA te sorprendió?
- ¿Cuándo te pareció poco fiable la IA?
- ¿Qué riesgos ves para los usuarios?
- ¿Qué papel crees que sigue siendo humano?
- ¿Cómo está cambiando la IA el papel de los testers?

> Quizás, en el futuro, el testing se desplace cada vez más de:
>
> "¿funciona?"
>
> hacia:
>
> "¿se comporta de forma responsable, comprensible y fiable?"
