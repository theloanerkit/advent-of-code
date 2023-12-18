import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc
import time
import heapq

class Node:
    def __init__(self, name, heat_lost,d_f,s_i):
        self.name = name
        self.heat_lost = heat_lost
        self.dij_dist = None # tentative distance for dijkstra (total heat lost)
        self.prev_node = None
        self.direction_from = d_f
        self.steps_inline = s_i
    
    def __repr__(self): # print method
        return f"{self.name} {self.direction_from} {self.steps_inline} {self.dij_dist}"
    
    def __lt__(self,other): # comparison method (for heap)
        if self.dij_dist == other.dij_dist == None:
            return True
        if self.dij_dist == None and other.dij_dist != None:
            return False
        if self.dij_dist != None and other.dij_dist == None:
            return True
        return self.dij_dist < other.dij_dist

def get_next_nodes(node,nodes):
    new_nodes = []
    left_right = ["l","r"]
    up_down = ["u","d"]
    for i in range(4):
        if i == 0:
            # go up
            new_pos = [node.name[0]-1,node.name[1]]
            new_dirn = "u"
        elif i == 1:
            # go right
            new_pos = [node.name[0],node.name[1]+1]
            new_dirn = "r"
        elif i == 2:
            # go down
            new_pos = [node.name[0]+1,node.name[1]]
            new_dirn = "d"
        elif i == 3:
            # go left
            new_pos = [node.name[0],node.name[1]-1]
            new_dirn = "l"

        if node.direction_from == new_dirn:
            new_steps = node.steps_inline +1
        else:
            new_steps = 1
        if new_pos[0]>=0 and new_pos[0]<len(data):
            # allowed row number
            if new_pos[1]>=0 and new_pos[1]<len(data[0]):
                # allowed col number
                if (node.direction_from in up_down and new_dirn in left_right) or (node.direction_from in left_right and new_dirn in up_down)or node.direction_from==None or node.direction_from==new_dirn:
                    if new_steps <= 3:
                        # allowed number of steps
                        new_node = next((n for n in nodes if (n.name==new_pos and n.direction_from==new_dirn and n.steps_inline==new_steps)),None)
                        if new_node != None:
                            new_nodes.append(new_node)
    return new_nodes

def dijkstra(nodes, start_node):
    start = time.time()
    unvisited = []
    seen = set()
    current_node = start_node
    current_node.dij_dist = 0
    run = True
    while run:
        next_nodes = get_next_nodes(current_node,nodes)
        for i in range(len(next_nodes)):
            next_node = next_nodes[i]
            if next_node not in seen:
                next_node_dist = next_node.heat_lost
                if next_node.dij_dist == None or next_node.dij_dist > current_node.dij_dist + next_node_dist:
                    next_node.dij_dist = current_node.dij_dist+next_node_dist
                    next_node.prev_node = current_node
                heapq.heappush(unvisited,next_node)
                if next_node.name == [len(data)-1,len(data[0])-1]:
                    return nodes,next_node
                seen.add(next_node)
                nodes_visited+=1
            else:
                skipped += 1
        current_node = heapq.heappop(unvisited)
    return nodes

data = aoc.read("2023","17","list")
nodes = []
directions = ["u","d","l","r"]
for i in range(len(data)):
    data[i] = data[i].replace("\n","")
    for j in range(len(data[i])):
        name = [i,j]
        for k in range(1,4):
            steps = k
            for l in range(4):
                dirn = directions[l]
                n = Node(name,int(data[i][j]),dirn,steps)
                nodes.append(n)
        if name == [0,0]:
            n = Node(name,int(data[i][j]),None,None)
            nodes.insert(0,n)

nodes,end_node = dijkstra(nodes,nodes[0])

n = end_node

while n.name != [0,0]:
    print(n,n.dij_dist)
    n = n.prev_node
print(n,n.dij_dist)
print()
print(f"distance = {end_node.dij_dist}")
