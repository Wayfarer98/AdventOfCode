from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 4).get_data()
data = np.array([x for x in data[:-1]])

#------------------ Part 1 ------------------#

class Card:

    num_cards = {i: 1 for i in range(1, len(data)+1)}

    def __init__(self, line):
        self.line = line
        self.parse_line()

    def parse_line(self):
        line_data = self.line.split(': ')[1].strip()
        self.card_num = int(self.line.split(': ')[0].split()[1].strip())
        
        numbers = line_data.split(' | ')
        self.winning_numbers = numbers[0].strip().split()
        self.our_numbers = numbers[1].strip().split()

    def get_score(self):
        count = 0
        for num in self.our_numbers:
            if num in self.winning_numbers:
                count += 1

        return np.power(2, count-1) if count else count

    def parse_winning_amount(self):
        count = 0
        for num in self.our_numbers:
            if num in self.winning_numbers:
                count += 1

        for i in range(1, count+1):
            self.num_cards[self.card_num+i] += self.num_cards[self.card_num]

res = [Card(x).get_score() for x in data]
solution = sum(res)
print(f"Solution 1: {solution}")

#------------------ Part 2 ------------------#

for line in data:
    Card(line).parse_winning_amount()
solution = sum(Card.num_cards.values())
print(f"Solution 2: {solution}")
