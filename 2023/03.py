import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc
import copy

class gear:
    def __init__(self,row,col,num):
        self.row = row
        self.col = col
        self.num = num
        self.ratio = 0

def surrounding_chars(data,num,i,gears=False):
    # creates an empty string for storing surrounding characters
    string = ""
    # gets the index of the start of the number
    idx = data[i].index(str(num))
    # set the lower bound for getting characters above and below (includes diagonals)
    lower = idx-1
    if lower < 0:
        lower = 0
    # set the upper bound for getting characters above and below (includes diagonals)
    upper = idx + len(str(num)) + 1
    if upper > len(data[i]) - 1:
        upper = len(data[i]) - 1

    if i != 0: # if the number isn't in the top row
        above = data[i-1][lower:upper]
        string += above
        if "*" in above: # if there's a gear 
            gearrow = i - 1
            gearcol = lower + above.index("*")

    if i != len(data) - 1: # if the number isn't in the bottom row
        below = data[i+1][lower:upper]
        string += below
        if "*" in below: # if there's a gear
            gearrow = i + 1
            gearcol = lower + below.index("*")

    if idx != 0: # if the number isn't against the left edge
        left = data[i][idx-1]
        string += left
        if "*" in left: # if there's a gear
            gearrow = i
            gearcol = idx - 1

    if idx+len(str(num)) < len(data[i])-1: # if the number isn't against the right edge
        right = data[i][idx+len(str(num))]
        string+=right
        if "*" in right: # if there's a gear
            gearrow = i
            gearcol = idx + len(str(num))

    # replace the number with . to avoid duplicate numbers in the same line
    data[i] = data[i].replace(str(num),"."*len(str(num)),1)
    if gears: # if part 2
        for char in string:
            if char == "*":
                return True, data, gearrow, gearcol
        return False, data, -1, -1
    else: # if part 1
        for char in string:
            if char != "." and not char.isdigit(): # if there's a symbol in the string
                return True, data
        return False, data

def get_gear_ratios(gears):
    for i in range(len(gears)):
        for j in range(len(gears)):
            if i != j: # don't compare a gear with itself
                if gears[i].row == gears[j].row  and gears[i].col == gears[j].col: # if the gears are the same
                    if gears[i].ratio == 0 and gears[j].ratio == 0: # if the gear ratios have not yet been set
                        gears[i].ratio = gears[i].num * gears[j].num
                        gears[j].ratio = -1
    return gears

def part_one(data):
    part_nums = []
    
    for i in range(len(data)):
        # get the numbers in each row
        nums = aoc.get_nums_from_string(data[i])

        if type(nums) == list: # if there is more than one number
            for num in nums: # for each number
                # get chars around number
                part, data = surrounding_chars(data,num,i)
                if part: # if number is a part
                    part_nums.append(num)

        elif nums != "": # if there is one number
            # get chars around number
            part, data = surrounding_chars(data,num,i)
            if part: # if number is a part
                part_nums.append(nums)
    
    # add up all the part numbers
    total = 0
    for num in part_nums:
        total +=  num
    return total

def part_two(data):
    gears = []

    for i in range(len(data)):
        # get the numbers in each row
        nums = aoc.get_nums_from_string(data[i])

        if type(nums) == list: # if there is more than one number
            for num in nums: # for each number
                # get position of gear around number
                part, data, row, col = surrounding_chars(data,num,i,True)
                if part: # if there is a gear
                    # make a gear
                    g = gear(row,col,num)
                    gears.append(g)
        
        elif nums != "": # if there is one number
            # get position of gear around number
            part, data, row, col = surrounding_chars(data,num,i,True)
            if part: # if there is a gear
                # make a gear
                g = gear(row,col,nums)
                gears.append(g)

    # get gear ratios
    gears = get_gear_ratios(gears)

    # add up the gear ratios
    total = 0
    for g in gears:
        if g.ratio != -1:
            total += g.ratio
    
    return total

data = aoc.read("2023","03","list")
for i in range(len(data)):
    data[i] = data[i].replace("\n","")

print(f"the answer to part one is {part_one(copy.deepcopy(data))}")
print(f"the answer to part two is {part_two(copy.deepcopy(data))}")