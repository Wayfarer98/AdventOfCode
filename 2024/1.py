import collections

import numpy as np
from Helpers.DataHelper import DataHelper

data = DataHelper(2024, 1).get_data()[0:-1]
# data = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
dat = np.array([x.split() for x in data])
dat = dat.T
dat = np.array([np.sort(x) for x in dat])
r1 = np.array([int(x) for x in dat[0]])
r2 = np.array([int(x) for x in dat[1]])


# Part 1
def part1():
    print(np.abs(r1 - r2).sum())


part1()


# Part 2
def part2():
    counts = collections.Counter(r2)
    print(sum([counts[x] * x for x in r1]))


part2()
