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

print('Welcom to the game "Rock, Paper, Scissors"')
result = ""
human_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
if human_move >= 3 or human_move < 0:
  result = "It's invalid move, you loose"
  print(result)
else:
  computer_move = random.randint(0,2)
  list = [rock, paper, scissors]
  print(f"Human_move\n{list[human_move]}\nComputer choose:\n{list[computer_move]}")
  if (human_move == 0 and computer_move == 1) or (human_move == 1 and computer_move == 2) or (human_move == 2 and computer_move == 0):
    result = "You Lose"
  elif (human_move == computer_move):
    result = "It's a tie"
  else:
    result = "You are the winner"
  print(result)
