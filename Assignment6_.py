import re


def userInput():
    # print('Please enter a filename:')
    while True:
        fileName = input("Please enter a filename: ")
        if not re.search(r"\.", fileName):
            print("File name needs to have an extension")
            # Filename can contain only Alphabets, digits and "_".
            # Filename only can start with Alphabets or '_'.
            # Can not contain any special characters.
        elif not re.search('^[a-zA-Z_]', fileName):
            print("Filename can only start with Alphabets or '_'.")
        elif re.search('[^a-zA-Z_0-9._]', fileName):
            print("Filename can only contain Alphabets, digits and underscore")
            # fileOpen = open(fileName, "a+")  # a+
        else:
            return fileName


def appendLines(fileName):
    openFile = open(fileName, "a+")
    while True:
        openFile.writelines([input("Please enter a sentence: "), "\n"])
        userInput = input("Do you want to add more lines? (Y/N) ")
        if userInput.upper() == "Y":
            pass
        elif userInput.upper() == "N":
            print("This is what's entered into file", fileName + ".")
            print("=============================")
            openFile.close()
            openFile = open(fileName, "r")
            print(openFile.read())
            print("=============================")
            openFile.close()
            break


def newFile():
    repeatProgram = input("Do you want to create another file? (Y/N) ")
    if repeatProgram.upper() == "Y":
        pass
    elif repeatProgram.upper() == "N":
        print("Thank you for playing!")
        return True
        # quit()
    else:
        print("Please enter y or n.")
        newFile()


def main():
    while True:
        fileName = userInput()
        appendLines(fileName)
        result = newFile()
        if result == True:
            break


main()
