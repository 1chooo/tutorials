# Week04 - 2023-1022

### 本週目標
- [ ] 回顧 `for` 迴圈的使用
- [ ] 更多 `for` 回圈使用的例子
- [ ] 補充 [`d490` 我也愛偶數](https://zerojudge.tw/ShowProblem?problemid=d490)
- [ ] [`e948` 基礎代謝率 (BMR Calculation)](https://zerojudge.tw/ShowProblem?problemid=e948)

### 上週回顧 `for` 迴圈的使用

#### `for` 迴圈的語法
```py
for 變數 in 可迭代物件:
    # 做些什麼
```

#### 用例子思考 `for` 的使用
我們從以下例子可以看出，在Python中，for 迴圈的使用非常靈活，它可以用於遍歷各種數據結構，包括列表，以及在不同情境下使用不同的迭代方式。以下是對每個情況的簡要說明：
- 第一個例子使用 for 迴圈遍歷列表 prices 中的元素，並將每個價格打印出來。
- 第二個例子使用 for 迴圈遍歷一個範圍，從0到5，並打印出每個數字。
- 第三個例子使用 for 迴圈和 range 函數，遍歷範圍內的數字，然後使用這些數字作為索引來訪問 prices 列表中的元素，並將它們打印出來。
- 最後一個例子是使用 for 迴圈和 range 函數，但使用步進值為2，這導致只遍歷 prices 列表中的偶數索引，並打印出相應的價格。
- 

```py
prices = [100, 200, 300, 400, 500]
for i in prices:
    print(i)

for i in range(0, 5, 1):
    print(i)
# 1
# 2
# 3
# 4
# 5

for i in range(0, 5, 1):
    print(prices[i])
# 100
# 200
# 300
# 400
# 500

for i in range(0, 5, 2):
    print(prices[i])
# 100
# 300
# 500
```

這些例子突出了 for 迴圈在Python中的多功能性和適應性，可以根據需要進行多種不同的迭代操作。

### 補充 [`d490` 我也愛偶數](https://zerojudge.tw/ShowProblem?problemid=d490)

文文愛偶數，無獨有「偶」地，珊珊也愛偶數。珊珊除了收藏偶數以外，每次她收到一些數字時，她還會把其中的偶數挑出來把玩並予以加總。今天珊珊又收到了一個範圍的連續整數，請問這次她從這段數字中所收集到的偶數的總和是多少？

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入只有一行，其中含有兩個由空白隔開的整數 a, b (0 ≤ a ≤ b ≤ 2147483647)。 | 請輸出一個整數，代表 a 與 b 之間 (含 a 與 b) 所有偶數的和，(答案會 ≤ 2147483647)。 |
| # 1 | 2 5 | 6 |

#### 等差數列解法（接續 [`d485` 我愛偶數](https://zerojudge.tw/ShowProblem?problemid=c485)）
```py
start, end = map(int, input().split())

if start % 2 == 1:
    start += 1
if end % 2 == 1:
    end -= 1

times = ((end - start) / 2) + 1

print(int(times))
```

#### `for` 迴圈解法
```py
a, b = map(int, input().split())
ans = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        ans += i

print(ans)
```

### [`e948` 基礎代謝率 (BMR Calculation)](https://zerojudge.tw/ShowProblem?problemid=e948)

題目: https://toi-reg.csie.ntnu.edu.tw/question/201903/B1-BMR(Q).pdf

每逢過年總是年菜滿漢全席、打牌零嘴永遠吃不完，每天都坐著一直吃，體重一去不復返。為了保持苗條的身材，因此要來計算每天的基礎代謝率，看每天能吃多少零嘴。基礎代謝率(BMR)是指：在身體保持靜態下消耗的最低熱量(單位：大卡)。美國運動醫學協會提供了一個公式：

- BMR(男) = (13.7×體重(kg)) + (5.0×身高(cm)) - (6.8×年齡) + 66。
- BMR(女) = (9.6×體重(kg)) + (1.8×身高(cm)) - (4.7×年齡) + 655。

### [`c418` Bert的三角形 (1)](https://zerojudge.tw/ShowProblem?problemid=c418)
Bert 想要一個 n 層的三角形，第 i 層就要有 i 個 " * "  
請你寫個程式幫幫可憐的 Bert ~~

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 單筆輸入~~<br>輸入只有一個整數 n (1 <= n <= 100) | 輸出整個三角形~~ |
| # 1 | 3 | \*<br>\*\*<br>*** |

```py
layer = int(input())

for i in range(1, layer + 1):
    print('*' * i)
```

### [`c419` Bert的三角形 (2)](https://zerojudge.tw/ShowProblem?problemid=c419)
Bert 又想要另外一種 n 層的三角形，定義如下:  
第 i 層一樣要有 i 個 " * "，但要向右對齊  
請你寫個程式幫幫 Bert ~~

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 單筆輸入~~<br>輸入只有一個整數 n (1 <= n <= 100) | 輸出整個三角形~~<br>因為空格不好辨識，請以"_" 代替 ~~ |
| # 1 | 3 | __\*<br>\_\*\*<br>*** |

```py
layer = int(input())

for i in range(1, layer + 1):
    print('_' * (layer - i) + '*' * i)
```

### [`c420` Bert的三角形 (3)](https://zerojudge.tw/ShowProblem?problemid=c420)
Bert 有天騎著海豚到了埃及，看到了金字塔不經意的發出『 哇～～ 』現在 Bert 想請你用程式記下金字塔的樣子～～現在有一種 n 層的三金字塔，定義如下:

第 i 層要有相對數量的 " * "，請注意要像金字塔一樣向中間對齊

請你寫個程式幫幫 Bert ~~

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 單筆輸入~~<br>輸入只有一個整數 n (1 <= n <= 100)<br>n 保證為奇數 | 輸出整個三角形~~<br>因為空格不好辨識，請以"_" 代替 ~~ |
| # 1 | 3 | \_\_\*\_\_<br>\_\*\*\*_<br>\*\*\*\*\* |

```py
layer = int(input())

for i in range(1, layer + 1):
    print('_' * (layer - i), end='')
    print('*' * ((2 * i) - 1), end='')
    print('_' * (layer - i))
```


<div align="center">
    <p>
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course04" target="_blank"><b>👨🏻‍💻 第四週課程</b></a> |
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course06" target="_blank"><b>👨🏻‍💻 第六週課程</b></a>
    </p>
</div>


## License

All of these teaching materials are owned by [Hugo ChunHo Lin](https://github.com/1chooo).   
These materials are intended for tutoring purposes. They are open-source to foster a more vibrant Python learning community. We warmly welcome fellow enthusiasts interested in Python to use them. If you use a substantial portion of the source code, please include a link back to this repository.
