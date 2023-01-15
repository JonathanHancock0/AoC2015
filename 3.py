if __name__ == '__main__':
    f = open("inputs/3.txt")
    directions = f.readline().strip('\n')
    f.close()

    pos1 = (0,0)            #(x,y)
    pos2 = (0,0)
    houses = {(0,0): 2}     #Coordinate: times visited
    santa = True

    for d in directions:
        if santa:
            oldpos = pos1
        else:
            oldpos = pos2

        match d:
            case '^':
                newpos = (oldpos[0], oldpos[1]+1)
            case 'v':
                newpos = (oldpos[0], oldpos[1]-1)
            case '>':
                newpos = (oldpos[0]+1, oldpos[1])
            case '<':
                newpos = (oldpos[0]-1, oldpos[1])

        if newpos in houses:
            houses[newpos] += 1
        else:
            houses[newpos] = 1
        if santa:
            pos1 = newpos
            santa = False
        else:
            pos2 = newpos
            santa = True
    
    repeats = len(houses)
    

    print(f"{repeats} houses were visited at least once.")

