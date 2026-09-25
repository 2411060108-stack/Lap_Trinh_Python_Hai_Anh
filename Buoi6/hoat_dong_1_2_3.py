# Bài tập 3.2 – **kwargs

def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")

    for khoa, gia_tri in kwargs.items():
        print(f" {khoa}: {gia_tri}")


print("\n===== BÀI TẬP 3.2 =====")

in_thong_tin(
    "Nguyen Truc Linh",
    20,
    lop="CNTT01",
    que_quan="Ha Noi"
)

in_thong_tin(
    "Tran Thi Ngoc Anh",
    21,
    email="tranthingocanh@gmail.com"
)