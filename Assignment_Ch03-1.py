hours = float(input("Please enter number of hours worked for this week: "))
rate = float(input("What is hourly rate? "))

# print("You entered wrong information for hours.")
# print("You entered wrong rate information")


if hours > 40:
    overtime = hours - 40
    overtime = overtime * rate * 1.5
    print(overtime)
elif hours > 60:
    doubleTime = hours - 60
    doubleTime = hours * rate * 2
    print(doubleTime + rate)
else:
    print(hours * rate)
