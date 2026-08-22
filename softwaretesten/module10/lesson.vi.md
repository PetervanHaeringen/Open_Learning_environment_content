# Module 10 — Kỹ thuật kiểm thử hộp đen (Black-box)

Cho đến giờ, bạn chủ yếu đã học về *việc* bạn kiểm thử. Module này nói về *cách* bạn lựa chọn một cách thông minh *cái gì* cần kiểm thử. Bởi vì bạn không thể nào kiểm thử tất cả mọi thứ — thường thì có vô số đầu vào có thể có. Nghệ thuật ở đây là tìm ra lỗi với một bộ nhỏ, được lựa chọn khôn ngoan, các test case.

---

## 1. Hộp đen: kiểm thử mà không nhìn vào code

Với **kiểm thử hộp đen (black-box)**, bạn coi chương trình như một chiếc hộp đen: bạn biết cái gì đi vào và cái gì cần phải đi ra, nhưng bạn không nhìn vào đoạn code bên trong. Bạn kiểm thử xem hành vi có khớp với những gì đã được hứa hẹn hay không — tức là bản đặc tả (specification).

Điều đối lập với nó là **kiểm thử hộp trắng (white-box)**, trong đó bạn thực sự nhìn vào code bên trong để xác định những gì cần kiểm thử. Cả hai đều có chỗ đứng riêng của mình. Kiểm thử hộp đen mạnh mẽ bởi vì các test case của bạn vẫn tiếp tục hoạt động ngay cả khi đoạn code bên trong được viết lại hoàn toàn — miễn là hành vi đã được hứa hẹn vẫn giữ nguyên.

Trong module này, chúng ta sẽ tìm hiểu bốn kỹ thuật hộp đen thường được sử dụng:
- Phân vùng tương đương (Equivalence classes)
- Phân tích giá trị biên (Boundary value analysis)
- Bảng quyết định (Decision tables)
- Chuyển trạng thái (State transitions)

---

## 2. Phân vùng tương đương: các nhóm được xử lý giống nhau

Hãy tưởng tượng: một trang web chỉ cho phép những người từ 18 tuổi trở lên tạo tài khoản. Độ tuổi có thể dao động từ 0 đến khoảng 120. Vậy bây giờ bạn có phải kiểm thử tất cả 121 độ tuổi hay không? Không.

Ý tưởng đằng sau **phân vùng tương đương** là chương trình xử lý các nhóm đầu vào lớn theo cách hoàn toàn giống nhau. Đối với việc kiểm tra độ tuổi, thực chất chỉ có hai nhóm:
- **quá trẻ**: từ 0 đến 17 (bị từ chối)
- **đủ tuổi**: từ 18 đến 120 (được chấp nhận)

Trong mỗi nhóm, việc bạn chọn giá trị nào không quan trọng — nếu 25 hoạt động tốt, thì 40 rất có thể cũng vậy. Vì vậy, bạn kiểm thử một giá trị cho mỗi nhóm. Ví dụ, tuổi 10 (quá trẻ) và tuổi 30 (đủ tuổi). Hai test case thay vì 121.

Một **phân vùng hợp lệ** chứa các giá trị nên được chấp nhận, một **phân vùng không hợp lệ** chứa các giá trị nên bị từ chối. Quan trọng: đừng quên các phân vùng không hợp lệ. Một chương trình xử lý tốt đầu vào hợp lệ nhưng lại crash với đầu vào không hợp lệ vẫn là một chương trình bị lỗi.

---

## 3. Phân tích giá trị biên: lỗi sống ở các cạnh

Các lập trình viên không mắc phần lớn lỗi ở giữa một nhóm, mà là ở **các ranh giới** giữa các nhóm. Là `>= 18` hay `> 18`? Sự khác biệt một năm đó chính xác là nơi mà mọi thứ thường sai sót.

Vì vậy, **phân tích giá trị biên (BVA)** tập trung vào các cạnh của một phân vùng tương đương. Tại ranh giới độ tuổi 18, các giá trị đáng chú ý là:
- **17** — vừa hơi quá trẻ (giá trị cuối cùng của nhóm bị từ chối)
- **18** — vừa đủ tuổi (giá trị đầu tiên của nhóm được chấp nhận)

Bằng cách kiểm thử chính xác hai giá trị này, bạn bắt được lỗi kinh điển "vừa đúng / vừa không đúng". Một lập trình viên vô tình viết `> 18` thay vì `>= 18` sẽ từ chối oan một người 18 tuổi — và bài kiểm thử của bạn ở tuổi 18 sẽ phát hiện ra điều đó.

Một số tester cũng bao gồm cả giá trị xa hơn một bước nữa (16, 17, 18 hoặc 17, 18, 19) để chắc chắn hơn. Bạn càng bao gồm nhiều giá trị biên, việc kiểm thử càng kỹ lưỡng — nhưng cũng càng tốn nhiều công sức hơn. Đó là một sự đánh đổi.

Lưu ý: phân tích giá trị biên chỉ hoạt động với đầu vào **có thứ tự**, nơi mà "lớn hơn" và "nhỏ hơn" có ý nghĩa — số, ngày tháng, số tiền. Với đầu vào không có thứ tự (như lựa chọn giữa đỏ, xanh lá, hoặc xanh dương), không tồn tại ranh giới nào cả.

---

## 4. Bảng quyết định: khi nhiều điều kiện kết hợp với nhau

Đôi khi hành vi của một chương trình phụ thuộc vào sự kết hợp của nhiều điều kiện. Ví dụ, một cửa hàng trực tuyến áp dụng giảm giá theo các quy tắc sau:
- Là thành viên câu lạc bộ khách hàng? **và**
- Đơn hàng trên 50 euro?

Với hai điều kiện, mỗi điều kiện có thể đúng hoặc sai, sẽ có bốn tổ hợp. Một **bảng quyết định** sắp xếp chúng một cách gọn gàng:

| Là thành viên? | Trên 50 euro? | Giảm giá |
|------|----------------|---------|
| có   | có             | 10%     |
| có   | không          | 5%      |
| không | có            | không có |
| không | không         | không có |

Mỗi cột (hoặc hàng, trong cách sắp xếp này) là một quy tắc riêng biệt mà bạn kiểm thử. Sức mạnh của bảng quyết định là bạn đi qua một cách có hệ thống *tất cả* các tổ hợp — bao gồm cả tổ hợp mà nếu không có nó bạn có thể sẽ quên mất. Hơn nữa, việc xây dựng bảng này buộc bạn phải làm rõ liệu các quy tắc có thực sự đầy đủ và không mâu thuẫn hay không.

Với hai điều kiện có bốn tổ hợp, với ba điều kiện đã là tám, với bốn điều kiện là mười sáu — con số luôn tăng gấp đôi. Với nhiều điều kiện, điều này trở nên không khả thi, và bạn chọn ra những tổ hợp quan trọng nhất dựa trên mức độ rủi ro.

---

## 5. Chuyển trạng thái: hành vi phụ thuộc vào lịch sử

Một số hệ thống hoạt động khác nhau tùy thuộc vào việc chúng đang ở đâu tại thời điểm đó — tức là **trạng thái (state)** của chúng. Hãy nghĩ đến một đèn giao thông đơn giản: đỏ → xanh lá → vàng → đỏ. Hoặc một đơn hàng trực tuyến: *bản nháp → đã đặt hàng → đã giao cho đơn vị vận chuyển → đã giao hàng*.

Với **kiểm thử chuyển trạng thái**, bạn kiểm thử xem hệ thống có chuyển đổi một cách gọn gàng từ trạng thái này sang trạng thái khác khi có điều gì đó xảy ra (một *sự kiện*) hay không, và — quan trọng không kém — liệu nó có *không* chuyển đổi khi gặp các hành động bị cấm hay không.

Ví dụ: một đơn hàng đã được giao cho đơn vị vận chuyển thì không nên có thể hủy được nữa. Đó là một **chuyển đổi không hợp lệ**. Một tester giỏi sẽ thử chính những bước bị cấm đó, bởi vì đó thường là nơi ẩn chứa những lỗi nguy hiểm nhất: một hệ thống vẫn cho phép hủy một gói hàng đã được gửi đi có thể dẫn đến những vấn đề thực sự.

Vì vậy, bạn kiểm thử hai điều:
- các **chuyển đổi hợp lệ**: chúng có xảy ra chính xác hết không?
- các **chuyển đổi không hợp lệ**: chúng có bị từ chối một cách chính xác hết không?

---

## 6. Kỹ thuật nào, khi nào?

Không có kỹ thuật nào là "tốt nhất" — chúng bổ sung cho nhau:
- **Phân vùng tương đương** khi có các nhóm đầu vào được xử lý theo cùng một cách.
- **Phân tích giá trị biên** ngay khi có các ranh giới có thứ tự liên quan (độ tuổi, số tiền, ngày tháng).
- **Bảng quyết định** khi hành vi phụ thuộc vào các tổ hợp điều kiện.
- **Chuyển trạng thái** khi hành vi phụ thuộc vào việc hệ thống hiện đang ở đâu.

Trong thực tế, bạn kết hợp chúng lại với nhau. Đối với việc kiểm tra độ tuổi, bạn sử dụng cả phân vùng tương đương và giá trị biên cùng nhau. Một tester giàu kinh nghiệm cảm nhận được kỹ thuật nào phù hợp với vấn đề nào — và cảm giác đó được phát triển thông qua việc luyện tập.

---

> **Đang trên con đường hướng tới một chứng chỉ?**
> Những kỹ thuật này tạo nên cốt lõi của các chứng chỉ kiểm thử cấp độ nhập môn được công nhận quốc tế, chẳng hạn như ISTQB Foundation. TestGarden chuẩn bị cho bạn về mặt khái niệm; kỳ thi chính thức bạn sẽ tham dự thông qua một tổ chức được công nhận (ở Hà Lan và Bỉ, đó là BNTQB). Hãy trao đổi với người hướng dẫn của bạn và ở nhà xem liệu bước đi này có phù hợp với bạn hay không, và khi nào thì nên thực hiện.
