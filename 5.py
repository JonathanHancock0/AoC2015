import re

def vowelTest(line):
    #There must be a minimum of three vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    vcount = 0

    for char in line:
        if char in vowels:
            vcount += 1
    #print(f"{vcount} vowels")
    return (vcount > 2)

def repeatTest(line):
    #There must be a letter immediately repeated (XX)
    prev = line[0]
    for char in line[1:]:
        if prev == char:
            return True
        prev = char
    return False

def excludeTest(line):
    #Must not contain any of these substrings
    bad = ["ab", "cd", "pq", "xy"]

    for test in bad:
        result = re.search(test, line)
        if result != None:
            #print(f"{test} found")
            return False
    return True

def twoPairsTest(line):
    #There must be two copies of a pair of letters
    #regex means 0 or more characters, then a particular character twice, then 0 or more characters, then the particular character twice more
    result = re.search(r'.*(.)\1.*\1{2}', line)
    if result != None:
        return False
    return True


def displacedPairTest(line):
    #There must be a letter that is repeated, with the two letters seperated by exactly one (XaX)
    first = line[0]
    second = line[1]
    for char in line[2:]:
        if first == char:
            return True
        first = second
        second = char
    return False


if __name__ == '__main__':
    nice = 0
    old = False
    f = open("inputs/5test.txt")
    for line in f:
        l = line.strip('\n')
        if old:
            if not repeatTest(l):
                continue
            if not vowelTest(l):
                continue
            if not excludeTest(l):
                continue
            nice += 1
        else:
            if not displacedPairTest(l):
                print("DP failed")
                continue
            if not twoPairsTest(l):
                continue
            nice += 1

        

    print(f"{nice} strings are nice.")