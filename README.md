# ImagesDownloadManager (IDM)
Phiên bản mới của XImage. Được xây dựng trên PyQt5, cải tiến một số chức năng, lượt bỏ những chức năng thừa.

# Design

ImagesDownloadManager được thiết kế để cho phép bạn tạo các plugging cắm thẳng vào app chỉ cần implement lại các class cần thiết.
Sau đây là các class **buộc bạn** phải implement, việc còn lại của app cho nhận diện các class trong file setting và vẽ giao diện
tương ứng cho bạn.

## XImage
Đây là một Abstract Class, class kế thừa class này buộc phải implement các phương thức sau:

- getName(): Trả về một **str** là tên của XImage đó (ví dụ: picture.jpg).
- ...

## URLImage
Đây là một Abstract Class, class kế thừa class này buộc phải implement các phương thức sau:

- getXImages(): Phương thức này trả về một list các XImage object. Đây cũng là nơi mà bạn implement trình cào hình ảnh của mình.

- Các method đi kèm tuỳ theo các trang mà bạn cào.
