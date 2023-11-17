# Week08 - 2023-1119

### 本週目標
- [ ] [a038. 數字翻轉](https://zerojudge.tw/ShowProblem?problemid=a038)
  - [ ] `reverse()` 用法介紹
  - [ ] `join()` 用法介紹

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

#### [小實驗]
```py
# 本測試可發現若 list 結尾有 0，則 reverse 後會消失

a = ['1', '2', '3', '4', '0', '0']
a.reverse()
ans = ''.join(a)
print(int(ans))
# 4321

```py

# 我們也可以發現，若是字串，倒轉後 0 也會消失
b = '123400'
b = b[::-1]
print(int(b))
# 4321
```

### [煲仔飯 (Clay Pot Rice)](https://tpmso.org/toi/wp-content/uploads/question/202310/ClayPotRice.pdf) [^1]

### [烤肉 (BBQ)](https://tpmso.org/toi/wp-content/uploads/question/202310/BBQ.pdf) [^1]

### [超市排隊 (Supermarket)](https://tpmso.org/toi/wp-content/uploads/question/202310/Supermarket.pdf) [^1]

### [d587. 參貳壹真好吃](https://zerojudge.tw/ShowProblem?problemid=d587)

### [j605. 1. 程式考試](https://zerojudge.tw/ShowProblem?problemid=j605)

### [c290. APCS 2017-0304-1秘密差](https://zerojudge.tw/ShowProblem?problemid=c290)

### [a149. 乘乘樂](https://zerojudge.tw/ShowProblem?problemid=a149)

### [a022. 迴文](https://zerojudge.tw/ShowProblem?problemid=a022)

### [e968. 2. 班級名單 (Student list)](https://zerojudge.tw/ShowProblem?problemid=e968)

### [c294. APCS-2016-1029-1三角形辨別](https://zerojudge.tw/ShowProblem?problemid=c294)

<div align="center">
    <p>
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course07" target="_blank"><b>👨🏻‍💻 第七週課程</b></a> |
        <!-- <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course08" target="_blank"><b>👨🏻‍💻 第八週課程</b></a> -->
    </p>
</div>


## License

All of these teaching materials are owned by [Hugo ChunHo Lin](https://github.com/1chooo).   
These materials are intended for tutoring purposes. They are open-source to foster a more vibrant Python learning community. We warmly welcome fellow enthusiasts interested in Python to use them. If you use a substantial portion of the source code, please include a link back to this repository.

[^1]: [TOI推廣線上練習賽歷屆試題](https://tpmso.org/toi/index.php/tasks)
