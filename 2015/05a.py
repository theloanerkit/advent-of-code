import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

VOWELS = ["a","e","i","o","u"]
BADSTRINGS = ["ab","cd","pq","xy"] 

def contains_bad(string):
    for b in BADSTRINGS:
        if b in string:
            return True
    return False

def vowel_count(string):
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    return count

def contains_double(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

nice_strings = 0

data = aoc.read("2015","05","list")

for string in data:
    is_bad = contains_bad(string)
    vowel_num = vowel_count(string)
    has_double = contains_double(string)
    if (not is_bad) and (vowel_num >= 3) and (has_double):
        nice_strings += 1

print(f"there are {nice_strings} nice strings")
