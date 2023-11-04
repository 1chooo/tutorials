# Week07 - 2023-1105


### 本週目標
- [ ] `While True`
  - [ ] `break`, `continue`
- [ ] [a104. 排序](https://zerojudge.tw/ShowProblem?problemid=a104)
  - [ ] `sort()` 用法介紹 
  - [ ] `EOF`
  - [ ] `try-except`
  - [ ] `break`, `continue`
- [ ] [a038. 數字翻轉](https://zerojudge.tw/ShowProblem?problemid=a038)
  - [ ] `reverse()` 用法介紹
  - [ ] `join()` 用法介紹

### `while` 迴圈使用

當條件成立時，重複執行某些程式碼，直到條件不成立為止。

```py
i = 0
while i < 5:
    print(i)
    i += 1
```

#### `while` 迴圈的語法
```py
while 條件:
    # 做些什麼
```

#### 用例子思考 `for` 和 `while` 的差別
我們可以想像 `for` 是已經知道次數，並且要每一個都走過；然而 `while` 是你只知道這麼做是對的，但你不知道終點在哪裡，所以你只能一直做下去，直到你發現終點。

- 命題：當今天肚子餓就要吃飯，並且要吃到飽
- `for`：我知道每碗飯有多少份量，我這餐吃五碗就會飽了，所以我一吃完五碗就不吃了。
- `while`：我不知道每碗飯有多少份量，但我知道我要吃到飽，所以我一直吃直到吃不下為止。

```py
# for
for i in 五碗飯:
    吃一碗飯

# while
while 肚子餓:
    吃一碗飯，直到吃飽為止
```

#### `break` 與 `continue` 的使用

##### `break` 的使用
```py
for i in range(5):
    if i == 3:
        break
    print(i)

# 0
# 1
# 2
```

##### `continue` 的使用
```py
for i in range(5):
    if i == 3:
        continue
    print(i)

# 0
# 1
# 2
# 4
# 0
# 1
# 2
```

#### EOF 實作

當題目說會有不斷輸出的時候，我們可以用 `while True` 來實作，並且用 `try-except` 來處理 EOF 的問題。

```py
while True:
    try:
        # 這裡放你的程式碼
    except EOFError:
        break
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


### [a038. 數字翻轉](https://zerojudge.tw/ShowProblem?problemid=a038)

輸入任意數字，並將其數字全部倒轉

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入一行包含一個整數，且不超過 $2^{31}$ | 輸出翻轉過後的數字 |
| # 1 | 12345 | 54321 |
| # 2 | 5050 | 505 |

#### Hint: 
- 前面有 0 的話應消除

#### [Python 解] (學校老師解)

```py
a = list(input())
a.reverse()
ans = ''.join(a)
print(int(ans))
```

<div align="center">
    <p>
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course06" target="_blank"><b>👨🏻‍💻 第六週課程</b></a> |
        <!-- <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course07" target="_blank"><b>👨🏻‍💻 第七週課程</b></a> -->
    </p>
</div>


## License

All of these teaching materials are owned by [Hugo ChunHo Lin](https://github.com/1chooo).   
These materials are intended for tutoring purposes. They are open-source to foster a more vibrant Python learning community. We warmly welcome fellow enthusiasts interested in Python to use them. If you use a substantial portion of the source code, please include a link back to this repository.
