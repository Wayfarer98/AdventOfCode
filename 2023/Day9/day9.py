from Helpers.DataHelper import DataHelper

data = DataHelper(2023, 9).get_data()[:-1]
# data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""
# data = data.split("\n")

#--------------------- Part 1 ---------------------#

def extrapolate(line):
    seq = list(map(int, line.split()))
    differences = [seq]
    while len(set(differences[-1])) > 1:
        differences.append([differences[-1][i+1] - differences[-1][i] for i in range(len(differences[-1])-1)])
    
    diff_pos = differences[-1][-1]
    diff_neg = differences[-1][0]
    for i in range(len(differences)-2, -1, -1):
        diff_pos = differences[i][-1] + diff_pos
        diff_neg = differences[i][0] - diff_neg
    
    return diff_pos, diff_neg


diffs = [extrapolate(line)[0] for line in data]
res = sum(diffs)
print(f"Solution 1: {res}")

#--------------------- Part 2 ---------------------#

diffs_neg = [extrapolate(line)[1] for line in data]
res = sum(diffs_neg)
print(f"Solution 2: {res}")