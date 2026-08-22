# Módulo 4 – Técnicas de prueba

En este módulo aprenderás a diseñar buenos casos de prueba (test cases).

No se trata de "hacer clic en cualquier cosa", sino de probar de forma estructurada, inteligente y creativa.

Estas técnicas te ayudan a encontrar errores que de otro modo nunca verías.

---

## 1. ¿Por qué usar técnicas de prueba?

Las técnicas de prueba te ayudan a probar de forma **más consciente, más completa y más inteligente**.

Se aseguran de que no solo pruebes los "caminos felices" (happy paths), sino también:
- escenarios de error
- entradas raras
- valores límite

Un buen tester usa técnicas para:
- encontrar más errores
- probar de forma más eficiente
- demostrar que se ha pensado en los casos de prueba
- crear casos de prueba reproducibles y claros

---

## 2. Partición de equivalencia (Equivalence Partitioning, EP)

Con la partición de equivalencia (EP) divides todas las entradas posibles en grupos ("particiones") de los que esperas que produzcan el mismo comportamiento.

### Ejemplo

Un campo de edad acepta edades entre **18 y 65**.

Entonces las particiones son:

- Demasiado joven (0–17)
- Válida (18–65)
- Demasiado mayor (66+)

> En lugar de probar 48 edades válidas posibles, pruebas solo 1.
> Menos trabajo, la misma cobertura.

---

## 3. Análisis de valores límite (Boundary Value Analysis, BVA)

Los errores suelen estar en los límites de los valores de entrada.

Por eso, las pruebas de límites se centran en:
- mínimos
- máximos
- valores justo fuera del límite

### Ejemplo

La edad 18–65 es válida.

Entonces pruebas:

- 17 (justo demasiado baja)
- 18 (la más baja válida)
- 65 (la más alta válida)
- 66 (justo demasiado alta)

Esta técnica encuentra muchos errores que afectan directamente a los usuarios.

---

## 4. Tablas de decisión (Decision Tables)

Úsalas cuando se aplican varias reglas o condiciones al mismo tiempo.

Pones todo en una tabla y creas un caso de prueba para cada combinación.

### Ejemplo: iniciar sesión

| Nombre de usuario | Contraseña | Resultado esperado |
|---|---|---|
| Correcto | Correcta | Login correcto |
| Correcto | Incorrecta | Mensaje de error |
| Incorrecto | Correcta | Mensaje de error |
| Incorrecto | Incorrecta | Mensaje de error |

---

## 5. Pruebas de transición de estados (State Transition Testing)

Algunos sistemas cambian de estado.

Por ejemplo:
- un usuario inicia o cierra sesión
- un pedido cambia de estado
- un flujo de trabajo pasa al siguiente paso

Aquí pruebas:
- transiciones válidas
- transiciones no válidas
- qué ocurre cuando se saltan pasos

### Ejemplo: estado de un pedido

#### Transiciones válidas
- Realizado → Pagado
- Pagado → Enviado

#### Transiciones no válidas
- Enviado → Realizado
- Enviado → Pagado

---

## 6. Ejercicio práctico: escribe 8 casos de prueba

Ahora vas a crear tus propios casos de prueba, para una pantalla de inicio de sesión o un campo de entrada de tu elección.

Usa al menos dos técnicas.

### Ejercicio

1. Elige un componente:
   - inicio de sesión
   - restablecimiento de contraseña
   - campo de edad
   - o algo distinto

2. Escribe 8 casos de prueba con:
   - pasos
   - resultado esperado
   - técnica utilizada

3. Haz que un compañero de clase ejecute tus casos de prueba.

4. Mejora tus casos de prueba a partir del feedback recibido.

> Un buen caso de prueba es:
> - breve
> - claro
> - reproducible

---

## 7. Reflexión

Piensa en tus casos de prueba:

- ¿Qué técnica te resultó más lógica?
- ¿Qué te llevó más tiempo?
- ¿Qué técnica te pareció sorprendentemente eficaz?
