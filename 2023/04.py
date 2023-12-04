import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

class card:
    def __init__(self, winning, mine, id):
        self.winning = winning # stores winning cards
        self.mine = mine# stores my cards
        self.points = 0 # points for part 1
        self.id = id # card id
        self.howmany = 1 # how many of each card (part 2)
        self.tidy() # turn the strings of nums into ints

    def __repr__(self):
        return f"{self.id}    {self.winning}    {self.mine}    {self.points}"
    
    def tidy(self):
        temp = []
        for num in self.winning:
            if num != "":
                temp.append(int(num))
        self.winning = temp
        temp = []
        for num in self.mine:
            if num != "":
                temp.append(int(num))
        self.mine = temp

    def getwins(self): # gets the number of matches
        wins = 0
        for num in self.mine:
            if num in self.winning:
                wins += 1
        return wins

    def getpoints(self): # part 1
        wins = self.getwins()
        if wins > 0:
            self.points = 2 ** (wins - 1)

    def getnextcards(self): #part 2
        wins = self.getwins()
        return wins, self.howmany
    

def part_one(cards):
    total = 0

    for c in cards:
        c.getpoints()
        total += c.points
    return total

def part_two(cards):
    total = 0

    for i in range(len(cards)):
        c = cards[i]
        cards_affected, times = c.getnextcards()
        # cards affected is how many of the next cards we get new ones of
        # times is how many new cards
        for j in range(i+1,i+1+cards_affected):
            cards[j].howmany += times

    for c in cards:
        total += c.howmany
    return total
    
data = aoc.read("2023","04","list")
cards = []

for i in range(len(data)):
    data[i] = data[i].replace("\n","")
    data[i] = data[i].split(": ")
    idx = int(data[i][0][4:9])
    data[i][1] = data[i][1].split(" | ")
    winning = data[i][1][0].split(" ")
    mine = data[i][1][1].split(" ")
    c = card(winning,mine,idx)
    cards.append(c)

print(f"the answer to part one is {part_one(cards)}")
print(f"the answer to part two is {part_two(cards)}")
