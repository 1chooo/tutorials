"""
Created Date: 2023-10-28
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://zerojudge.tw/ShowProblem?problemid=b139
Status: AC
"""

# L, M = map(int, input().split())
# tree_positions = [1] * (L + 1)      # 0 ~ L

# for i in range(M):
#     start, end = map(int, input().split())
#     for j in range(start, end + 1): # start ~ end
#         tree_positions[j] = 0

# remaining_trees = sum(tree_positions)
# print(remaining_trees)

l, m = map(int, input().split())
a = [1] * (l + 1)
for i in range(m):
    s, e = map(int, input().split())
    for j in range(s, e + 1):
        a[j] = 0

print(sum(a))


