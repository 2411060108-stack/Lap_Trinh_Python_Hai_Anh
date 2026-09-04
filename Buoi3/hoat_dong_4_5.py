#Hoạt động 4: Tuple – khai báo, bất biến, unpacking
#Bài tập 4.1 – Khai báo & tính bất biến
#toa_do = (3, 5)
#print(toa_do, type(toa_do))

# Thu gan lai:
#toa_do[0] = 10

#Bài tập 4.2: – Unpacking
#x, y = toa_do

#print("x =", x, "- y =", y)

# Đổi giá trị 2 biến bằng unpacking
#a, b = 10, 20

#a, b = b, a

#print("a =", a, "- b =", b)

#Bài tập 4.3 – Trả về nhiều giá trị từ một biểu thức
#c, d = 17, 5

#thuong_du = divmod(c, d)

#thuong, du = thuong_du

#print(f"{c} / {d} thuong {thuong}, du {du}")

#Hoạt động 5: Vận dụng Tuple – Tọa độ điểm & khoảng cách
import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print(f"Khoang cach giua {diem_a} va {diem_b}: {round(khoang_cach, 2)}")

# Tính khoảng cách từ từng điểm đến gốc tọa độ (0, 0)
cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    khoang_cach = math.sqrt(x ** 2 + y ** 2)
    print(f"Khoang cach tu {diem} den goc toa do (0, 0): {round(khoang_cach, 2)}")