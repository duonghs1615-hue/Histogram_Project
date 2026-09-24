[Vietnamese](README.md) | [English](README_EN.md)
# Histogram và Cân bằng Histogram
Xây dựng chương trình minh họa thuật toán Histogram Equalization trên ảnh xám 8-bit bằng Python.
## Chức năng

- Đọc ảnh đầu vào và chuyển sang ảnh xám 8-bit.
- Tự cài đặt các bước tính Histogram, chuẩn hóa Histogram, tính CDF, tạo bảng ánh xạ mức xám và tạo ảnh sau cân bằng.
- Sử dụng `cv2.equalizeHist()` để tạo kết quả đối chiếu với phương pháp thủ công (Manual).
- Tính tỷ lệ **Exact Match** giữa hai ảnh kết quả.
- Hiển thị ảnh đầu vào, hai ảnh kết quả, Histogram trước và sau xử lý, cùng đồ thị CDF trong dashboard 2 × 3.
- Lưu riêng hai ảnh kết quả vào thư mục `results/`.

## Cấu trúc chương trình

```text
Histogram_Project/
├── main.py                    # Đọc ảnh và điều khiển chương trình
├── histogram_equalization.py  # Cài đặt thuật toán và so sánh kết quả
├── visualization.py           # Hiển thị ảnh, Histogram và CDF
├── images/                    # Ảnh đầu vào
└── results/                   # Ảnh kết quả sau xử lý
```

## Cài đặt

Máy cần cài Python. Mở Terminal tại thư mục dự án và cài các thư viện:

```powershell
py -m pip install -r requirements.txt
```

Nếu chưa tải mã nguồn, có thể lấy dự án bằng Git:

```powershell
git clone https://github.com/duonghs1615-hue/Histogram_Project.git
cd Histogram_Project
```

## Chạy chương trình

Đặt ảnh cần xử lý trong thư mục `images/`, sau đó chạy:

```powershell
py main.py images/image1.jpg
```

Có thể thay đường dẫn bằng ảnh khác, ví dụ:

```powershell
py main.py images/image3.tif
```

Nếu chạy `py main.py` mà không truyền đường dẫn, chương trình sử dụng ảnh mặc định được khai báo trong biến `DEFAULT_IMAGE_PATH` của `main.py`.

## Kết quả

Chương trình in thông tin ảnh và tỷ lệ Exact Match trên Terminal, đồng thời mở cửa sổ dashboard để quan sát kết quả. Hai ảnh sau xử lý được lưu với tên:

```text
results/<ten_anh>_manual.png
results/<ten_anh>_opencv.png
```

Dashboard chỉ được hiển thị trên màn hình, không tự động lưu thành ảnh.

**Lưu ý:** Exact Match bằng 100% nghĩa là hai ảnh kết quả giống nhau tại mọi pixel; chỉ số này không khẳng định ảnh sau xử lý đẹp hơn ảnh ban đầu.

## Mã nguồn

Phần Histogram Equalization thủ công được thực hiện trong `histogram_equalization.py`. Hàm `cv2.equalizeHist()` chỉ được sử dụng để đối chiếu kết quả, không thay thế các bước cài đặt thủ công.
