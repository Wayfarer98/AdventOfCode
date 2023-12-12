from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 11).get_data()[:-1]
# data = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""
# data = data.split("\n")
data = np.array([list(x) for x in data])

#------------------ Part 1 ------------------#

def expand_univers(data):
    cpy = data.copy()
    for i in range(len(data)-1, -1 , -1 ):
        if len(set(data[i])) == 1 and data[i][0] == '.':
            cpy = np.insert(cpy, i, cpy[i], axis=0)
    for i in range(len(data[0])-1, -1, -1):
        if len(set(data[:, i])) == 1 and data[:, i][0] == '.':
            cpy = np.insert(cpy, i, cpy[:, i], axis=1)
    return cpy
new_data = expand_univers(data)

def get_vertices(data):
    vertices = np.where(data == '#')
    vertices = [(x, y) for x, y in zip(vertices[0], vertices[1])]
    return vertices

vertices = get_vertices(new_data)

def get_steps(vertices):
    sum = 0
    for i in range(len(vertices)):
        for j in range(i, len(vertices)):
            if vertices[i] == vertices[j]:
                continue
            x1, y1 = vertices[i]
            x2, y2 = vertices[j]
            steps = abs(x1 - x2) + abs(y1 - y2)
            sum += steps
    return sum

res = get_steps(vertices)
print(f"Solution 1: {res}")
#------------------ Part 2 ------------------#

vertices = get_vertices(data)

def expand_univers_big(vertices, data):
    for i in range(len(data)-1, -1, -1):
        if len(set(data[i])) == 1 and data[i][0] == '.':
            for j in range(len(vertices)):
                if vertices[j][0] > i:
                    vertices[j] = (vertices[j][0] + 999999, vertices[j][1])
    for i in range(len(data[0])-1, -1, -1):
        if len(set(data[:, i])) == 1 and data[:, i][0] == '.':
            for j in range(len(vertices)):
                if vertices[j][1] > i:
                    vertices[j] = (vertices[j][0], vertices[j][1] + 999999)
    return vertices

vertices = expand_univers_big(vertices, data)
res = get_steps(vertices)
print(f"Solution 2: {res}")