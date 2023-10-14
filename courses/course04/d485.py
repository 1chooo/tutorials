start, end = map(int, input().split())

if start % 2 == 1:
    start += 1
if end % 2 == 1:
    end -= 1

times = ((end - start) / 2) + 1

print(int(times))
