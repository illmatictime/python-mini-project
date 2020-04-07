def stringFinder(counter):
    try:
        if counter == 0:
            myString = input(
                'Enter a string with two "!" surrounding portion of the string: '
            )
        else:
            myString = input(
                "Please enter a string with a word surrounded by !!: ")
        number1 = myString.find("!")
        number2 = myString.rfind("!")
        if number1 == number2:
            raise
        newString = myString[number1 + 1:number2]
        word = newString[len(newString)::-1]
        if word == "":
            raise
        return word
    except Exception:
        print("Invalid string.")
        return ""


def stringPrinter(word):
    for letter in word:
        print(letter)
    # index = 0
    # while index < len(newString):
    #     singleLetter = newString[index]
    #     print(singleLetter)
    #     index = index + 1


def repeat():
    repeatProgram = input("Do you want to try again? (y/n) ")
    if repeatProgram.upper() == "Y":
        print("")
    elif repeatProgram.upper() == "N":
        print("Thank You for playing.")
        quit()
    else:
        print("Please enter y or n.")
        repeat()


def main():
    index = 0
    while True:
        word = stringFinder(index)
        if word != "":
            stringPrinter(word)
            index += 1
            repeat()


main()
