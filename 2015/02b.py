import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

def get_ribbon(present):
    dims = aoc.str_to_list(present,"x","int")
    ribbon = 0
    ribbon += volume(dims)
    ribbon += perimeter(dims)
    return ribbon

def perimeter(dims):
    smallest = aoc.get_smallest(dims,2)
    return (2*smallest[0])+(2*smallest[1])

def volume(dims):
    return dims[0] * dims[1] * dims[2]

data = aoc.read("2015","02","list")
ribbon = 0

for present in data:
    ribbon += get_ribbon(present)

print(ribbon)