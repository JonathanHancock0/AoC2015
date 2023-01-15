if __name__ == '__main__':
    f = open("inputs/1.txt")
    line = f.readline().strip('\n')
    f.close()

    floor = 0
    basement = False
    for cnum, char in enumerate(line):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if (floor == -1) and (not basement):
            print(f"Basement entered on step {cnum+1}")
            basement = True
    
    print(f"Final floor is {floor}")