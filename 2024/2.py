import numpy as np
from Helpers.DataHelper import DataHelper

data = DataHelper(2024, 2).get_data()[0:-1]
# inp = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""
# data = inp.split("\n")


# part 1
def part1():
    dat = [x.split() for x in data]
    dat_int = []
    for i in range(len(dat)):
        dat_int.append([int(x) for x in dat[i]])
    diffs = []
    less = []
    greater = []
    abs_diffs = []
    amnt_greater = []
    amnt_less = []
    amnt = []
    correct = []
    for i in range(len(dat_int)):
        diffs.append(np.diff(dat_int[i]))
        less.append(diffs[i] < 0)
        greater.append(diffs[i] > 0)
        abs_diffs.append(np.abs(diffs[i]))
        amnt_greater.append(abs_diffs[i] > 0)
        amnt_less.append(abs_diffs[i] < 4)
        amnt.append(np.logical_and(amnt_greater[i], amnt_less[i]))
        correct.append(
            np.logical_and(
                np.logical_or(np.all(less[i]), np.all(greater[i])),
                np.all(amnt[i]),
            )
        )
    print(sum(correct))


part1()


def check_safe(readings):
    subsets = [readings[:i] + readings[i + 1 :] for i in range(len(readings))]
    for subset in subsets:
        diffs = np.diff(subset)
        less = diffs < 0
        greater = diffs > 0
        abs_diffs = np.abs(diffs)
        amnt_greater = abs_diffs > 0
        amnt_less = abs_diffs < 4
        amnt = np.logical_and(amnt_greater, amnt_less)
        correct = np.logical_and(
            np.logical_or(np.all(less), np.all(greater)),
            np.all(amnt),
        )
        if correct:
            return True
    return False


def part2():
    dat = [x.split() for x in data]
    dat_int = []
    for i in range(len(dat)):
        dat_int.append([int(x) for x in dat[i]])
    results = []
    for reading in dat_int:
        results.append(check_safe(reading))
    print(sum(results))


part2()
