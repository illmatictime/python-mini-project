import string


def openFile():
    while True:
        try:
            fileName = input("Please enter file name to process: ")
            fileOpen = open(fileName)
            wordTuple = dict()

            for line in fileOpen:
                if not line.startswith('From'): continue
                line = line.split()
                for word in line:
                    if '@' in word:
                        wordTuple[word] = wordTuple.get(word, 0) + 1
                        break
            return wordTuple
        except IOError:
            print("File", fileName, "doesn't exist.")
            print("Please enter correct file name.")


def sort(wordTuple):
    sortList = list()

    for k, v in wordTuple.items():
        sortList.append((v, k))
    sortedTuple = sorted(sortList, reverse=True)

    return sortedTuple


def printResults(sortedTuple):
    print("Here is a list of top 5 email users:")
    print("====================================")
    for key, val in sortedTuple[:5]:
        print(key, "\t", val)
        # print("Sum of even numbers is: {:>4}".format(even))
    print("====================================")


def repeat():
    repeatProgram = input("Do you want to try another file? (y or n) ")
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