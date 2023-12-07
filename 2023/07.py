import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

CARDS1 = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
CARDS2 = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]

class hand:
    def __init__(self, cards, bid, part):
        self.cards = cards
        self.bid = bid
        self.strength = None # low is bad
        self.unique = []
        self.label = []
        self.sorted = False

        self.check_type()
        self.what_kind_of_hand()
        if part == 2:
            self.the_jokers_are_jokering()

    def __repr__(self):
        return f"{self.cards}    {self.bid}    {self.strength}"
    
    def the_jokers_are_jokering(self):
        # get how many jokers
        numj = self.cards.count("J")
        if numj == 0: # you have no jokers
            return
        else: 
            if numj == 4:
                self.strength = 7 # turns 4 of a kind into 5 of a kind
            if numj == 3:
                if self.strength == 5:
                    self.strength = 7 # turns full house into 5 of a kind
                elif self.strength  == 4:
                    self.strength = 6 # turns 3 of a kind into 4 of a kind
            if numj == 2:
                if self.strength == 5:
                    self.strength = 7 # turns full house into 5 of a kind
                elif self.strength == 3:
                    self.strength = 6 # turns 2 pair into 4 of a kind
                elif self.strength == 2:
                    self.strength = 4 # turns 1 pair into 3 of a kind
            if numj == 1:
                if self.strength == 6:
                    self.strength = 7 # turns 4 of a kind into 5 of a kind
                elif self.strength == 4:
                    self.strength = 6 # turns 3 of a kind into 4 of a kind
                elif self.strength == 3:
                    self.strength = 5 # turns 2 pair into full house
                elif self.strength == 2:
                    self.strength = 4 # turns 1 pair into 3 of a kind
                elif self.strength == 1:
                    self.strength = 2 # turns high card into 1 pair

    def check_type(self):
        for char in self.cards:
            if char in self.unique: # card is repeated
                # increment the number of that card
                idx = self.unique.index(char)
                self.label[idx] += 1
            else: # card is unique (so far)
                self.unique.append(char)
                self.label.append(1)

    def what_kind_of_hand(self):
        # only 1 kind of card
        if len(self.unique) == 1: 
            self.strength = 7
        # 2 kinds of card, 1 appears 4 times
        elif len(self.unique) == 2 and 4 in self.label:
            self.strength = 6
        # 2 kinds of cards, 1 appears thrice
        elif len(self.unique) == 2:# and 3 in self.label:# and 2 in self.label:
            self.strength = 5
        # 3 kinds of cards, 1 appears thrice
        elif len(self.unique) == 3 and 3 in self.label:
            self.strength = 4
        # 2 kinds of cards, 2 appear twice
        elif len(self.unique) == 3 and self.label.count(2) == 2:
            self.strength = 3
        # 4 kinds of cards
        elif len(self.unique) == 4:
            self.strength = 2
        # 5 kinds of cards
        elif len(self.unique) == 5:
            self.strength = 1

def compare_two(card1,card2,part):
    if part == 1:
        CARDS = CARDS1
    else:
        CARDS = CARDS2
    for i in range(len(card1.cards)):
        idx1 = CARDS.index(card1.cards[i])
        idx2 = CARDS.index(card2.cards[i])
        # if card1 is stronger than card2
        if idx1 < idx2:
            return card1, card2
        # if card2 is stronger than card1
        elif idx2 < idx1:
            return card2, card1
        # neither is stronger, check next card

def sort_by_strength(hands):
    sorted_hands = []
    for strength in range(7,0,-1):
        for h in hands:
            if h.strength == strength and not h.sorted:
                sorted_hands.append(h)
                h.sorted = True
    return sorted_hands

def sort_by_card(sorted_hands,part):
    sorts = 0
    sorted = False
    while not sorted:
        for i in range(len(sorted_hands)-1):
            if sorted_hands[i+1].strength == sorted_hands[i].strength:
                card1, card2 = compare_two(sorted_hands[i],sorted_hands[i+1],part)
                if sorted_hands[i] != card1:
                    sorts += 1
                    sorted_hands[i] = card1
                    sorted_hands[i+1] = card2
        if sorts == 0:
            sorted = True
        sorts = 0
    return sorted_hands

def add_up_the_bids(sorted_hands):
    sorted_hands.reverse()
    total = 0
    for i in range(len(sorted_hands)):
        total += (i+1) * sorted_hands[i].bid
    return total

def run(part,data):
    hands = []
    for i in range(len(data)):
        h = hand(data[i][0], int(data[i][1]),part)
        hands.append(h)
    sorted_hands = sort_by_strength(hands)
    sorted_hands = sort_by_card(sorted_hands,part)
    total = add_up_the_bids(sorted_hands)
    return total

def part_one(data):
    total = run(1,data)
    return total

def part_two(data):
    total = run(2,data)
    return total

data = aoc.read("2023","07","list")

for i in range(len(data)):
    data[i] = data[i].replace("\n","")
    data[i] = data[i].split()

print(f"the answer to part one is {part_one(data)}")
print(f"the answer to part two is {part_two(data)}")