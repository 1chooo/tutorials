"""
Created Date: 2023-10-28
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://zerojudge.tw/ShowProblem?problemid=c420
Status: AC
"""

layer = int(input())

for i in range(1, layer + 1):
    print('_' * (layer - i), end='')
    print('*' * ((2 * i) - 1), end='')
    print('_' * (layer - i))
