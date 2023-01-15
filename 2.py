import re

if __name__ == '__main__':
    paper = 0
    ribbon = 0
    f = open("inputs/2.txt")
    for line in f:
        str_lengths = re.split("x", line)
        lengths = [int(l) for l in str_lengths]
        s1 = lengths[0] * lengths[1]
        s2 = lengths[0] * lengths[2]
        s3 = lengths[1] * lengths[2]
        volume = lengths[0]*lengths[1]*lengths[2]
        #The min perimeter is the sum of the two smallest sides doubled, so we can just add all three then subtract the biggest
        per_min = 2*(lengths[0] + lengths[1] + lengths[2]) - 2*(max(lengths[0],lengths[1],lengths[2]))  
        paper += min(s1, s2, s3)
        paper += 2*(s1+s2+s3)
        ribbon += per_min
        ribbon += volume

    print(f"{paper} square feet of paper needed.")
    print(f"{ribbon} feet of ribbon needed.")
