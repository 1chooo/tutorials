txt = "The best things in life are free!"
print("free" in txt)

print("Hello" + "World")

# 解法一
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

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


print("Hello", "World", 1, True, 3.14, sep=" ", end="123\n")
print("Hello")
var = 123
print("Hello", 123, "World")
print(f"Hello {var} World")

print("Hello", "World")
print("Hello" + "World")

word = "Hello"
word = word + "World"
# word += "World"
print(word)

goal_list1 = []
for i in range(100):
    goal_list1.append(i)

print(goal_list1)

goal_list2 = [i for i in range(100)]
print(goal_list2)

print(i)

goal_list2 = [i for x in range(100)]
print(goal_list2)

for i in range(100):
    print(i)


num = 99
goal_list2 = [num for x in range(100)]
print(goal_list2)