def crout_tridiagonal(a, b, c, d):
    n = len(d)
    l = [0] * n
    u = [0] * (n - 1)
    y = [0] * n
    x = [0] * n

    # Crout 分解
    l[0] = a[0]
    u[0] = b[0] / l[0]
    for i in range(1, n - 1):
        l[i] = a[i] - c[i] * u[i - 1]
        u[i] = b[i] / l[i]
    l[n - 1] = a[n - 1] - c[n - 1] * u[n - 2]

    # 前代 Ly = d
    y[0] = d[0] / l[0]
    for i in range(1, n):
        y[i] = (d[i] - c[i] * y[i - 1]) / l[i]

    # 回代 Ux = y
    x[n - 1] = y[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = y[i] - u[i] * x[i + 1]

    return x

# 三對角系統
a = [3, 3, 3, 3]        # 對角線
b = [-1, -1, -1]        # 上對角線
c = [0, -1, -1, -1]     # 下對角線
d = [2, 3, 4, 1]        # 常數項

solution = crout_tridiagonal(a, b, c, d)
print("\n第三題：Crout 解三對角矩陣")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")
