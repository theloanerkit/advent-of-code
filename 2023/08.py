import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc
import math



class node:
    def __init__(self,name,left,right):
        self.name = name
        self.lname = left
        self.rname = right
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"{self.name}    {self.left.name}    {self.right.name}"

def build_nodes(data):
    nodes = []
    for line in data:
        name = line[0:3]
        left = line[7:10]
        right = line[12:15]
        n = node(name,left,right)
        nodes.append(n)
    for n in nodes:
        for m in nodes:
            if m.name == n.lname:
                n.left = m
            if m.name == n.rname:
                n.right = m
    return nodes

def condition_one(n):
    if n.name == "ZZZ":
        return True
    return False

def condition_two(n):
    if n.name[2] == "Z":
        return True
    return False

conditions = [condition_one,condition_two]

def find_the_end(c_idx,current_node,instructions):
    idx = 0
    steps = 0
    while not conditions[c_idx](current_node):
        char = instructions[idx]
        current_node = node_step(char,current_node)
        steps += 1
        idx = (idx+1) % len(instructions)

    return steps

def node_step(char,n):
    if char == "R":
        return n.right
    if char == "L":
        return n.left

def part_one(nodes,instructions):
    for n in nodes:
        if n.name == "AAA":
            current_node = n
    steps = find_the_end(0,current_node,instructions)
    return steps

def part_two(nodes,instructions):
    current_node = []
    for n in nodes:
        if n.name[2] == "A":
            current_node.append(n)

    steps_to_endpoint = []
    for n in current_node:
        steps_to_endpoint.append(find_the_end(1,n,instructions))
    total_steps = 1
    for num in steps_to_endpoint:
        total_steps = math.lcm(total_steps,num)
    return total_steps


data = aoc.read("2023","08","list")

for i in range(len(data)):
    data[i] = data[i].replace("\n","")
instructions = data[0]
data.pop(0)
data.pop(0)

nodes = build_nodes(data)

print(f"the answer to part one is {part_one(nodes,instructions)}")
print(f"the answer to part two is {part_two(nodes,instructions)}")