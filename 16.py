import re

class Sue:
    def __init__(self, number, data):
        self.number = number
        self.stuff = {}
        for i in range(len(data)//2):
            self.stuff[data[2*i]] = int(data[(2*i)+1])

    def checkPresence(self, word):
        for key in self.stuff:
            if key == word:
                return True
        return False
    
    def getValue(self, word):
        return self.stuff[word]

    def getNumber(self):
        return self.number

def checkSues(suelist, info):
    for s in suelist:
        ok = True
        for clue, amount in info.items():
            if s.checkPresence(clue):
                match clue:
                    case ("cats" | "trees"):
                        if s.getValue(clue) <= amount:
                            ok = False
                            break
                    case ("pomeranians" | "goldfish"):
                        if s.getValue(clue) >= amount:
                            ok = False
                            break
                    case _:
                        if s.getValue(clue) != amount :
                            ok = False
                            break
                
        if ok:
            return s.getNumber()

if __name__ == '__main__':
    info = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
    }
    suelist = []

    f = open("inputs/16.txt")
    for line in f:
        result = re.search(r'(\d+):\s(.+):\s(\d+),\s(.+):\s(\d+),\s(.+):\s(\d+)', line)
        suelist.append(Sue(result.groups()[0] , result.groups()[1:]))

    possible = checkSues(suelist, info)
    print(f"Sue number {possible} is the correct one!")