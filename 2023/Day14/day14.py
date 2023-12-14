from Helpers.DataHelper import DataHelper
import numpy as np
from functools import cache

data = DataHelper(2023, 14).get_data()[:-1]
# data = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....'''
# data = data.split("\n")
data = np.array([list(x) for x in data])

#------------------ Part 1 ------------------#

def count_load(column):
    l = len(column)
    stopping_point = 0
    count = 0
    for i in range(l):
        if column[i] == "O":
            count += l - stopping_point
            stopping_point = stopping_point + 1
        if column[i] == "#":
            stopping_point = i + 1
    return count

res = list(map(count_load, data.T))
solution = sum(res)
print("Solution 1: ", solution)

#------------------ Part 2 ------------------#

def slide(row):
    l = len(row)
    stopping_point = 0
    for i in range(l):
        if row[i] == "O":
            row[i] = "."
            row[stopping_point] = "O"
            stopping_point += 1
        if row[i] == "#":
            stopping_point = i + 1
            
    return row

def rotate(arr):
    cpy = arr.copy()
    cpy = np.rot90(cpy)
    for _ in range(4):
        for i in range(len(cpy)):
            cpy[i] = slide(cpy[i])
        cpy = np.rot90(cpy, k=-1)
    cpy = np.rot90(cpy, k=-1)
    return cpy

def count_loads(arr):
    count = 0
    arr = arr.T
    l = len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "O":
                count += l - j
    return count

previous = [data]
for i in range(1000000000):
    data = rotate(data)
    if any((l == data).all() for l in previous):
        for j in range(len(previous)):
            if (previous[j] == data).all():
                idx = j
                loop_length = i + 1 - idx
                data = previous[idx + (1000000000 - i) % loop_length - 1]
                break
        break
    previous.append(data)

# for i in range(len(previous)):
#     print(count_loads(previous[i]))

solution = count_loads(data)
print("Solution 2: ", solution)
