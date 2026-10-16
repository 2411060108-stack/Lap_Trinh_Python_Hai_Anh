#Hoạt động 2: Radiobutton – chọn loại tài khoản
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Ví dụ Radiobutton")
cua_so.geometry("300x200")

bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")  # gia tri mac dinh

tk.Label(cua_so, text="Chọn loại tài khoản:", font=("Arial", 12)).pack(pady=10)
tk.Radiobutton(cua_so, text="Cá nhân", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30)
tk.Radiobutton(cua_so, text="Doanh nghiệp", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30)

def xem_loai_tai_khoan():
    nhan_ket_qua.config(text=f"Bạn đã chọn: {bien_loai_tai_khoan.get()}")

tk.Button(cua_so, text="Xác nhận", command=xem_loai_tai_khoan).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()