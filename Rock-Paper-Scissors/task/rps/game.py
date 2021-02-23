# Write your code here
import random
options = ["rock", "fire", "scissors", "snake", "human", "tree",
           "wolf", "sponge", "paper", "air", "water", "dragon",
           "devil", "lightning", "gun"]
name = input("Enter your name:")
print("Hello " + name)
file = open("rating.txt", "r+")
player_list = []
for line in file:
    [player, score] = line.split()
    score = int(score)
    player_list.append(player)
    if name == player:
        break
if name not in player_list:
    score = 0
    file.write("\n" + name + " " + str(score))
user_options = input("Select options")
if user_options == "":
    user_options = ["paper", "rock", "scissors"]
else:
    user_options = user_options.split(",")
print("Okay, let's start")

while True:
    selection = input()
    c_select = random.choice(user_options)
    if selection == "!exit":
        print("Bye!")
        file.close()
        break
    elif selection == "!rating":
        print(score)
    elif selection not in user_options:
        print("Invalid input")
    elif selection in user_options:
        index_p_select = options.index(selection)
        index_c_select = options.index(c_select)
        case_1 = index_c_select - index_p_select
        case_2 = index_c_select - (index_p_select - 7)
        if index_p_select < 8 and 0 < case_1 < 8:
            #win
            score += 100
            print("Well done. The computer chose "+ c_select +" and failed")
        elif index_c_select == index_p_select:
            #empate
            score += 50
            print("There is a draw " + c_select)
        elif index_p_select > 7 and (case_2 > 7 or case_2 < 0 ):
            #win
            score += 100
            print("Well done. The computer chose " + c_select + " and failed")
        else:
            #loose
            print("Sorry, but the computer chose " + c_select)






