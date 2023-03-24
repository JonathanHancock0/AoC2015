import re
def decode(filename):
    f = open(filename)
    total = 0
    for line in f:
        line = line.strip('\n')
        line = line[1:-1]
        diff = 2
        i = 0
        while i < len(line):
            if line[i] == '\\':
                if line[i+1] == 'x':    #Character encoded as /xij (i and j are hex digits)
                    diff += 3
                    i += 3 
                else:
                    diff += 1
                    i += 1
            i += 1
        total += diff
    f.close()
    return total

def encode(filename):
    f = open(filename)
    total = 0
    for line in f:
        line = line.strip('\n')
        line = line[1:-1]
        increase = 4
        for char in line:
            if char == '\\' or char == '\"':
                increase += 1
        total += increase
    return total

if __name__ == '__main__':
    answer1 = decode("inputs/8.txt")
    answer2 = encode("inputs/8.txt")
    
    print(f"Characters in code - characters in memory = {answer1}")
    print(f"Characters in encoding - original characters = {answer2}")