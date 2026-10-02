# Danh sach sinh vien ban dau
danh_sach_sinh_vien = [
    {
        "ma_sv": "SV001",
        "ho_ten": "Nguyen Van An",
        "lop": "CNTT01",
        "diem_tb": 8.0,
        "xep_loai": "Gioi"
    },
    {
        "ma_sv": "SV002",
        "ho_ten": "Tran Thi Binh",
        "lop": "CNTT02",
        "diem_tb": 7.2,
        "xep_loai": "Kha"
    },
    {
        "ma_sv": "SV003",
        "ho_ten": "Le Van Cuong",
        "lop": "CNTT01",
        "diem_tb": 5.8,
        "xep_loai": "Trung binh"
    },
    {
        "ma_sv": "SV004",
        "ho_ten": "Pham Thi Dung",
        "lop": "CNTT03",
        "diem_tb": 9.0,
        "xep_loai": "Xuat sac"
    }
]


# Ham xep loai sinh vien
def xep_loai_sinh_vien(diem_tb):
    if diem_tb >= 8.5:
        return "Xuat sac"
    elif diem_tb >= 7.0:
        return "Gioi"
    elif diem_tb >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"


# Ham hien thi danh sach sinh vien
def hien_thi_danh_sach():
    print("\n" + "=" * 80)
    print(f"{'Ma SV':<10}{'Ho ten':<25}{'Lop':<12}{'Diem TB':<12}{'Xep loai':<15}")
    print("-" * 80)

    for sinh_vien in danh_sach_sinh_vien:
        print(
            f"{sinh_vien['ma_sv']:<10}"
            f"{sinh_vien['ho_ten']:<25}"
            f"{sinh_vien['lop']:<12}"
            f"{sinh_vien['diem_tb']:<12}"
            f"{sinh_vien['xep_loai']:<15}"
        )

    print("=" * 80)


# Ham tim sinh vien theo ma
def tim_sinh_vien_theo_ma(ma_sv):
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien["ma_sv"] == ma_sv:
            return sinh_vien

    return None


# Ham them sinh vien
def them_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai, khong the them.")
        return

    sinh_vien = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "lop": lop,
        "diem_tb": diem_tb,
        "xep_loai": xep_loai_sinh_vien(diem_tb)
    }

    danh_sach_sinh_vien.append(sinh_vien)

    print(f"-> Da them sinh vien {ma_sv} thanh cong.")


# Ham tim kiem sinh vien
def tim_kiem_sinh_vien(ma_sv):
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    print("\nTHONG TIN SINH VIEN:")
    print(f"Ma sinh vien: {sinh_vien['ma_sv']}")
    print(f"Ho ten: {sinh_vien['ho_ten']}")
    print(f"Lop: {sinh_vien['lop']}")
    print(f"Diem trung binh: {sinh_vien['diem_tb']}")
    print(f"Xep loai: {sinh_vien['xep_loai']}")


# Ham sua thong tin sinh vien
def sua_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    sinh_vien["ho_ten"] = ho_ten
    sinh_vien["lop"] = lop
    sinh_vien["diem_tb"] = diem_tb
    sinh_vien["xep_loai"] = xep_loai_sinh_vien(diem_tb)

    print(f"-> Da sua thong tin sinh vien {ma_sv} thanh cong.")


# Ham xoa sinh vien
def xoa_sinh_vien(ma_sv):
    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    danh_sach_sinh_vien.remove(sinh_vien)

    print(f"-> Da xoa sinh vien {ma_sv} thanh cong.")


# Ham thong ke sinh vien
def thong_ke_sinh_vien():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien dang rong.")
        return

    tong_sinh_vien = len(danh_sach_sinh_vien)

    tong_diem = 0

    so_xuat_sac = 0
    so_gioi = 0
    so_trung_binh = 0
    so_yeu = 0

    for sinh_vien in danh_sach_sinh_vien:
        tong_diem += sinh_vien["diem_tb"]

        if sinh_vien["xep_loai"] == "Xuat sac":
            so_xuat_sac += 1
        elif sinh_vien["xep_loai"] == "Gioi":
            so_gioi += 1
        elif sinh_vien["xep_loai"] == "Trung binh":
            so_trung_binh += 1
        else:
            so_yeu += 1

    diem_trung_binh = tong_diem / tong_sinh_vien

    print("\nTHONG KE SINH VIEN")
    print("-" * 40)
    print(f"Tong so sinh vien: {tong_sinh_vien}")
    print(f"Diem trung binh: {diem_trung_binh:.2f}")
    print(f"So sinh vien Xuat sac: {so_xuat_sac}")
    print(f"So sinh vien Gioi: {so_gioi}")
    print(f"So sinh vien Trung binh: {so_trung_binh}")
    print(f"So sinh vien Yeu: {so_yeu}")


# Ham nhap so thuc an toan
def nhap_diem():
    while True:
        try:
            diem = float(input("Nhap diem trung binh: "))

            if 0 <= diem <= 10:
                return diem

            print("-> Diem phai nam trong khoang tu 0 den 10.")

        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so.")


# Ham hien thi menu
def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach sinh vien")
    print("2. Tim kiem sinh vien")
    print("3. Them sinh vien")
    print("4. Sua thong tin sinh vien")
    print("5. Xoa sinh vien")
    print("6. Thong ke sinh vien")
    print("0. Thoat chuong trinh")


# Ham chay chuong trinh
def chay_chuong_trinh():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()

        elif lua_chon == "2":
            ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()
            tim_kiem_sinh_vien(ma_sv)

        elif lua_chon == "3":
            ma_sv = input("Nhap ma sinh vien moi: ").strip().upper()
            ho_ten = input("Nhap ho ten sinh vien: ").strip().title()
            lop = input("Nhap lop: ").strip().upper()
            diem_tb = nhap_diem()

            them_sinh_vien(ma_sv, ho_ten, lop, diem_tb)

        elif lua_chon == "4":
            ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()
            ho_ten = input("Nhap ho ten moi: ").strip().title()
            lop = input("Nhap lop moi: ").strip().upper()
            diem_tb = nhap_diem()

            sua_sinh_vien(ma_sv, ho_ten, lop, diem_tb)

        elif lua_chon == "5":
            ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
            xoa_sinh_vien(ma_sv)

        elif lua_chon == "6":
            thong_ke_sinh_vien()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


# Chay chuong trinh
if __name__ == "__main__":
    chay_chuong_trinh()