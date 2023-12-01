import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
STRDIGITS = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def part_one(data):
    # get numbers from string
    nums = get_nums(data)

    # get the digits at the start and end
    endnums = get_endnums(nums)

    # add up the total
    total = get_total(endnums)

    return total

def part_two(data):
    n = []
    for i in range(len(data)):
        currentstr = ""
        temp = ""
        for char in data[i]: # for each character in the string
            currentstr += char
            for s in STRDIGITS: # for each number string
                if s in currentstr: # if a number string is in the current string
                    temp = temp + str(STRDIGITS.index(s)) # add the index of the number string
                    currentstr = currentstr[-1] # there can be one letter of overlap between number strings
            for d in DIGITS: # for each digit
                if d in currentstr: # if digit is in the current string
                    temp = temp + str(d) # add the digit
                    currentstr = "" # no overlap between digits
        n.append(temp)

    # get numbers from string
    nums = get_nums(n)

    # get the digits at the start and end
    endnums = get_endnums(nums)

    # add up the total
    total = get_total(endnums)

    return total

def get_nums(data):
    nums = []
    for line in data:
        num = aoc.get_nums_from_string(line)
        nums.append(num)
    return nums

def get_endnums(nums):
    endnums = []
    for num in nums:
        if type(num)==list: # if there was more than one number in the original string
            # get the first digit of the first number and the last digit of the last number
            newnum = int(str(num[0])[0]+str(num[-1])[-1])
        else: # if there is only one number in the string
            newnum = int(str(num)[0]+str(num)[-1])
        endnums.append(newnum)
    return endnums

def get_total(endnums):
    total = 0
    for num in endnums:
        total += num
    return total

data = aoc.read("2023","01","list")

for i in range(len(data)):
    data[i] = data[i].replace("\n","")

print(f"the answer to part one is {part_one(data)}")
print(f"the answer to part two is {part_two(data)}")