# Week03 - 2023-1008

### 上週回顧
- [ ] `float()` 取位數補充
- [ ] 練習 "d065"

### `float()` 取位數補充

#### 透過型別轉換
另外我們也可以透過先前學習到的型別轉換先轉換成 `str`，再透過對 `str` 的處理轉換成 `float` 因而得到我們想要的數值。

```py
probability = 0.123456789
probability_str = str(probability)
probability_str = probability_str[:4]
probability = float(probability_str)
print(probability)      # 0.12
```

#### 透過運算的方式截斷
將一個浮點數 `probability` 乘以 100，然後再將結果轉換為整數。接著，它會再將該整數轉換回浮點數，並保留兩位小數。這樣的處理方式通常稱為「四捨五入到兩位小數」。

這樣的處理方式可能有助於限制浮點數的小數部分，以確保它只保留兩位小數，而不進行四捨五入

```py
probability = 0.123456789
print(int(probability * 100) / 100)
```

#### Zerojudge "[d065](https://zerojudge.tw/ShowProblem?problemid=d065)"
###### `變數`, `一行`, `map`, `input`, `split`, `int`, `max`, `if`
文文和兩個同學最近喜歡在 ZeroJudge 上解題。有一天他們看到了孔子說的：「三人行必有我師焉。」就吵了起來，因為他們每個人都認為自己是三個人之中的「老師」。後來他們決定要比比看誰在 ZeroJudge 上的 AC 題數最多。

**Input**  
輸入只有一行，含有三個由空白所隔開的非負整數。

**Output**  
輸出這三個整數中最大的那一個。
| Sample | Input    | Output |
| ------ | -------- | ------ |
| # 1    | 35 26 48 | 48     |
| # 2    | 37 59 59 | 59     |

**解法一：搭配先前課程解法**  
透過變數先將使用者的輸入保存，並且以及邏輯判斷以找出最大值。

- 使用者的概念：我們是**撰寫程式的角色**，而使用我們程式的角色就是使用者，我們為了滿足使用者的使用，因此要設計能夠運行的程式，因此以此概念便有了 `input()` 的搭配使用，以此達到與使用者互動。

```py
a, b, c = map(int, input().split())

max_value = a

if b > max_value:
    max_value = b
if c > max_value:
    max_value = c

print(max_value)
```

**解法二：將程式行數縮短**
因為 Python 本身有內建取最大值的方法

```py
a, b, c = map(int, input().split())
print(max(a, b, c))
```

---

### `string` 字串操作
在 Pyhton 中如果我們想要輸入 `string` 我們會透過
`""` 一個引號的方式，其中在 Python 中 `"` 跟 `'` 的效力是相同的
> [!IMPORTANT]  
> 左右兩邊的引號要一模一樣  
> 1. 合格：`'Hello World'`
> 2. 合格：`"Hello World"`
> 3. 不合格：`'Hello World"`
> 3. 不合格：`"Hello World'`

#### 字串的索引
字串的索引是從 0 開始，也就是說第一個字的索引是 0，第二個字的索引是 1，以此類推。
```py
word = "Hello Python!"

print(word)
```

#### 字串其實就是 `list`
```py
word = "Hello Python!"

print(word[0])      # H
print(word[1])      # e

for i in word:
    print(x)
```

#### 字串的長度
```py
word = "Hello Python!"
print(len(word))
```

#### 字串檢查
我們如果想檢查一個單詞又或是字母是否在字串之中，我們會有以下的方法
```py
txt = "The best things in life are free!"
print("free" in txt)
```

```py
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
```

#### 字串的切片 (在 `list` 細講)
```py
word = "Hello Python!"
# 取得 word 中第 2~5 個字元
print(word[1:5])    # ello
# 取得 word 中第 2~最後一個字元
print(word[1:])     # ello Python!
# 取得 word 中第 1~5 個字元
print(word[:5])     # Hello
# 取得 word 中第 1~最後一個字元
print(word[:])      # Hello Python!
# 取得 word 中第 1~倒數第 2 個字元
print(word[:-1])    # Hello Python
# 取得 word 中第 1~倒數第 2 個字元
print(word[:-2])    # Hello Pytho
```

#### 多行 `string`
當我們今天想輸入多行的 `string` 過去我們會用 `""` 一個引號的方式，為了程式碼的可讀性，我們會改用 `""""""` 三個引號的方式。

```py
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

### `print` 函式的使用

### `list` 串列操作

### `for` 迴圈使用
