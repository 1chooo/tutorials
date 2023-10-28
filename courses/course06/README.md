# Week06 - 2023-1029

### [`c420` Bert的三角形 (3)](https://zerojudge.tw/ShowProblem?problemid=c420)
Bert 有天騎著海豚到了埃及，看到了金字塔不經意的發出『 哇～～ 』現在 Bert 想請你用程式記下金字塔的樣子～～現在有一種 n 層的三金字塔，定義如下:

第 i 層要有相對數量的 " * "，請注意要像金字塔一樣向中間對齊

請你寫個程式幫幫 Bert ~~

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 單筆輸入~~<br>輸入只有一個整數 n (1 <= n <= 100)<br>n 保證為奇數 | 輸出整個三角形~~<br>因為空格不好辨識，請以"_" 代替 ~~ |
| # 1 | 3 | \_\_\*\_\_<br>\_\*\*\*_<br>\*\*\*\*\* |

#### [Python 解]

```py
layer = int(input())

for i in range(1, layer + 1):
    print('_' * (layer - i), end='')
    print('*' * ((2 * i) - 1), end='')
    print('_' * (layer - i))
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

### [f345. 新手練習題—陣列](https://zerojudge.tw/ShowProblem?problemid=f345)

本題是給新手練習陣列使用的（其實是出給學弟妹練習陣列用的）。  
題目很簡單，給你一堆數字，只要將它們的順序倒過來輸出就可以了。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 每個測資點僅單筆輸入。<br>第一行有一個正整數N，表示接下來有N個數字。（N<=10^6）<br>第二行有N個數字Pi。（Pi的大小在int變數型別的範圍內，也就是-2147483648~2147483647） | 請將輸入的N個數字順序顛倒後輸出並以空白隔開。 |
| # 1 | 5<br>1 2 3 4 5 | 5 4 3 2 1 |
| # 2 | 4<br>100 250 -200 450 | 450 -200 250 100 |

- 測資資訊：
  - 記憶體限制： 512 MB
  - 公開 測資點#0 (11%): 10.0s , <1K
  - 公開 測資點#1 (11%): 10.0s , <1K
  - 公開 測資點#2 (11%): 10.0s , <1M
  - 公開 測資點#3 (11%): 10.0s , <1M
  - 公開 測資點#4 (11%): 10.0s , <1M
  - 公開 測資點#5 (11%): 10.0s , <1M
  - 公開 測資點#6 (11%): 10.0s , <1M
  - 公開 測資點#7 (11%): 10.0s , <50M
  - 公開 測資點#8 (12%): 10.0s , <50M

> Hint ：
> 可以使用 `<algorithm>` 函式庫裡面的 reverse 把陣列內容反轉後輸出；也可以直接從陣列的尾端跑到首端逐一輸出；也歡迎高手直接調整 stdin 的存取位置來解題！

#### [Python 解]
```py
n = int(input())
a = [int(x) for x in input().split()]
# a = list(map(int, input().split()))

for i in a[::-1]:
    print(i, end=" ")

print()
```

### [a104. 排序](https://zerojudge.tw/ShowProblem?problemid=a104)

幫我排個數字謝謝QQ

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 有多筆測資以EOF為結束<br>第一行有一個正整數n(1<=n<=1000)，代表有幾個數字要請你幫忙排<br>第二行有n個可以用int儲存的正整數 | 輸出n個已由小到大排序好的正整數 |
| # 1 | 6<br>7 9 0 4 1 8<br>8<br>1 9 9 0 0 9 2 8 | 0 1 4 7 8 9<br>0 0 1 2 8 9 9 9 |

#### [Python 解]

```py
while True:
    try:
        n = int(input())
        a = [int(x) for x in input().split()]
        a.sort()
        print(*a)
    except EOFError:
        break
```

如果寫 `print(a)` 將會 print 出整個 list 在 python 會把 `[]` 以及
 `,` 印出來，但是我們如果只要 print 出 list 內容，可以使用 `*` 來 unpack list 內容，如此一來就可以 print 出 list 內容。


### [d583. 幼稚的企鵝](https://zerojudge.tw/ShowProblem?problemid=d583)

小企鵝總是天真可愛，但擺脫不了幾分幼稚。
現在企鵝幼稚園的企鵝老師要小企鵝任意排隊。
而小企鵝們卻很堅持要照老師給他們的座號來排隊，
偏偏有的小企鵝就是會忘記自己的座號亂排，
於是可以想見的是一群短鳥喙的小企鵝爭吵互啄的景象了…

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 本題有2個測資點，每個50分，每個測資點有多組測資。<br>每組測資的第一行有整數n(1<=n<=100000)代表有幾隻企鵝。<br>第二行則有n個數字的數列代表每隻企鵝的座號，並且座號必定有1~n不重覆。 | 請由小到大輸出已經排序的數列。 |
| # 1 | 10<br>9 5 10 4 3 6 1 2 7 8<br>30<br>30 29 28 27 26 25 10 11 12 13 15 14 16 19 18 17 20 24 23 22 21 8 9 7 6 5 3 4 2 1 | 1 2 3 4 5 6 7 8 9 10<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 |

#### [Python 解]

```py
while True:
    try:
        n = int(input())
        a = [int(x) for x in input().split()]
        a.sort()
        print(*a)
    except EOFError:
        break
```

### [d074. 電腦教室](https://zerojudge.tw/ShowProblem?problemid=d074)

蝸牛老師在一所優質高中擔任電腦老師，在學校裡有一間他專用的電腦教室。最近學校有一筆經費要幫這個電腦教室更新電腦。學校的原則是，每個上課的學生都要有自己的電腦，但是不希望購買多餘的電腦。給你蝸牛老師的任教班級數及每班人數，請你幫他算出要買幾部新電腦給學生使用。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入只有兩行。第一行有一個正整數 n (n≤10)，代表蝸牛老師的任教班級數。第二行有 n 個由空白隔開的正整數，代表各班人數。 | 輸出需購買的電腦數量。 |
| # 1 | 5<br>42 39 41 43 30 | 43 |
| # 2 | 1<br>39 | 39 |

#### [Python 解]
```py
n = int(input())
a = [int(x) for x in input().split()]

print(max(a))
```

<div align="center">
    <p>
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course05" target="_blank"><b>👨🏻‍💻 第五週課程</b></a> |
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course07" target="_blank"><b>👨🏻‍💻 第七週課程</b></a>
    </p>
</div>


## License

All of these teaching materials are owned by [Hugo ChunHo Lin](https://github.com/1chooo).   
These materials are intended for tutoring purposes. They are open-source to foster a more vibrant Python learning community. We warmly welcome fellow enthusiasts interested in Python to use them. If you use a substantial portion of the source code, please include a link back to this repository.
