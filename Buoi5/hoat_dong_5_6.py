# ==========================================
# Bài tập 6.2 - Hình thoi sao
# ==========================================

n = 4

# Nửa trên của hình thoi

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Nửa dưới của hình thoi

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))