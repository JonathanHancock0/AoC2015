def getNeighbors(row, col):
    n = []                  #List of 8 tuples
    n.append((row+1 , col))
    n.append((row-1 , col))
    n.append((row , col+1))
    n.append((row , col-1))
    n.append((row+1 , col+1))
    n.append((row-1 , col+1))
    n.append((row+1 , col-1))
    n.append((row-1 , col-1))
    return n

def iterate(grid, stuck):
    newgrid = {}
    for s in stuck:                             #Force the stuck lights to be on  
        grid[s] = '#'


    for row in range(100):
        for col in range(100):
            neighbors = 0
            for n in getNeighbors(row, col):
                if n in grid.keys():            #Not existing means off
                    if grid[n] == '#':
                        neighbors += 1

            if grid[(row,col)] == '#':          #Stay on if 2 or 3 neighbors are on
                if neighbors == 2 or neighbors == 3:
                    newgrid[(row,col)] = '#'
                else:
                    newgrid[(row,col)] = '.'
            else:                               #Turn on if 3 neighbors are on
                if neighbors == 3:
                    newgrid[(row,col)] = '#'
                else:
                    newgrid[(row,col)] = '.'

    for s in stuck:                             #Force the stuck lights to be on (again)
        newgrid[s] = '#'
    return newgrid




if __name__ == '__main__':
    grid = {}           #Key:Val = (row,col):'#'
    stuck = [(0,0), (0,99), (99,0), (99,99)]
    iterations = 100

    f = open("inputs/18.txt")
    for row, line in enumerate(f):
        for col, char in enumerate(line.strip('\n')):
            grid[(row, col)] = char
    f.close()

    for _ in range(iterations):
        grid = iterate(grid, stuck)
    
    count = 0
    for val in grid.values():
        if val == '#':
            count += 1

    print(f"{count} lights are on after {iterations} iterations.")

    