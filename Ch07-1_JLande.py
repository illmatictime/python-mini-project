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
    print(count)


def consonantCounter(files, fileName):
    count = 0
    consonants = "bcdfghjklmnpqrstvwxyz"
    for letters in files:
        if letters in consonants or letters in consonants.upper():
            count = count + 1
    print(count)


def numCharCounter(files, fileName):
    count = 0
    numChar = "0123456789"
    for numbers in files:
        if numbers in numChar:
            count = count + 1
    print(count)
# vowels = [a, e, i, o, u]
# print("File fileName has # vowels")
# # consonants = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z]
# print("File fileName has # consonants")

# print("File fileName has # numerical characters")

# print("Do you want to try it again? (y or n)")

# print("Thanks for playing!\n>>>")


files, fileName = fileOpener()
lineCounter(files, fileName)
vowelCounter(files, fileName)
consonantCounter(files, fileName)
numCharCounter(files, fileName)
