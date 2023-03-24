import re

class Ingredient:
    def __init__(self, data):
        self.name = data[0]
        self.calories = int(data[-1])
        self.scores = []
        d = data[1:-1]
        for points in d:
            self.scores.append(int(points))
    
    def getScore(self, n):
        return self.scores[n]

    def getCal(self):
        return self.calories

def make_combinations(size):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for i in range(size+1):
        l1.append([i])

    for val in l1:
        left = size - val[0]
        for i in range(left+1):
            l2.append([val[0] , i])

    for val in l2:
        left = size - (val[0] + val[1])
        for i in range(left+1):
            l3.append([val[0] , val[1] , i])

    for val in l3:
        left = size - (val[0] + val[1] + val[2])
        l4.append([val[0] , val[1] , val[2] , left])
    return(l4)
    


if __name__ == '__main__':
    ingredients = []
    i_count = 0
    spoons = 100
    best_score = -1
    best_state = []
    best_score_500 = -1
    best_state_500 = []

    f = open("inputs/15.txt")
    for line in f:
        result = re.search(r'(.*):.+?([-\d]+).+?([-\d]+).+?([-\d]+).+?([-\d]+).+?([-\d]+)', line)
        ingredients.append(Ingredient(result.groups()))
        i_count += 1

    states = make_combinations(spoons)
    for s in states:
        scorelist = []
        final_score = 1
        badstate = False
        for n in range(4):    #For each property
            score = 0
            for i, ing in enumerate(ingredients):       #We go over each ingredient
                score += (s[i] * ing.getScore(n))       #Number of spoons times the score
            if score <= 0:
                badstate = True
                break
            scorelist.append(score)
        if badstate:                                    #If the state will have zero score, skip to the next
            continue
        calories = 0
        for i, ing in enumerate(ingredients):
            calories += (s[i] * ing.getCal())

        for sc in scorelist:
            final_score *= sc
        if final_score > best_score:
            best_score = final_score
            best_state = s
        if calories == 500 and final_score > best_score_500:
            best_score_500 = final_score
            best_state_500 = s
    
    print(f"Best possible score is {best_score}, from recipe {best_state}.")
    print(f"Best possible 500 cal. score is {best_score_500}, from recipe {best_state_500}.")