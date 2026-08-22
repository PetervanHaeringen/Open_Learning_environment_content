# Module 9 – Dự án cuối khóa

Đây là thời điểm mà tất cả kiến thức từ TestGarden hội tụ lại với nhau.

Bạn sẽ thực hiện một quy trình kiểm thử hoàn chỉnh giống như những tester chuyên nghiệp vẫn làm:

- từ kế hoạch kiểm thử đến báo cáo lỗi
- từ kiểm thử khám phá đến kiểm tra API
- từ phân tích rủi ro đến thuyết trình

Bạn sẽ làm việc:
- một mình
- hoặc theo nhóm nhỏ

tùy theo hướng dẫn của giảng viên.

---

## 1. Mục tiêu của dự án cuối khóa

Dự án cuối khóa cho thấy rằng bạn có thể:

- làm việc một cách có tổ chức
- nhận diện được các rủi ro
- thiết kế các test case
- thành thạo kiểm thử khám phá
- viết các báo cáo lỗi rõ ràng
- kiểm thử API
- trình bày các phát hiện một cách chuyên nghiệp

Và có lẽ điều quan trọng hơn nữa là:

> bạn đang học cách nhìn nhận chất lượng, hành vi, và trải nghiệm người dùng một cách phản biện.

---

## 2. Nhiệm vụ dự án

Bạn sẽ kiểm thử một ứng dụng demo do giảng viên cung cấp.

Điều đó có thể là, ví dụ:

- một cửa hàng trực tuyến
- một biểu mẫu đăng ký
- một mini API
- một bảng điều khiển (dashboard)
- hoặc một sự kết hợp của những thứ này

---

## 3. Bộ hồ sơ kiểm thử hoàn chỉnh

Cuối cùng, bạn sẽ nộp một bộ hồ sơ kiểm thử hoàn chỉnh.

### Checklist

- [ ] Một kế hoạch kiểm thử 1 trang
- [ ] 8–12 test case với các kỹ thuật đã sử dụng
- [ ] Một smoke test đã được thực hiện
- [ ] Một báo cáo phiên kiểm thử khám phá (exploratory session report)
- [ ] Ít nhất 5 báo cáo lỗi
- [ ] 4–6 lần kiểm tra API
- [ ] (Tùy chọn) một bài kiểm thử tự động
- [ ] Một bài thuyết trình ngắn

---

## 4. Các sản phẩm bàn giao (Deliverables)

### 1) Kế hoạch kiểm thử

Sử dụng mẫu từ Module 3.

Đảm bảo rằng những điều sau đây rõ ràng:
- bạn đang kiểm thử cái gì
- rủi ro nào là quan trọng
- điều gì nằm ngoài phạm vi

---

### 2) Test case

Nộp 8–12 test case.

Sử dụng ít nhất:
- Phân vùng tương đương (Equivalence Partitioning)
- Phân tích giá trị biên (Boundary Value Analysis)
- Bảng quyết định (Decision Tables) hoặc Kiểm thử chuyển trạng thái (State Transitions)

---

### 3) Smoke Test

Thực hiện smoke test của riêng bạn.

Ghi lại:
- Pass/Fail
- GO/NO-GO
- những rủi ro đáng chú ý

---

### 4) Phiên kiểm thử khám phá

Thực hiện một phiên kiểm thử khám phá khoảng 60 phút.

Tạo ra:
- ghi chú
- quan sát
- phát hiện
- kết luận

---

### 5) Báo cáo lỗi

Viết ít nhất 5 báo cáo lỗi chuyên nghiệp.

Sử dụng:
- các bước rõ ràng
- kết quả mong đợi so với kết quả thực tế
- mức độ nghiêm trọng (severity) / mức độ ưu tiên (priority)
- ảnh chụp màn hình nếu có thể

---

### 6) Kiểm tra API

Thực hiện 4–6 bài kiểm thử API.

Mô tả:
- endpoint
- đầu vào
- mã trạng thái
- phản hồi
- phát hiện

---

### 7) (Tùy chọn) tự động hóa

Ví dụ, tạo:
- một bài kiểm thử đăng nhập
- một smoke test
- một luồng (flow) Playwright đơn giản

---

### 8) Thuyết trình

Thực hiện một bài thuyết trình ngắn từ 5–10 phút.

Trình bày về:
- cách tiếp cận của bạn
- những rủi ro lớn nhất
- những lỗi quan trọng nhất
- những gì bạn đã học được

---

## 5. Chất lượng hiện đại: nhiều hơn là chỉ có lỗi

Ngày nay, chất lượng phần mềm không chỉ còn xoay quanh:

> "nó có hoạt động về mặt kỹ thuật không?"

mà còn về:

- độ tin cậy
- bảo mật
- khả năng tiếp cận (accessibility)
- trải nghiệm người dùng
- hiệu năng
- hành vi của AI
- tính minh bạch

Vì vậy, hãy suy nghĩ thêm về:

- Ứng dụng này mang lại cảm giác gì cho người dùng?
- Những rủi ro nào phát sinh từ việc tự động hóa?
- Điều gì xảy ra khi có hành vi bất ngờ?
- Lỗi có tác động như thế nào đến con người?

---

## 6. Hợp tác với tư cách là một tester

Kiểm thử chuyên nghiệp hầu như không bao giờ là công việc đơn độc.

Bạn hợp tác với:
- các nhà phát triển
- product owner
- người dùng
- nhà thiết kế
- các công cụ AI
- các tester khác

Vì vậy, giao tiếp và hợp tác cũng quan trọng không kém kỹ thuật.

---

## 7. Mẹo để thành công

### Sắp xếp thời gian của bạn
Làm việc theo từng khối nhỏ.

### Suy nghĩ một cách phản biện
Tại sao điều gì đó lại là một lỗi?
Tác động của nó là gì?

### Kết hợp các kỹ thuật
Sử dụng:
- kiểm thử theo kịch bản
- kiểm thử khám phá
- kiểm thử API
- tự động hóa

### Để người khác cùng xem xét
Các tester khác thường tìm ra những góc nhìn mới.

### Thu thập bằng chứng
Ảnh chụp màn hình, log, và các ví dụ giúp ích rất nhiều.

---

## 8. Suy ngẫm

Hãy nhìn lại quá trình học tập của bạn:

- Bạn đã sử dụng kỹ thuật nào nhiều nhất?
- Bạn muốn phát triển thêm kỹ năng nào?
- Bạn đã học được gì về chất lượng?
- Lỗi nào bạn thấy thú vị nhất?
- Bạn nhìn nhận vai trò của tester trong tương lai như thế nào?

> Có lẽ, cuối cùng, kiểm thử không chỉ đơn thuần là tìm ra lỗi,
>
> mà là giúp xây dựng nên những hệ thống đáng tin cậy, dễ hiểu, và mang tính con người.
