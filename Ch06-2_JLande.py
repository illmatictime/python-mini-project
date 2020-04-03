def stringFinder():
    while True:
        try:
            myString = input("Enter a string with two " + "!" +
                             "surrounding of the string: ")
            number1 = myString.find("!")
            number2 = myString.rfind("!")
            if number1 == number2:
                raise
            newString = myString[number1 + 1: number2]
            word = newString[len(newString):: -1]
            return word
        except Exception:
            print("Please enter a string with a word surrounded by !!:")


def stringPrinter(word):
    for letter in word:
        print(letter)
    # index = 0
    # while index < len(newString):
    #     singleLetter = newString[index]
    #     print(singleLetter)
    #     index = index + 1


def repeat():
    repeat = input("Do you want to try again? (y/n)")
    if repeat.upper() == "Y":
        print("")
        main()
    elif repeat.upper() == "N":
        print("Thank You for playing.")
        quit()
    else:
        print("Please enter y or n")
        repeat()


def main():
    while True:
        word = stringFinder()
        stringPrinter(word)
        repeat()


main()
