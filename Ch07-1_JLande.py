def fileOpener():
    while True:
        try:
            fileName = input("Please enter file name: ")
            fileOpen = open(fileName)
            files = fileOpen.read()
            return files, fileName
        except IOError:  # except IOError as error: print("File cannot be opened: ", error)
            print("File cannot be opened: ")


def Counter(files, fileName):
    lineCount = 0
    countVowels = 0
    countConsonants = 0
    countNumbers = 0
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyz"
    numChar = "0123456789"

    for x in open(fileName):
        lineCount += 1

    for x in files:
        if x in vowels:
            countVowels += 1
        elif x in consonants or x in consonants.upper():
            countConsonants += 1
        elif x in numChar:
            countNumbers += 1
    return fileName, lineCount, countVowels, countConsonants, countNumbers


def printResults(fileName, lineCount, countVowels, countConsonants,
                 countNumbers):
    print("File", fileName, "has", lineCount, "lines")
    print("File", fileName, "has", countVowels, "vowels")
    print("File", fileName, "has", countConsonants, "consonants")
    print("File", fileName, "has", countNumbers, "numerical characters")


# def lineCounter(fileName):
#     lines = 0
#     for line in open(fileName):
#         lines += 1
#     print("File", fileName, "has", lines, "lines")

# def vowelCounter(files, fileName):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for letters in files:
#         if letters in vowels:
#             count = count + 1
#     print("File", fileName, "has", count, "vowels")

# def consonantCounter(files, fileName):
#     count = 0
#     consonants = "bcdfghjklmnpqrstvwxyz"
#     for letters in files:
#         if letters in consonants or letters in consonants.upper():
#             count = count + 1
#     print("File", fileName, "has", count, "consonants")

# def numCharCounter(files, fileName):
#     count = 0
#     numChar = "0123456789"
#     for numbers in files:
#         if numbers in numChar:
#             count = count + 1
#     print("File", fileName, "has", count, "numerical characters")


def repeat():
    repeatProgram = input("\nDo you want to try it again? (y or n) ")
    if repeatProgram.upper() == "Y":
        main()
    elif repeatProgram.upper() == "N":
        print("Thanks for playing!")
        quit()
    else:
        print("Please enter y or n.")
        repeat()


def main():
    files, fileName = fileOpener()
    fileName, lineCount, countVowels, countConsonants, countNumbers = Counter(
        files, fileName)
    printResults(fileName, lineCount, countVowels, countConsonants,
                 countNumbers)
    # lineCounter(fileName)
    # vowelCounter(files, fileName)
    # consonantCounter(files, fileName)
    # numCharCounter(files, fileName)
    repeat()


main()
