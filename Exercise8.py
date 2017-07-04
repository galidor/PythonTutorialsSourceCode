print("Rock, paper, scissors game.")

next_game = False

if str(input("Do you want to start a new game? (y/n)")).lower() == "y":
    next_game = True
    print("Starting a new game...")
else:
    print("Exiting the game...")
    exit(1)

while True:
    player1 = ""
    player2 = ""
    while (player1 != "rock") and (player1 != "paper") and (player1 != "scissors"):
        player1 = str(input("Player 1 turn, pick one: rock/paper/scissors...\n"))
        print(player1)
    while (player2 != "rock") and (player2 != "paper") and (player2 != "scissors"):
        player2 = str(input("Player 2 turn, pick one: rock/paper/scissors...\n"))

    if (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        print("Player 1 wins!")
    elif (player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper"):
        print("Player 2 wins!")
    elif player1 == player2:
        print("It's a draw!")
    else:
        print("An error occured. Try again.")

    if str(input("Do you want to play once again? (y/n)")).lower() == "y":
        next_game = True
    else:
        next_game = False
        print("Exiting the game...")
        break

