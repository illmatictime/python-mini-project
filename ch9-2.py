def openFile():
    while True:
        try:
            fileName = input("Please enter file name to process: ")
            fileOpen = open(fileName)
            fileOpen = fileOpen.read()
            return fileName, fileOpen
        except IOError:
            print("File name", fileName, "doesn't exist.")


def Counter(fileOpen):
    wordList = dict()

    for word in fileOpen:
        wordList[word] = wordList.get(word, 0) + 1
    return wordList


def printResults(fileName, wordList):
    print(wordList)


def repeat():
    repeatProgram = input("\nDo you want to try another file? (y or n) ")
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
        fileName, fileOpen = openFile()
        wordList = Counter(fileOpen)
        printResults(fileName, wordList)
        result = repeat()
        if result == True:
            break


main()