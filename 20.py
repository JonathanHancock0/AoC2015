import math as m

def findHouse(start, target):
    '''The sum of all divisors is equal to the product of the sums S, where 
    for a particular prime factor, S = 1 + p + p^2 up until the number of times p appears in the factorisation.
    36 = (2^2)*(3^2). SoD = 1+2+3+4+6+9+12+18+36= 91 =(1+2+4)*(1+3+9)=7*13'''
    house = start
    while True:
        presents = 1
        for i in range(2, int(m.sqrt(house))+1):    #Biggest possible prime factor is sqrt(n)
            prime = True
            for x in range(2, (i//2)+1):            #We need to check primality
                if i % x == 0:
                    prime = False
                    break
            if not prime:
                continue
            num = house
            power = 0
            while num % i == 0:
                power += 1
                num = num // i
            if power == 0:                      #No point timesing by 1
                continue
            term = 1
            for a in range(1, power+1):
                term += (i**a)
            presents *= term 
        presents *= 10
        if presents >= target:
            return house
        house += 1

def findHouseLazy(target):
    '''We can't use the same trick here: so we will make a huge array of houses and simulate elves.'''
    length = 2_000_000
    houses = [0] * (length+1)        #Part one had a solution of about 700000, so 2 million should be safe
    for elf in range(1,length):
        for i in range(1,51):
            pos = i*elf
            if pos > length:    #Elf has left the region
                break
            new = houses[pos] + elf*11
            houses[pos] = new
    for i, h in enumerate(houses):
        if h >= target:
            return i



def findHouseHC(target):
    '''Higly composite numbers will have high scores, so we should look in between two of them'''
    HC = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560,
    10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640,
    498960, 554400, 665280, 720720, 1081080, 1441440, 2162160
    ]
    previous = (0,0)
    for house in HC:
        present = 0
        for i in range(1, house+1):
            if house % i == 0: 
                present += (10*i)
        if present >= target:
            return [previous, (house,present)]
        previous = (house,present)

if __name__ == '__main__':
    target = 33_100_000
    HCdata = findHouseHC(target)
    lazy = True

    if lazy:
        h2 = findHouseLazy(target)
        print(f"First house to get over {target} presents with lazy elves is number {h2}.")

    else:
        print(f"House {HCdata[0][0]} got {HCdata[0][1]} presents.")
        print(f"House {HCdata[1][0]} got {HCdata[1][1]} presents.")
        print(f"Therefore our house should be between houses {HCdata[0][0]} and {HCdata[1][0]}.")
        h1 = findHouse(HCdata[0][0], target)
        print(f"First house to get over {target} presents normally is number {h1}.")


