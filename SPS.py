from random import *

import self





class Game():
    def __init__(self,):
        choices = ["rock", "paper", "scissors"]


    def getchoice(self):
        return random.choice(self.choices)

    def action(self):
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while player_choice not in ["rock", "paper", "scissors"]:
            user_input = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
        return player_choice

    def result(self,player_choice,aichoice):
        if player_choice==aichoice:
            print("it is a tie")
        elif player_choice=="scissors" and aichoice=="paper" :
            print("you win")
        elif player_choice=="rock" and aichoice=="scissors" :
            print("you win")
        elif player_choice=="paper" and aichoice=="rock" :
            print("you win")
        else:
            print("you lose")



