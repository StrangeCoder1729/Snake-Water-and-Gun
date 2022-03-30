# Rules:-
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.


import random

user_won = 0
user_won_scoreboard = []
comp_won = 0
comp_won_scoreboard = []
number_of_times = int(input("How many times do you want to play the game : "))
i = 1


print("Your Choices :-")
print("(1) snake")
print("(2) sater")
print("(3) gun")
while(i <= number_of_times):
    print()
    # print(i)
    user_choice = ["Snake","Water","Gun"]

    user_choices = int(input("Enter your Choice (Serial Number) : "))
    user = (user_choice[user_choices - 1])
    user = user.lower()
    print(user)


    print()
    computer_choices =["snake","water","gun"]
    comp_choice = random.randint(0,2)
    print("Computer Choice :-")
    comp = computer_choices[comp_choice]
    print(comp)

    if((user == "snake" and comp == "water") ):
        print("You Win !!")
        user_won +=1
        user_won_scoreboard.append(user_won)
    elif(user == "water" and comp == "gun"):
        print("You Win !!")
        user_won +=1
        user_won_scoreboard.append(user_won)


    elif(user == "gun" and comp == "snake"):
        print("You Win !!")
        user_won +=1
        user_won_scoreboard.append(user_won)

    else:
        print("You Lose !!")
        comp_won +=1
        comp_won_scoreboard.append(comp_won)
   
    i+=1
print("***************************************************Score Results************************************************************")
print()
# print(f"User Won : {user_won_scoreboard}")   
# print(f"Compter Won : {comp_won_scoreboard}")
print()
use = len(user_won_scoreboard)
 
comp = len(comp_won_scoreboard)
if(len(user_won_scoreboard) > len(comp_won_scoreboard)):
    print("You Won !!!")
    print(f"You won {use} time(s) and Computer won {comp} time(s)")
elif(len(comp_won_scoreboard) > len(user_won_scoreboard)):
    print("You Lose !!!")
    print(f"You won {use} time(s) and Computer won {comp} time(s)")
else:
    print("Its a tie !")