import requests

# Bai tap 5.2: Lay ty gia USD sang VND
print("\n===== BAI TAP 5.2 =====")

url_ty_gia = "https://open.er-api.com/v6/latest/USD"

try:
    response = requests.get(url_ty_gia, timeout=15)

    if response.status_code == 200:
        du_lieu = response.json()

        ty_gia_vnd = du_lieu["rates"]["VND"]

        print(f"1 USD = {ty_gia_vnd:,.0f} VND")

    else:
        print("Khong lay duoc ty gia:", response.status_code)

except requests.RequestException as e:
    print("Loi ket noi:", e)