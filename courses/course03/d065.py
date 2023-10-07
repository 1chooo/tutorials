a, b, c = map(int, input().split())

max_value = a

if b > max_value:
    max_value = b
if c > max_value:
    max_value = c

print(max_value)

# With max() function
a, b, c = map(int, input().split())
print(max(a, b, c))
