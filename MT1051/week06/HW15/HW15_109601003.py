"""
Date: 2023/10/23
HW: 15
Author: 林群賀
Student Number: 109601003
"""

# 初始化硬幣數量
num_10 = 0
num_5 = 0
num_1 = 0

# 初始化總值
total_value = 0

# 開始迭代計算硬幣數量
for num_10 in range(0, 21):  # 10元硬幣的數量範圍從0到20
    for num_5 in range(0, 41):  # 5元硬幣的數量範圍從0到40
        num_1 = 20 - num_10 - num_5  # 1元硬幣的數量根據已知條件計算

        # 檢查是否所有硬幣數量都為非負數並且總值為108元
        if num_1 >= 0 and num_5 >= 0 and num_10 >= 0 and (num_10 * 10 + num_5 * 5 + num_1 == 108):
            break

    if (num_10 * 10 + num_5 * 5 + num_1 == 108):
        break

# 輸出結果
print("10 元硬幣數量：", num_10)
print("5  元硬幣數量：", num_5)
print("1  元硬幣數量：", num_1)

