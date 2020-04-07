a = input("Please enter the first integer: ")
b = input("Please enter the second integer: ")
c = input("Please enter the third integer: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
    print("")
except Exception:
    print("Not a valid input")
    quit()

if a >= b and b >= c:
    print("Input three integer numbers in ascending order:")
    print(c, b, a)
elif a >= c and c >= b:
    print("Input three integer numbers in ascending order:")
    print(b, c, a)
elif b >= a and a >= c:
    print("Input three integer numbers in ascending order:")
    print(c, a, b)
elif b >= c and c >= a:
    print("Input three integer numbers in ascending order:")
    print(a, c, b)
elif c >= b and b >= a:
    print("Input three integer numbers in ascending order:")
    print(a, b, c)
elif c >= a and a >= b:
    print("Input three integer numbers in ascending order:")
    print(b, a, c)
