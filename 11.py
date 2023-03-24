import re

def increment(word):
    word = word[::-1]           #Make it little-endian
    newword = ""
    done = False

    for char in word:
        if done:
            newword += char
            continue

        newchar = chr(ord(char) + 1)
        if (newchar != '{'):  
            newword += newchar
            done = True
            continue

        newword += 'a'          #If the char was z, it increments to a and we move to the next

    newword = newword[::-1]        #Back to normal
    return newword

def test(word):
    norun = True
    for i in range(len(word)-2):
        v1 = ord(word[i])
        v2 = ord(word[i+1])
        v3 = ord(word[i+2])
        if v2 != v1+1:
            continue
        if v3 != v2+1:
            continue
        norun = False       #We found a run!
        break
    if norun:
        return False

    prev = word[0]
    pairs = []
    for char in word[1:]:
        if char == prev:
            if char not in pairs:
                pairs.append(char)
        else:
            prev = char
    if len(pairs) < 2:
        return False

    bad = ['i', 'l', 'o']
    for char in word:
        if char in bad:
            return False

    return True

if __name__ == '__main__':
    word = "hxbxwxba"
    required = 10
    found = 0
    
    while found < required:
        word = increment(word)
        if test(word):
            found += 1
            print(word)
    
