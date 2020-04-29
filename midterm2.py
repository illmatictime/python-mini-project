# The program reads a string and then removes the spaces at the beginning
# and at the end, prints the length of string, count of digits, count of
# alphabets, and total sum of digits, able to repeat program


# This program reads the word and strips the beginning and end spaces
def readWord():
    myWord = input(
        "Please enter a string consists of alphanumeric characters: ")
    myWord = myWord.strip()
    return myWord


# counts the alphabets, digits, and finds the total length of the sum
# also gives a sum of the digits in the string
def counter(myWord):
    countAlphabets = 0
    countDigits = 0
    digitSum = 0
    # alphabets = "abcdefghijklmnopqrstuvwxyz"
    # digits = "0123456789"

    lenMyWord = len(myWord)  # finds length of string

    for x in myWord:
        if (x.isdigit()) == True:
            countDigits += 1  # counts the digits
            digitSum += int(x)  # counts the total sum of digits
        elif (x.isalpha()) == True:
            countAlphabets += 1  # counts the alphabets
    return lenMyWord, countDigits, countAlphabets, digitSum


# prints the results of my counter function
# length of string, count of digits, count of alphabets, total sum of digits
def printResults(lenMyWord, countDigits, countAlphabets, digitSum):
    print("Your string is", lenMyWord, "long.")
    print("Your string has", countAlphabets, "alphabets.")
    print("Your string is", countDigits, "digits.")
    print("Your string digits total is:", digitSum, "\n")


# gives the opportunity to repeat a program
# ask for Y, N
def repeat():
    repeatProgram = input("Do you want to try again? (y or n) ")
    if repeatProgram.upper() == "Y":
        print("\n")
    elif repeatProgram.upper() == "N":
        print("\nThank you for playing.")
        return True
    else:
        print("Please enter y or n.")
        repeat()


# main function that calls all the other functions in the program
# it is in a while loop to constantly run until directed by the user to stop
def main():
    while True:
        myWord = readWord()
        lenMyWord, countDigits, countAlphabets, digitSum = counter(myWord)
        printResults(lenMyWord, countDigits, countAlphabets, digitSum)
        result = repeat()
        if result == True:
            break


main()