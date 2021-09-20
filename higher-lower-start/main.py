import random
from game_data import data
from art import logo, vs

def random_number(number):
  rand_num = random.randint(0, len(data))
  while rand_num == number:
    rand_num = random.randint(0, len(data))
  return rand_num

def formating(index):
  return f"{data[index]['name']}, {data[index]['description']}, from {data[index]['country']}."

def is_winner(index1, index2):
  if data[index1]['follower_count'] > data[index2]['follower_count']:
    winner = "A"
  else:
    winner = "B"
  return winner

def save_winner(index1, index2):
  if data[index1]['follower_count'] > data[index2]['follower_count']:
    saved_winner = index1
  else:
    saved_winner = index2
  return saved_winner

def play_game():
  print(logo)
  score = 0 
  end_game = False
  random_a = random.randint(0, len(data))
  while not end_game:   
    random_b = random_number(random_a) 
    print(f"Compare A: {formating(random_a)}")
    print(vs)    
    print(f"Against B: {formating(random_b)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    winner = is_winner(random_a, random_b)
    if answer == winner:
      score += 1
      random_a = save_winner(random_a, random_b)
      print(f"You're right! Current score: {score}.")
    else: 
      print(f"Sorry, that's wrong. Final score: {score}")
      end_game = True
    
play_game()