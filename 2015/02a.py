import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

def get_paper(present):
    dims = aoc.str_to_list(present,"x","int")
    paper = 0
    paper += box_net(dims)
    paper += extra_paper(dims)
    return paper

def box_net(dims):
    return (2*dims[0]*dims[1])+(2*dims[1]*dims[2])+(2*dims[2]*dims[0])

def extra_paper(dims):
    smallest = aoc.get_smallest(dims,2)
    return smallest[0]*smallest[1]

data = aoc.read("2015","02","list")
paper = 0

for present in data:
    paper += get_paper(present)

print(paper)