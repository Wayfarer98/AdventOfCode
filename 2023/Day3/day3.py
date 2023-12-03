from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 3).get_data()
data = np.array([np.array(list(line)) for line in data[:-1]])

#---------------------PART 1---------------------#

def check_vertical(x, y):
    if y != 0:
        if not data[y-1][x].isnumeric() and not data[y-1][x] == '.':
            return True
    if y != len(data)-1:
        if not data[y+1][x].isnumeric() and not data[y+1][x] == '.':
            return True
    return False

def check_horizontal(x, y, left):
    if x != 0 and left:
        if (
            not data[y][x-1].isnumeric() and
            not data[y][x-1] == '.' or
            check_vertical(x-1, y)
        ):
            return True
    if x != len(data[y])-1 and not left:
        if (
            not data[y][x+1].isnumeric() and
            not data[y][x+1] == '.' or
            check_vertical(x+1, y)
        ):
            return True
    return False


def sum_line(line, line_idx):
    i = 0
    line_sum = 0
    while i < len(line):
        if line[i].isnumeric():
            number = line[i]
            check = ( 
                check_horizontal(i, line_idx, True) or
                check_vertical(i, line_idx)
            )
                
            while i + 1 < len(line) and line[i+1].isnumeric():
                number += line[i+1]
                i += 1
                if not check:
                    check = check_vertical(i, line_idx)
            if not check:
                check = check_horizontal(i, line_idx, False)
            if check:
                line_sum += int(number)
        i += 1
    return line_sum

res = [sum_line(line, idx) for idx, line in enumerate(data)]
solution = sum(res)
print(f"Solution 1: {solution}")


#---------------------PART 2---------------------#

def get_numbers_vertical(x, y, top):
    check_left = False
    check_right = False
    check_middel = False
    line_idx = y-1 if top else y+1
    if top and y == 0 or not top and y == len(data)-1:
        return []
    if data[line_idx][x].isnumeric():
        check_middel = True
    if not check_middel and not x-1 < 0 and data[line_idx][x-1].isnumeric():
        check_left = True
    if not check_middel and not x+1 >= len(data[line_idx]) and data[line_idx][x+1].isnumeric():
        check_right = True

    if check_middel:
        num = [data[line_idx][x]]
        i_left = x
        i_right = x
        while i_left > 0 and data[line_idx][i_left-1].isnumeric():
            num.insert(0, data[line_idx][i_left-1])
            i_left -= 1
        while i_right < len(data[line_idx])-1 and data[line_idx][i_right+1].isnumeric():
            num.append(data[line_idx][i_right+1])
            i_right += 1
        return [int("".join(num))]

    nums = []
    if check_left:
        num = [data[line_idx][x-1]]
        i = x - 1
        while i > 0 and data[line_idx][i-1].isnumeric():
            num.insert(0, data[line_idx][i-1])
            i -= 1
        nums.append(int("".join(num)))
    if check_right:
        num = [data[line_idx][x+1]]
        i = x + 1
        while i < len(data[line_idx])-1 and data[line_idx][i+1].isnumeric():
            num.append(data[line_idx][i+1])
            i += 1
        nums.append(int("".join(num)))

    return nums

def get_numbers_horizontal(x, y, left):
    check = False
    idx = x-1 if left else x+1
    if left and x == 0 or not left and x == len(data[y])-1:
        return []
    if data[y][idx].isnumeric():
        check = True
    if check:
        num = [data[y][idx]]
        i = idx
        while left and i > 0 and data[y][i-1].isnumeric():
            num.insert(0, data[y][i-1])
            i -= 1
        while not left and i < len(data[y])-1 and data[y][i+1].isnumeric():
            num.append(data[y][i+1])
            i += 1
        return [int("".join(num))]
    return []
    
def get_gear_ratio(x, y):
    top = get_numbers_vertical(x, y, True)
    bot = get_numbers_vertical(x, y, False)
    left = get_numbers_horizontal(x, y, True)
    right = get_numbers_horizontal(x, y, False)

    nums = top + bot + left + right

    if len(nums) == 2:
        return nums[0] * nums[1]

    return 0

ratios = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == '*':
            ratios.append(get_gear_ratio(x, y))

solution = sum(ratios)
print(f"Solution 2: {solution}")
