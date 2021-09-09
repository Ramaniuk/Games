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
human_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
computer_move = random.randint(0,2)
list = [rock, paper, scissors]
print(f"human_move\n{list[human_move]}\nComputer choose:\n{list[computer_move]}")
result = ""
if (human_move == 0 and computer_move == 1) or (human_move == 1 and computer_move == 2) or (human_move == 2 and computer_move == 0):
  result = "You Lose"
elif (human_move == 0 and computer_move == 0) or (human_move == 1 and computer_move == 1) or (human_move == 2 and computer_move == 2):
  result = "It's a tie"
else:
  result = "You are the winner"
print(result)
