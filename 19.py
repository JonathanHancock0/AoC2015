import re


def calibrate(molecule, operations):
    outputs = []
    for op in operations:
        target_length = len(op[0])
        locations = [m.start() for m in re.finditer(op[0], molecule)]   #Every position where the target string can be found
        for l in locations:
            outputs.append(molecule[:l] + op[1] + molecule[(l+target_length):])
    outputs = list(dict.fromkeys(outputs))                              #Turns to a dictionary and back (for deduping)
    return len(outputs)

def fabricate(molecule, operations):
    '''
    Two sets of molecules, those which can be transformed, and those that can't. The latter is [Ar, Rn, Y].
    If we call the sets X and . then the transformations are X -> XX, X -> X.X., X -> X.X.X. X -> X.X.X.X.
    Since a given pair of X can only be reduced to one other X, ordering shouldn't matter.
    We will prioritise removing . since then a string of length N will only take N-1 more steps
    '''
    reduce = []
    transform = []
    dots = ["Ar", "Rn", "Y"]
    steps = 0
    
    for op in operations:
        red = True
        for d in dots:
            if d in op[0]:
                transform.append(op)
                red = False
                break
        if red:
            reduce.append(op)

    while True:
        keep_t = True
        keep_r = True
        while keep_t:
            keep_t = False
            for t in transform:
                target_length = len(t[0])
                targets = [m.start() for m in re.finditer(t[0], molecule)]      #Everywhere we can do this transformation
                if targets != []:                                               #If we can do something, do the first in the list
                    pos = targets[0]
                    molecule = molecule[:pos] + t[1] + molecule[(pos+target_length):]
                    steps += 1
                if len(targets) > 1:                                            #if there was more to transform, we need to keep going
                    keep_t = True

        nodot = True
        for d in dots:                      #We see if we got rid of all the dots yet
            if d in molecule:
               nodot = False
               break
        if nodot:
            steps += (len(molecule)-1)
            break

        while keep_r:                       #Otherwise we reduce as much as we can, then restart
            keep_r = False
            for r in reduce:
                target_length = len(r[0])
                targets = [m.start() for m in re.finditer(r[0], molecule)]      #Everywhere we can do this reduction
                if targets != []:                                               #If we can do something, do the first in the list
                    pos = targets[0]
                    molecule = molecule[:pos] + r[1] + molecule[(pos+target_length):]
                    steps += 1
                if len(targets) > 1:                                            #if there was more to reduce, we need to keep going
                    keep_r = True
    return steps  

if __name__ == '__main__':
    operations = []
    outputs = []
    f = open("inputs/19.txt")
    for line in f:
        if line.strip('\n') == "":
            break
        result = re.search(r'(\b.+\b)\s=>\s(\b.+\b)', line)
        operations.append(result.groups())
    molecule = f.readline()
    f.close()

    r_operations = [(o[1] , o[0]) for o in operations]

    print(f"{calibrate(molecule, operations)} distinct molecules can be made in one step.")
    print(f"{fabricate(molecule, r_operations)} steps to make the target molecule.")
