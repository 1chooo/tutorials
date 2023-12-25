# Week08 - 2023-1126

### [a017. 五則運算](https://zerojudge.tw/ShowProblem?problemid=a017)

計算五則運算式的結果，包含加、減、乘、除、餘

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入資料若干行直到 EOF 為止。每一行包含輸入一個字串，其中包含運算元及運算子，為了方便讀取，所有的運算子及運算元均以空格區隔。<br>運算元為 0 ~231 -1 的整數<br運算子則包含 + - * / % 及 ( )<br>運算時請注意先乘除後加減及() 優先運算的計算規則 | 對每一行輸入，輸出運算結果。<br>為了避免小數點誤差，所有的運算過程都不會產生小數點，可以放心使用整數進行運算 |
| # 1 | 2 + 3 * 4<br>2 * ( 3 + 4 ) * 5 | 14<br>70 |

### [h966]

#### [Python 解]
```py
a = [[0] * 14 for x in range(14)]

for i in range(1, 14):
    for j in range(1, i + 1):
        if i == 1 and j == 1:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]

    t = int(input())
    for i in range(t):
        m, n = map(int, input().split())
        print(a[m][n])
```

### [a011. 00494 - Kindergarten Counting Game](https://zerojudge.tw/ShowProblem?problemid=a011)

算一算每行有幾個字（word）。

Word的定義是連續的字元（letter: A~Z a~z）所組成的字。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 一段文字(string) | 字數(int) |
| # 1 | Hello everybody!!<br>This is school principal speeking. | 2<br>5 |

#### [Python 解]
```py
while 1:  # Continuous loop until broken
    try:
        n = 0  # Counter for word endings
        s = input()  # Take input from user

        # Loop through each character in the input string except the last character
        for i in range(len(s) - 1):
            # Check if the current character is an alphabet character and the next character is not an alphabet character
            if s[i].isalpha() and not s[i + 1].isalpha():
                n += 1  # Increment the counter when an alphabet character is followed by a non-alphabet character

        # Check the special case where the second last character is not an alphabet character and the last character is an alphabet character
        if not s[-2].isalpha() and s[-1].isalpha():
            n += 1  # Increment the counter for this special case

        print(n)  # Print the total count of word endings
    except:  # Catch any exceptions to break out of the loop
        break
```

### [a244. 新手訓練 ~ for + if](https://zerojudge.tw/ShowProblem?problemid=a244)

### [d587. 參貳壹真好吃](https://zerojudge.tw/ShowProblem?problemid=d587)

### [e968. 2. 班級名單 (Student list)](https://zerojudge.tw/ShowProblem?problemid=e968)

### [c294. APCS-2016-1029-1三角形辨別](https://zerojudge.tw/ShowProblem?problemid=c294)