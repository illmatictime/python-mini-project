myInput = input("Enter a string with a colon and a number after it: ")

findColon = myInput.find(":")

# aNumber = slice(findColon+1, len(myInput))
myInput = myInput[findColon + 1:len(myInput)]

myInput = float(myInput) + 2.0
print("Extracted a number from given string and added 2.0 to it:", myInput)
