import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Ví dụ Biến điều khiển")
cua_so.geometry("350x220")

bien_ho_ten = tk.StringVar(value="Đinh Đặng Hải Anh")
bien_tuoi = tk.IntVar(value=18)
bien_dong_y_dieu_khoan = tk.BooleanVar(value=False)

tk.Label(cua_so, text="Họ tên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_ho_ten).grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Tuổi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_tuoi).grid(row=1, column=1, padx=10, pady=10)

tk.Checkbutton(cua_so, text="Đồng ý điều khoản", variable=bien_dong_y_dieu_khoan).grid(
    row=2, column=0, columnspan=2, pady=10
)

def xem_gia_tri_bien():
    print("Họ tên (StringVar):", bien_ho_ten.get())
    print("Tuổi (IntVar):", bien_tuoi.get())
    print("Đồng ý điều khoản (BooleanVar):", bien_dong_y_dieu_khoan.get())
    bien_tuoi.set(bien_tuoi.get() + 1)  # vi du dung set() de cap nhat gia tri

tk.Button(cua_so, text="Xem giá trị biến (và +1 tuổi)", command=xem_gia_tri_bien).grid(
    row=3, column=0, columnspan=2, pady=10
)

cua_so.mainloop()