from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 10).get_data()[:-1]
# data = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L"""
# data = data.split("\n")
data = np.array([list(x) for x in data])

directions = {
    '|': ('N', 'S'),
    '-': ('E', 'W'),
    'L': ('N', 'E'),
    'J': ('N', 'W'),
    'F': ('S', 'E'),
    '7': ('S', 'W'),
    '.': (),
}

opposite = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

mappings = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}

#------------------ Part 1 ------------------#

def traverse_pipes(start_pos):
    x, y = start_pos
    starting_directions = []
    for orientation, mapping in mappings.items():
        new_pos = (x + mapping[0], y + mapping[1])
        if new_pos[0] < 0 or new_pos[1] < 0:
            continue
        if opposite[orientation] in directions[data[new_pos[1], new_pos[0]]]:
            starting_directions.append(orientation)
    
    ori_1 = starting_directions[0]
    ori_2 = starting_directions[1]
    pos_1 = (x + mappings[ori_1][0], y + mappings[ori_1][1])
    pos_2 = (x + mappings[ori_2][0], y + mappings[ori_2][1])
    steps = 1
    vertices_1 = [start_pos, pos_1]
    vertices_2 = [pos_2]
    while pos_1 != pos_2:
        steps += 1
        came_1 = opposite[ori_1]
        came_2 = opposite[ori_2]
        if came_1 == directions[data[pos_1[1], pos_1[0]]][0]:
            ori_1 = directions[data[pos_1[1], pos_1[0]]][1]
        else:
            ori_1 = directions[data[pos_1[1], pos_1[0]]][0]
        if came_2 == directions[data[pos_2[1], pos_2[0]]][0]:
            ori_2 = directions[data[pos_2[1], pos_2[0]]][1]
        else:
            ori_2 = directions[data[pos_2[1], pos_2[0]]][0]
        pos_1 = (pos_1[0] + mappings[ori_1][0], pos_1[1] + mappings[ori_1][1])
        pos_2 = (pos_2[0] + mappings[ori_2][0], pos_2[1] + mappings[ori_2][1])
        vertices_1.append(pos_1)
        vertices_2.append(pos_2)
    vertices_2 = vertices_2[:-1]
    vertices_2.reverse()
    return steps, vertices_1 + vertices_2

start_pos = np.where(data == 'S')
x, y = start_pos[1][0], start_pos[0][0]
steps, vertices = traverse_pipes((x, y))
print(f"Solution 1: {steps}")

#------------------ Part 2 ------------------#

def check_if_point_in_polygon(point, polygon):

    n = len(polygon)
    inside = False
    x, y = point

    if (x, y) in polygon:
        return False
    
    count = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            count += 1
    
    if count % 2 == 1:
        inside = True

    return inside

sum = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if check_if_point_in_polygon((j, i), vertices):
            sum += 1

print(f"Solution 2: {sum}")