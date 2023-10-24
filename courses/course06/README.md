# Week06 - 2023-1029

f345
a104

金字塔延伸題目
```py
row = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
```



### [a038. 數字翻轉](https://zerojudge.tw/ShowProblem?problemid=a038)
輸入任意數字，並將其數字全部倒轉

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入一行包含一個整數，且不超過 $2^{31}$ | 輸出翻轉過後的數字 |
| # 1 | 12345 | 54321 |
| # 2 | 5050 | 505 |

#### Hint: 
- 前面有 0 的話應消除

#### [Python 解]
```py
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
```

### [b139. NOIP2005 2.校门外的树](https://zerojudge.tw/ShowProblem?problemid=b139)

某校大门外长度为L的马路上有一排树，每两棵相邻的树之间的间隔都是1米。我们可以把马路看成一个数轴，马路的一端在数轴0的位置，另一端在L的位置；数轴上的每个整数点，即0，1，2，……，L，都种有一棵树。

由于马路上有一些区域要用来建地铁。这些区域用它们在数轴上的起始点和终止点表示。已知任一区域的起始点和终止点的坐标都是整数，区域之间可能有重合的部分。现在要把这些区域中的树（包括区域端点处的两棵树）移走。你的任务是计算将这些树都移走后，马路上还有多少棵树。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 每組输入的第一行有两个整数L（1 <= L <= 10000）和 M（1 <= M <= 100），L代表马路的长度，M代表区域的数目，L和M之间用一个空格隔开。接下来的M行每行包含两个不同的整数，用一个空格隔开，表示一个区域的起始点和终止点的坐标。 | 每組输出包括一行，这一行只包含一个整数，表示马路上剩余的树的数目。 |
| # 1 | 500 3<br>150 300<br>100 200<br>470 471 | 298 |

#### [Python 解]
```py
l, m = map(int, input().split())
a = [1] * (l + 1)
for i in range(m):
    s, e = map(int, input().split())
    for j in range(s, e + 1):
        a[j] = 0

print(sum(a))
```

<div align="center">
    <p>
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course05" target="_blank"><b>👨🏻‍💻 第五週課程</b></a> |
        <!-- <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course06" target="_blank"><b>👨🏻‍💻 第六週課程</b></a> -->
    </p>
</div>


## License

All of these teaching materials are owned by [Hugo ChunHo Lin](https://github.com/1chooo).   
These materials are intended for tutoring purposes. They are open-source to foster a more vibrant Python learning community. We warmly welcome fellow enthusiasts interested in Python to use them. If you use a substantial portion of the source code, please include a link back to this repository.
