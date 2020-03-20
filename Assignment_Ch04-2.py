aUser = input("Please enter the first integer: ")
bUser = input("Please enter the second integer: ")
cUser = input("Please enter the third integer: ")

# Error Check


def positiveIntegerCheck(value):
    try:
        value = int(value)
    except Exception:
        print("Please input aUser valid Integer!")
        quit()

# Compare Inputs


def compareInput(aUser, bUser, cUser):
    positiveIntegerCheck(aUser)
    positiveIntegerCheck(bUser)
    positiveIntegerCheck(cUser)
    aUser = int(aUser)
    bUser = int(bUser)
    cUser = int(cUser)

    if aUser >= bUser and bUser >= cUser:
        asorted = str(cUser)+" "+str(bUser)+" "+str(aUser)
    elif aUser >= cUser and cUser >= bUser:
        asorted = str(bUser)+" "+str(cUser)+" "+str(aUser)
    elif bUser >= aUser and aUser >= cUser:
        asorted = str(cUser)+" "+str(aUser)+" "+str(bUser)
    elif bUser >= cUser and cUser >= aUser:
        asorted = str(aUser)+" "+str(cUser)+" "+str(bUser)
    elif cUser >= bUser and bUser >= aUser:
        asorted = str(aUser)+" "+str(bUser)+" "+str(cUser)
    elif cUser >= aUser and aUser >= bUser:
        asorted = str(bUser)+" "+str(aUser)+" "+str(cUser)
    return asorted
