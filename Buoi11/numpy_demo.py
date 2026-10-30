import numpy as np

# Danh sach diem Python
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]

# Chuyen danh sach thanh mang NumPy
diem_array = np.array(diem_list)

# In kieu du lieu
print("Kieu cua list:", type(diem_list))
print("Kieu cua array:", type(diem_array))

# Cong them 0.5 diem cho toan bo mang
diem_cong_them = diem_array + 0.5
print("Diem sau khi cong:", diem_cong_them)

# Cong diem bang list comprehension
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("Diem cong bang list:", diem_cong_them_list)

# Tinh toan thong ke
print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))

# Tao ma tran
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])

print("Ma tran:\n", ma_tran)
print("Kich thuoc:", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)