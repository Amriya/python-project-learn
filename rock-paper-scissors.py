#rock paper scissors-- R,P,S
# user 1: user
# user 2 : cmputer
# check combo
# rock and paper -- PAPER win-- R,P--P
# paper sciss-- scissor win--P,S--S
# rock scissor-- rock win-- R,S--R
# if both same, play again
import random
user_wins=0
computer_wins=0
choices=['rock','paper','sci']
while True:
    user_input = input("Choose Rock/Paper/Scissor or Q to quit: ")
    if user_input == 'Q' :
        break
    if user_input not in choices:
        print('Choose a valid choice.')
        continue
    random_number=random.randint(0,2)
    computer_pick=choices[random_number]
    print("Computer chose:",computer_pick+".")
    if user_input == "rock"  and computer_pick == "sci":
        print('You won!')
    elif user_input == "sci"  and computer_pick == "paper":
        print('You won!')
    elif user_input == "paper"  and computer_pick == "rock":
        print('You won!')
    else:
        print("You lose!")
print('Bye!')

