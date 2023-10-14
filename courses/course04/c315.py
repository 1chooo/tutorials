x = 0
y = 0

times = int(input())

for i in range(times):
    a, b = map(int, input().split())

    if a == 0:
        y = y + b
    elif a == 1:
        x = x + b
    elif a == 2:
        y = y - b
    elif a == 3:
        x = x - b

print(x, y)
