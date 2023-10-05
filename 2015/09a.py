import sys
import itertools
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

NODE_NAMES = []
NODES = []
def build_nodes(data):
    for line in data:
        words = line.split()
        for word in words:
            if word != "to" and word != "=" and not word.isdigit()and word not in NODE_NAMES:
                NODE_NAMES.append(word)
                node = aoc.Node(word)
                NODES.append(node)

def build_connections(data):
    for line in data:
        words = line.split()
        node_idx = NODE_NAMES.index(words[0])
        node = NODES[node_idx]
        conn_idx = NODE_NAMES.index(words[2])
        conn = NODES[conn_idx]
        #print(node_idx,conn_idx)
        #print(node,conn)
        dist = int(words[-1])
        node.routes.append(conn)
        node.dists.append(dist)
        conn.routes.append(node)
        conn.dists.append(dist)

def route_distance(route):
    dist = 0
    for i in range(len(route)-1):
        current = route[i]
        next = route[i+1]
        idx = current.routes.index(next)
        dist += current.dists[idx]
    return dist


data = aoc.read("2015","09","list")
#print(data)
build_nodes(data)
build_connections(data)
for n in NODES:
    print(n)

routes = list(itertools.permutations(NODES))
dists = []
for r in routes:
    dists.append(route_distance(r))

print(f"the shortest route for santa to take is {min(dists)}")