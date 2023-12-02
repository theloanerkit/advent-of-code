import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

# setting up the max cube colours for part 1
RED = 12 
GREEN = 13
BLUE = 14
# use a list to give each colour an index
colours = ["red","green","blue"]
# make a list for reference for part 1
c_nums = [RED,GREEN,BLUE]
# game ID is stored at index 1
id_idx = 1

def part_one(data):
    # set up list to hold IDs of valid games
    ids = []
    # for each game
    for game in data:
        draws = int((len(game)-2)/2)
        count = 0
        # loop through every other element in the list, starting from index 2
        for i in range(2,len(game),2):
            # index of the colour of the current cube
            col_idx = colours.index(game[i+1][:-1]) # index we loop through is the number of cubes, each colour has an extra char on the end
            # if amount of cubes requested is less than or equal to cubes available
            if int(game[i])<=c_nums[col_idx]:
                count+=1
        # if we could draw all cubes successfully
        if count == draws:
            # add ID to list of successful IDs
            ids.append(int(game[id_idx][:-1]))

    # add up the total
    total = 0
    for i in ids:
        total += i
    return total

def part_two(data):
    # set up list to hold set powers for each game
    set_powers = []
    # for each game
    for game in data:
        draws = int((len(game)-2)/2)
        count = 0
        # set up list for storing cubes required for each game, indecies match with colours list
        mincube = [0,0,0]
        # loop through every other element in the list, starting from index 2
        for i in range(2,len(game),2):
            # index of the colour of the current cube
            col_idx = colours.index(game[i+1][:-1])
            # if number of cubes stored is less than cubes we need
            if mincube[col_idx]<int(game[i]):
                # set number of cubes to what we need
                mincube[col_idx]=int(game[i])
        # append the multiplied list to set_powers
        set_powers.append(aoc.multiply_list(mincube))
    # add up the total
    total = 0
    for i in set_powers:
        total += i
    return total

data = aoc.read("2023","02","list")

for i in range(len(data)):
    data[i] = data[i].replace("\n","")
    data[i] = data[i].split(" ")
    data[i][-1]+=";" # adds an extra character to the final string, so slicing is easier

print(f"the answer to part one is {part_one(data)}")
print(f"the answer to part two is {part_two(data)}")