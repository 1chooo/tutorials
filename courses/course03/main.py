txt = "The best things in life are free!"
print("free" in txt)

print("Hello" + "World")

# 解法二
word = "Hello World"
word = word.split(" ")

print("解法一: ")
print(word[1], word[0])
print(word[0])

# 解法二
word = "Hello World"
print("解法二: ")
print(word[6: 11], word[0: 6])
print(word[0: 6])
