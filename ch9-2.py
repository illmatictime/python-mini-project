def openFile():
    while True:
        try:
            fileName = input("Please enter file name to process: ")
            fileOpen = open(fileName)
            fileOpen = fileOpen.read()
            return fileOpen
        except IOError:
            print("File name", fileName, "cannot be found.")


def Counter(fileOpen):
    wordList = dict()
    fileOpen = fileOpen.split()

    for word in fileOpen:
        word = word.lower()
        word = word.strip("[]!,().#'[]:;?")
        wordList[word] = wordList.get(word, 0) + 1
    return wordList


def printResults(wordList):
    for k, v in sorted(wordList.items()):
        print(k, v)


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
        fileOpen = openFile()
        wordList = Counter(fileOpen)
        printResults(wordList)
        result = repeat()
        if result == True:
            break


main()