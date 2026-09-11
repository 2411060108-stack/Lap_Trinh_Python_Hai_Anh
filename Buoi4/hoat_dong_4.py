#Hoạt động 4: Chuyển đổi kiểu dữ liệu tường minh & ngầm định 
#Bài tập 4.1 - Ép kiểu tường minh: 
chuoi_so = "25"

so = int(chuoi_so)
print(so, type(so))

so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

danh_sach = list((1, 2, 3))

bo_ba = tuple([4, 5, 6])

tap_hop = set([1, 2, 2, 3, 3, 3])

tu_dien = dict([
    ("a", 1),
    ("b", 2)
])

print(danh_sach)
print(bo_ba)
print(tap_hop)
print(tu_dien)

#Bài tập 4.2 - Trường hợp gây lỗi khi ép kiểu:  
#int("abc")
#int("3.14")
#so_hop_le = int(float("3.14"))

#Bài tập 4.3 - Chuyển đổi ngầm định: 
ket_qua = 5 + 2.5

print(ket_qua)
print(type(ket_qua))

ket_qua_2 = "Diem: " + str(8.5)

print(ket_qua_2)
