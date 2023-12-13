from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 13).get_data()[:-1]
data = '\n'.join(data)
# data = '''#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#'''
data = data.split("\n\n")
data = [x.split("\n") for x in data]
data = [np.array([list(x) for x in y]) for y in data]


#------------------ Part 1 ------------------#

# Create function that finds the horizontal and vertical line that mirrors
# the 2d array
def find_mirror_line(arr):
    # Find the horizontal line
    horizontal_line = None, None
    for i in range(len(arr) - 1):
        cond = False
        if np.all(arr[i] == arr[i+1]):
            cond = True
            horizontal_line = i, i+1
            j = i + 1
            k = i
            while j < len(arr) and k >= 0:
                if np.all(arr[j] == arr[k]):
                    j += 1
                    k -= 1
                else:
                    horizontal_line = None, None
                    cond = False
                    break
        if cond:
            break
    
    # Find the vertical line
    vertical_line = None, None
    for i in range(len(arr[0]) - 1):
        cond = False
        if np.all(arr[:,i] == arr[:,i+1]):
            cond = True
            vertical_line = i, i-1
            j = i + 1
            k = i
            while j < len(arr[0]) and k >= 0:
                if np.all(arr[:,j] == arr[:,k]):
                    j += 1
                    k -= 1
                else:
                    vertical_line = None, None
                    cond = False
                    break
        if cond:
            break

    left = vertical_line[0] + 1 if vertical_line[0] != None else 0
    above = horizontal_line[0] + 1 if horizontal_line[0] != None else 0
    return left, above

res = [find_mirror_line(x) for x in data]
left = sum(x[0] for x in res)
above = sum(x[1] for x in res)
solution = left + 100 * above
print(f"Solution 1: {solution}")

#------------------ Part 2 ------------------#

def find_mirror2(arr):
    left, above = find_mirror_line(arr)
    # Find the horizontal line
    horizontal_line = None, None
    for i in range(len(arr) - 1):
        cond = False
        sum = np.sum(arr[i] != arr[i+1])
        if sum <= 1:
            sum = 0
            cond = True
            horizontal_line = i, i+1
            if above == (horizontal_line[0] + 1 if horizontal_line[0] != None else 0):
                horizontal_line = None, None
                continue
            j = i + 1
            k = i
            while j < len(arr) and k >= 0:
                sum += np.sum(arr[j] != arr[k])
                if sum <= 1:
                    j += 1
                    k -= 1
                else:
                    horizontal_line = None, None
                    cond = False
                    break
        if cond and sum == 1:
            break
    
    # Find the vertical line
    vertical_line = None, None
    for i in range(len(arr[0]) - 1):
        cond = False
        sum = np.sum(arr[:, i] != arr[:, i+1])
        if sum <= 1:
            sum = 0
            cond = True
            vertical_line = i, i+1
            if left == (vertical_line[0] + 1 if vertical_line[0] != None else 0):
                vertical_line = None, None
                continue 
            j = i + 1
            k = i
            while j < len(arr[0]) and k >= 0:
                sum += np.sum(arr[:, j] != arr[:, k])
                if sum <= 1:
                    j += 1
                    k -= 1
                else:
                    vertical_line = None, None
                    cond = False
                    break
        if cond and sum == 1:
            break

    left = vertical_line[0] + 1 if vertical_line[0] != None else 0
    above = horizontal_line[0] + 1 if horizontal_line[0] != None else 0
    return left, above

res = [find_mirror2(x) for x in data]
left = sum(x[0] for x in res)
above = sum(x[1] for x in res)
solution = left + 100 * above
print(f"Solution 2: {solution}")