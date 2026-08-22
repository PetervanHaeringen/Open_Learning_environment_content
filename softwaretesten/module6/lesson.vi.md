# Module 6 – Báo cáo lỗi (Bug Reporting)

Viết báo cáo lỗi là một trong những kỹ năng quan trọng nhất của một tester.

Một báo cáo lỗi tốt cần phải:
- rõ ràng
- có thể tái tạo lại được
- đầy đủ
- hữu ích cho các nhà phát triển

Trong module này, bạn sẽ học cách viết các báo cáo lỗi chuyên nghiệp.

---

## 1. Bug là gì?

**Bug** là tình huống trong đó phần mềm không hoạt động như mong đợi.

Điều này có thể bao gồm:

- lỗi chức năng
- vấn đề về bố cục
- thông báo lỗi không chính xác
- hành vi bất ngờ
- vấn đề bảo mật
- vấn đề về hiệu năng

Vì vậy, bug chính là sự khác biệt giữa:

> hành vi mong đợi ↔ hành vi thực tế

---

## 2. Điều gì tạo nên một báo cáo lỗi tốt?

Một báo cáo lỗi tốt cần phải:

- **Rõ ràng** — ai cũng hiểu được vấn đề
- **Có thể tái tạo lại được** — người khác có thể làm cho lỗi xảy ra lần nữa
- **Đầy đủ** — chứa tất cả thông tin liên quan
- **Trung lập** — mang tính khách quan, không đổ lỗi hay cảm xúc

### Ví dụ

#### Báo cáo lỗi kém

> "Trang web không hoạt động. Sửa giúp với."

#### Báo cáo lỗi tốt

> "Khi nhấp vào 'Lưu', xuất hiện lỗi 500 và biểu mẫu không được lưu lại."

---

## 3. Mức độ nghiêm trọng (Severity) và Mức độ ưu tiên (Priority)

Các tester thường gắn nhãn cho các bug.

### Mức độ nghiêm trọng (Severity)

Vấn đề này nghiêm trọng đến mức nào đối với hệ thống?

### Mức độ ưu tiên (Priority)

Cần phải sửa nhanh đến mức nào?

### Ví dụ

#### Mức độ nghiêm trọng cao, mức độ ưu tiên thấp
Một lỗi crash trong một tính năng mà hầu như không ai sử dụng.

#### Mức độ nghiêm trọng thấp, mức độ ưu tiên cao
Một lỗi chính tả trên trang chủ của một khách hàng quan trọng.

---

## 4. Mẫu báo cáo lỗi (Bug Report Template)

Sử dụng mẫu này khi viết báo cáo lỗi.

```text
Tiêu đề:
  Mô tả ngắn gọn và rõ ràng

Môi trường:
  Trình duyệt, hệ điều hành, phiên bản, thiết bị

Mức độ nghiêm trọng (Severity):
Mức độ ưu tiên (Priority):

Các bước để tái tạo lỗi:
  1. ...
  2. ...
  3. ...

Kết quả mong đợi:
  Điều gì lẽ ra phải xảy ra?

Kết quả thực tế:
  Điều gì đã xảy ra thay vào đó?

Ảnh chụp màn hình / log:
  (không bắt buộc nhưng nên có)

Ghi chú thêm:
  tần suất, mức độ ảnh hưởng, các chi tiết đặc biệt
```

---

## 5. Bài tập thực hành: viết 3 báo cáo lỗi

Bây giờ, bạn sẽ viết ba báo cáo lỗi dựa trên những lỗi bạn đã tìm thấy trước đó trong quá trình kiểm thử khám phá.

### Nhiệm vụ

1. Chọn ba vấn đề từ báo cáo phiên (session report) của bạn.
2. Viết một báo cáo lỗi đầy đủ cho mỗi vấn đề.
3. Sử dụng mẫu ở trên.
4. Kiểm tra xem lỗi đó có thể tái tạo lại được hay không.
5. Nhờ một bạn cùng lớp kiểm tra báo cáo của bạn.

> Một báo cáo lỗi chỉ thực sự tốt khi người khác có thể tái tạo lại chính xác cùng một vấn đề.

---

## 6. Suy ngẫm

Hãy nhớ lại các báo cáo lỗi của bạn:

- Báo cáo nào rõ ràng nhất?
- Ban đầu bạn đã bỏ sót thông tin gì?
- Bạn cùng lớp của bạn đã phản hồi như thế nào?
- Lần sau bạn sẽ làm gì khác đi?
