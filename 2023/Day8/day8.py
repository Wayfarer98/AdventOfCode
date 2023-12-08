from Helpers.DataHelper import DataHelper
import math

data = DataHelper(2023, 8).get_data()
# data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# """

# data = data.split("\n")
#-------------------------PART 1-------------------------#

def parse_input(data):
    instructions = data[0]
    nodes = {}
    for line in data[2:-1]:
        line = line.split(" = ")
        targets = line[1].split(", ")
        left = targets[0][1:]
        right = targets[1][:-1]
        nodes[line[0]] = {'L': left, 'R': right}

    return instructions, nodes


instructions, nodes = parse_input(data)


def get_steps(instructions, nodes):
    current = "AAA"
    target = "ZZZ"
    steps = 0
    i = 0
    while current != target:
        steps += 1
        current = nodes[current][instructions[i]]
        i += 1
        if i == len(instructions):
            i = 0
    return steps

print(get_steps(instructions, nodes))

#-------------------------PART 2-------------------------#

def get_steps2(instructions, nodes):
    current = [node for node in nodes if node.endswith("A")]

    steps_for_all = []
    for node in current:
        pos = node
        steps = 0
        i = 0
        while not pos.endswith("Z"):
            steps += 1
            pos = nodes[pos][instructions[i]]
            i += 1
            if i == len(instructions):
                i = 0
        steps_for_all.append(steps)

    return math.lcm(*steps_for_all)

print(get_steps2(instructions, nodes))