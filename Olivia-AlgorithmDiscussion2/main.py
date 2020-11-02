def main():
    # Define usable digits for the UCN (tuple)
    usableDigits = ("0","1","2","3","4","5","6","7","8","9","A","C","D","E","F","H","J","K","L","M","N","P","R","T","V","W","X")
    # Define the values used to compute the check digit (tuple)
    computeValues = (2, 4, 5, 7, 8, 10, 11, 13)
    # Map the digit substitutions (dictionary)
    dictConfusing = {
        "B": "8", 
        "G": "C", 
        "I": "1", 
        "O": "0", 
        "Q": "0", 
        "S": "5", 
        "U": "V", 
        "Y": "V", 
        "Z": "2"
    }
    
    # Initialize the check digit verification variable (int) 
    verifyCheckDigit = int()
    # Initialize the output decimal variable (int)
    decimalValue = int()
    
    # Read in the user-inputed UCN to be tested (including the check digit) (.strip() removes leading/trailing spaces, and new lines)
    ucn = str(input("Input UCN with check digit: ")).strip()
    # Verify the UCN is long enough (including the check digit at the end)
    if len(ucn) != 9:
        exit("Incorrect input!")
    
    # Iterate through the dictionary, and apply the necessary replacements to the UCN and check digit, as defined by the dictionary
    for entry in dictConfusing:
        ucn = ucn.replace(entry, dictConfusing[entry])
    
    # Iterate through the UCN, and ensure there are no illegal characters
    for i, digit in enumerate(ucn):
        if digit not in usableDigits:
            exit("Incorrect input!")
        # Keep a persistent total for the check digit computation, as well as the final decimal value
        # Being sure to not include the check digit value
        elif i < 8:
            verifyCheckDigit += usableDigits.index(digit) * computeValues[i]
            decimalValue += usableDigits.index(digit) * (27 ** (7 - i))
    
    # Pull the check digit from the end of the UCN for convenience (str and int index from usable digits)
    checkDigitStr = str(ucn[8])
    checkDigit = usableDigits.index(checkDigitStr)
    
    # Complete the check digit computation (and convert into str for convenience)
    verifyCheckDigit = verifyCheckDigit % 27
    verifyCheckDigitStr = str(usableDigits[verifyCheckDigit])
    
    # Test the computed check digit against the inputed check digit, and output the decimal value of the UCN if they match
    if verifyCheckDigit == checkDigit:
        print("check digit: " + checkDigitStr)
        print("checkDigit index: " + str(checkDigit))
        print("decimalValue: " + str(decimalValue))
    else:
        print("Check Digit is wrong!")
        print("check digit: " + checkDigitStr)
        print("checkDigit index: " + str(checkDigit))
        print("verifyCheckDigit: " + verifyCheckDigitStr)
        print("verifyCheckDigit index: " + str(verifyCheckDigit))
        print("decimalValue: " + str(decimalValue))
    
if __name__ == "__main__":
    main()