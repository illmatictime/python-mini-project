theList = [3, 8, 5, 1, 4, 9, 2, 10, 7]


def evenOdd(value):
    even = 0
    odd = 0
    for x in value:
        if (x % 2) == 0:
            even = even + x
        elif (x % 2) == 1:
            odd = odd + x
    return odd, even


def minInteger(value):
    smallest = None
    for x in value:
        if smallest is None or x < smallest:
            smallest = x
    return smallest


def maxInteger(value):
    largest = None
    for x in value:
        if largest is None or x > largest:
            largest = x
    return largest


def printResults(even, odd, largest, smallest):
    print("Sum of even numbers is: {:>4}".format(even))
    print("Sum of odd numbers is: {:>5}".format(odd))
    print("Largest number in the list is: {:>4}".format(largest))
    print("Smallest number in the list is: {:>3}".format(smallest))


odd, even = evenOdd(theList)
largest = maxInteger(theList)
smallest = minInteger(theList)
printResults(even, odd, largest, smallest)
