import random

choice=["stone","paper","scissor"]
your_turn=input("Choise one of the among :Stone,Paper,Scissor\n")
your_turn=your_turn.lower()
print("You Choose "+ your_turn)
computer_turn=random.choice(choice)
print("opponent choose", computer_turn)

if(your_turn==computer_turn):
    print("You both choose same,The Game Is over.....")
elif(your_turn=="stone"):
    if(computer_turn=='paper'):
        print("Paper covers stone, You loose the game...")
    elif(computer_turn=="scissor"):
        print("Stone breaks the scissor,You    Wins.....")
elif(your_turn=="paper"):
    if(computer_turn=="scissor"):
        print("Scissor cuts the paper,You Loose the Game...")
    elif(computer_turn=="stone"):
        print("Paper covers stone,You wins...")
elif(your_turn=="scissor"):
    if(computer_turn=="paper"):
        print("Scissor cuts the paper,You wins the Game....")
    elif(computer_turn=="stone"):
        print("Stone breaks the Scissor,You loose the Game...")
else:
    print("You choose the wrong thing,GAME OVER....")


