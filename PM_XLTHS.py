#
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plot_signal(data):
    plt.figure(figsize=(8, 4))
    plt.plot(data)
    plt.title("Biểu đồ tín hiệu số")
    plt.xlabel("Thời gian")
    plt.ylabel("Amplitude")
    plt.show()

def apply_fourier_transform(data):
    fft_result = np.fft.fft(data)
    magnitude = np.abs(fft_result)
    frequency = np.fft.fftfreq(len(data))
    plot_signal(magnitude)

def apply_filter(data, cutoff_frequency):
    b, a = signal.butter(4, cutoff_frequency, fs=1)
    filtered_data = signal.lfilter(b, a, data)
    plot_signal(filtered_data)

def get_user_input():
    input_data = entry.get()
    data = [float(x) for x in input_data.split()]
    return data

def process_data():
    data = get_user_input()
    plot_signal(data)

app = tk.Tk()
app.title("Phần mềm Xử lí Tín hiệu Số")

entry_label = tk.Label(app, text="Nhập dãy số tín hiệu (cách nhau bởi khoảng trắng):")
entry_label.pack()

entry = tk.Entry(app)
entry.pack()

process_button = tk.Button(app, text="Xử lí Tín hiệu", command=process_data)
process_button.pack()

fourier_button = tk.Button(app, text="Biến đổi Fourier", command=lambda: apply_fourier_transform(data))
fourier_button.pack()

filter_button = tk.Button(app, text="Lọc Tín hiệu", command=lambda: apply_filter(data, 0.1))
filter_button.pack()

app.mainloop()
