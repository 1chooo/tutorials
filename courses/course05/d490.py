# Method 1: for loop method
a, b = map(int, input().split())
ans = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        ans += i

print(int(ans))

# Method 2: math formula method
start, end = map(int, input().split())

if start % 2 == 1:
    start += 1
elif start % 2 == 0:
    start = start

if end % 2 == 1:
    end -= 1
elif end % 2 == 0:
    end = end

times = ((end - start) / 2) + 1

ans = (start + end) * times / 2
print(int(ans))
