import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

def get_coords(string):
    coords = []
    for word in string:
        if word.isdigit():
            coords.append(int(word))
    return coords # coords [x_start,y_start,x_end,y_end]

def toggle(grid,coords):
    for row in range(coords[1],coords[3]+1):
        for col in range(coords[0],coords[2]+1):
            if grid[row][col] == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = 0
    return grid

def turn(grid,coords,set):
    for row in range(coords[1],coords[3]+1):
        for col in range(coords[0],coords[2]+1):
            if set == "on":
                grid[row][col] = 1
            elif set == "off":
                grid[row][col] = 0
    return grid

data = aoc.read("2015","06","list")
grid = aoc.build_grid(1000,1000,0)
# top left is 0,0
# bottom right is 999,999

for string in data:
    string = string.replace(","," ").split()
    coords = get_coords(string)
    if string[0] == "toggle":
        grid = toggle(grid,coords)
    elif string[0] == "turn":
        grid = turn(grid,coords,string[1])

lights_on = 0
for row in grid:
    lights_on += row.count(1)

print(f"there are {lights_on} lights on")