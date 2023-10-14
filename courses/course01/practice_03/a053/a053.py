# Problem link: https://zerojudge.tw/ShowProblem?problemid=a053

inNum = int(input())

if inNum <= 10:
    print(6 * inNum)
elif inNum >= 11 and inNum <= 20:
    print(60 + (inNum - 10) * 2)
elif inNum >= 21 and inNum <= 40:
    print(80 + (inNum - 20))
else:
    print(100)
