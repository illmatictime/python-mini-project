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
    print("Input three integer numbers in ascending order:\n" +
          str(c)+" "+str(b)+" "+str(a))
elif a >= c and c >= b:
    print("Input three integer numbers in ascending order:\n" +
          str(b)+" "+str(c)+" "+str(a))
elif b >= a and a >= c:
    print("Input three integer numbers in ascending order:\n" +
          str(c)+" "+str(a)+" "+str(b))
elif b >= c and c >= a:
    print("Input three integer numbers in ascending order:\n" +
          str(a)+" "+str(c)+" "+str(b))
elif c >= b and b >= a:
    print("Input three integer numbers in ascending order:\n" +
          str(a)+" "+str(b)+" "+str(c))
elif c >= a and a >= b:
    print("Input three integer numbers in ascending order:\n" +
          str(b)+" "+str(a)+" "+str(c))
