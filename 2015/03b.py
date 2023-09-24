import sys
import copy
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

def move(dirn,location):
    # North increases y by 1
    # East increases x by 1
    # South decreases y by 1
    # West decreases x by 1
    if dirn == "^": #N
        location[1] += 1
    elif dirn == ">": #E
        location[0] += 1
    elif dirn == "v": #S
        location[1] -= 1
    elif dirn == "<": #W
        location[0] -= 1
    return location

data = aoc.read("2015","03","str")
houses = 1
visited = [[0,0]]
santa = [0,0]
robo_santa = [0,0]

for i in range(len(data)):
    if i%2==0:
        new_loc = move(data[i],santa)
    else:
        new_loc = move(data[i],robo_santa)
    if new_loc not in visited:
        visited.append(new_loc)
        houses+=1
    if i%2==0:
        santa = copy.deepcopy(new_loc)
    else:
        robo_santa = copy.deepcopy(new_loc)


print(f"santa and robo-santa visited {houses} houses")
