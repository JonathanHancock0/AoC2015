import re
import copy

class SeatData:
    def __init__(self, g, namedict):
        self.me = namedict[g[0]]
        if g[1] == "gain":
            self.score = int(g[2])
        else:
            self.score = -int(g[2])
        self.them = namedict[g[3]]

    def __str__(self):
        out = f"Me = {self.me} Them = {self.them} Score = {self.score}"
        return out

class SeatDataManager:
    def __init__(self):
        self.data = []
        self.namedict = {}
        self.namecount = 0

    def __str__(self):
            return f"{len(self.data)} objects saved. Name to number mapping is {self.namedict}"

    def addData(self, g):
        if g[0] not in self.namedict.keys():
            self.namedict[g[0]] = self.namecount
            self.namecount += 1
        if g[3] not in self.namedict.keys():
            self.namedict[g[3]] = self.namecount
            self.namecount += 1
        self.data.append(SeatData(g, self.namedict))

    def search(self, x, y):
        for entry in self.data:
            if (entry.me == x and entry.them == y):
                return entry.score
    
    def selfInsert(self):
        self.namedict["me"] = self.namecount
        self.namecount += 1

        for name in self.namedict:
            if name != "me":
                tup1 = ("me", "gain", "0", name)
                tup2 = (name, "gain", "0", "me")
                self.data.append(SeatData(tup1, self.namedict))
                self.data.append(SeatData(tup2, self.namedict))      
    
    def generate_permutations(self, n, route=""):
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
                to_add = self.generate_permutations(newlist, newroute)
                if type(to_add) == str:
                    output.append(to_add)
                else:
                    output.extend(to_add)
            return output

    def findBest(self, withme=False):
        bestScore = -999999999
        if withme:
            self.selfInsert()
        plist = self.generate_permutations(self.namecount)
        for perm in plist:
            score = 0
            #Do the edges manually
            score += self.search(int(perm[0]) , int(perm[-1]))
            score += self.search(int(perm[0]) , int(perm[1]))
            score += self.search(int(perm[-1]) , int(perm[0]))
            score += self.search(int(perm[-1]) , int(perm[-2]))
            #Now do the middle people
            for i in range(1, self.namecount-1):
                score += self.search(int(perm[i]) , int(perm[i+1]))
                score += self.search(int(perm[i]) , int(perm[i-1]))
            if score > bestScore:
                bestScore = score 
                bestPerm = perm
        return (bestPerm, bestScore)

if __name__ == '__main__':
    f = open("inputs/13.txt")
    s = SeatDataManager()
    for line in f:
        result = re.search(r'(\b.+\b)\s.+\s(\b.+\b)\s(\d+).+(\b.+\b)', line)
        s.addData(result.groups())
    f.close()
    answer = s.findBest(withme=True)
    print(f"The optimum solution is {answer[0]}, with score {answer[1]}")