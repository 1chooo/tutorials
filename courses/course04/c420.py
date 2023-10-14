layer = int(input())

for i in range(1, layer + 1):
    print('_' * (layer - i), end='')
    print('*' * ((2 * i) - 1), end='')
    print('_' * (layer - i))
