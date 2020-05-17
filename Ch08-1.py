
def openFile():
    while True:
        try:
            fileName = input("Enter file name: ")
            fileOpen = open(fileName)
            fileOpen = fileOpen.read()
            return fileName, fileOpen
        except IOError:
            print("File not found, please enter correct file name.\n")
            

def Counter(fileOpen):
    wordList = []
    fileOpen = fileOpen.split()

    for word in fileOpen:
        word = word.lower()
        if word not in wordList:
            wordList.append(word)
            wordList.sort()
    return wordList

def printResults(fileName, wordList):
    print()
    print(wordList)
    print("\nFile", fileName, "has", len(wordList), "different words.")


def repeat():
    repeatProgram = input("\nDo you want to try it again? (y or n) ")
    if repeatProgram.upper() == "Y":
        pass
    elif repeatProgram.upper() == "N":
        print("\n\nThank you for playing.")
        return True
        # quit()
    else:
        print("Please enter y or n.")
        repeat()


def main():
    while True:
        fileName, fileOpen = openFile()
        wordList = Counter(fileOpen)
        printResults(fileName, wordList)
        result = repeat()
        if result == True:
            break


main()