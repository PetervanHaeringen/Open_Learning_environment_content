# Module 7 – API Testing

In this module you'll learn the basics of API Testing.

A lot of software consists of components that communicate with each other via APIs.

As a tester, you can check these APIs directly with tools like Postman.
That makes testing:
- faster
- more precise
- more powerful

---

## 1. What is an API?

API stands for:

> **Application Programming Interface**

An API is a way for software components to communicate with each other.

When you test an API, you check things like:

- what happens on GET requests
- what happens on POST/PUT requests
- which error messages come back
- whether the JSON structure is correct
- how quickly the server responds

### Example

A webshop app asks:

> "Give me all products in the books category."

The server then sends back JSON data.

---

## 2. HTTP Status Codes

Every API response contains a status code.

It tells you whether the request was successful.

### Commonly used status codes

- **200** — OK
- **201** — Created
- **400** — Bad Request
- **401** — Unauthorized
- **404** — Not Found
- **500** — Server Error

> A 500 status code usually points to a bug in the backend.

---

## 3. JSON: the language of APIs

Many APIs communicate using JSON.

JSON is structured text data.

### Example

```json
{
  "id": 42,
  "name": "Test product",
  "price": 9.99
}
```

### During API testing, you check:

- are all the fields there?
- are the values correct?
- is any data missing?
- is there any unexpected data?

---

## 4. Testing APIs with Postman

Postman is a popular tool for API testing.

You can use it to test:

- whether endpoints exist
- how an API responds to errors
- response times
- JSON structures

### Basic request

1. Open Postman
2. Choose method: GET
3. Enter the URL:
   `https://example.com/api/products`
4. Click Send
5. Check:
   - status code
   - headers
   - body

---

## 5. Basic API checklist

Use this checklist during API testing.

- [ ] Endpoint exists (no 404)
- [ ] Correct response to valid input
- [ ] Correct response to invalid input
- [ ] JSON structure is correct
- [ ] Values make sense
- [ ] Response time is acceptable

---

## 6. Practical assignment: 6 API checks

You're now going to run six API tests yourself.

### Assignment

1. Choose a public API or demo API.
2. Run three positive tests.
3. Run three negative tests.
4. Note down:
   - status code
   - response time
   - response body
5. Describe any deviations or bugs.

> Error codes aren't always errors.
> Often they show that the API is responding correctly.

---

## 7. Reflection

Think back on your tests:

- Which status codes did you see the most?
- Was the API predictable?
- Which negative test gave interesting results?
- Where might a security risk be lurking?
