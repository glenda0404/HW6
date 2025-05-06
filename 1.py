import numpy as np

# 原始增廣矩陣資料
A = np.array([
    [1.19, 2.11, -100, 1],
    [14.2, -0.112, 12.2, -1],
    [0, 100, -99.9, 1],
    [15.3, 0.110, -13.1, -1]
], dtype=float)
b = np.array([1.12, 3.44, 2.15, 4.16], dtype=float)

n = len(b)
Ab = np.hstack((A, b.reshape(-1, 1)))  # 增廣矩陣 [A|b]

# Gaussian elimination with partial pivoting
for i in range(n):
    max_row = np.argmax(np.abs(Ab[i:, i])) + i
    if np.abs(Ab[max_row, i]) < 1e-12:
        raise ValueError(f"第 {i+1} 列主元接近零，無法進行消去法")
    Ab[[i, max_row]] = Ab[[max_row, i]]  # Swap rows
    for j in range(i+1, n):
        factor = Ab[j][i] / Ab[i][i]
        Ab[j, i:] -= factor * Ab[i, i:]

# Back substitution
x = np.zeros(n)
for i in range(n-1, -1, -1):
    if Ab[i, i] == 0:
        raise ValueError(f"第 {i+1} 列係數為零，無法回代")
    x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]

print("第一題：Gaussian 消去法（含部分選主元）")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")
