# -*- coding: utf-8 -*-
"""
Date: 2023/11/27
HW: 29
Author: 林群賀
Student Number: 109601003
"""

import numpy as np

seasons = np.array([
    "Q1",
    "Q2",
    "Q3",
    "Q4",
])
location = np.array([
    "台北 - 桃園", 
    "台北 - 新竹", 
    "台北 - 台中", 
    "台北 - 嘉義", 
    "台北 - 高雄", 
    "台北 - 花蓮",
])
prices = np.array(
    [44, 116, 241, 386, 544, 284]
)
people = np.array([
    [35273, 21534, 12573, 31567, 52386, 44138],
    [25673, 55728, 31245, 33278, 51342, 22464],
    [21345, 22179, 32189, 36296, 33106, 43278],
    [53278, 32785, 43167, 21367, 44579, 32685],
])

revenue = prices * people

print("Q1: ")
print(revenue)

print("")
print("Q2: ")
max_values = np.max(revenue.T, axis=1)
print(max_values)

print("")
print("Q3: ")

max_value = np.max(max_values)
max_value_index = np.where(revenue == max_value)

print(f"{location[max_value_index[1][0]]} 在 {seasons[max_value_index[0][0]]} 的營收最高，為 {max_value} 元。")
