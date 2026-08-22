# Module 7 – Kiểm thử API (API Testing)

Trong module này, bạn sẽ học những kiến thức cơ bản về Kiểm thử API.

Rất nhiều phần mềm được cấu thành từ các thành phần giao tiếp với nhau thông qua API.

Là một tester, bạn có thể kiểm tra trực tiếp các API này bằng các công cụ như Postman.
Điều đó làm cho việc kiểm thử trở nên:
- nhanh hơn
- chính xác hơn
- mạnh mẽ hơn

---

## 1. API là gì?

API có nghĩa là:

> **Giao diện lập trình ứng dụng (Application Programming Interface)**

API là cách mà các thành phần phần mềm giao tiếp với nhau.

Khi bạn kiểm thử một API, bạn kiểm tra ví dụ như:

- điều gì xảy ra với các yêu cầu GET
- điều gì xảy ra với các yêu cầu POST/PUT
- những thông báo lỗi nào được trả về
- cấu trúc JSON có chính xác không
- máy chủ phản hồi nhanh như thế nào

### Ví dụ

Một ứng dụng cửa hàng trực tuyến hỏi:

> "Cho tôi tất cả các sản phẩm thuộc danh mục sách."

Sau đó, máy chủ sẽ gửi lại dữ liệu JSON.

---

## 2. Mã trạng thái HTTP (HTTP Status Codes)

Mỗi phản hồi API đều chứa một mã trạng thái.

Mã này cho biết yêu cầu đó có thành công hay không.

### Các mã trạng thái thường được sử dụng

- **200** — OK (Thành công)
- **201** — Created (Đã tạo)
- **400** — Bad Request (Yêu cầu không hợp lệ)
- **401** — Unauthorized (Chưa được ủy quyền)
- **404** — Not Found (Không tìm thấy)
- **500** — Server Error (Lỗi máy chủ)

> Mã trạng thái 500 thường chỉ ra một lỗi ở phía backend.

---

## 3. JSON: ngôn ngữ của API

Nhiều API giao tiếp bằng JSON.

JSON là dữ liệu văn bản có cấu trúc.

### Ví dụ

```json
{
  "id": 42,
  "name": "Sản phẩm thử nghiệm",
  "price": 9.99
}
```

### Trong quá trình kiểm thử API, bạn kiểm tra:

- tất cả các trường có đầy đủ không?
- các giá trị có chính xác không?
- có thiếu dữ liệu nào không?
- có dữ liệu bất ngờ nào không?

---

## 4. Kiểm thử API với Postman

Postman là một công cụ phổ biến để kiểm thử API.

Bạn có thể sử dụng nó để kiểm thử:

- các endpoint có tồn tại hay không
- API phản hồi như thế nào với các lỗi
- thời gian phản hồi (response time)
- cấu trúc JSON

### Yêu cầu cơ bản

1. Mở Postman
2. Chọn phương thức: GET
3. Nhập URL:
   `https://example.com/api/products`
4. Nhấp vào Send
5. Kiểm tra:
   - mã trạng thái
   - headers
   - body

---

## 5. Checklist API cơ bản

Sử dụng checklist này trong quá trình kiểm thử API.

- [ ] Endpoint tồn tại (không bị lỗi 404)
- [ ] Phản hồi chính xác với dữ liệu đầu vào hợp lệ
- [ ] Phản hồi chính xác với dữ liệu đầu vào không hợp lệ
- [ ] Cấu trúc JSON chính xác
- [ ] Các giá trị hợp lý
- [ ] Thời gian phản hồi chấp nhận được

---

## 6. Bài tập thực hành: 6 lần kiểm tra API

Bây giờ, bạn sẽ tự mình thực hiện sáu bài kiểm thử API.

### Nhiệm vụ

1. Chọn một API công khai hoặc một API demo.
2. Thực hiện ba bài kiểm thử tích cực (positive test).
3. Thực hiện ba bài kiểm thử tiêu cực (negative test).
4. Ghi lại:
   - mã trạng thái
   - thời gian phản hồi
   - nội dung phản hồi (response body)
5. Mô tả các sai lệch hoặc lỗi mà bạn tìm thấy.

> Mã lỗi không phải lúc nào cũng là lỗi.
> Thường thì chúng cho thấy chính xác rằng API đang phản hồi đúng cách.

---

## 7. Suy ngẫm

Hãy nhớ lại các bài kiểm thử của bạn:

- Bạn thấy những mã trạng thái nào nhiều nhất?
- API này có dễ đoán không?
- Bài kiểm thử tiêu cực nào cho ra kết quả thú vị?
- Rủi ro bảo mật có thể nằm ở đâu?
