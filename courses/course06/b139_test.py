l, m = map(int, input().split())
a = ["hello"] * (l + 1)
for i in range(m):
    s, e = map(int, input().split())
    for j in range(s, e + 1):
        a[j] = 9

count = 0
for i in a:
    if i == "hello":
        count += 1

print(count)