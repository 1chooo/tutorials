# method 1
a = list(input())
a.reverse()
ans = ''.join(a)

all_zeros = True

for char in ans:
    if char != '0':
        all_zeros = False
        break

if all_zeros:
    print(0)
else:
    for i in range(len(ans)):
        if ans[i] != '0':
            print(ans[i:])
            break


# method 2
inStr = input()
inStrLen = len(inStr)
mark = 0
pivot = inStrLen
i = inStrLen

while mark != 1:
    i -= 1
    if i == 0:
        break
    if inStr[i] != '0':
        mark = 1
    pivot = i

if mark == 0:
    print(0)
else:
    for j in range(pivot, -1, -1):
        print(inStr[j], end='')
    print()

print(int(''.join(reversed(input()))))
