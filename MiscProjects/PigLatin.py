
def translate(line):
    return "test"

def PigLatin():
    # Change fName to match the file name to be inputed
    fName = "lines.txt"
    fDir = "PigLatin_InputFiles/"
    fDir += fName
    print("")
    
    try:
        f = open(fName, "r")
    except FileNotFoundError:
        print("Unable to open input file.")
        return

    lines = f.readlines()
    f.close()
    
    if(len(lines) == 0):
        return
    
    for line in lines:
        translated = translate(line)
        print(translated)
        
PigLatin()