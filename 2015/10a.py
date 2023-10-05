import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

def split_groups(string):
    string_split = []
    next_string = ""
    for i in range(len(string)):
        if next_string == "": # next string is empty, start a new next string
            next_string+=string[i]
        else:
            if next_string[-1] == string[i]: # last char of next string is the same as the next char, keep adding
                next_string+=string[i]
            else: # next character is different
                string_split.append(next_string)
                next_string = ""
                next_string+=string[i]
    string_split.append(next_string)
    return string_split

def look_and_say(split_string):
    new_string = ""
    for elem in split_string:
        new_string+=str(len(elem))
        new_string+=elem[0]
    return new_string

data = aoc.read("2015","10","str")
#print(data)
#print(split_groups(data))

for i in range(40):
    split_data = split_groups(data)
    data = look_and_say(split_data)

print(len(data))
