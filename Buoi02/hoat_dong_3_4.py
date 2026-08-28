#Hoạt động 3: Number - int, float, complex & hàm built-in
#Bài tập 3.1:Các kiểu số & chuyển đổi:
#so_nguyen = 15
#so_thuc = 4.2
#so_phuc = 3 + 4j

#print(type(so_nguyen), type(so_thuc), type(so_phuc))

#print(float(so_nguyen))   # ep int -> float
#print(int(so_thuc))       # ep float -> int (cat phan thap phan)

#Bài tập 3.2: Các hàm built-in

#a = -7
#b = 2.6789
#c, d = 17, 5

#print(abs(a))             # gia tri tuyet doi
#print(round(b))           # lam tron
#print(round(b, 2))        # lam tron 2 chu so thap phan
#print(pow(c, 2))          # c mu 2
#print(divmod(c, d))       # thuong va du dang tuple

#bài tập 3.3:
#import math

#a, b, c = 1, -3, 2

#delta = b ** 2 - 4 * a * c

#x1 = (-b + math.sqrt(delta)) / (2 * a)
#x2 = (-b - math.sqrt(delta)) / (2 * a)

#print(f"Delta = {delta}")
#print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

#Hoạt động 4:
#Bài tập 4.1:
#cau = "Lap trinh Python rat thu vi"

#print(cau[0])
#print(cau[-1])
#print(cau[4:10])
#print(cau[:8])
#print(cau[11:])
#print(cau[::-1])

# Kiem tra palindrome
#print(cau == cau[::-1])

#Bài tập 4.2:
#ten = "Tải Anh"

# ten[0] = "T"   # Neu bo comment dong nay se xuat hien TypeError

#ten_moi = "H" + ten[1:]

#print(ten_moi)

#Bài tập 4.3:
cau = "  Toi dang Hoc Python rat vui  "

print(cau.strip())
print(cau.strip().upper())
print(cau.strip().lower())
print(cau.strip().replace("Hoc", "hoc"))
print(cau.strip().split())
print(len(cau.strip()))
print(cau.count("o"))
print(cau.find("Python"))
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "rat", "thu", "vi"]))