import re

class Equipment:
    def __init__(self, values):
        self.name = values[0]
        self.cost = int(values[1])
        self.damage = int(values[2])
        self.armour = int(values[3])

    def __str__(self):
        return f"{self.name}: +{self.damage} atk, {self.armour} def, {self.cost} g"

    def getPrice(self):
        return self.cost

    def getAttack(self):
        return self.damage

    def getArmour(self):
        return self.armour

class Player:
    def __init__(self, set):
        self.hp = 100
        self.atk = 0
        self.arm = 0
        for item in set[0]:
            self.atk += item.getAttack()
            self.arm += item.getArmour()

    def getAttack(self):
        return self.atk

    def takeDamage(self, damage):
        realDamage = damage-self.arm
        if realDamage < 1:
            self.hp -= 1
        else:
            self.hp -= realDamage
    
    def isDead(self):
        return (self.hp <= 0)


class Boss:
    def __init__(self):
        self.hp = 104
        self.atk = 8
        self.arm = 1

    def getAttack(self):
        return self.atk

    def takeDamage(self, damage):
        realDamage = damage-self.arm
        if realDamage < 1:
            self.hp -= 1
        else:
            self.hp -= realDamage

    def isDead(self):
        return (self.hp <= 0)

def getAllSets(items):
    #A set has form ([i1, i2], cost)
    l1 = []
    for wep in items[0]:        #We have to buy one weapon
        l1.append(([wep], wep.getPrice())) 
    l2 = []
    for choice in l1:           #We can buy up to one armour
        l2.append(choice)       #This is where we buy no armour
        for arm in items[1]:
            newlist = choice[0] + [arm]
            newcost = choice[1] + arm.getPrice()
            l2.append((newlist , newcost))
    
    ringCombos = [([],0)]       #All the no ring options (there is one)
    for ring in items[2]:       #All the 1 ring options
        ringCombos.append(([ring] , ring.getPrice())) 
    end = len(items[2])
    for i in range(end-1):
        for j in range(i+1 , end):
            ringCombos.append(([items[2][i],items[2][j]] , (items[2][i].getPrice() + items[2][j].getPrice())))
    print(len(ringCombos))
    l3 = []
    for choice in l2:
        for rc in ringCombos:
            newlist = choice[0] + rc[0]
            newcost = choice[1] + rc[1]
            l3.append((newlist , newcost))
    return l3

def setValue(set):
    return set[1]

def fight(player, boss):
    while True:
        boss.takeDamage(player.getAttack())
        if boss.isDead():
            return True
        player.takeDamage(boss.getAttack())
        if player.isDead():
            return False

def findCheapestWin(items):
    sets = getAllSets(items)
    sets.sort(key=setValue)
    for s in sets:
        p = Player(s)
        b = Boss()
        if fight(p,b):
            return s[1]

def findExpensiveLoss(items):
    sets = getAllSets(items)
    sets.sort(reverse=True, key=setValue)
    for s in sets:
        p = Player(s)
        b = Boss()
        if not fight(p,b):
            return s[1]
        
if __name__ == '__main__':
    items = [[], [], []]
    f = open("inputs/21.txt")
    for x in range(3):
        f.readline()
        while True:
            line = f.readline()
            result = re.search(r'(\b.+\b).+(\b\d+\b).+(\b\d+\b).+(\b\d+\b)' , line)
            if result == None:
                break
            items[x].append(Equipment(result.groups()))
    f.close()
    costlow = findCheapestWin(items)
    print(f"The cheapest item set that can kill the boss costs {costlow} gold.")
    costhigh = findExpensiveLoss(items)
    print(f"The most expensive item set that loses to the boss costs {costhigh} gold.")

    
