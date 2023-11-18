"""
Created Date: 2023-11-18
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://tpmso.org/toi/wp-content/uploads/question/202310/ClayPotRice.pdf
Status: AC
"""

T, G, W, E, B = map(int, input().split())

if T < G + W + E + B:
    print(-1)
else:
    print(G + W + E + B)

