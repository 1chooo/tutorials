a_list = map(int, input('請輸入兩個數字：').split())

print(type(a_list).__name__)

import math
a = 1.23456789
print(math.floor(a))

apple_price = int(input())

if apple_price > 50:
    print("Do not buy")
elif apple_price < 50:
    print("buy less")
elif apple_price == 50: 
    print("buy equal")


print(5 // 2)
print(5.0 // 2)
print(5 // 2.0)
print(5.0 // 2.0)

print(5 % 2)
print(5.0 % 2)
print(5 % 2.0)
print(5.0 % 2.0)

a = 10
b = 3
c = 1
x = 1

print(a * x ** 2 + b * x + c)

print(2 * 1 ** 2 + 3 * 1 + 1)

probability = 0.123456789

print(probability)         # 0.123456789
print('{}'.format(probability))
print(f'{probability}')     # 0.12

print(f'{probability:.2f}')     # 0.12
print('%.2f' % probability)     # 0.12

probability_str = str(probability)
print(probability_str[:4])
probability = float(probability_str)
print(type(probability))

probability = 0.123456789
print(round(probability, 4))   # 0.12

num = 450.2389
print(f"{num:.2f}")
print('%.2f' % num)     # 0.12
print(round(num, 2))

name = input('請輸入你的名字：')

print(f'你好，{name}')

a, b = map(int, input('請輸入兩個數字：').split())
c = a + b
print(f'計算結果：{c}')

a, b, c = map(int, input().split())
print(a, b, c)

a = '1 2 3'
print(type(a))
b = a.split()
print(type(b))
print(b)        # ['Hello', 'World']

a = '1 2 3'
print(a.split())