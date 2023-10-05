import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

data = aoc.read("2015","12","str")
#print(data)
test = '{"a":{"b":4},"c":-1}'
nums = aoc.get_nums_from_string(data)
print(nums)

total = 0
for num in nums:
    total+=num
print(total)