if __name__ == '__main__':
    containers = []
    f = open("inputs/17.txt")
    for line in f:
        containers.append(int(line.strip('\n')))
    f.close()
    containers.sort()
    goodlist = []
    target = 150
    n_cont = len(containers)
    c_num = 2 ** n_cont
    #A container is either in a combination or out. Therefore we encode combinations as binary
    for c in range(c_num):
        sum = 0
        this_list = []
        for bit in range(n_cont):
            if ((c >> bit) % 2 == 1):   #Select nth bit by shifting n to the right and taking modulo 2
                sum += containers[bit]
                this_list.append(containers[bit])
                if sum > target:        #If the total is too much then give up
                    break
        if sum == target:
            goodlist.append(this_list)
    print(f"There are {len(goodlist)} ways of partitioning {target} litres with these containers.")
    goodlist.sort(key=len)
    bestlen = len(goodlist[0])
    count = 0
    for l in goodlist:
        if len(l) == bestlen:
            count += 1
        else:
            break
    print(f"There are {count} ways to fill {bestlen} containers with {target} litres.")