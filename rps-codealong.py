# Welcoming player and giving instructions.
print("Welcome Players 1 and 2\n When asked for your choice, plase enter 'r', 'p',or 's'")

# Getting players input.
playerOneInput = input("Player one slect: r, p, or s; ")
playerTwoInput = input("Player two slect: r, p, or s; ")

# Compare player input to determine result. Either player1 wins, player2 wins, or its a tie.
if playerOneInput == "s":
    if playerTwoInput == "s":
        print("It's a tie!!! Womp Womp.")
    if playerTwoInput == "r":
        print("Player 2 wins!")
    if playerTwoInput == "p":
        print("Player 1 wins!")

if playerOneInput == "r":
    if playerTwoInput == "s":
        print("Player 1 wins!!!")
    if playerTwoInput == "p":
        print("Player 2 wins!!")
    if playerTwoInput == "r":
        print("It's a tie! Womp Womp.")

if playerOneInput == "p":
    if playerTwoInput == "s":
        print("Player 2 wins!!")
    if playerTwoInput == "r":
        print("Player 1 wins!!!")
    if playerTwoInput == "p":
        print("It's a tie.. Womp Womp")




