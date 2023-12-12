from Helpers.DataHelper import DataHelper
from functools import cache

data = DataHelper(2023, 12).get_data()[:-1]
# data = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""
# data = data.split("\n")
data = [x.split(" ") for x in data]
data = [(x[0], tuple(int(y) for y in x[1].split(","))) for x in data]
print(data[:5])

#------------------ Part 1 ------------------#
@cache
def find_num_solutions(line, group_sizes, current_group_size=0):
    if not line:
        return not group_sizes and not current_group_size

    solutions = 0
    
    symbols = ['.', '#'] if line[0] == '?' else line[0]
    for symbol in symbols:
        if symbol == '#':
            solutions += find_num_solutions(line[1:], group_sizes, current_group_size + 1)
        else:
            if current_group_size > 0:
                if group_sizes and group_sizes[0] == current_group_size:
                    solutions += find_num_solutions(line[1:], group_sizes[1:])
            else:
                solutions += find_num_solutions(line[1:], group_sizes)
    
    return solutions

res = [find_num_solutions(line + '.', groups) for line, groups in data]
solution = sum(res)
print(f"Solution 1: {solution}")

#------------------ Part 2 ------------------#

res = [find_num_solutions('?'.join([line]*5) + '.', groups*5) for line, groups in data]
solution = sum(res)
print(f"Solution 2: {solution}")