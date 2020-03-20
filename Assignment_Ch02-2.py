seconds = input("Enter the time elapsed in seconds: ")
print("The elapsed time in seconds = " + seconds)

seconds = int(seconds)
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remSeconds = seconds % 60

print("The equivalent time in hours:minutes:seconds = ", hours, ":", minutes, ":", remSeconds)
print(
    "The equivalent time in hours:minutes:seconds = "
    + str(hours)
    + ":"
    + str(minutes)
    + ":"
    + str(remSeconds)
)
