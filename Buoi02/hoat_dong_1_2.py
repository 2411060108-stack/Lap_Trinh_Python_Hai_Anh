#Hoạt động 1: Nhập/xuất dữ liệu và định dạng chuỗi
#Bài tập 1.1: input() và ép kiểu
#ho_ten = input("Nhap ho ten: ")
#nam_sinh = int(input("Nhap nam sinh: "))
#diem_tb = float(input("Nhap diem trung binh: "))

#Bài tập 1.2 - print() với sep/end:
#print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
#print("Dong 1", end=" | ")
#print("Dong 2")

#Bài tập 1.3: 
#ho_ten = "Đinh Đặng Hải Anh"
#nam_sinh = 2006
#diem_tb = 8.9


# Cách 1: f-string
#print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")


# Cách 2: str.format()
#print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(
#    ho_ten, nam_sinh, diem_tb
#))


# Cách 3: toán tử %
#print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (
#    ho_ten, nam_sinh, diem_tb
#))

# Hoạt động 2: Chú thích & các kiểu trích dẫn
#Bài tập 2.1: Chú thích
# Chu thich mot dong: khai bao thong tin sinh vien

"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""

ho_ten = "Đinh Đặng Hải Anh"  # bien luu ho ten

#Bài tập 2.2: Các kiểu trích dẫn
s1 = 'Xin chao'

s2 = "Ban co khoe khong?"

s3 = """Day la
mot chuoi
nhieu dong..."""

s4 = "Duong dan: C:\\Python\\data"

s5 = r"Duong dan: C:\Python\data"

s6 = "Toi ten la \"Hải Anh\", con ban ten gi?"


# In kết quả
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)



