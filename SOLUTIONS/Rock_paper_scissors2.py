def main():
    print("Welcome to RPS")
    start_game = input("Would you like to play a new game? Y/N")
    while start_game != "N":
        player1 = input("What's your choose player 1(R - P - S): ")
        player2 = input("What's your choose player 2(R - P - S): ")
        if player1 == player2:
            print("DRAW")
        elif player1 == "R" and player2 == "S" or player1 == "S" and player2 == "P" or player1 == "P" and player2 == "R":
            print("Congrat player 1, you won !!!")
        else:
            print("Congrat player 2, you won !!!")
        start_game = input("Would you like to play a new game? Y/N")

main()