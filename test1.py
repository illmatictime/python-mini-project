import random

for i in range(10):
    x = random.uniform(0, 999)
    print(int(x))

# Jerry Landeros
# 3.6.2020
# Calculates pay based on input of hours and rate

hours = input("Please enter number of hours worked for this week: ")
rate = input("What is hourly rate? ")

try:
    while True:
        hours = float(hours)
        if hours <= 0:
            raise
    pass
except Exception:
    print("You entered wrong information for hours.")
    quit()

try:
    rate = float(rate)
    if rate <= 0:
        raise
except Exception:
    print("You entered wrong rate information.")
    quit()

if 0 < hours <= 40:
    pay = hours * rate
    print("Your pay for this week:", hours * rate)
elif 40 < hours <= 60:
    pay = ((hours*rate) + ((hours - 40)*rate*.5))
    print("Your pay for this week:", pay)
elif hours > 60:
    pay = ((hours*rate) + (20 * rate * .5) + ((hours-60) * rate))
    print("Your pay for this week:", pay)
else:
    print("SHOULD NEVER GET HERE.")
    quit()
