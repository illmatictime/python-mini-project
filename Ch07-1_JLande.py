def fileOpener():
    while True:
        try:
            fileName = input("Please enter file name: ")
            fileOpen = open(fileName)
            files = fileOpen.read()
            return files, fileName
        except IOError:
            print("File cannot be opened: ", fileName)


def lineCounter(files, fileName):
    count = 1
    for lines in files:
        if lines in "\n":
            count = count + 1
    print("File", fileName, "has", count, "lines")


def vowelCounter(files, fileName):
    count = 0
    vowels = "aeiouAEIOU"
    for letters in files:
        if letters in vowels:
            count = count + 1
    print("File", fileName, "has", count, "vowels")


def consonantCounter(files, fileName):
    count = 0
    consonants = "bcdfghjklmnpqrstvwxyz"
    for letters in files:
        if letters in consonants or letters in consonants.upper():
            count = count + 1
    print("File", fileName, "has", count, "consonants")


def numCharCounter(files, fileName):
    count = 0
    numChar = "0123456789"
    for numbers in files:
        if numbers in numChar:
            count = count + 1
    print("File", fileName, "has", count, "numerical characters")


def repeat():
    repeatProgram = input("\nDo you want to try it again? (y or n) ")
    if repeatProgram.upper() == "Y":
        main()
    elif repeatProgram.upper() == "N":
        print("Thanks for playing!\n>>>")
        quit()
    else:
        print("Please enter y or n.")
        repeat()


def main():
    files, fileName = fileOpener()
    lineCounter(files, fileName)
    vowelCounter(files, fileName)
    consonantCounter(files, fileName)
    numCharCounter(files, fileName)
    repeat()


main()
