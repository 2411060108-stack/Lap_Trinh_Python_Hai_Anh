import sqlite3

TEN_FILE_CSDL = "kho_hang.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
    CREATE TABLE IF NOT EXISTS hang_hoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_hang TEXT NOT NULL,
        loai_hang TEXT NOT NULL,
        so_luong INTEGER NOT NULL DEFAULT 1,
        khu_vuc TEXT NOT NULL,
        con_hang INTEGER NOT NULL DEFAULT 1
    )
    """)
    
   
    con_tro.execute("SELECT COUNT(*) FROM hang_hoa")
    if con_tro.fetchone()[0] == 0:
        du_lieu_mau = [
            ('Gạo Tám Thái', 'Thực phẩm', 50, 'Kho lạnh'),
            ('Nước lau sàn', 'Hóa chất', 12, 'Khu A'),
            ('Bóng đèn LED', 'Thiết bị điện tử', 30, 'Tầng 2'),
            ('Nồi cơm điện', 'Đồ gia dụng', 5, 'Khu B')
        ]
        con_tro.executemany(
            "INSERT INTO hang_hoa (ten_hang, loai_hang, so_luong, khu_vuc, con_hang) VALUES (?, ?, ?, ?, 1)",
            du_lieu_mau
        )
        
    ket_noi.commit()
    ket_noi.close()

def them_hang_hoa(ten_hang, loai_hang, so_luong, khu_vuc):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO hang_hoa (ten_hang, loai_hang, so_luong, khu_vuc, con_hang) VALUES (?, ?, ?, ?, 1)",
        (ten_hang, loai_hang, so_luong, khu_vuc)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_hang_hoa():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_hang, loai_hang, so_luong, khu_vuc, con_hang FROM hang_hoa ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_hang_hoa(id_hang):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM hang_hoa WHERE id = ?", (id_hang,))
    ket_noi.commit()
    ket_noi.close()

def danh_dau_het_hang(id_hang):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE hang_hoa SET con_hang = 0, so_luong = 0 WHERE id = ?", (id_hang,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_loai():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT loai_hang, SUM(so_luong) FROM hang_hoa WHERE con_hang = 1 GROUP BY loai_hang")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua