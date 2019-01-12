# Name: rock-paper-scissors.py
# Author: Joseph Crandal
# Date: Oct 15th, 2018
import random

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

CHOICES = ["rock", "paper", "scissors"]

def NewRound():
    answer = "maybe"
    while answer != "yes" and answer != "no":
        print("##########################################")
        print("Rock Paper Scissors v1")
        print("Would you like to play a round of rock-paper-scissors?")
        answer = str(raw_input("Enter: (yes or no)\n"))
    return answer

def PlayGame():
    player = ""
    while player not in CHOICES:
        print("Player1 choose your weapon:")
        player = str(raw_input("rock paper or scissors?\n"))
    enemy = ""
    while enemy not in CHOICES:
        print("Player2 choose your weapon:")
        enemy = str(raw_input("rock paper or scissors?\n"))
    
    GameResults(player, enemy)

def GameResults(player, enemy):
    print("#########################################")
    print("# RESULTS                                ")
    print("#########################################")
    print("Player1 chose: " + player)
    print("Player2 chose: " + enemy)
    
    if((player == "rock" and enemy == "paper") or (player == "paper" and enemy == "scissors") or (player == "scissors" and enemy == "rock")):
        print("Player2 wins!")
    elif ((player == "rock" and enemy == "scissors") or (player == "paper" and enemy == "rock") or (player == "scissors" and enemy == "paper")):
        print("Player1 wins!")
    elif ((player == "rock" and enemy == "rock") or (player == "paper" and enemy == "paper") or (player == "scissors" and enemy == "scissors")):
        print("The round is a tie!")
    print("#########################################")

def main():
    PLAY = True
    
    while PLAY == True:
        answer = NewRound()
        if(answer == "yes"):
            PlayGame()
        else:
            PLAY = False;

main()
