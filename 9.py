import re
import copy

class Route:
    def __init__(self, start, end, d):
        self.start = start
        self.end = end
        self.distance = d
    
    def __str__(self):
        n1 = min(self.start, self.end)
        n2 = max(self.start, self.end)
        return f"{n1} --> {n2}: {self.distance}"

class Routelist:
    def __init__(self):
        self.routes = []

    def Print(self):
        for r in self.routes:
            print(r)

    def find_route(self, x, y):
        for r in self.routes:
            if (x == r.start and y == r.end) or (y == r.start and x == r.end):
                return r.distance
    
    def add_route(self, start, end, d):
        self.routes.append(Route(start, end, d))

def generate_permutations(n, route=""):
    ''' Given an integer n, produces a list of strings representing all possible permutations of n objects'''
    if type(n) == int:
        numbers = list(range(n))
    else:
        numbers = n
    if len(numbers) == 1:
        final_route = route + str(numbers[0])
        return(final_route)
    else:
        output = []
        for n in numbers:
            newroute = route + str(n)
            newlist = copy.deepcopy(numbers)
            newlist.remove(n)
            to_add = generate_permutations(newlist, newroute)
            if type(to_add) == str:
                output.append(to_add)
            else:
                output.extend(to_add)
        return output



if __name__ == '__main__':
    f = open("inputs/9.txt")
    short = False
    namedict = {}
    r = Routelist()
    num = 0
    for line in f:
        result = re.search(r'(.+)\sto\s(.+)\s=\s(\d+)', line)
        place1 = result.groups()[0]
        place2 = result.groups()[1]
        d = int(result.groups()[2])

        if place1 in namedict.keys():
            n1 = namedict[place1]
        else:
            namedict[place1] = num
            n1 = num
            num += 1
        if place2 in namedict.keys():
            n2 = namedict[place2]
        else:
            namedict[place2] = num
            n2 = num
            num += 1

        r.add_route(n1, n2, d)
    f.close()
    possible = generate_permutations(num)         #list() turns range(n) into a list of all the number in the range
    if short:
        best = 999999999
        for permutation in possible:
            total = 0
            for i in range(num-1):
                x = int(permutation[i])
                y = int(permutation[i+1])
                total += r.find_route(x, y)
            if total < best:
                best = total
                goodperm = permutation

    else:
        best = -1
        for permutation in possible:
            total = 0
            for i in range(num-1):
                x = int(permutation[i])
                y = int(permutation[i+1])
                total += r.find_route(x, y)
            if total > best:
                best = total
                goodperm = permutation

    
    print(f"Best route is {goodperm}, total distance {best}")
            
