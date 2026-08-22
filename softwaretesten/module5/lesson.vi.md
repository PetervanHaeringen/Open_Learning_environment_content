# Module 5 – Kiểm thử khám phá (Exploratory Testing)

Kiểm thử khám phá là một trong những cách kiểm thử mạnh mẽ nhất và thú vị nhất.

Bạn sẽ đi trên một hành trình khám phá xuyên suốt phần mềm, giống như một người dùng thực sự sẽ làm:
tò mò, sáng tạo, và không có các bước được định sẵn từ trước.

Đây chính là nơi các tester mang lại giá trị thực sự.

---

## 1. Kiểm thử khám phá là gì?

Kiểm thử khám phá có nghĩa là bạn kiểm thử bằng cách **khám phá**:

bạn đồng thời:
- suy nghĩ về những gì mình muốn kiểm thử
- thực hiện nó
- và học hỏi trong quá trình kiểm thử

Đây là điều đối lập hoàn toàn với một kịch bản cứng nhắc.

> Bạn đi theo đôi mắt, trực giác của mình, và những tín hiệu mà phần mềm mang lại.

### Đặc điểm

- Bạn suy nghĩ như một người dùng
- Bạn nhấp chuột, thử nghiệm, và thí nghiệm
- Bạn theo dõi những trục trặc kỳ lạ hoặc những tình huống bất ngờ
- Bạn khám phá mà không có một danh sách các bước cố định

---

## 2. Tại sao kiểm thử khám phá lại quan trọng?

Kiểm thử khám phá thường tìm ra những lỗi không bao giờ xuất hiện trong bất kỳ tài liệu hay test case nào.

### Những vấn đề mà bạn thường chỉ tìm thấy được qua khám phá

- Hành vi kỳ lạ khi nhấp chuột nhanh
- Hành vi trên di động khác với trên máy tính để bàn
- Các luồng thiếu logic
- Các chuyển màn hình gây khó hiểu
- Những vấn đề nhỏ về bố cục hoặc văn bản

Vì vậy, kiểm thử khám phá là một sự bổ sung hoàn hảo cho kiểm thử theo kịch bản (scripted testing).

---

## 3. Quản lý kiểm thử dựa trên phiên (Session-Based Test Management, SBTM)

Trong quá trình kiểm thử khám phá, bạn thường làm việc theo các phiên (session) ngắn.

Một phiên như vậy thường có ba phần:

- **Charter (Bản định hướng)** — bạn sẽ khám phá điều gì?
- **Timer (Bộ đếm giờ)** — thường từ 30 đến 60 phút
- **Ghi chú** — bạn thấy gì, và điều gì nổi bật?

### Ví dụ về một Charter

> Khám phá trang đăng ký để tìm các luồng thiếu logic, thông báo lỗi, và trải nghiệm sử dụng trên di động.

---

## 4. Làm thế nào để thực hiện Kiểm thử khám phá?

Một vài gợi ý thực tế:

- Bắt đầu với một mục tiêu rõ ràng
- Suy nghĩ như một người dùng
- Đặt câu hỏi:
  - "Điều gì sẽ xảy ra nếu…?"
- Theo dõi những tình huống bất ngờ
- Ghi chú lại bất cứ điều gì nổi bật
- Kiểm thử cả nhanh lẫn chậm
- Kiểm thử trên di động, máy tính bảng, và các trình duyệt khác

> Kiểm thử khám phá không phải là hỗn loạn.
> Bạn làm việc có mục đích, nhưng vẫn để lại không gian cho sự khám phá.

---

## 5. Báo cáo phiên (Session Report)

Hãy sử dụng một báo cáo ngắn gọn trong hoặc sau phiên kiểm thử của bạn.

```text
Báo cáo phiên – [thành phần] – [ngày]

Charter:
  Mục tiêu của bạn là gì?

Thời lượng:
  Bạn đã kiểm thử trong bao lâu?

Quan sát:
  - Bạn đã thấy gì?
  - Những tình huống kỳ lạ nào đã xuất hiện?

Vấn đề đã tìm thấy:
  - Bug 1: mô tả + có thể tái tạo lại được không?
  - Bug 2: mô tả + có thể tái tạo lại được không?
  - Bug 3: mô tả + có thể tái tạo lại được không?

Ghi chú:
  Câu hỏi, ý tưởng, băn khoăn
```

---

## 6. Bài tập thực hành: Phiên kiểm thử khám phá 60 phút

Bây giờ, bạn sẽ tự mình thực hiện một phiên kiểm thử khám phá.

### Nhiệm vụ

1. Chọn một thành phần:
   - đăng ký
   - đăng nhập
   - giỏ hàng
   - hoặc một thành phần khác

2. Viết một charter chỉ trong một câu.

3. Đặt bộ đếm giờ trong 60 phút.

4. Kiểm thử theo hướng khám phá và ghi chú lại mọi thứ nổi bật.

5. Viết một báo cáo phiên.

6. Nộp ít nhất 3 lỗi dưới dạng các báo cáo lỗi riêng biệt.

> Hãy thường xuyên tự hỏi:
> "Người dùng có thể bị bối rối ở đâu?"

---

## 7. Suy ngẫm

Hãy nhớ lại phiên kiểm thử của bạn:

- Điều gì khiến bạn bất ngờ?
- Lỗi nào bạn sẽ không bao giờ tìm ra được nếu chỉ dựa vào test case?
- Những kỹ năng nào đã phát huy tác dụng?
- Lần sau bạn sẽ làm gì khác đi?
