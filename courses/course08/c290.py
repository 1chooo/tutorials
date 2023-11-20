"""
Created Date: 2023-11-17
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://zerojudge.tw/ShowProblem?problemid=c290
Status: AC
"""

s = [int(x) for x in input()]   # [2, 6, 3, 5, 4, 1] 同一行有多個輸入
# 263541 not 2 6 3 5 4 1

odd = even = 0

for i in range(len(s)):
    if i % 2 == 0:
        odd += s[i]
    else:
        even += s[i]

print(abs(odd - even))
