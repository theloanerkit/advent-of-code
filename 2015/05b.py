import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

def has_repeated_pair(string):
    for i in range(len(string)-1):
        pair = string[i]+string[i+1]
        new_str = string[:i]+" "+string[i+2:]
        if pair in new_str:
            return True
    return False

def has_in_between(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

data = aoc.read("2015","05","list")
nice_strings = 0

for string in data:
    has_pair = has_repeated_pair(string)
    has_between = has_in_between(string)
    if (has_between) and (has_pair):
        nice_strings+=1

print(f"there are {nice_strings} nice strings")