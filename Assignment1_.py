def userInput():  # takes user input for number of sides and lenght of sides
    year = int(input('Please enter the 4 digit year: '))
    month = int(input('Please enter the month: '))
    return year, month


def leapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysMonth(year, month):
    list = [1, 3, 5, 7, 8, 10, 12]
    list2 = [4, 6, 9, 11]
    if month in list:
        days = 31
    elif month in list2:
        days = 30
    elif leapYear(year):
        days = 29
        print("leap year")
    elif leapYear(False):
        days = 28
        print("not a leap year")

    return days


def printResults(year, month, days):
    print("Year", year, "Month", month, "has", days, "days in a month")


def repeat():
    repeatProgram = input("Do you want to repeat? (Y/N) ")
    if repeatProgram.upper() == "Y":
        pass
    elif repeatProgram.upper() == "N":
        print("Thank you for playing! ")
        quit()
        # quit()
    else:
        print("Please enter y or n.")
        repeat()


def main():
    while True:
        year, month = userInput()
        leapYear(year)
        days = daysMonth(year, month)
        printResults(year, month, days)
        repeat()


main()
