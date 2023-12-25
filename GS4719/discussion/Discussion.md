# Discussion

### 用例子思考 `for` 和 `while` 的差別

最近在教家教學生時，準備進到 `for` 以及 `while` 迴圈，因此在教材中想了一個例子，想要分享給一起修課的大家，希望大家能給予建議，如果大神覺得如何描述可以更好，我一定會加入教材！

（偷抱怨：教高中生好辛苦，一直說還有國、英、數、物、化等主科沒空複習，大家如果也有家教經驗也可以一起在下方分享、討論）

---
**(以下原文)**

我們可以想像 `for` 是已經知道次數，並且要每一個都走過；然而 `while` 是你只知道這麼做是對的，但你不知道終點在哪裡，所以你只能一直做下去，直到你發現終點。

#### 命題：當今天肚子餓就要吃飯，並且要吃到飽
- `for`：我知道每碗飯有多少份量，我這餐吃五碗就會飽了，所以我一吃完五碗就不吃了。
- `while`：我不知道每碗飯有多少份量，但我知道我要吃到飽，所以我一直吃直到吃不下為止。

以下是將 `for` 以及 `while` 想法轉換成 pseudocode 的過程：
```py
# for
for i in 五碗飯:
    吃一碗飯

# while
while 肚子餓:
    吃一碗飯，直到吃飽為止
```

### [我在 Python 中 `tuple` 會有哪些應用場景](https://github.com/NCU-GS4719-Python/Python-Community/discussions/1667)

今天課堂中有講解到 `tuple` 引此我想分享我在開發的時候會用到 `tuple` 的時機，我會在 function `return` 太多變數的時候包上 `tuple` 如此可以讓程式碼變得更具可讀性，就不會 return 後面一長串。下面舉個簡單的例子：

```python
def get_several_objs(
        word, 
        num,
    ) -> tuple[
        str, 
        int,
    ]:
    """
    __function description__
    ...
    """
    word = "HiHi"
    num = 123
    return (
        word, 
        num,
    )
```

這樣的做法也跟很多人討論過，有些人會覺這樣寫包太多括號反而有失可讀性，我想就是個人習慣吧！只要變數命名看得懂，排版不要太誇張，我覺得就沒問題。

文末分享一下我是從哪裡發現可以這樣寫 function，我是去看一些 Python 的官方套件的源碼，通常都非常多程式碼，大多都是用這種方式寫，我覺得這樣寫很好讀，所以我就學起來了，因此分享給大家，或許大家未來開發的道路也會派上用場。


## [AWS 服務搭建 LINE BOT 助手](https://github.com/NCU-GS4719-Python/Python-Community/discussions/1794)

我是 AWS 的校園大使，我是 Hugo 為了準備技術工作坊，我做了一個 LINE BOT 目的是介紹 AWS Educate 這個 Program，把 LINE 的服務放到 AWS 上最大的好處就是可以讓大家在無時無刻都能使用，提供資源給大家參考，如果期末有想要一起做 LINE BOT 當專案的同學也可以一起做討論！

| Post | Post | LINE QRCODE |
|:-:|:-:|:-:|
| <img src="https://github.com/1chooo/aws-line-business-card-workshop/raw/main/imgs/post/01_post.gif" width="300"> | <img src="https://github.com/1chooo/aws-line-business-card-workshop/raw/main/imgs/post/02_post.jpg" width="300"> | <img src="https://github.com/1chooo/aws-line-business-card-workshop/raw/main/imgs/line_qrcode/L_gainfriends_2dbarcodes_BW.png" width="300"> |


### 架構圖

<img width="926" alt="Screenshot 2023-12-20 at 2 06 38 PM" src="https://github.com/NCU-GS4719-Python/Python-Community/assets/94162591/aaa4fd25-5570-4f4c-8dfa-b80b15009b8b">

### Reference

- LINE BOT URL: https://lin.ee/61E7HdZ
- GitHub Repo: https://github.com/1chooo/aws-line-business-card-workshop
- Hands-on Tips: https://github.com/1chooo/aws-line-business-card-workshop/blob/main/hands_on_tips.md

### 如何註冊 AWS Educate
- AWS Educate: https://awseducate.tw/2

