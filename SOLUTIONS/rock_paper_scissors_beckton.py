# Author: Bec Braughton
# Date: 10.22.18
# FileName: rock_paper_scissors_beckton

playerOneChoice = 0
playerTwoChoice = 0
playerOneName = ""
playerTwoName = ""
playAgain = ''

playerOneName = raw_input("\n - Welcome to Beckton's Rock Paper Scissors Game -\n\nWhat is player one's name: ")
playerTwoName = raw_input("\nWhat is player two's name: ")
playAgain = raw_input("\nWould you like to play, " + playerOneName + " and " + playerTwoName + "? (y or n): ")


if playAgain == 'y':
    print("\nHere are the rules:\n\t* Scissors cuts paper\n\t* Paper covers rock\n\t* Rock smashes scissors\n\nHere are your weapons choices:\n\t* 1 = Rock\n\t* 2 = Paper\n\t* 3 = Scissors")
    while playAgain == 'y':
        playerOneChoice = input("\nChoose your weapon, " + playerOneName + ": ")
        if (playerOneChoice > 0) and (playerOneChoice < 4):
            playerTwoChoice = input("\nChoose your weapon, " + playerTwoName + ": ")

            if (playerTwoChoice > 0) and (playerTwoChoice < 4):

                #playerOne choses rock
                if (playerOneChoice == 1) and(playerTwoChoice == 1):
                    playAgain = raw_input("\n\t- Rock vs. Rock -\n\nYou tied. Would you like to play again? (y or n): ")
                elif (playerOneChoice == 1) and(playerTwoChoice == 2):
                    playAgain = raw_input("\n\t- Rock vs. Paper -\n\n" + playerTwoName + " wins!! Would you like to play again? (y or n): ")
                elif (playerOneChoice == 1) and(playerTwoChoice == 3):
                    playAgain = raw_input("\n\t- Rock vs. Scissors -\n\n" + playerOneName + " wins!! Would you like to play again? (y or n): ")
                    
                #playerOne chooses paper
                elif (playerOneChoice == 2) and(playerTwoChoice == 2):
                    playAgain = raw_input("\n\t- Paper vs. Paper -\n\nYou tied. Would you like to play again? (y or n): ")
                elif (playerOneChoice == 2) and(playerTwoChoice == 1):
                    playAgain = raw_input("\n\t- Paper vs. Rock -\n\n" + playerOneName + " wins!! Would you like to play again? (y or n): ")
                elif (playerOneChoice == 2) and(playerTwoChoice == 3):
                    playAgain = raw_input("\n\t- Paper vs. Scissors -\n\n" + playerTwoName + " wins!! Would you like to play again? (y or n): ")
                    
                #playerOne chooses scissors
                elif (playerOneChoice == 3) and(playerTwoChoice == 3):
                    playAgain = raw_input("\n\t- Scissors vs. Scissors -\n\nYou tied, would you like to play again? (y or n): ")
                elif (playerOneChoice == 3) and(playerTwoChoice == 2):
                    playAgain = raw_input("\n\t- Scissors vs. Paper -\n\n" + playerOneName + " wins!! Would you like to play again? (y or n): ")
                elif (playerOneChoice == 3) and(playerTwoChoice == 1):
                    playAgain = raw_input("\n\t- Scissors vs. Rock -\n\n" + playerTwoName + " wins!! Would you like to play again? (y or n): ")

            elif playAgain == 'n':
                print("\nThanks for stopping by, see you again soon!")    
            else:
                playAgain = raw_input("You must pick a number 1 - 3.\nWould you like to try again? (y or n): ")


if playAgain == 'n':
    print("\nThanks for stopping by, see you again soon!")