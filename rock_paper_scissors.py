import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_move = int(input("What do you choose ? Type 0 for Rock, 1 for paper or 2 for scissors. : "))
print(f"Your move is {player_move}")
computer_move = random.randint(0, 2)
# print(computer_move)
if player_move == computer_move:
  print("It is tie")
elif player_move == 0:
  print(rock)
  if computer_move == 1:
    print(paper)
    print(f"Computer move is {computer_move}")
    print("Computer Wins !")
  else:
    print(scissors)
    (f"Computer move is {computer_move}")
    print("Player wins !")
elif player_move == 1:
  print(paper)
  if computer_move == 0:
    print(rock)
    (f"Computer move is {computer_move}")
    print("Player Wins !")
  else:
    print(scissors)
    (f"Computer move is {computer_move}")
    print("Computer wins !")
elif player_move == 2:
  print(scissors)
  if computer_move == 0:
    print(rock)
    (f"Computer move is {computer_move}")
    print("Computer Wins !")
  else:
    print(paper)
    (f"Computer move is {computer_move}")
    print("Player wins !")
else:
  print("This is not valid move")
