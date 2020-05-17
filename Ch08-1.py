
def openFile():
    while True:
        try:
            fileName = input("Enter file name: ")
            fileOpen = open(fileName)
            return fileOpen, fileName
        except IOError:
            print("File not found, please enter correct file name.")

def Counter(fileOpen, fileName):
    wordCount = 0
    wordList = []
    newWordList = []
    for x in open(fileName):
        x = x.lower()
        x = x.split()
        wordList.extend(x)
        # wordList = list(set(wordList))
        wordList.sort()
        
    print(wordList)
    print(len(wordList))
    for x in wordList:
        if x not in newWordList:
            newWordList.extend(x)
    print("newWordList:",newWordList)
    wordCount = len(wordList)
    
    return wordCount, wordList

def printResults(fileName, wordCount, wordList):
    print(wordList)
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
        wordCount, wordList = Counter(fileOpen, fileName)
        printResults(fileName, wordCount, wordList)
        # lineCounter(fileName)
        # vowelCounter(files, fileName)
        # consonantCounter(files, fileName)
        # numCharCounter(files, fileName)
        result = repeat()
        if result == True:
            break


main()