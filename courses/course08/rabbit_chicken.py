"""
Created Date: 2023-11-18
Author: @1chooo (Hugo ChunHo Lin)
Status: AC
"""

find = False

for chicken in range(1, 10):
    rabbit = 9 - chicken  # 因為雞兔總數是9，所以兔子數量等於9減去雞的數量
    legs = chicken * 2 + rabbit * 4

    if (legs == 30 and rabbit > 0):
        find = True
        break

if find:
    print("Chicken: ", chicken)
    print("Rabbit: ", rabbit)
else:
    print("No solution found.")
