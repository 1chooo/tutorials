a = [[0] * 14 for x in range(14)]

for i in range(1, 14):
    for j in range(1, i + 1):
        if i == 1 and j == 1:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]

    t = int(input())
    for i in range(t):
        m, n = map(int, input().split())
        print(a[m][n])
