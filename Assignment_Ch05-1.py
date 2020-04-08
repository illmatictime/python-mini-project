def errorCheckHours():
    while True:
        try:
            hours = input(
                "Please enter number of hours worked for this week: ")
            hours = float(hours)
            if hours <= 0 or hours > 168:
                raise ValueError
            return hours
        except ValueError:
            print("You entered wrong information for number of hours.")


def errorCheckRate():
    while True:
        try:
            rate = input("What is hourly rate? ")
            rate = float(rate)
            if rate <= 0:
                raise ValueError
            return rate
        except ValueError:
            print("You entered improper information for the rate.")


def CalPay(hours, rate):
    hours = float(hours)
    rate = float(rate)

    if 0 < hours <= 40:
        pay = hours * rate
    elif 40 < hours <= 60:
        pay = (hours * rate) + ((hours - 40) * rate * 0.5)
    elif 60 < hours and hours <= 168:
        pay = (hours * rate) + (20 * rate * 0.5) + ((hours - 60) * rate)
    return pay


def printPay(pay):
    print("Your pay for this week:", pay)
    print("==========================================================")


def calculator():
    hours = errorCheckHours()
    rate = errorCheckRate()
    pay = CalPay(hours, rate)
    printPay(pay)
    repeatCalc()


def repeatCalc():
    repeat = input("Do you want another pay calculation? (y or n) ")
    if repeat.upper() == "Y":
        calculator()
    elif repeat.upper() == "N":
        print("Good bye!")
        quit()
    else:
        print("Please enter y or n.")
        repeatCalc()


calculator()
