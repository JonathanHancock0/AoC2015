import re

class Lights:
    def __init__(self):
        self.grid = []
        for y in range(1000):
            self.grid.append([])
            for x in range(1000):
                self.grid[y].append(0)

    def __len__(self):
        n = 0
        for x in range(1000):
            for y in range(1000):
                if self.grid[x][y]:
                    n += 1
        return n

    def count(self):
        n = 0
        for x in range(1000):
            for y in range(1000):
                n += self.grid[x][y]
        return n

    def on(self, x, y):
        self.grid[x][y] += 1
    
    def off(self, x, y):
        if self.grid[x][y] != 0:
            self.grid[x][y] -= 1
    
    def toggle(self, x, y):
        self.grid[x][y] += 2

if __name__ == '__main__':
    f = open("inputs/6.txt")
    l = Lights()     #A list of tuples

    for line in f:
        result = re.search(r'([a-zA-Z\s]+)(\d+),(\d+).{9}(\d+),(\d+)', line)
        instruction = result.group(1)
        start_coords = (int(result.group(2)) , int(result.group(3)))
        end_coords = (int(result.group(4)) , int(result.group(5)))

        affected = []
        x1 = min(start_coords[0] , end_coords[0])
        x2 = max(start_coords[0] , end_coords[0])
        y1 = min(start_coords[1] , end_coords[1])
        y2 = max(start_coords[1] , end_coords[1])
        for x in range(x1 , x2+1):
            for y in range(y1 , y2+1):
                affected.append((x,y))
        match instruction:
            case "turn off ":
                for a in affected:
                    l.off(a[0], a[1])
            
            case "turn on ":
                for a in affected:
                    l.on(a[0], a[1])
                        
            case "toggle ":
                for a in affected:
                    l.toggle(a[0], a[1])

    print(l.count())
