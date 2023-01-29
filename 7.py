import re
import copy

class Instruction:
        def __init__(self, line):
            self.line = line
            result = re.search(r'(.+)\s\-\>\s([a-zA-Z]+)', self.line)
            self.target = result.groups()[1]
            inst = result.groups()[0].split()
            self.binary = False
            self.waiting = True

            match len(inst):
                case 3:     #Binary
                    self.first = inst[0]
                    self.op = inst[1]
                    self.second = inst[2]
                    self.binary = True
                case 2:     #Unary
                    self.op = inst[0]
                    self.first = inst[1]
                case 1:     #Assignment
                    self.op = "ASSIGN"
                    self.first = inst[0]

        def __str__(self):
            return self.line

def process(queue, alt=False, b=0):
    wires = {}
    for q in queue:             #Do all the initial assignments of numbers to variables
        if q.op == "ASSIGN" and q.first.isnumeric():
            wires[q.target] = int(q.first)
            q.waiting = False
    queue = [q for q in queue if q.waiting]

    if alt:
        wires['b'] = b

    while queue != []:
        for q in queue:     #First we check if we have the required information
            if q.first.isnumeric():
                first = int(q.first)
            else:
                if q.first not in wires.keys():
                    continue
                first = wires[q.first]
            if q.binary:
                if q.second.isnumeric():
                    second = int(q.second)
                else:
                    if q.second not in wires.keys():
                        continue
                    second = wires[q.second]
            match q.op:
                case "AND":
                    wires[q.target] = first & second
                case "OR":
                    wires[q.target] = first | second
                case "LSHIFT":
                    wires[q.target] = first << second
                case "RSHIFT":
                    wires[q.target] = first >> second
                case "NOT":
                    wires[q.target] = ~first
                case "ASSIGN":
                    wires[q.target] = first
            q.waiting = False
        queue = [q for q in queue if q.waiting]

    return wires['a']

if __name__ == '__main__':
    f = open("inputs/7.txt")
    queue = []
    for line in f:
        queue.append(Instruction(line))
    f.close()

    x = copy.deepcopy(queue)
    y = copy.deepcopy(queue)
    a1 = process(x)
    print(a1)
    a2 = process(y, alt=True, b=a1)
    print(a2)
        



    