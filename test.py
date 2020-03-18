while True:
    try:
        hours = input("Please enter number of hours worked for this week: ")
        hours = float(hours)
        if hours <= 0:
            raise
        break
    except Exception:
        print("You entered wrong information for hours.")
        print("Try again!")


while True:
    try:
        rate = input("What is hourly rate? ")
        rate = float(rate)
        if rate <= 0:
            raise
        break
    except Exception:
        print("You entered wrong rate information.")
        print("Try again!")


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
