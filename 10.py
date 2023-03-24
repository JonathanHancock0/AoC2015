def process(num):
    output = ""
    prev = ""

    for digit in num:
        if prev == "":      #Initialise
            prev = digit
            count = 1
            continue
        
        if prev != digit:   #A sequence has ended
            output += str(count)
            output += prev
            prev = digit
            count = 1
            continue
        count +=1

    output += str(count)
    output += prev
    return output

if __name__ == '__main__':
    value = "1113222113"
    iterations = 50
    for _ in range(iterations):
        value = process(value)

    print(f"Length of final sequence is {len(value)}")