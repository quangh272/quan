#
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def enhance_image(input_image_path, output_image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(input_image_path)

    # Chuyển đổi ảnh sang độ xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng xử lý tăng cường ánh sáng, ví dụ: sử dụng histeq
    enhanced_image = cv2.equalizeHist(gray_image)

    # Lưu ảnh sau khi tăng cường ánh sáng
    cv2.imwrite(output_image_path, enhanced_image)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        process_image(file_path)

def process_image(input_image_path):
    output_image_path = "enhanced_image.jpg"
    enhance_image(input_image_path, output_image_path)
    display_image(output_image_path)

def display_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(image)

    # Hiển thị ảnh trong cửa sổ mới
    window = tk.Toplevel(root)
    window.title("Enhanced Image")
    label = tk.Label(window, image=photo)
    label.photo = photo
    label.pack()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Image Enhancer")

# Tạo nút để mở hộp thoại chọn tệp
open_button = tk.Button(root, text="Open Image", command=open_file_dialog)
open_button.pack(pady=10)

# Bắt đầu vòng lặp sự kiện
root.mainloop()
