hours = input("Please enter number of hours worked for this week: ")
rate = input("What is hourly rate? ")


def CalPay(hours, rate):
    errorCheckPositiveFloat(hours, "You entered wrong information for hours.")
    errorCheckPositiveFloat(rate, "You entered wrong rate information.")
    hours = float(hours)
    rate = float(rate)

    if 0 < hours <= 40:
        pay = hours * rate
        print("Your pay for this week:", hours * rate)
    elif 40 < hours <= 60:
        pay = (hours * rate) + ((hours - 40) * rate * 0.5)
        print("Your pay for this week:", pay)
    elif hours > 60:
        pay = (hours * rate) + (20 * rate * 0.5) + ((hours - 60) * rate)
        print("Your pay for this week:", pay)
    else:
        print("SHOULD NEVER GET HERE.")
        quit()


def errorCheckPositiveFloat(value, errorMessage):
    try:
        value = float(value)
        if value <= 0:
            raise
    except Exception:
        print(errorMessage)
        quit()


CalPay(hours, rate)
