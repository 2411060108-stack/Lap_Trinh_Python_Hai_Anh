#Hoạt động 3: Listbox & Combobox – chọn từ danh sách 
#Bài tập 3.2 – Combobox – chọn thành phố

import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Ví dụ Combobox")
cua_so.geometry("300x180")

tk.Label(cua_so, text="Chọn thành phố:").pack(pady=10)

combobox_thanh_pho = ttk.Combobox(cua_so, values=["Hà Nội", "Đà Nẵng", "TP.HCM", "Huế"])
combobox_thanh_pho.current(0)  # chon gia tri dau tien lam mac dinh
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua.config(text=f"Bạn đã chọn: {combobox_thanh_pho.get()}")

tk.Button(cua_so, text="Xác nhận", command=xem_thanh_pho).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()