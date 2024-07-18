# Method 1: for loop method
a, b = map(int, input().split())
ans = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        ans += i

print(int(ans))


