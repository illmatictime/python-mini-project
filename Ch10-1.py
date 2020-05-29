import string


def openFile():
    while True:
        try:
            fileName = input("Please enter file name to process: ")
            fileOpen = open(fileName)
            wordTuple = dict()

            for line in fileOpen:
                line = line.translate(str.maketrans('', '',
                                                    string.punctuation))
                line = line.translate(str.maketrans('', '', string.whitespace))
                for char in line:
                    char = char.lower()
                    wordTuple[char] = wordTuple.get(char, 0) + 1
            return wordTuple
        except IOError:
            print("File name", fileName, "cannot be found.")


def sort(wordTuple):
    sortList = list()

    for k, v in wordTuple.items():
        sortList.append((v, k))
    sortedTuple = sorted(sortList)
    return sortedTuple


def printResults(sortedTuple):
    print(sortedTuple)


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
        wordTuple = openFile()
        sortedTuple = sort(wordTuple)
        printResults(sortedTuple)
        result = repeat()
        if result == True:
            break


main()