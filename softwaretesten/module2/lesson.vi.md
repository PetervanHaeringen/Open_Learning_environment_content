# Module 2 — Các cấp độ kiểm thử (Test Levels) & Kiểm thử khói (Smoke Testing)

Trong module này, bạn sẽ khám phá việc kiểm thử phần mềm được thực hiện qua các lớp khác nhau như thế nào, và vai trò của **smoke test** nổi tiếng là gì.

Chúng ta sẽ đi từ cái nhìn tổng quan đến thực hành, để bạn hiểu công việc kiểm thử của mình là một phần của bức tranh lớn hơn như thế nào.

---

## 1. Các cấp độ kiểm thử là gì?

Phần mềm không được kiểm thử một lần duy nhất. Mỗi phần được kiểm tra ở một cấp độ khác nhau.

Chúng ta gọi những cấp độ này là **test levels**.

- **Kiểm thử đơn vị (Unit Testing)** — những đoạn code nhỏ, được kiểm thử bởi các nhà phát triển
- **Kiểm thử tích hợp (Integration tests)** — mọi thứ có hoạt động cùng nhau đúng như dự định không?
- **Kiểm thử hệ thống (System tests)** — toàn bộ ứng dụng có hoạt động như một thể thống nhất không?
- **Kiểm thử chấp nhận (Acceptance tests)** — nó có hoạt động tốt đối với người dùng và khách hàng không?

### Ví dụ

Trong một cửa hàng trực tuyến:

- kiểm thử đơn vị → việc tính toán giảm giá có hoạt động đúng không?
- kiểm thử tích hợp → giỏ hàng và kho hàng có hoạt động cùng nhau không?
- kiểm thử hệ thống → quy trình đặt hàng có hoạt động thông suốt từ đầu đến cuối không?
- kiểm thử chấp nhận → khách hàng có thấy quy trình này hợp lý và dễ sử dụng không?

---

## 2. Các loại kiểm thử: chức năng & phi chức năng

Bên cạnh các cấp độ kiểm thử, còn có **các loại kiểm thử (test types)**.

Điều này mô tả *bạn đang kiểm thử cái gì*.

- **Kiểm thử chức năng (Functional testing)** — chức năng đó có làm đúng những gì nó phải làm không?
- **Kiểm thử phi chức năng (Non-functional testing)** — tốc độ, bảo mật, tính dễ sử dụng, độ ổn định

Trong TestGarden, chúng ta chủ yếu tập trung vào kiểm thử chức năng, như smoke test và kiểm thử khám phá (exploratory testing).

---

## 3. Smoke Test là gì?

Smoke test là một **bài kiểm tra ngắn, nhanh** để xem hệ thống có "tương đối khỏe mạnh" hay không sau một bản release, cập nhật, hoặc triển khai (deploy) mới.

Nó giống như phiên bản kỹ thuật số của câu hỏi:

> "chuông báo khói có kêu không?"

Nếu có điều gì đó cơ bản bị hỏng, bạn muốn biết điều đó ngay lập tức.

### Tại sao cần smoke test?

- Chúng nhanh chóng và mang lại sự rõ ràng ngay lập tức
- Chúng giúp tránh lãng phí thời gian vào các bản build bị hỏng
- Chúng đưa ra kết luận GO / NO-GO cho các bước kiểm thử tiếp theo

### Ví dụ về một smoke test

- Ứng dụng có tải được không?
- Người dùng có thể đăng nhập không?
- Luồng chính (main flow) có hoạt động không?
- Có xuất hiện lỗi 404 hay 500 nào không?

---

## 4. Ví dụ về Checklist cho Smoke Test

- [ ] Trang web có thể truy cập được không?
- [ ] Người dùng thử nghiệm có thể đăng nhập không?
- [ ] Chức năng chính có hoạt động không?
- [ ] Các liên kết và nút bấm chính có hoạt động không?
- [ ] Không có lỗi lớn nào hiển thị chứ?
- [ ] Nó có hoạt động trên di động hoặc trình duyệt khác không?

Bạn kết thúc một smoke test bằng:

**GO / NO-GO**

---

## 5. Bài tập thực hành

1. Chọn một web app demo
2. Tạo một smoke checklist
3. Thực hiện checklist đó
4. Ghi lại Pass / Fail
5. Viết một kết luận

> Smoke test không phải là một bài kiểm thử đầy đủ.
> Nó là một lần quét sức khỏe nhanh.

---

## 6. Suy ngẫm

Hãy suy nghĩ về:

- Bước kiểm tra nào là quan trọng nhất?
- Vấn đề nào là rủi ro lớn nhất?
- Bạn sẽ cải thiện checklist của mình như thế nào?
