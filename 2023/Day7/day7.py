from Helpers.DataHelper import DataHelper

data = DataHelper(2023, 7).get_data()[:-1]

#--------------------- Part 1 ---------------------#

class Hand:
    cards_rank = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7' : 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }
    def __init__(self, line):
        split = line.split()
        self.hand = split[0]
        self.bid = split[1]

    def get_type(self):
        cards = {}
        for card in self.hand:
            cards[card] =  cards[card] + 1 if card in cards else 1
        if len(cards) == 1:
            return 1
        if len(cards) == 2:
            if 4 in cards.values():
                return 2
            return 3
        if len(cards) == 3:
            if 3 in cards.values():
                return 4
            return 5
        if len(cards) == 4:
            return 6
        return 7

    def __lt__(self, other):
        type1 = self.get_type()
        type2 = other.get_type()
        if type1 > type2:
            return True
        if type1 == type2:
            for i in range(len(self.hand)):
                if self.cards_rank[self.hand[i]] < self.cards_rank[other.hand[i]]:
                    return True
                if self.cards_rank[self.hand[i]] > self.cards_rank[other.hand[i]]:
                    return False
        return False
    
    def __repr__(self):
        return f"Hand: {self.hand} Bid: {self.bid}"
    
hands = [Hand(line) for line in data]
hands.sort()
res = [i*int(hands[i-1].bid) for i in range(1, len(hands)+1)]
print(f"Solution 1: {sum(res)}")
#--------------------- Part 2 ---------------------#

class HandJoker(Hand):
    cards_rank = Hand.cards_rank
    cards_rank['J'] = 1

    def __init__(self, line):
        super().__init__(line)

    def get_type(self):
        cards = {}
        for card in self.hand:
            cards[card] =  cards[card] + 1 if card in cards else 1
        jokers = cards['J'] if 'J' in cards else 0
        if len(cards) == 1:
            return 1
        if len(cards) == 2:
            if jokers:
                return 1
            if 4 in cards.values():
                return 2
            return 3
        if len(cards) == 3:
            if jokers == 3 or jokers == 2:
                return 2
            if jokers == 1:
                if 3 in cards.values():
                    return 2
                return 3
            if 3 in cards.values():
                return 4
            return 5
        if len(cards) == 4:
            if jokers == 2 or jokers == 1:
                return 4
            return 6
        if jokers:
            return 6
        return 7
    

    def __lt__(self, other):
        type1 = self.get_type()
        type2 = other.get_type()
        if type1 > type2:
            return True
        if type1 == type2:
            for i in range(len(self.hand)):
                if self.cards_rank[self.hand[i]] < self.cards_rank[other.hand[i]]:
                    return True
                if self.cards_rank[self.hand[i]] > self.cards_rank[other.hand[i]]:
                    return False
        return False

hands = [HandJoker(line) for line in data]
hands.sort()
res = [i*int(hands[i-1].bid) for i in range(1, len(hands)+1)]
print(f"Solution 2: {sum(res)}")