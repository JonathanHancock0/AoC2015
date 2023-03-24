import copy
import math

class Effects:
    def __init__(self):
        self.timeleft = {
            "shield": 0,
            "poison": 0,
            "recharge": 0
        }
        self.durations = {
            "shield": 6,
            "poison": 6,
            "recharge": 5
        }
    
    def start_spell(self, name):
        t = self.durations[name]
        self.timeleft[name] = t

    def trigger(self):
        out = []
        for spell in self.timeleft:
            if self.timeleft[spell] != 0:
                out.append(spell)
                self.timeleft[spell] -= 1
        return out
    
    def get_forbidden(self):
        out = []
        for spell in self.timeleft:
            if self.timeleft[spell] != 0:       #We can't cast effect spells if they are ongoing
                out.append
        return out

    def shield_done(self):
        return self.timeleft["shield"] == 0

class Wizard:
    def __init__(self):
        self.hp = 50
        self.arm = 0
        self.mana = 500
        self.spent = 0
        self.costs = {
            "missile": 53,
            "drain": 73,
            "shield": 113,
            "poison": 173,
            "recharge": 229
        }

    def take_damage(self, damage):
        realDamage = damage-self.arm
        if realDamage < 1:
            self.hp -= 1
        else:
            self.hp -= realDamage
    
    def shield_on(self):
        self.arm = 7

    def shield_off(self):
        self.arm = 0

    def recharge(self):
        self.mana += 101

    def heal(self, amount):
        self.hp += amount

    def get_affordable(self):
        out = []
        for spell in self.costs:
            if self.costs[spell] <= self.mana:
                out.append(spell)
        return out
    
    def getSpent(self):
        return self.spent

    def cast(self, spell):
        cost = self.costs[spell]
        self.mana -= cost
        self.spent += cost

    def isDead(self):
        return (self.hp <= 0)

    def getHealth(self):
        return self.hp

class Boss:
    def __init__(self):
        self.hp = 55
        self.atk = 8

    def getAttack(self):
        return self.atk

    def take_damage(self, dmg):
        self.hp -= dmg

    def isDead(self):
        return (self.hp <= 0)

    def getHealth(self):
        return self.hp

class State:
    def __init__(self, w, b, e):
        self.wizard = w
        self.boss = b
        self.effects = e
        self.history = []

    def __str__(self):
        return f"Wiz hp: {self.wizard.getHealth()} Boss hp: {self.boss.getHealth()}"
    
    def hard(self):
        self.wizard.take_damage(1)

    def resolve_effects(self):
        todo = self.effects.trigger()
        for effect in todo:
            match effect:
                case "shield":
                    self.wizard.shield_on()
                case "poison":
                    self.boss.take_damage(3)
                case "recharge":
                    self.wizard.recharge()
    
    def get_affordable(self):
        final = []
        start = self.wizard.get_affordable()
        bad = self.effects.get_forbidden()
        for spell in start:
            if spell not in bad:
                final.append(spell)
        return final

    def checkwin(self):
        if self.boss.isDead():
            return self.wizard.getSpent()
        else:
            return None
    
    def checklose(self):
        return self.wizard.isDead()
         

    def cast_spell(self, spell):
        match spell:
            case "missile":
                self.boss.take_damage(4)
            case "drain":
                self.boss.take_damage(2)
                self.wizard.heal(2)
            case _:                                 #Effects are all handled the same
                self.effects.start_spell(spell)
        
        self.wizard.cast(spell)
        self.history.append(spell)

    def check_shield(self):
        if self.effects.shield_done():
            self.wizard.shield_off()

    def boss_turn(self):
        dmg = self.boss.getAttack()
        self.wizard.take_damage(dmg)

    def getSpent(self):
        return self.wizard.getSpent()

class StateHeap:
    '''
    This is a binary tree that satisfies the (min)heap property: no child can have a smaller key than its parent.
    In this case, the key is the amount of mana spent. Indexing is in order of row. (all the first layer, then all the second etc)
    Node i has children at 2i+1 and 2i+2, and a parent at the floor of (i-1)/2
    '''
    def __init__(self, root):
        self.data = [root]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        out = f"Binary Heap of {len(self.data)} states!\n"
        next_break = 0
        increment = 2
        for n, state in enumerate(self.data):
            out += str(state.getSpent())
            if n == next_break:
                out += '\n'
                next_break += increment
                increment *= 2
            else:
                out += ' '
        if out[-1] != '\n':
            out += '\n'
        return out
    
    def addState(self, newState):
        self.data.append(newState)
        pos = len(self.data) - 1
        parent = math.floor((pos-1)/2)
        while pos != 0:     #We end if the new node reaches the top
            if self.data[pos].getSpent() >= self.data[parent].getSpent():           #Larger values should be lower down
                break
            self.data[pos], self.data[parent] = self.data[parent], self.data[pos]   #Bubble the new node up
            pos = parent
            if pos == 0:
                break
            parent = math.floor((pos-1)/2)

    def getMin(self):
        output = self.data[0]
        if len(self.data) == 1:
             self.data = []
             return output
        
        newroot = self.data.pop(-1) #We take the last element
        self.data[0] = newroot      #And put it at the top
        
        pos = 0

        while True:
            child1 = 2*pos + 1
            child2 = 2*pos + 2
            if child1 >= len(self.data):        #No children, so we are done
                break
            if child2 >= len(self.data):        #Only one child
                if self.data[child1].getSpent() >= self.data[pos].getSpent():
                    break                       #This is the desired state, so we stop
                else:
                    self.data[pos], self.data[child1] = self.data[child1], self.data[pos]
                    pos = child1
            else:
                #We will swap with the smallest child, so that it is fine to have it above the other
                if self.data[child1].getSpent() <= self.data[child2].getSpent():
                    small_child = child1
                else:
                    small_child = child2
                if self.data[small_child].getSpent() >= self.data[pos].getSpent():
                    break                       #This is the desired state, so we stop
                else:
                    self.data[pos], self.data[small_child] = self.data[small_child], self.data[pos]
                    pos = small_child
        return output

def log2(x):
    return (math.log10(x) / math.log10(2))
                
def findPrice(state):
    return state.getSpent()

def astar(hardmode=False):
    milestone = 100
    startstate = State(Wizard(), Boss(), Effects())
    #We are using something like a*, albiet with h(x)=0
    openlist = StateHeap(startstate)

    while len(openlist) != 0:
        currentstate = openlist.getMin()              #Get the state with the least mana spent
        if hardmode:
            currentstate.hard()                     #The wizard takes 1 damage
            if currentstate.checklose():            #If he dies from it, throw out this state
                continue
        currentstate.resolve_effects()
        if currentstate.checkwin() != None:         #Boss might die from poison
            return currentstate
        allowed_spells = currentstate.get_affordable()
        if allowed_spells == []:                    #Instantly lose if we can't cast anything
            continue
        for spell in allowed_spells:                #Make a branch for each possible spell
            newstate = copy.deepcopy(currentstate)
            newstate.cast_spell(spell)
            if newstate.checkwin() != None:     #Boss might die from the spell
                return newstate
            newstate.check_shield()
            newstate.resolve_effects()
            if newstate.checkwin() != None:     #Boss might die from poison
                return newstate
            newstate.boss_turn()
            if newstate.checklose():            #We don't want states where we die!
                continue
            openlist.addState(newstate)

        if currentstate.getSpent() >= milestone:
            print(milestone)
            milestone += 100

if __name__ == '__main__':
    beststate = astar(hardmode=True)
    print(f"Least mana needed to kill the boss is {beststate.getSpent()}")
    print(beststate.history)
    print(beststate.effects.timeleft)
    print(beststate)