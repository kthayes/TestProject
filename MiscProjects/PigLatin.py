# Dictionary of vowels
VOWELS = {"a", "e", "i", "o", "u", "y"}

# Takes a line of words and converts them to Pig Latin
def translate(line):
    tr = ""
    # Make a list of each word in the line
    line = line.strip()
    words = line.split()
    # Step through each word in the list
    for word in words:
        # Check if the first letter is a vowel, if it is, add "yay" to end of the word
        if(word[0] in VOWELS):
            word += "yay "
        # If the first letter is not a vowel, then it is a consonant
        else:
            # Step through each letter in the current word
            for letter in word:
                # If the current letter is a consonant, remove it from the front of the word, and place it at the end of the word
                if(letter not in VOWELS):
                    word = word[1:] + word[0]
                # If we hit a vowel, we are done moving consonants
                else:
                    break
            # Add "ay" to the end of the word
            word += "ay "
        # Add the translated word to the sentence
        tr += word
    # Use .strip() on the return to eliminate the trailing " "
    return tr.strip()

# "main" function, called at the bottom
def PigLatin():
    # Change fName to match the file name to be inputed
    fName = "same.txt"
    fDir = "PigLatin_InputFiles/"
    fDir += fName
    
    # try-except to catch non-exiting or corrupt files
    try:
        f = open(fDir, "r")
    except FileNotFoundError:
        print("Unable to open input file.")
        return

    # Store all lines in the file in a list
    lines = f.readlines()
    f.close()
    
    # Call translate() function for each line in the list, and print the result
    for line in lines:
        print(translate(line))
        
PigLatin()