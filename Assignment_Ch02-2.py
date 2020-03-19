seconds = input("Enter the elapsed time in seconds: ")
print("The elapsed time in seconds = " + seconds)

seconds = int(seconds)
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remSeconds = seconds % 60

time = str(hours) + ":" + str(minutes) + ":" + str(remSeconds)

print("The equivalent time in hours:minutes:seconds =", time)
