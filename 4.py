import hashlib

if __name__ == '__main__':
    f = open("inputs/4.txt")
    secret = f.readline()
    f.close()

    zeros_needed = 6
    test = 1
    while True:
        if test % 100000 == 0:
            print(test)
        message = secret + str(test)
        bmessage = bytes(message, 'ascii')
        hash = hashlib.md5(bmessage)
        hashstring = hash.hexdigest()
        testpart = hashstring[0:zeros_needed]
        success = True
        for char in testpart:
            if char != '0':
                success = False
                break
        if success:
            break

        test += 1

    print(f"First number to produce a good hash is {test}")
    print(f"Hash is {hashstring}")