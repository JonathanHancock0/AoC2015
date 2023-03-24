import json

def count(filename):
    f = open(filename)
    buffer = ""
    total = 0
    for char in f.readline():
        if char.isdigit() or char == '-':
            buffer += char
        else:
            if buffer != "":
                total += int(buffer)
                buffer = ""
    
    if buffer != "":
                total += int(buffer)
                buffer = ""
    f.close()
    return total
    
def sum_dict(data):
    total = 0
    for key in data:
        if data[key] == "red":      #If anything in the object is red, skip it all!
            return 0
        
    for key in data:
        match data[key]:
            case int():
                total += data[key]

            case dict():
                total += sum_dict(data[key])

            case list():
                total += sum_list(data[key])

    return total

def sum_list(data):        
    '''Same thing but without the red clause'''
    total = 0
    for item in data:
        match item:
            case int():
                total += item

            case dict():
                total += sum_dict(item)

            case list():
                total += sum_list(item)

    return total

if __name__ == '__main__':
    filename = "inputs/12.txt"
    sum1 = count(filename)
    with open(filename) as json_file:
        data = json.load(json_file)
    sum2 = sum_dict(data)
    print(f"Sum of all numbers: {sum1}")
    print(f"Sum of all numbers avoiding red: {sum2}")