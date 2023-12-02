from Helpers.DataHelper import DataHelper

data = DataHelper(2023, 2).get_data()

#-------------------- Part 1 --------------------#
# 12 red, 13 green, 14 blue

class Game:

    exact_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def __init__(self, line: str):
        self.line = line
        self.parse_line(line)

    def parse_line(self, line: str):
        seperate = line.split(':')
        self.game_id = int(seperate[0].split(' ')[1].strip())
            
        game_data = seperate[1].split(';')
        game_data = [x.strip() for x in game_data]

        draws = []
        for draw in game_data:
            each = draw.split(',')
            draw_data = {}
            for i in each:
                i = i.strip()
                cubes = i.split(' ')
                draw_data[cubes[1]] = int(cubes[0])

            if 'red' not in draw_data:
                draw_data['red'] = 0
            if 'green' not in draw_data:
                draw_data['green'] = 0
            if 'blue' not in draw_data:
                draw_data['blue'] = 0
            draws.append(draw_data)
        self.draws = draws

    def check_possible(self):
        for draw in self.draws:
            if (
                    draw['red'] > Game.exact_cubes['red'] or
                    draw['green'] > Game.exact_cubes['green'] or
                    draw['blue'] > Game.exact_cubes['blue']
            ):
                return 0
        return self.game_id

    def get_minimum_possible(self):
        minimum = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for draw in self.draws:
            if draw['red'] > minimum['red']:
                minimum['red'] = draw['red']
            if draw['green'] > minimum['green']:
                minimum['green'] = draw['green']
            if draw['blue'] > minimum['blue']:
                minimum['blue'] = draw['blue']

        return minimum

    def calculate_product(self):
        minimum = self.get_minimum_possible()
        return minimum['red'] * minimum['green'] * minimum['blue']

    def __str__(self):
        return f'Game {self.game_id}: {self.draws}'



possible = [Game(x).check_possible() for x in data[:-1]]
solution = sum(possible)
print(f'Part 1 Solution: {solution}')


#____________________ Part 2 ____________________#
powers = [Game(x).calculate_product() for x in data[:-1]]
solution = sum(powers)
print(f'Part 2 Solution: {solution}')
