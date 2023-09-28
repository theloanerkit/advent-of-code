import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

WIRES = []
GATES = []
WIRE_NAMES = []
GATE_TYPES = ["RSHIFT","OR","NOT","AND","LSHIFT"]


class Wire:
    def __init__(self, name):
        self.name = name
        #self.signal = format(signal,"b")
        self.signal = None
            
    def __repr__(self):
        return f"name: {self.name}    signal: {self.signal}"

class AND:
    def __init__(self, wire_one, wire_two, wire_out):
        self.wire_one = wire_one
        self.wire_two = wire_two
        self.wire_out = wire_out

    def operate(self):
        self.wire_out.signal = self.wire_one.signal & self.wire_two.signal

class OR:
    def __init__(self, wire_one, wire_two, wire_out):
        self.wire_one = wire_one
        self.wire_two = wire_two
        self.wire_out = wire_out

    def operate(self):
        self.wire_out.signal = self.wire_one.signal | self.wire_two.signal

class NOT:
    def __init__(self, wire_in, wire_out):
        self.wire_in = wire_in
        self.wire_out = wire_out

    def operate(self):
        self.wire_out.signal = ~self.wire_in.signal

class LSHIFT:
    def __init__(self, wire_in, bits,wire_out):
        self.wire_in = wire_in
        self.bits = bits
        self.wire_out = wire_out

    def operate(self):
        self.wire_out.signal = self.wire_in.signal << self.bits

class RSHIFT:
    def __init__(self, wire_in, bits,wire_out):
        self.wire_in = wire_in
        self.bits = bits
        self.wire_out = wire_out

    def operate(self):
        self.wire_out.signal = self.wire_in.signal >> self.bits

GATE_CLASS = [RSHIFT,OR,NOT,AND,LSHIFT]

def get_wire(name):
    idx = WIRE_NAMES.index(name)
    return WIRES[idx]

def get_wires(string):
    string = string.split()
    for word in string:
        if word not in GATE_TYPES and word != "->" and not word.isdigit():
            # word is a wire
            if word not in WIRE_NAMES:
                WIRE_NAMES.append(word)
                WIRES.append(Wire(word))

def is_a_gate(string):
    string = string.split()
    for i in range(len(string)):
        if string[i] in GATE_TYPES:
            return i
    return -1

# FIXME breaks when AND, OR input contains integer
def build_gate(string,idx):
    string = string.split()
    gate_type = GATE_TYPES.index(string[idx])
    out = get_wire(string[-1])
    if gate_type == 2: #NOT gate
        in_1 = string[1]
        in_1_id = WIRE_NAMES.index(in_1)
        in_1 = WIRES[in_1_id]

        gate = GATE_CLASS[gate_type](in_1,out)
    elif gate_type == 0 or gate_type == 4: #LSHIFT or RSHIFT
        in_1 = string[0]
        in_1_id = WIRE_NAMES.index(in_1)
        in_1 = WIRES[in_1_id]
        shift = int(string[2])

        gate = GATE_CLASS[gate_type](in_1,shift,out)
    elif gate_type == 1 or gate_type == 3: #AND or OR
        in_1 = string[0]
        if in_1.isdigit():
            sig = int(in_1)
            in_1 = Wire("nan")
            in_1.signal = sig
        else:
            in_1_id = WIRE_NAMES.index(in_1)
            in_1 = WIRES[in_1_id]
        in_2 = string[2]
        if in_2.isdigit():
            sig = int(in_2)
            in_2 = Wire("nan")
            in_2.signal = sig
        else:
            in_2_id = WIRE_NAMES.index(in_2)
            in_2 = WIRES[in_2_id]

        gate = GATE_CLASS[gate_type](in_1,in_2,out)
    GATES.append(gate)
    return gate

def wires_in_cmd(string):
    string = string.split()
    #print(string)
    wires_in = []
    for i in range(0,len(string)-2):
        if string[i] not in GATE_TYPES and not string[i].isdigit():
            wires_in.append(string[i])
    return wires_in

def wires_have_signal(wires):
    for w in wires:
        wire = get_wire(w)
        if wire.signal == None:
            return False
    return True


data = aoc.read("2015","07b","list")

#FIXME
# get wires
for string in data:
    get_wires(string)
#for w in WIRES:
#    print(w)

##FIXME
## get gates
#for string in data:
#    gate_pos = is_a_gate(string)
#    if gate_pos != -1:
#        build_gate(string, gate_pos)


rmv = []
for i in range(len(data)):
    string = data[i]
    string = string.split()
    if len(string)==3 and string[0].isdigit():
        wire = get_wire(string[2])
        wire.signal = int(string[0])
        rmv.insert(0,i)
print(len(data))
for idx in rmv:
    data.pop(idx)
print(len(data))
idx = 0
stop = False
while len(data)>1 and not stop:
    string = data[idx]
    wires_in = wires_in_cmd(string)
    #print(wires_in)
    gate_idx = is_a_gate(string)
    #if len(data) == 301:
    #    print(string)
    #    print(wires_in)
    #    print(f"signal: {wires_have_signal(wires_in)}")
    #    print(gate_idx)
    #    input()
        
    if wires_have_signal(wires_in) and gate_idx != -1:
        gate = build_gate(string,gate_idx)
        print(f"GATE: {gate}")
        gate.operate()
        print(gate.wire_out)
        data.pop(idx)
        print(len(data))
        idx-=1
        #stop=True
    idx+=1
    if idx>=len(data):
        idx = 0

    #if len(data) == 301:
    #    stop=True
print(data)
wire_lx_idx = WIRE_NAMES.index("lx")
wire_lx = WIRES[wire_lx_idx]
print(wire_lx)


#for wire in WIRES:
#    print(wire.name,wire.signal)