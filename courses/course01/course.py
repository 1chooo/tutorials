# -*- coding: utf-8 -*-
"""
Date: 2023/09/24
Week: 01
Author: 1chooo
"""

word = 'Hello CIA!'
print(word)

print('Hello CIA!')

area = 5 * 2
print(area)

print(5 * 2)

apple_price = 50

if apple_price > 50:
    print("Do not buy")
elif apple_price < 50:
    print("buy less")
elif apple_price == 50: 
    print("buy equal")

apple_price = 50

if apple_price > 50:
    print("Do not buy")
else:  
    print("buy")

apple_price = 50

if apple_price > 50:
    print("Do not buy")
elif apple_price <= 50:  
    print("buy")


for i in range(0, 10):
    print(i)

for i in range(10):
    print(i)

for i in range(0, 10, 1):
    if i == 5:
        print(i)
        print("舉手發問")
    else:
        print(i)
        print("不舉手發問")

for i in range(100):
    if i == 20:
        print(i)
        print("hi")
    elif i == 27:
        print(i)
        print("hi")
    elif i == 52:
        print(i)
        print("hi")
    else:
        print(i)
        print("no")

apple_price = int(input("請輸入蘋果價格"))
print(apple_price)


print(max(map(int, input().split())))

n = int(input())
if n >= 70:
    print("yes")
else:
    print("no")