import random
from art import logo

def choose_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    play_level = 10
  elif level == "hard":
    play_level = 5
  return play_level

def check_the_answer(number, guessed_number):
  if number < guessed_number:
    print(f"Too low.")
  elif number > guessed_number:
    print(f"Too high.")   
  elif number == guessed_number:
    print(f"You got it! The answer was {guessed_number}.")

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  guessed_number = random.randint(1,100)
  attempt = choose_level()
  print(f"You have {attempt} attempts remaining to guess the number.") 
  choice = 0
  while choice != guessed_number:  
    choice = int(input("Make a guess: ")) 
    attempt -= 1
    check_the_answer(choice, guessed_number)
    if attempt == 0:
      print("You've run out of guesses, you lose.")      
      return
    if choice != guessed_number:
      print(f"Guess again. \nYou have {attempt} attempts remaining to guess the number.")    

play_game() 