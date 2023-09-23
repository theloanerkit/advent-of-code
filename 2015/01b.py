import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

data = aoc.read("2015","01","str")

floor = 0
position = 0
basement = False

for char in data:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    position +=1
    if floor == -1 and not basement:
        print(f"santa first enters the basement at character {position}")
        basement = True

