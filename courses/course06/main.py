row = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

height = 7
num = 1

for i in range(1, height + 1):
    row = ''
    for j in range(i):
        row += str(num) + ' '
        num += 1
    print(row.center(2 * height - 1))

