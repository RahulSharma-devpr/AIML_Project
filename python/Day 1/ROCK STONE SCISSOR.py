"""
Workflow of project :
 1 input your option(ROCK,PAPER,Scissor)
 2 computer choice(chooose randomly)
 3 result print

 cases
  1
  rock-rock= tie
  rock-paper= paper win
  rock-scissor= rock win
  2
  paper-scissor= scissor win
  paper-paper= tie
  paper-rock=rock win
  3
  scissor-paper= scissor win
  scissor-rock= rock win
  scissor-scissor=tie win

"""
import random

item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Please enter your choice: Rock,Paper,Scissor\n")
computer_choice = random.choice(item_list)

print(f"User Choice= {user_choice}, Computer Choice = {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie ")

elif user_choice == "Rock":
    if computer_choice == "Paper":

     print("Paper cover Rock = COMPUTER WIN  ")

else:
    print("Rock Smash Scissor= YOU WIN ")


elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor Cuts Paper = COMPUTER WIN")

    else:
        print("Paper Covers Rock = YOU WIN")

elif user_choice == "Scissor":
     if computer_choice == "Paper":
     print("Scissor Cuts Paper = YOU WIN  ")

 else:
     print("Rock Smash Scissor = YOU LOOSE  ")




