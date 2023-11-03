import tkinter as tk
import math

def tinh_dien_tich_chu_vi_hinh_tron():
    ban_kinh = float(entry_ban_kinh.get())
    dien_tich = math.pi * ban_kinh ** 2
    chu_vi = 2 * math.pi * ban_kinh
    hien_thi_ket_qua(f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}")

def tinh_dien_tich_chu_vi_hinh_vuong():
    canh = float(entry_canh.get())
    dien_tich = canh ** 2
    chu_vi = 4 * canh
    hien_thi_ket_qua(f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}")

def tinh_dien_tich_chu_vi_hinh_chu_nhat():
    chieu_dai = float(entry_chieu_dai.get())
    chieu_rong = float(entry_chieu_rong.get())
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
    hien_thi_ket_qua(f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}")

def tinh_dien_tich_chu_vi_hinh_tam_giac():
    a = float(entry_canh_a.get())
    b = float(entry_canh_b.get())
    c = float(entry_canh_c.get())
    s = (a + b + c) / 2
    dien_tich = math.sqrt(s * (s - a) * (s - b) * (s - c))
    chu_vi = a + b + c
    hien_thi_ket_qua(f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}")

def hien_thi_ket_qua(ket_qua):
    label_ket_qua.config(text=ket_qua)

def xoa_ket_qua():
    label_ket_qua.config(text="")

app = tk.Tk()
app.title("Tính diện tích và chu vi các hình")

label_hinh_tron = tk.Label(app, text="Hình tròn")
label_hinh_tron.pack()

label_ban_kinh = tk.Label(app, text="Nhập bán kính:")
label_ban_kinh.pack()

entry_ban_kinh = tk.Entry(app)
entry_ban_kinh.pack()

button_tinh_hinh_tron = tk.Button(app, text="Tính diện tích và chu vi hình tròn", command=tinh_dien_tich_chu_vi_hinh_tron)
button_tinh_hinh_tron.pack()

label_hinh_vuong = tk.Label(app, text="Hình vuông")
label_hinh_vuong.pack()

label_canh = tk.Label(app, text="Nhập cạnh:")
label_canh.pack()

entry_canh = tk.Entry(app)
entry_canh.pack()

button_tinh_hinh_vuong = tk.Button(app, text="Tính diện tích và chu vi hình vuông", command=tinh_dien_tich_chu_vi_hinh_vuong)
button_tinh_hinh_vuong.pack()

label_hinh_chu_nhat = tk.Label(app, text="Hình chữ nhật")
label_hinh_chu_nhat.pack()

label_chieu_dai = tk.Label(app, text="Nhập chiều dài:")
label_chieu_dai.pack()

entry_chieu_dai = tk.Entry(app)
entry_chieu_dai.pack()

label_chieu_rong = tk.Label(app, text="Nhập chiều rộng:")
label_chieu_rong.pack()

entry_chieu_rong = tk.Entry(app)
entry_chieu_rong.pack()

button_tinh_hinh_chu_nhat = tk.Button(app, text="Tính diện tích và chu vi hình chữ nhật", command=tinh_dien_tich_chu_vi_hinh_chu_nhat)
button_tinh_hinh_chu_nhat.pack()

label_hinh_tam_giac = tk.Label(app, text="Hình tam giác")
label_hinh_tam_giac.pack()

label_canh_a = tk.Label(app, text="Nhập cạnh a:")
label_canh_a.pack()

entry_canh_a = tk.Entry(app)
entry_canh_a.pack()

label_canh_b = tk.Label(app, text="Nhập cạnh b:")
label_canh_b.pack()

entry_canh_b = tk.Entry(app)
entry_canh_b.pack()

label_canh_c = tk.Label(app, text="Nhập cạnh c:")
label_canh_c.pack()

entry_canh_c = tk.Entry(app)
entry_canh_c.pack()

button_tinh_hinh_tam_giac = tk.Button(app, text="Tính diện tích và chu vi hình tam giác", command=tinh_dien_tich_chu_vi_hinh_tam_giac)
button_tinh_hinh_tam_giac.pack()

button_xoa_ket_qua = tk.Button(app, text="Xoá kết quả", command=xoa_ket_qua)
button_xoa_ket_qua.pack()

label_ket_qua = tk.Label(app, text="")
label_ket_qua.pack()

app.mainloop()
