import sys
import copy
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

def move_santa(move,location):
    # North increases y by 1
    # East increases x by 1
    # South decreases y by 1
    # West decreases x by 1
    if move == "^": #N
        location[1] += 1
    elif move == ">": #E
        location[0] += 1
    elif move == "v": #S
        location[1] -= 1
    elif move == "<": #W
        location[0] -= 1
    return location


data = aoc.read("2015","03","str")

location = [0,0]
visited = [[0,0]]
house_count = 1

for move in data:
    new_location = move_santa(move,location)
    if new_location not in visited:
        visited.append(new_location)
        house_count += 1
    location = copy.deepcopy(new_location)

print(f"santa has visited {house_count} houses at least once")