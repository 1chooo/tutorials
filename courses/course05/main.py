print("Hello", end="\n")
print("World", end="---")

print("Hello", end=" ")
print("World")

prices = [100, 200, 300, 400, 500]
for i in prices:
    print("i")

for i in range(0, 5, 1):
    print("i")
# 0
# 1
# 2
# 3
# 4

for i in range(0, 5, 1):
    print(prices[i])
# 100
# 200
# 300
# 400
# 500

for i in range(0, 5, 2):
    print(prices[i])
# 100
# 300
# 500

for i in range(5):
    if i % 2 == 0:
        print(prices[i])
# 100
# 300
# 500