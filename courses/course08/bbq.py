"""
Created Date: 2023-11-18
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://tpmso.org/toi/wp-content/uploads/question/202310/BBQ.pdf
"""

N, M, X, Y = map(int, input().split())

# 初始化各類肉串的數量為 0
pork_count = 0
beef_count = 0

# 檢查每一種可能的情況，計算吃了多少串豬肉串和牛肉串
for i in range(N + 1):
    for j in range(M + 1):
        total_cost = i * X + j * Y
        if total_cost == N and (i + j) == M:
            pork_count = i
            beef_count = j
            break

# 判斷是否有解，並輸出結果
if pork_count + beef_count == M and (pork_count * X + beef_count * Y) == N:
    print(pork_count, beef_count)
else:
    print(-1, -1)

