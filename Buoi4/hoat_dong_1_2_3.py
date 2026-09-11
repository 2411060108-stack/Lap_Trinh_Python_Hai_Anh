#Hoạt động 1: Dictionary cơ bản - khai báo, truy xuất, thêm/sửa/xóa 
# Bài tập 1.1 - Khai báo & truy xuất: 
#sinh_vien = {
 #   "ho_ten": "Nguyen Van A",
  #  "nam_sinh": 2004,
   # "diem_tb": 8.5
#}

#print(sinh_vien["ho_ten"])
#print(sinh_vien.get("diem_tb"))
#print(sinh_vien.get("lop", "Chua co"))

#Bài tập 1.2 - Thêm/sửa/xóa:
#sinh_vien = {
 #   "ho_ten": "dinh Dang Hai Anh",
 #   "nam_sinh": 2006,
 #   "diem_tb": 8.5
#}

#sinh_vien["lop"] = "CNTT01"

#sinh_vien["diem_tb"] = 9.0

#print(sinh_vien)

#diem_cu = sinh_vien.pop("diem_tb")

#print(sinh_vien, "- diem da xoa:", diem_cu)

#sinh_vien.update({
#    "nam_sinh": 2006,
#    "email": "a@example.com"
#})

#print(sinh_vien)

#Hoạt động 2: Duyệt Dictionary bằng for - keys/values/items 
#diem_mon_hoc = {
#    "Toan": 8.0,
 #   "Ly": 7.5,
  #  "Hoa": 9.0,
   # "Van": 6.5
#}

#print("Danh sach mon hoc:")
#for mon in diem_mon_hoc.keys():
#    print(mon)

#print("Danh sach diem:")
#for diem in diem_mon_hoc.values():
 #   print(diem)

#print("Danh sach mon va diem:")
#for mon, diem in diem_mon_hoc.items():
 #   print(f"{mon}: {diem}")

#tong_diem = 0

#for diem in diem_mon_hoc.values():
#    tong_diem = tong_diem + diem

#diem_trung_binh = tong_diem / len(diem_mon_hoc)

#print("Diem trung binh:", round(diem_trung_binh, 2))

#Hoạt động 3: Dictionary comprehension & giới thiệu Set 
#Bài tập 3.1 - Dictionary comprehension: 
#diem_mon_hoc = {
 #   "Toan": 8.0,
  #  "Ly": 7.5,
   # "Hoa": 9.0,
   # "Van": 6.5
#}

#diem_cong_diem = {
 #   mon: round(diem + 0.5, 2)
  #  for mon, diem in diem_mon_hoc.items()
#}

#print(diem_cong_diem)

#ten_mon_viet_hoa = {
 #   mon.upper(): diem
  #  for mon, diem in diem_mon_hoc.items()
#}

#print(ten_mon_viet_hoa)

#Bài tập 3.2 - So sánh nhanh với Set:
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print("Mon hoc chung:", mon_hoc_ky1 & mon_hoc_ky2)

print("Tat ca mon hoc:", mon_hoc_ky1 | mon_hoc_ky2)

print("Mon chi co o hoc ky 1:", mon_hoc_ky1 - mon_hoc_ky2)

