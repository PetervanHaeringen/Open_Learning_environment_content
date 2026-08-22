# Module 3 – Kế hoạch kiểm thử & Phân tích rủi ro

Trong module này, bạn sẽ học những kiến thức cơ bản về một kế hoạch kiểm thử gọn nhẹ (lightweight).

Không phải những tài liệu dày cộp, mà là một bản tóm tắt mang tính thực tiễn về:

**chúng ta sẽ kiểm thử cái gì, tại sao, bằng cách nào, và khi nào thì đủ tốt?**

---

## 1. Kế hoạch kiểm thử là gì?

Kế hoạch kiểm thử là một tài liệu ngắn, mang lại định hướng cho việc kiểm thử.

Nó mô tả:

- những gì cần được kiểm thử
- những rủi ro nào là quan trọng
- phương pháp nào được lựa chọn

Trong các dự án hiện đại, và chắc chắn là trong TestGarden, chúng ta luôn cố gắng làm cho các kế hoạch kiểm thử đơn giản nhất có thể.

Thường thì chỉ một trang là đã đủ.

### Một kế hoạch kiểm thử thường bao gồm

- Phạm vi (Scope) — chúng ta kiểm thử cái gì, và không kiểm thử cái gì?
- Những rủi ro chính
- Phương pháp — smoke test, test case, kiểm thử khám phá (exploratory testing)
- Môi trường kiểm thử
- Tiêu chí bắt đầu & kết thúc (Entry & Exit criteria)
- Vai trò — ai làm việc gì?

---

## 2. Kiểm thử dựa trên rủi ro (Risk-based testing) là gì?

Rủi ro giúp bạn quyết định phần nào là quan trọng nhất cần kiểm thử.

Một rủi ro xuất hiện khi một **lỗi có thể xảy ra** kết hợp với **mức độ ảnh hưởng** của nó.

Chúng ta sử dụng một công thức đơn giản:

> **Rủi ro = xác suất × mức độ ảnh hưởng**

Rủi ro càng cao, phần đó càng cần nhiều sự chú ý trong kế hoạch kiểm thử của bạn.

### Ví dụ về một cửa hàng trực tuyến

- Trang "Xem sản phẩm" → mức độ ảnh hưởng thấp
- Trang "Thanh toán" (Checkout) → mức độ ảnh hưởng cao

Vì vậy, quy trình thanh toán sẽ được kiểm thử nhiều hơn và sâu hơn.

---

## 3. Ví dụ về một kế hoạch kiểm thử 1 trang

Hãy sử dụng mẫu này làm cơ sở khi bạn tự viết kế hoạch kiểm thử của riêng mình.

```text
Tiêu đề: Kế hoạch kiểm thử cho [thành phần/ứng dụng]
Ngày:
Người viết:

1. Phạm vi (Scope):
   - Chúng ta kiểm thử cái gì?
   - Chúng ta không kiểm thử cái gì?

2. Những rủi ro chính:
   - R1: [rủi ro + lý do]
   - R2: [rủi ro + lý do]

3. Phương pháp:
   - Smoke test
   - Test case
   - Kiểm thử khám phá

4. Môi trường kiểm thử:
   - URL, dữ liệu, tài khoản

5. Tiêu chí bắt đầu (Entry criteria):
   - Bản build hoạt động
   - Dữ liệu kiểm thử đã sẵn sàng

6. Tiêu chí kết thúc (Exit criteria):
   - Không còn lỗi P1/P0 nào đang mở
   - Smoke test đã đạt

7. Vai trò:
   - (Các) tester
   - Người hướng dẫn / Product owner
```

---

## 4. Bài tập thực hành: Tạo mini kế hoạch kiểm thử của riêng bạn

Bây giờ, lần đầu tiên bạn sẽ tự viết một kế hoạch kiểm thử cho một phần nhỏ của ứng dụng demo.

### Nhiệm vụ

1. Chọn một phần của ứng dụng demo, ví dụ như tính năng đăng ký.
2. Xác định 3 rủi ro bằng cách sử dụng xác suất × mức độ ảnh hưởng.
3. Mô tả những gì bạn sẽ kiểm thử (*phạm vi*).
4. Chọn phương pháp của bạn:
   - smoke testing
   - test case
   - kiểm thử khám phá
5. Điền đầy đủ vào mẫu kế hoạch kiểm thử 1 trang.

> **Mẹo:**
> Hãy giữ nó ngắn gọn, rõ ràng và thực tế.
> Kế hoạch kiểm thử không phải là một bản báo cáo — nó là chiếc la bàn của bạn.

---

## 5. Suy ngẫm

Hãy suy nghĩ về kế hoạch kiểm thử của bạn:

- Rủi ro nào là quan trọng nhất?
- Bạn đã để những gì *ngoài* phạm vi, và tại sao?
- Bạn có muốn thêm nhiều chi tiết hơn hay ít hơn không?

Hãy thử tìm hiểu:

- những lựa chọn nào là có chủ đích
- những phần nào nhận được sự chú ý đặc biệt
- và cách tiếp cận của bạn sẽ thay đổi ra sao với một ứng dụng lớn hơn
