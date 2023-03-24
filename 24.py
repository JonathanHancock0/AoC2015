import itertools as it

def testRemainder_2(group_weight, others):
    for size in range(2, len(others)-1):
        #First we find all groups that contain n boxes
        right_size = it.combinations(others, size)
        for g in right_size:
            weight = 0
            for box in g:
                weight += box
            if weight == group_weight:  #If we can form one good group, the other is good too.
                return True
    return False

def testRemainder_3(group_weight, others):
    good_groups = []
    for x in range(1, len(others)-1):
        ok_groups = []
        #First we find all groups that contain n boxes
        right_size = it.combinations(boxes, x)
        for g in right_size:
            weight = 0
            for box in g:
                weight += box
            if weight == group_weight:
                ok_groups.append(list(g))
        if ok_groups == []:     #Skip the rest if there's no groups of size n
            continue
        #Now we have to make sure that the remaining boxes can be partitioned into two groups
        for g in ok_groups:
            others = [b for b in boxes if b not in g]
            if testRemainder_2(group_weight, others):
                return True
    return False

def getQE(group):
    acc = 1
    for b in group:
        acc *= b
    return acc

def calculate(boxes):
    n_boxes = len(boxes)
    weight_sum = 0
    for b in boxes:
        weight_sum += b
    group_weight = weight_sum // 4
    #A smaller group always wins. Thus, we can test in ascending order of size
    good_groups = []
    for x in range(1, n_boxes):
        ok_groups = []
        #First we find all groups that contain n boxes
        right_size = it.combinations(boxes, x)
        for g in right_size:
            weight = 0
            for box in g:
                weight += box
            if weight == group_weight:
                ok_groups.append(list(g))
        if ok_groups == []:     #Skip the rest if there's no groups of size n
            continue
        #Now we have to make sure that the remaining boxes can be partitioned into two groups
        for g in ok_groups:
            others = [b for b in boxes if b not in g]
            if testRemainder_3(group_weight, others):
                good_groups.append(g)
        if good_groups != []:   #If we've found small groups we don't care about the big ones
            break
    
    good_groups.sort(key=getQE) #Smallest quantum entanglement wins
    return getQE(good_groups[0])

if __name__ == '__main__':
    boxes = []
    f = open("inputs/24.txt")
    for line in f:
        boxes.append(int(line.strip('\n')))
    bestQE = calculate(boxes)
    print(f"The quantum entanglement of the best arrangement is {bestQE}")