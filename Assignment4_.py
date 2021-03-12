# Jerry Landeros
def userInput():
    number = int(input("Please enter a number: "))
    return number


def primeChecker(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number.")
                break
        else:
            print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
    # return aPrime, notPrime
    pass


# def printResults(number):
#    print(number, " is a prime number")


def repeat():
    repeatProgram = input("Do you want to play again? (Y or N) ")
    print("\n")
    if repeatProgram.upper() == "Y":
        pass
    elif repeatProgram.upper() == "N":
        print("Thank you for playing!")
        quit()
        # quit()
    else:
        print("Please enter Y or N.")
        repeat()


def main():
    while True:
        number = userInput()
        primeChecker(number)

        # printResults(number)
        repeat()


main()
