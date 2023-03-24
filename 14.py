import re

class Reindeer:
    def __init__(self, g):
        self.pos = 0
        self.points = 0
        self.name = g[0]
        self.speed = int(g[1])
        self.max_stamina = int(g[2])
        self.current_stamina = int(g[2])
        self.rest_total = int(g[3])
        self.rest_left = int(g[3])

    def __str__(self):
        return f"{self.name} has moved {self.pos} km. Current Stamina is {self.current_stamina}."

    def move(self):
        if self.current_stamina != 0:                       #If it's not too tired, it moves
            self.pos += self.speed
            self.current_stamina -= 1
        else:
            self.rest_left -= 1
            if self.rest_left == 0:                         #If the rest is over
                self.current_stamina = self.max_stamina     #Regain all stamina
                self.rest_left = self.rest_total            #And reset the rest for next time
    def getName(self):
        return self.name

    def getPos(self):
        return self.pos

    def getPoints(self):
        return self.points

    def award(self):
        self.points += 1

def test(r, t):
    for i in range(t):
        r.move()
        print(f"After {i+1} seconds, {r}")

if __name__ == '__main__':
    Reindeers = []
    time = 2503
    f = open("inputs/14.txt")
    for line in f: 
        result = re.search(r'(\b[a-zA-Z]+\b).+(\b\d+\b).+(\b\d+\b).+(\b\d+\b).+', line)
        Reindeers.append(Reindeer(result.groups()))
    f.close()

    #test(Reindeers[0], 500)
    front = -1
    for _ in range(time):
        for r in Reindeers:
            r.move()
            if r.getPos() > front:
                front = r.getPos()
        for r in Reindeers:
            if r.getPos() == front:
                r.award()
        
    bestDist = -1
    bestScore = -1
    for r in Reindeers:
        if r.getPos() > bestDist:
            bestDist = r.getPos()
            bestBoi = r.getName()
        if r.getPoints() > bestScore:
            bestScore = r.getPoints()
            bestScorer = r.getName()

    print(f"{bestBoi} is at the front, travelling {bestDist} km!")
    print(f"{bestScorer} is the winner, with {bestScore} points!")
    