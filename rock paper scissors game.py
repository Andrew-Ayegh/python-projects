import random 

# this is where user makes their choice for rock, paper or scissors
user_input = input(" rock/paper/scissors  ").strip()

# this is where the computer makes in choice for rock, paper or scissors
computer_choice = random.randint(1, 3)

if computer_choice == 1 :
    computer_choice = "rock"
    print(computer_choice)
elif computer_choice == 2:
    computer_choice = "paper"
    print(computer_choice)
elif computer_choice == 3:
    computer_choice = "scissors"
    print(computer_choice)
else:
    pass

print(user_input)

if computer_choice == "rock" and user_input == "rock":
    print("draw")
if computer_choice ==  "rock" and user_input == "paper":
    print("yay, you won")
if computer_choice == "rock" and user_input == "scissors":
    print("you lost")
if computer_choice == "paper" and user_input == "rock":
    print("you lost")
if computer_choice == "paper" and user_input == "paper":
    print("draw")
if computer_choice == "paper" and user_input == "scissors":
    print("you won")
if computer_choice == "scissors" and user_input == "rock":
    print("you win")
if computer_choice == "scissors" and user_input == "paper":
    print("you lost")
if computer_choice == "scissors" and user_input == "scissors":
    print("draw")

# print('''
#       scissors
#         __
#        / /__________
#      |    __________/
#      |    __________/
#      |    __________/
#      |__________/     
#       ''')