print("Enter [R]ock, [P]aper, or [S]cissor")
player1 = input("Player 1: ")

print("Enter [R]ock, [P]aper, or [S]cissor")
player2 = input("Player 2: ")


def nobodyWins():
    print("Nobody Wins")


def paperCoversRock(player):
    print("Paper covers rock.\n" + "Player", player, "WINS!")


def rockSmashesScissor(player):
    print("Rock smashes scissor.\n" + "Player", player, "WINS!")


def scissorCutsPaper(player):
    print("Scissors cut paper.\n" + "Player", player, "WINS!")


def inputChecker(player):
    try:
        validInput = ["r", "R", "p", "P", "s", "S"]
        if player not in validInput:
            raise
    except Exception:
        print("Invalid Input")


def rockPaperScissor(player1, player2):
    inputChecker(player1)
    inputChecker(player2)
    ifStatements(player1.upper(), player2.upper())


def ifStatements(player1, player2):
    if player1 == player2:
        nobodyWins()
    elif player1 == "R":
        if player2 == "P":
            paperCoversRock(2)
        elif player2 == "S":
            rockSmashesScissor(1)
    elif player1 == "P":
        if player2 == "R":
            paperCoversRock(1)
        elif player2 == "S":
            scissorCutsPaper(2)
    elif player1 == "S":
        if player2 == "R":
            rockSmashesScissor(2)
        elif player2 == "P":
            scissorCutsPaper(1)


rockPaperScissor(player1, player2)
