def repeatProgram():
    myString = input("Enter a string with two " + "!" + "surrounding of the string: ")
    number1 = myString.find("!")
    number2 = myString.rfind("!")
    newString = myString[number1 + 1 : number2]
    newString = newString[len(newString) :: -1]

    index = len(newString)
    newString1 = []
    while index > 0:
        newString1 += newString[index - 1]
        index = index - 1
        print(newString1)


repeatProgram()
