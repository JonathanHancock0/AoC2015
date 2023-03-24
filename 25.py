if __name__ == '__main__':
    target = (2978 , 3083)  #Row column
    pos = (1 , 1)           #The latest value in the sequence that we have
    val = 20151125
    while True:
        if pos[0] == 1:
            newrow = pos[1] + 1
            pos = (newrow , 1)
        else:
            newrow = pos[0] - 1
            newcol = pos[1] + 1
            pos = (newrow , newcol)
        val = val * 252533
        val = val % 33554393

        if pos == target:
            print(f"Desired code at {pos} is {val}")
            break
        elif pos[0] == pos[1] and pos[0] % 100 == 0:
            print(pos)

