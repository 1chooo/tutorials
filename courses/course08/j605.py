"""
Created Date: 2023-11-17
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://zerojudge.tw/ShowProblem?problemid=j605
Status: AC
"""

n = int(input())
t = [0] * n
s = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    t[i] = x
    s[i] = y

# 最高分 - 總提交次數 - 總嚴重錯誤次數 * 2
ans = max(s) - n - s.count(-1) * 2

# 若計算出來的分數為負數則計為 0。
if ans < 0:
    ans = 0

# 輸出總分和第一次獲得最高分的時間點。
print(ans, t[s.index(max(s))])
