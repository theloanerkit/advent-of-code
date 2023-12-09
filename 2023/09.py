import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

class history:
    def __init__(self,values):
        self.values = values
        self.diff = []
        self.diff.append(values)
        while self.diff[-1].count(0) != len(self.diff[-1]):
            self.get_diffs()

    def __repr__(self):
        return f"{self.diff}"

    def get_diffs(self):
        newdiff = []
        for i in range(len(self.diff[-1])-1):
            newdiff.append(self.diff[-1][i+1]-self.diff[-1][i])
        self.diff.append(newdiff)

    def extrapolate(self,where):
        m = where
        if m == 0 :
            m = 1
        for i in range(len(self.diff)-1,-1,-1):
            if where == -1:
                newidx = len(self.diff[i])
            else:
                newidx = 0
            if self.diff[i] == self.diff[-1]:
                self.diff[i].insert(newidx,0)
            else:
                newnum = self.diff[i][where]+(-m*self.diff[i+1][where])
                self.diff[i].insert(newidx,newnum)

def run(histories,where):
    total = 0
    for h in histories:
        h.extrapolate(where)
        total += h.diff[0][where]
    return total

def part_one(histories):
    total = run(histories,-1)
    return total

def part_two(histories):
    total = run(histories,0)
    return total

data = aoc.read("2023","09","list")

histories = []

for i in range(len(data)):
    data[i] = data[i].replace("\n","")
    data[i] = aoc.get_nums_from_string(data[i],True)
    h = history(data[i])
    histories.append(h)


print(f"the answer to part one is {part_one(histories)}")
print(f"the answer to part two is {part_two(histories)}")