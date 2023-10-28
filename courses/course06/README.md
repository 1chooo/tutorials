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


### [a104. 排序](https://zerojudge.tw/ShowProblem?problemid=a104)

幫我排個數字謝謝QQ

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 有多筆測資以EOF為結束<br>第一行有一個正整數n(1<=n<=1000)，代表有幾個數字要請你幫忙排<br>第二行有n個可以用int儲存的正整數 | 輸出n個已由小到大排序好的正整數 |
| # 1 | 5<br>1 2 3 4 5 | 5 4 3 2 1 |
| # 2 | 4<br>100 250 -200 450 | 450 -200 250 100 |

<div align="center">
    <p>
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course05" target="_blank"><b>👨🏻‍💻 第五週課程</b></a> |
        <!-- <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course06" target="_blank"><b>👨🏻‍💻 第六週課程</b></a> -->
    </p>
</div>


## License

All of these teaching materials are owned by [Hugo ChunHo Lin](https://github.com/1chooo).   
These materials are intended for tutoring purposes. They are open-source to foster a more vibrant Python learning community. We warmly welcome fellow enthusiasts interested in Python to use them. If you use a substantial portion of the source code, please include a link back to this repository.
