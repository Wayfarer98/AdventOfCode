from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 16).get_data()[:-1]
# data = '''.|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|....'''
# data = data.split('\n')

#------------------ Part 1 ------------------#

positions = {complex(x, y): char for y, line in enumerate(data) for x, char in enumerate(line)}

def get_energized(todo):
    done = set()
    while todo:
        pos, dir = todo.pop()
        while not (pos, dir) in done:
            done.add((pos, dir))
            pos += dir
            match positions.get(pos):
                case '|':
                    dir = 1j
                    todo.append((pos, -dir))
                case '-':
                    dir = -1
                    todo.append((pos, -dir))
                case '/':
                    dir = -complex(dir.imag, dir.real)
                case '\\':
                    dir = complex(dir.imag, dir.real)
                case None:
                    break
    return len(set(pos for pos, _ in done)) - 1

print(f'Solution 1: {get_energized([(-1 , 1)])}')

#------------------ Part 2 ------------------#

res = list(map(get_energized, ([(pos-dir, dir)] for dir in (1, 1j, -1, -1j) for pos in positions if pos-dir not in positions)))
print(f'Solution 2: {max(res)}')