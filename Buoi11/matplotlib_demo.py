import pandas as pd
import matplotlib.pyplot as plt

# Doc du lieu
df = pd.read_csv(r"D:\Baitap Python\Buoi11\diem_sinh_vien.csv")

# Bai tap 3.2: Bieu do duong
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize=(6, 4))

plt.plot(
    lan_kiem_tra,
    diem_qua_cac_lan,
    marker="o",
    color="green"
)

plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")

plt.savefig("bieu_do_duong.png")
plt.show()