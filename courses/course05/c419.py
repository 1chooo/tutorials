layer = int(input())

for i in range(1, layer + 1):
    print('_' * (layer - i) + '*' * i)
