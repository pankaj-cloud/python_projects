import random
rand_num = random.randint(0,2)

player = input("Player, please make your move :").lower()
if rand_num == 0:
    computer_move = "rock"
elif rand_num == 1:
    computer_move = "paper"
else:
    computer_move = 'scissors'

print(f"Computer plays {computer_move}")

# print(computer_move)

if player == computer_move:
    print("It is tie !")
elif player == "rock":
    if computer_move == "scissors":
        print("player wins !")
    elif computer_move == "paper":
        print("computer wins !")
elif player == "paper":
    if computer_move == "rock":
        print("player wins !")
    elif computer_move == "scissors":
        print("computer wins !")
elif player == "scissors":
    if computer_move == "paper":
        print("player wins !")
    elif computer_move == "rock":
        print("computer wins !")
else:
    print("something went wrong")