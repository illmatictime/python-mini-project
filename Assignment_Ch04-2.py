aUser = input("Please enter the first integer: ")
bUser = input("Please enter the second integer: ")
cUser = input("Please enter the third integer: ")


# Compare Inputs
def compareInput(aUser, bUser, cUser):
    aUser = integerCheck(aUser)
    bUser = integerCheck(bUser)
    cUser = integerCheck(cUser)

    if aUser >= bUser and bUser >= cUser:
        inputSorted = str(cUser) + " " + str(bUser) + " " + str(aUser)
    elif aUser >= cUser and cUser >= bUser:
        inputSorted = str(bUser) + " " + str(cUser) + " " + str(aUser)
    elif bUser >= aUser and aUser >= cUser:
        inputSorted = str(cUser) + " " + str(aUser) + " " + str(bUser)
    elif bUser >= cUser and cUser >= aUser:
        inputSorted = str(aUser) + " " + str(cUser) + " " + str(bUser)
    elif cUser >= bUser and bUser >= aUser:
        inputSorted = str(aUser) + " " + str(bUser) + " " + str(cUser)
    elif cUser >= aUser and aUser >= bUser:
        inputSorted = str(bUser) + " " + str(aUser) + " " + str(cUser)
    return inputSorted


# Error Check


def integerCheck(value):
    try:
        return int(value)
    except Exception:
        print("Please input a valid Integer!")
        quit()


def printResults(inputSorted):
    print("Input three integer numbers in ascending order:\n" + inputSorted)


inputSorted = compareInput(aUser, bUser, cUser)
printResults(inputSorted)
