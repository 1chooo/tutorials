"""
Created Date: 2023-11-18
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://tpmso.org/toi/wp-content/uploads/question/202310/Supermarket.pdf
Status: AC
"""

A, B, C = map(int, input().split())

times = []
for i in range(3):
    customers = list(map(int, input().split()))
    total_time = sum(customers) * 3 + (len(customers) - 1) * 2
    times.append(total_time)

min_time = min(times)
min_index = times.index(min_time) + 1

print(min_index, min_time)

