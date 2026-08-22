# Module 8 – Tự động hóa & Kiểm thử AI

Trong module này, bạn sẽ làm quen với hai xu hướng phát triển lớn trong kiểm thử phần mềm hiện đại:

- tự động hóa kiểm thử (test automation)
- kiểm thử có sự hỗ trợ của AI (AI-assisted testing)

Việc phát triển phần mềm đang thay đổi nhanh chóng.
Các hệ thống AI viết code, tạo ra các bài kiểm thử, phân tích log, và hỗ trợ các tester trong công việc của họ.

Nhưng đồng thời, một thách thức mới cũng xuất hiện:

> Làm thế nào để bạn kiểm tra được những hệ thống không phải lúc nào cũng phản hồi chính xác giống nhau?

Vì vậy, vai trò của tester đang dần chuyển từ:
- chỉ đơn thuần kiểm tra
sang:
- quan sát
- đánh giá
- diễn giải
- tư duy phản biện

---

## 1. Tự động hóa kiểm thử là gì?

Tự động hóa kiểm thử có nghĩa là các bài kiểm thử được thực hiện tự động bởi các script hoặc công cụ.

Thay vì lặp đi lặp lại thủ công cùng một quy trình, bạn để cho phần mềm tự lặp lại việc đó.

Bạn thường tự động hóa:

- smoke test
- kiểm thử hồi quy (regression tests)
- kiểm tra API
- các luồng end-to-end
- kiểm tra hiệu năng

### Tại sao lại tự động hóa?

Tự động hóa giúp:
- nhận được phản hồi nhanh hơn
- kiểm thử có thể lặp lại được
- giảm thiểu lỗi do con người
- kiểm thử thường xuyên hơn

### Những gì thường không được tự động hóa?

Một số hình thức kiểm thử vẫn mang tính con người rất cao:

- kiểm thử khám phá
- khả năng sử dụng (usability)
- sự sáng tạo
- sự đồng cảm
- hiểu ngữ cảnh
- nhận ra các tình huống bất ngờ

> Tự động hóa giúp tester mạnh mẽ hơn.
> Nó không thay thế được nhận thức sâu sắc của họ.

---

## 2. Các công cụ hiện đại cho tự động hóa

Các công cụ thường được sử dụng gồm:

- **Playwright**
- **Cypress**
- **Selenium**
- **Postman**
- Các pipeline CI/CD như GitHub Actions

### Ví dụ về tự động hóa

Một script có thể tự động:

1. mở một trang web
2. đăng nhập
3. điền vào các biểu mẫu
4. kiểm tra xem có điều gì đó hiển thị hay không
5. báo cáo lỗi

Điều đó giúp cho việc kiểm thử hồi quy nhanh chóng trở nên khả thi với mỗi bản release mới.

---

## 3. Kiểm thử có sự hỗ trợ của AI

AI ngày càng được sử dụng nhiều hơn để hỗ trợ việc kiểm thử.

Ví dụ, để:

- tạo ra các test case
- tóm tắt log
- nhận diện các mẫu lỗi (error patterns)
- dự đoán các rủi ro hồi quy
- tạo dữ liệu kiểm thử
- tự động viết tài liệu

### Nhưng hãy cẩn thận

Đầu ra của AI thường nghe có vẻ thuyết phục.

Điều đó không đồng nghĩa với việc nó tự động đúng.

Một AI có thể:
- đưa ra các giả định sai
- bịa ra các chi tiết
- bỏ sót các kịch bản quan trọng
- đưa ra các câu trả lời thiếu nhất quán

Vì vậy, sự kiểm soát của con người vẫn là điều thiết yếu.

> Những tester giỏi không tin tưởng AI một cách mù quáng.
> Họ sử dụng AI một cách phản biện.

---

## 4. Hệ thống tất định (Deterministic) so với hệ thống xác suất (Probabilistic)

Phần mềm truyền thống thường hoạt động theo kiểu tất định (deterministic).

Điều đó có nghĩa là:

```text
cùng một đầu vào → cùng một đầu ra
```

Với các hệ thống AI, điều này thường hoạt động khác đi.

Một mô hình ngôn ngữ lớn (LLM) hoặc hệ thống gợi ý (recommender system) có thể phản hồi theo cách:

```text
cùng một đầu vào → nhiều đầu ra khả dĩ khác nhau
```

Chúng ta gọi đây là hành vi xác suất (probabilistic behavior).

### Tại sao điều này lại quan trọng?

Bởi vì điều đó làm thay đổi cách bạn kiểm thử.

Với phần mềm cổ điển, bạn thường kiểm tra:

- kết quả chính xác
- các quy tắc cố định
- kết quả có thể dự đoán được

Với các hệ thống AI, bạn thường đánh giá nhiều hơn về:

- chất lượng
- tính nhất quán
- tính hợp lý
- sự an toàn
- thiên vị (bias)
- độ nhạy cảm với ngữ cảnh

---

## 5. Đánh giá đầu ra của AI một cách phản biện

Các hệ thống AI có thể nghe có vẻ thuyết phục nhưng vẫn có thể mắc lỗi.

Vì vậy, với tư cách là tester, bạn kiểm tra:

- thông tin có chính xác không?
- hệ thống có bám sát nhiệm vụ được giao không?
- có xuất hiện ảo giác (hallucination) không?
- đầu ra có an toàn không?
- hệ thống có phản hồi ổn định không?
- nó có đối xử công bằng với người dùng không?

### Ảo giác (Hallucinations)

Một AI có thể tạo ra thông tin:
- nghe có vẻ đáng tin
- nhưng thực chất lại sai về mặt thực tế

Ví dụ như:
- các nguồn thông tin bịa đặt
- các tính năng không tồn tại
- các kết luận sai
- các bản tóm tắt không chính xác

Vì vậy, một tester cần phải học được rằng:

> "Nghe có vẻ hợp lý" không giống với "là chính xác".

---

## 6. Những rủi ro quan trọng với các hệ thống AI

### Thiên vị (Bias)

Hệ thống có đối xử công bằng với các nhóm người dùng khác nhau không?

### Trôi dạt (Drift)

Hành vi có dần thay đổi do dữ liệu mới không?

### Độ nhạy với prompt (Prompt sensitivity)

Một thay đổi nhỏ trong cách diễn đạt có đột nhiên tạo ra những câu trả lời hoàn toàn khác nhau không?

### An toàn

Điều gì xảy ra khi có:
- đầu vào kỳ lạ
- các prompt mang tính thao túng
- các tình huống cực đoan?

### Khả năng giải thích (Explainability)

Bạn có thể hiểu được tại sao hệ thống lại làm điều gì đó hay không?

---

## 7. Kiểm thử AI trong thực tế

Kiểm thử AI thường giống với việc làm nghiên cứu hơn là kiểm tra theo kiểu cổ điển.

Bạn làm việc với:
- các giả thuyết
- các quan sát
- so sánh các đầu ra
- nhận diện các mẫu (pattern)

### Ví dụ về các bài kiểm thử AI

- Hệ thống có đưa ra câu trả lời nhất quán không?
- Nó phản ứng thế nào trước thông tin mâu thuẫn?
- Nó có thể xử lý được đầu vào không đầy đủ không?
- Có xuất hiện các mẫu mang tính phân biệt đối xử không?
- Nó có phản ứng an toàn trước hành vi lạm dụng không?

---

## 8. Bài tập thực hành: Điều tra một chức năng AI

Bây giờ, bạn sẽ điều tra một cách phản biện về một hệ thống AI.

### Nhiệm vụ

1. Chọn một chức năng AI:
   - chatbot
   - hệ thống nhận diện hình ảnh
   - hệ thống gợi ý
   - trợ lý AI

2. Nghĩ ra ít nhất 5 bài kiểm thử:
   - 2 kịch bản bình thường
   - 2 trường hợp biên
   - 1 bài kiểm thử về tính công bằng/thiên vị (fairness/bias)

3. Với mỗi bài kiểm thử, hãy ghi lại:
   - đầu vào
   - hành vi mong đợi
   - hành vi thực tế

4. Phân tích:
   - khả năng dự đoán
   - tính nhất quán
   - sự an toàn
   - tính công bằng

---

## 9. Suy ngẫm

Hãy suy nghĩ về:

- Phản ứng nào của AI khiến bạn bất ngờ?
- Khi nào bạn cảm thấy AI không đáng tin cậy?
- Bạn thấy những rủi ro nào đối với người dùng?
- Theo bạn, vai trò nào vẫn thuộc về con người?
- AI đang thay đổi vai trò của tester như thế nào?

> Có lẽ trong tương lai, việc kiểm thử sẽ ngày càng dịch chuyển từ:
>
> "nó có hoạt động không?"
>
> sang:
>
> "nó có hành xử một cách có trách nhiệm, dễ hiểu, và đáng tin cậy không?"
