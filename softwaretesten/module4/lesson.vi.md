# Module 4 – Kỹ thuật kiểm thử

Trong module này, bạn sẽ học cách thiết kế các test case tốt.

Không phải là "cứ nhấp lung tung", mà là kiểm thử một cách có cấu trúc, thông minh và sáng tạo.

Những kỹ thuật này giúp bạn tìm ra những lỗi mà nếu không, bạn sẽ không bao giờ phát hiện được.

---

## 1. Tại sao cần kỹ thuật kiểm thử?

Các kỹ thuật kiểm thử giúp bạn kiểm thử **có ý thức hơn, đầy đủ hơn, và thông minh hơn**.

Chúng đảm bảo rằng bạn không chỉ kiểm thử những "đường đi thuận lợi" (happy paths), mà còn:
- các kịch bản lỗi
- những dữ liệu đầu vào kỳ lạ
- các giá trị biên

Một tester giỏi sử dụng các kỹ thuật để:
- tìm ra nhiều lỗi hơn
- kiểm thử hiệu quả hơn
- cho thấy rằng đã có sự suy nghĩ kỹ lưỡng đằng sau các test case
- tạo ra các test case rõ ràng và có thể lặp lại được

---

## 2. Phân vùng tương đương (Equivalence Partitioning, EP)

Với Phân vùng tương đương (EP), bạn chia tất cả các đầu vào có thể có thành các nhóm ("phân vùng"/partitions) mà bạn kỳ vọng sẽ tạo ra cùng một hành vi.

### Ví dụ

Một trường tuổi chấp nhận độ tuổi từ **18 đến 65**.

Khi đó, các phân vùng sẽ là:

- Quá trẻ (0–17)
- Hợp lệ (18–65)
- Quá già (66+)

> Thay vì kiểm thử 48 độ tuổi hợp lệ có thể có, bạn chỉ cần kiểm thử 1 giá trị.
> Ít công sức hơn, nhưng độ bao phủ vẫn tương đương.

---

## 3. Phân tích giá trị biên (Boundary Value Analysis, BVA)

Lỗi thường nằm ở ranh giới của các giá trị đầu vào.

Vì vậy, kiểm thử biên tập trung vào:
- giá trị nhỏ nhất
- giá trị lớn nhất
- các giá trị vừa vượt qua ranh giới

### Ví dụ

Độ tuổi 18–65 là hợp lệ.

Khi đó, bạn sẽ kiểm thử:

- 17 (vừa thấp hơn một chút)
- 18 (giá trị hợp lệ thấp nhất)
- 65 (giá trị hợp lệ cao nhất)
- 66 (vừa cao hơn một chút)

Kỹ thuật này tìm ra rất nhiều lỗi ảnh hưởng trực tiếp đến người dùng.

---

## 4. Bảng quyết định (Decision Tables)

Sử dụng phương pháp này khi nhiều quy tắc hoặc điều kiện áp dụng cùng lúc.

Bạn đưa tất cả vào một bảng, và tạo một test case cho mỗi tổ hợp.

### Ví dụ: đăng nhập

| Tên đăng nhập | Mật khẩu | Kết quả mong đợi |
|---|---|---|
| Đúng | Đúng | Đăng nhập thành công |
| Đúng | Sai | Thông báo lỗi |
| Sai | Đúng | Thông báo lỗi |
| Sai | Sai | Thông báo lỗi |

---

## 5. Kiểm thử chuyển trạng thái (State Transition Testing)

Một số hệ thống có sự thay đổi về trạng thái.

Ví dụ:
- người dùng đăng nhập hoặc đăng xuất
- đơn hàng thay đổi trạng thái
- quy trình làm việc (workflow) chuyển sang bước tiếp theo

Ở đây, bạn kiểm thử:
- các chuyển đổi hợp lệ
- các chuyển đổi không hợp lệ
- điều gì xảy ra khi các bước bị bỏ qua

### Ví dụ: trạng thái đơn hàng

#### Các chuyển đổi hợp lệ
- Đã đặt hàng → Đã thanh toán
- Đã thanh toán → Đã giao hàng

#### Các chuyển đổi không hợp lệ
- Đã giao hàng → Đã đặt hàng
- Đã giao hàng → Đã thanh toán

---

## 6. Bài tập thực hành: viết 8 test case

Bây giờ, bạn sẽ tự tạo các test case cho một màn hình đăng nhập hoặc một trường nhập liệu tùy chọn.

Sử dụng ít nhất hai kỹ thuật.

### Nhiệm vụ

1. Chọn một thành phần:
   - đăng nhập
   - đặt lại mật khẩu
   - trường tuổi
   - hoặc thứ khác

2. Viết 8 test case với:
   - các bước thực hiện
   - kết quả mong đợi
   - kỹ thuật đã sử dụng

3. Nhờ một bạn cùng lớp thực hiện các test case của bạn.

4. Cải thiện các test case của bạn dựa trên phản hồi nhận được.

> Một test case tốt là:
> - ngắn gọn
> - rõ ràng
> - có thể tái tạo lại được

---

## 7. Suy ngẫm

Hãy suy nghĩ về các test case của bạn:

- Kỹ thuật nào cảm thấy hợp lý nhất?
- Điều gì tốn nhiều thời gian nhất?
- Kỹ thuật nào bạn thấy hiệu quả một cách bất ngờ?
