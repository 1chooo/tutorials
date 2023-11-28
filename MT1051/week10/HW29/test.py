import numpy as np

location = np.array([
    "台北 - 桃園", 
    "台北 - 新竹", 
    "台北 - 台中", 
    "台北 - 嘉義", 
    "台北 - 高雄", 
    "台北 - 花蓮",
])
prices = np.array([44, 116, 241, 386, 544, 284])
people = np.array([
    [35273, 21534, 12573, 31567, 52386, 44138],
    [25673, 55728, 31245, 33278, 51342, 22464],
    [21345, 22179, 32189, 36296, 33106, 43278],
    [53278, 32785, 43167, 21367, 44579, 32685],
])

revenue = np.zeros((len(location), len(people[0])), dtype=int)

for i in range(len(location)):
    for j in range(len(people)):
        revenue[i][j] = prices[i] * people[j][i]

print("Q1: ")
print("| 起站 | 終站 | Q1 營收 | Q2 營收 | Q3 營收 | Q4 總營收 |")
print("| ---- | ---- | --------- | --------- | --------- | --------- |")

total_revenue = np.array([
    revenue[i][0] + revenue[i][1] + revenue[i][2] + revenue[i][3] for i in range(len(location))
])

for i in range(len(location)):
    start, end = location[i].split(' - ')
    print(f"| {start} | {end} | {revenue[i][0]} | {revenue[i][1]} | {revenue[i][2]} | {revenue[i][3]} |")

print("")

print("Q2: ")
print("| 起站 | 終站 | Q1, Q2, Q3, Q4 的總營收 |")
print("| ---- | ---- | ----------------------- |")

for i in range(len(location)):
    start, end = location[i].split(' - ')
    print(f"| {start} | {end} | {total_revenue[i]} |")

print("Q3:")

max_revenue = np.max(revenue, axis=1)
max_revenue_index = np.argmax(revenue, axis=1)

print("各站年度最高營收季度: ")
print("| 起站 | 終站 | 最高營收 | 季度 |")
print("| ---- | ---- | -------- | ---- |")

for i in range(len(location)):
    start, end = location[i].split(' - ')
    print(f"| {start} | {end} | {max_revenue[i]} |  Q{max_revenue_index[i] + 1} |")

print("")

# 找出整個營收陣列中最大值的索引位置
max_revenue_index_overall = np.argmax(revenue)
# 將索引轉換為二維索引
max_revenue_index_row, max_revenue_index_col = np.unravel_index(max_revenue_index_overall, revenue.shape)
# 取得對應的起站和終站
route_with_max_revenue = location[max_revenue_index_row]
quarter_with_max_revenue = max_revenue_index_col + 1  # 季度從索引0開始，因此加1
# 獲取該航線在該季度的營收
max_revenue_for_route = revenue[max_revenue_index_row, max_revenue_index_col]

print(f"最高營收的航線是：{route_with_max_revenue} 在第 {quarter_with_max_revenue} 季度，該航線在該季度的營收為：{max_revenue_for_route} 元")




