import re

class Machine:
    def __init__(self, filename, a=0, b=0):
        self.a = a
        self.b = b
        self.position = 0
        self.program = [] 
        
        f = open(filename)
        for line in f:
            self.program.append(line.strip('\n'))
        f.close()
        self.length = len(self.program)

    def execute(self):
        while self.position < self.length:
            current = re.split(r',\s|\s', self.program[self.position])  #Selects the current line, and splits it
            print(f"Executing line{self.position}")
            match current[0]:
                case "hlf":
                    reg = getattr(self, current[1])                     #Finds the right register
                    reg = reg // 2
                    setattr(self, current[1], reg)
                    self.position += 1
                case "tpl":
                    reg = getattr(self, current[1])
                    reg *= 3
                    setattr(self, current[1], reg)
                    self.position += 1
                case "inc":
                    reg = getattr(self, current[1])
                    reg += 1
                    setattr(self, current[1], reg)
                    self.position += 1

                case "jmp":
                    num = current[1]
                    if num[0] == '+':
                        self.position += int(num[1:])
                    else:
                        self.position -= int(num[1:])

                case "jie":
                    reg = getattr(self, current[1])
                    if reg % 2 == 0:
                        num = current[2]
                        if num[0] == '+':
                            self.position += int(num[1:])
                        else:
                            self.position -= int(num[1:])
                    else:
                        self.position += 1
                
                case "jio":
                    reg = getattr(self, current[1])
                    if reg == 1:
                        num = current[2]
                        if num[0] == '+':
                            self.position += int(num[1:])
                        else:
                            self.position -= int(num[1:])
                    else:
                        self.position += 1


            #print(f"a={self.a} b={self.b}")
    def getReg(self):
        return (self.a, self.b)

if __name__ == '__main__':
    m = Machine("inputs/23.txt", 1, 0)
    m.execute()
    tup = m.getReg()
    print(f"a={tup[0]} b={tup[1]}")