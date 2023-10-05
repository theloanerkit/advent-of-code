import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc


data = aoc.read("2015","08","list")


def actual_chars(data):
    chars = 0
    for line in data:
        chars+=len(line)
    return chars

def string_chars(data):
    chars = 0
    for line in data:
        chars+=extra_chars(line)#get_string_chars(line)
    return chars

def extra_chars(line):
    chars = 0
    i=0
    while i < len(line):
        #print(i)
        current_char = line[i]
        if current_char == '"':
            #print("quote mark")
            chars+=1
            pass
        elif current_char == '\\':
            if line[i+1] == '\\' or line[i+1] == '"':
                #print("backslash")
                chars+=1
                chars+=3 # extra
                i+=1
            elif line[i+1] == 'x':
                #print("hex")
                chars+=1
                chars+=4 # extra
                i+=3
        else:
            chars+=1
        i+=1
    #print(chars)
    chars+=4 # for start and end quotes
    print(chars)
    return chars


#print(data)
a = actual_chars(data)
b = string_chars(data)
print(f"a = {a}")
print(f"b = {b}")
print(f"b - a = {b-a}")