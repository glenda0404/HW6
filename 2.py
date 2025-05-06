import numpy as np

A = np.array([
    [4, 1, -1, 0],
    [1, 3, -1, 0],
    [-1, -1, 6, 2],
    [0, 0, 2, 5]
], dtype=float)

A_inv = np.linalg.inv(A)

np.set_printoptions(precision=4, suppress=True)
print("\n第二題：A 的反矩陣 A⁻¹ 為：")
print(A_inv)
