# Week 01 - 2023-0924

### 變數的概念

左方為變數，`=` 的概念為賦予，右邊為給定的值
```py
num = 100       # 變數 num 被賦予為 100 的數值
word = 'hello'  # 變數 word 被賦予為 'hello' 的字串
area = 5 * 2    # 變數 area 被賦予為 5 * 2 的運算式
```

### 邏輯判斷練習

命題：我們今天身上只有五十元，如果超過五十元我們買不了，只要等於五十元以及小於五十元，我們可以買。

#### 解法一
分成三個條件：
1. 比五十大
2. 比五十小
3. 剛好等於五十
```py
apple_price = 50

if apple_price > 50:
    print("Do not buy")
elif apple_price < 50:
    print("buy less")
elif apple_price == 50: 
    print("buy equal")
```

#### 解法二
由於我們已經知道題目只有大於五十不買，所以其他的價格我們都能買，也就是透過 `elif` 的方式包括其他的案例
```py
apple_price = 50

if apple_price > 50:
    print("Do not buy")
elif apple_price <= 50:  
    print("buy")
```

#### 解法三
由於我們已經知道題目只有大於五十不買，所以其他的價格我們都能買，也就是透過 `else` 的方式包括其他的案例
```py
apple_price = 50

if apple_price > 50:
    print("Do not buy")
else:  
    print("buy")
```

#### 總結
從以上知識點我們能看出變數的運用以及看出運算子，及判斷的差異，像是 `=` and `==` ，`=` 我們用在「賦予」的概念，也就是把值給予至變數，`==` 我們用在判斷是「是否等於」的情形之中。

並且我們可以看出 `elif` 和 `else` 的差異在於 `elif` 會將判斷的依據寫出來，然而 `else` 是直接包括剩下的可能性。

### 迴圈的概念
迴圈的寫法大致上分為三種，(`起始`, `終點`, `間隔`)，其中起始的預設為 0，及間隔的預設為 1，因此我們要一定給予的是終點的值。

#### 給予終點值
```py
for i in range(10):
    print(i)
```

#### 給予起始值以及終點值
```py
for i in range(0, 10):
    print(i)
```

#### 給予起始、終點以及間隔值
```py
for i in range(0, 10, 1):
    print(i)
```

#### 迴圈練習 1
找出 0 ~ 9 之間的偶數

```py
for i in range(0, 10, 2):
    print(i)
```

#### 迴圈練習 2
在 0 ~ 9 這十位同學中，編號五號同學要回答，其他同學不用回答。
```py
for i in range(0, 10, 1):
    if i == 5:
        print(i)
        print("舉手發問")
    else:
        print(i)
        print("不舉手發問")
```

### 課後練習
在編號 0 ~ 99 這一百位同學中，點出編號 20, 27, 52 三位同學回答，其餘的同學不用回答。
```py
for i in range(100):
    if i == 20:
        print(i)
        print("hi")
    elif i == 27:
        print(i)
        print("hi")
    elif i == 52:
        print(i)
        print("hi")
    else:
        print(i)
        print("no")
```

### 課後補充（下堂課細講）

#### input 的概念
input 的概念為輸入，也就是讓使用者輸入資料，並且透過 `int()` 的方式將字串轉換為數字，因為 input 輸入的資料型態為字串，因此我們要透過 `int()` 的方式將字串轉換為數字，才能進行運算。
```py
apple_price = int(input("請輸入蘋果價格:"))
print(apple_price)
```

#### 上課例題 map 搭配 input 以及 split 使用

```py
a, b, c = max(map(int, input().split()))
print(map(a, b, c))
```
