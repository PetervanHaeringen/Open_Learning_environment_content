# Módulo 7 – Pruebas de API (API Testing)

En este módulo aprenderás los fundamentos de las pruebas de API.

Gran parte del software se compone de partes que se comunican entre sí mediante API.

Como tester, puedes comprobar estas API directamente con herramientas como Postman.
Eso hace que el testing sea:
- más rápido
- más preciso
- más potente

---

## 1. ¿Qué es una API?

API significa:

> **Application Programming Interface** (Interfaz de Programación de Aplicaciones)

Una API es una forma en la que los componentes de software se comunican entre sí.

Cuando pruebas una API, compruebas, por ejemplo:

- qué ocurre con las peticiones GET
- qué ocurre con las peticiones POST/PUT
- qué mensajes de error se devuelven
- si la estructura JSON es correcta
- con qué rapidez responde el servidor

### Ejemplo

Una app de tienda online pregunta:

> "Dame todos los productos de la categoría libros."

El servidor entonces devuelve datos en formato JSON.

---

## 2. Códigos de estado HTTP

Cada respuesta de una API contiene un código de estado.

Este indica si la petición se realizó con éxito.

### Códigos de estado más usados

- **200** — OK
- **201** — Created (Creado)
- **400** — Bad Request (Solicitud incorrecta)
- **401** — Unauthorized (No autorizado)
- **404** — Not Found (No encontrado)
- **500** — Server Error (Error del servidor)

> Un código de estado 500 suele indicar un error en el backend.

---

## 3. JSON: el lenguaje de las API

Muchas API se comunican mediante JSON.

JSON son datos de texto estructurados.

### Ejemplo

```json
{
  "id": 42,
  "name": "Producto de prueba",
  "price": 9.99
}
```

### Durante las pruebas de API, compruebas:

- ¿están todos los campos presentes?
- ¿son correctos los valores?
- ¿falta algún dato?
- ¿hay datos inesperados?

---

## 4. Probar API con Postman

Postman es una herramienta popular para las pruebas de API.

Con ella puedes probar:

- si los endpoints existen
- cómo responde una API ante errores
- los tiempos de respuesta
- las estructuras JSON

### Petición básica

1. Abre Postman
2. Elige el método: GET
3. Introduce la URL:
   `https://example.com/api/products`
4. Haz clic en Send
5. Observa:
   - el código de estado
   - las cabeceras (headers)
   - el cuerpo (body)

---

## 5. Checklist básica de API

Usa esta checklist durante las pruebas de API.

- [ ] El endpoint existe (sin 404)
- [ ] Respuesta correcta ante una entrada válida
- [ ] Respuesta correcta ante una entrada incorrecta
- [ ] La estructura JSON es correcta
- [ ] Los valores son lógicos
- [ ] El tiempo de respuesta es aceptable

---

## 6. Ejercicio práctico: 6 comprobaciones de API

Ahora vas a realizar seis pruebas de API por tu cuenta.

### Ejercicio

1. Elige una API pública o una API de demostración.
2. Realiza tres pruebas positivas.
3. Realiza tres pruebas negativas.
4. Anota:
   - el código de estado
   - el tiempo de respuesta
   - el cuerpo de la respuesta
5. Describe cualquier desviación o error.

> Los códigos de error no siempre son fallos.
> A menudo, precisamente demuestran que la API responde correctamente.

---

## 7. Reflexión

Piensa de nuevo en tus pruebas:

- ¿Qué códigos de estado viste con más frecuencia?
- ¿Fue la API predecible?
- ¿Qué prueba negativa dio resultados interesantes?
- ¿Dónde podría haber un riesgo de seguridad?
