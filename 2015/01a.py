import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

data = aoc.read("2015","01","str")

floor = 0

for char in data:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

print(floor)