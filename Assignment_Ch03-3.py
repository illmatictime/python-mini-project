print("Enter [R]ock, [P]aper, or [S]cissor")
player1 = input("Player 1: ")

print("Enter [R]ock, [P]aper, or [S]cissor")
player2 = input("Player 2: ")


try:
    validInput = ["r", "R", "p", "P", "s", "S"]
    if player1 not in validInput:
        raise
    elif player2 not in validInput:
        raise
except Exception:
    print("Invalid Input")
    quit()

if player1 == "r" or player1 == "R":
    if player2 == "r" or player2 == "R":
        print("Nobody WINS!")
    elif player2 == "p" or player2 == "P":
        print("Paper covers rock.\nPlayer 2 WINS!")
    elif player2 == "s" or player2 == "S":
        print("Rock smashes scissor.\nPlayer 1 WINS")
elif player1 == "p" or player1 == "P":
    if player2 == "p" or player2 == "P":
        print("Nobody WINS!")
    elif player2 == "r" or player2 == "R":
        print("Paper covers rock.\nPlayer 1 WINS!")
    elif player2 == "s" or player2 == "S":
        print("Scissors cut paper.\nPlayer 2 WINS")
elif player1 == "s" or player1 == "S":
    if player2 == "s" or player2 == "S":
        print("Nobody WINS!")
    elif player2 == "r" or player2 == "R":
        print("Rock smashes scissor.\nPlayer 1 WINS!")
    elif player2 == "p" or player2 == "P":
        print("Paper covers rock.\nPlayer 2 WINS")
