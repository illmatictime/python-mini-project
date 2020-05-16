
def openFile():
    while True:
        try:
            fileName = input("Enter file name:")
            fileOpen = open(fileName)
            return fileOpen, fileName
        except IOError:
            print("File not found, please enter correct file name.")

def Counter(fileOpen):
    wordCount = 0
    for x in fileOpen:
        x = x.split()
    
    return x, wordCount

def printResults(fileName, wordCount):
    print("File", fileName, "has", wordCount, "different words.")


def repeat():
    repeatProgram = input("\nDo you want to try it again? (y or n) ")
    if repeatProgram.upper() == "Y":
        pass
    elif repeatProgram.upper() == "N":
        print("Thank you for playing.")
        return True
        # quit()
    else:
        print("Please enter y or n.")
        repeat()

def main():
    while True:
        fileOpen, fileName = openFile()
        wordCount = Counter(fileOpen)
        printResults(fileName, wordCount)
        # lineCounter(fileName)
        # vowelCounter(files, fileName)
        # consonantCounter(files, fileName)
        # numCharCounter(files, fileName)
        result = repeat()
        if result == True:
            break


main()