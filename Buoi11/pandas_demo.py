import pandas as pd

# Doc file CSV
df = pd.read_csv(r"D:\Baitap Python\Buoi11\diem_sinh_vien.csv")

# Bai tap 2.3: Tinh diem trung binh tung sinh vien
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)

print("\nDiem trung binh tung sinh vien:")
print(diem_tb_sv)

# Loc sinh vien dat
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]

# Loc sinh vien khong dat
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)

print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)