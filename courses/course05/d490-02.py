# Method 2: math formula method
start, end = map(int, input().split())

if start % 2 == 1:
    start += 1
elif start % 2 == 0:
    pass

if end % 2 == 1:
    end -= 1
elif end % 2 == 0:
    pass

times = ((end - start) / 2) + 1

ans = (start + end) * times / 2
print(int(ans))
