def sixIntegers():
    print("Please enter 6 integers:")
    i = 0
    even = 0
    odd = 0

    while i < 6:
        six = input(">")
        six = int(six)
        i += 1
        if (six % 2) == 0:
            even = even + six
        elif (six % 2) == 1:
            odd = odd + six
    return even, odd


def printResults(even, odd):
    print("\n\nEven sum:", even)
    print("Odd sum:", odd, "\n")


while True:
    even, odd = sixIntegers()
    printResults(even, odd)
    repeat = input("Do you wish to return this program? (y/n) \n>")
    if repeat.upper() == "Y":
        print("")
        continue
    elif repeat.upper() == "N":
        print("\nDone!")
        quit()
