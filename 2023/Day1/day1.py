from Helpers.DataHelper import DataHelper
import numpy as np
import regex as re

data = DataHelper(2023, 1).get_data()


def get_first_and_last_num_as_int(text: str):
    f = "".join(list(filter(str.isnumeric, text)))
    if f == "":
        return 0
    if len(f) == 1:
        return int(f[0] + f[0])
    return int(f[0] + f[-1])


res = np.array([get_first_and_last_num_as_int(x) for x in data])
solution1 = np.sum(res)
print(f"Solution 1: {solution1}")

def get_first_and_last_int_and_pos(text: str):
    reg = r"[0-9]"

    matches = list(re.finditer(reg, text))

    if len(matches) == 0:
        return None, None

    first = (matches[0].group(), matches[0].start())
    last = (matches[-1].group(), matches[-1].start())

    if len(matches) == 1:
        return first, None

    return first, last

def convert_text_to_int(text: str):
    reg = r"(one|two|three|four|five|six|seven|eight|nine)"
    

    matches = list(re.finditer(reg, text, overlapped=True))

    if len(matches) == 0:
        return None, None

    first = (matches[0].group(1), matches[0].end()-1)
    last = (matches[-1].group(1), matches[-1].end()-1)


    if len(matches) == 1:
        return first, None

    return first, last

    
def get_first_and_last_from_text(text: str):
    str_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five":5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    first_int, last_int = get_first_and_last_int_and_pos(text)
    first_text, last_text = convert_text_to_int(text)
    L = [first_int, last_int, first_text, last_text]
    L = [x for x in L if x is not None]
    if len(L) == 0:
        return 0
    L = [(str_to_num[x[0]], x[1]) if x[0] in str_to_num else x for x in L]
    L.sort(key=lambda x: x[1])

    return int(str(L[0][0]) + str(L[-1][0]))

res = np.array([get_first_and_last_from_text(x) for x in data])
solution2 = np.sum(res)
print(f"Solution 2: {solution2}")
