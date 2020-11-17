VALUES = {
    "xxxxxx...xx...xx...xx...xx...xxxxxx": 0,
    "....x....x....x....x....x....x....x": 1,
    "xxxxx....x....xxxxxxx....x....xxxxx": 2,
    "xxxxx....x....xxxxxx....x....xxxxxx": 3,
    "x...xx...xx...xxxxxx....x....x....x": 4,
    "xxxxxx....x....xxxxx....x....xxxxxx": 5,
    "xxxxxx....x....xxxxxx...xx...xxxxxx": 6,
    "xxxxx....x....x....x....x....x....x": 7,
    "xxxxxx...xx...xxxxxxx...xx...xxxxxx": 8,
    "xxxxxx...xx...xxxxxx....x....xxxxxx": 9,
    ".......x....x..xxxxx..x....x.......": -1,
    "0": "xxxxxx...xx...xx...xx...xx...xxxxxx",
    "1": "....x....x....x....x....x....x....x",
    "2": "xxxxx....x....xxxxxxx....x....xxxxx",
    "3": "xxxxx....x....xxxxxx....x....xxxxxx",
    "4": "x...xx...xx...xxxxxx....x....x....x",
    "5": "xxxxxx....x....xxxxx....x....xxxxxx",
    "6": "xxxxxx....x....xxxxxx...xx...xxxxxx",
    "7": "xxxxx....x....x....x....x....x....x",
    "8": "xxxxxx...xx...xxxxxxx...xx...xxxxxx",
    "9": "xxxxxx...xx...xxxxxx....x....xxxxxx",
}

''' input_lines is a list of lines from the readlines() file function '''
def generate(input_lines):
    ''' Write your code here '''
    # Remove newline characters (\n)
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()
    
    # Determine both numbers to be summed, based on the input_lines list
    text = ""
    for char in range(0, len(input_lines[0]), 5):
        currVal = ""
        for row in range(len(input_lines)):
            for col in range(char, char + 5):
                currVal += input_lines[row][col]
        # Dictionary lookup
        currVal = str(VALUES.get(currVal))
        # Build text, accounting for -1 as '+'
        if(currVal == "-1"):
            text += "+"
        else:
            text += currVal
    
    # Calculate the sum
    text = text.split("+")
    result = str(int(text[0]) + int(text[1]))
    
    """
    ret = ""
    for num in range(len(result)):
        charVal = VALUES.get(result[num])
        #print(charVal)
        for row in range(7):
            for val in range(len(charVal)):
                ret += charVal[val][row*5:row*5+5]
        ret += "\n"
    """
    
    
    # Extract each number in the result into a list
    retList = list()
    for num in result:
        retList.append(VALUES.get(num))
    
    # Convert the sum to ASCII, as a returnable string
    ret = ""
    for row in range(7):
        for val in range(len(retList)):
            ret += retList[val][row*5:row*5+5]
        ret += "\n"
    
    return ret
    
    """
    text = ""
    input_lines = [line[:-1] for line in input_lines]
    
    # repeat for all lines
    for i in range(0, len(input_lines[0]), 6):
        single_number = ""
        for k in range(7):
            for j in range(5):
                single_number += input_lines[k][i + j]

        # If -1 that means + is found
        if VALUES.get(single_number) == -1:
            text += '+'
        else:
            text += str(VALUES.get(single_number))

    # Get the split here
    data = text.split("+")
    number1, number2 = int(data[0]), int(data[1])

    output = number1 + number2
    # Prepare the output
    ret = [""] * 7
    for num in str(output):
        number_text = VALUES[num]
        col = 0
        # Add the columns here
        for i in range(7):
            ret[i] += number_text[col:col + 5] + '.'
            col += 5

    # Now, get the value
    return_value = ""
    for line in ret:
        return_value += line[0:-1] + "\n"
    return return_value
    """

def ASCIIGraphics():
    fname = "ASCIIGraphics_InputFiles/"
    fname += input("Enter filename: ")
    print("")
    try:
        f = open(fname, "r")
    except FileNotFoundError:
        print("Unable to open input file '{}'.".format(fname))
        return

    lines = f.readlines()
    f.close()
    if len(lines) != 7:
        print("Lines is {}, not 7.".format(len(lines)))

    output = generate(lines)

    print(output.strip())
    #print(len(lines[0].strip()))

ASCIIGraphics()