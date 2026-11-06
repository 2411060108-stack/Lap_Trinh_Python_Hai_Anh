import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_kho_hang as db

DANH_SACH_LOAI = ["Thực phẩm", "Đồ gia dụng", "Thiết bị điện tử", "Hóa chất", "Khác"]
DANH_SACH_KHU_VUC = ["Khu A", "Khu B", "Kho lạnh", "Tầng 2"]

class UngDungKhoHang(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Kho Dự Trữ Hàng Hóa")
        self.geometry("620x530")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Tên hàng hóa:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=32)
        self.o_nhap_ten.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Số lượng:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_so_luong = tk.Entry(khung_nhap, width=32)
        self.o_nhap_so_luong.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Loại hàng:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_loai = ttk.Combobox(khung_nhap, values=DANH_SACH_LOAI, width=29, state="readonly")
        self.chon_loai.current(0)
        self.chon_loai.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Khu vực lưu trữ:").grid(row=3, column=0, sticky="w", pady=5)
        self.chon_khu_vuc = ttk.Combobox(khung_nhap, values=DANH_SACH_KHU_VUC, width=29, state="readonly")
        self.chon_khu_vuc.current(0)
        self.chon_khu_vuc.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm vào kho", command=self.xu_ly_them, bg="#4CAF50", fg="white").grid(row=4, column=0, columnspan=2, pady=10)

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox = tk.Listbox(khung_danh_sach, width=82, height=12)
        self.listbox.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=thanh_cuon.set)

        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Đánh dấu đã hết", command=self.xu_ly_het_hang).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut, text="Xóa mặt hàng", command=self.xu_ly_xoa).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut, text="Thống kê tồn kho", command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach(self):
        self.listbox.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_hang_hoa()
        for hang in self.danh_sach_hien_tai:
            id_h, ten, loai, sl, khu, con = hang
            trang_thai = f"[Còn: {sl}]" if con == 1 and sl > 0 else "[HẾT HÀNG]"
            self.listbox.insert(tk.END, f"{trang_thai} {ten} - {loai} (Vị trí: {khu})")

    def xu_ly_them(self):
        ten = self.o_nhap_ten.get().strip()
        sl_str = self.o_nhap_so_luong.get().strip()
        loai = self.chon_loai.get()
        khu = self.chon_khu_vuc.get()

        if not ten or not sl_str:
            messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập đầy đủ tên hàng và số lượng!")
            return

        try:
            sl = int(sl_str)
            if sl <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Lỗi nhập liệu", "Số lượng phải là một số nguyên dương!")
            return

        db.them_hang_hoa(ten, loai, sl, khu)
        self.o_nhap_ten.delete(0, tk.END)
        self.o_nhap_so_luong.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", f"Đã thêm thành công mặt hàng: {ten}")

    def xu_ly_het_hang(self):
        lua_chon = self.listbox.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một mặt hàng trong danh sách!")
            return
        id_h = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_het_hang(id_h)
        self.tai_lai_danh_sach()

    def xu_ly_xoa(self):
        lua_chon = self.listbox.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một mặt hàng để xóa!")
            return
        id_h = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_hang_hoa(id_h)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        data = db.thong_ke_theo_loai()
        if not data:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu hàng hóa để thống kê!")
            return
        
        cac_loai = [d[0] for d in data]
        so_luong = [d[1] for d in data]

        plt.figure(figsize=(7, 4.5))
        plt.bar(cac_loai, so_luong, color="cornflowerblue")
        plt.title("TỔNG SỐ LƯỢNG HÀNG HÓA THEO LOẠI", fontsize=12, fontweight="bold")
        plt.xlabel("Loại hàng hóa", fontsize=10)
        plt.ylabel("Số lượng tồn kho", fontsize=10)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungKhoHang()
    app.mainloop()