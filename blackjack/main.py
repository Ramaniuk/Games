import random
from replit import clear
from art import logo

def deal_cards():
  """"returns a random card from a pile"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def current_score(player_result, computer_result):
  print(f"Your cards: {player_result}, current score: {sum(player_result)} ")
  print(f"Dealer\'s first card: {computer_result[0]} ")

def final_score(player_result, computer_result):
  print(f"Your final hand: {player_result}, final score: {sum(player_result)} ")
  print(f"Dealer\'s: {computer_result}, final score: {sum(computer_result)} ")

def check_score(player_result, computer_result):
  player_score = sum(player_result)
  computer_score = sum(computer_result)
  if player_score == 21 and len(player_result) == 2:
    final_score(player_result, computer_result)
    print("Win with a Blackjack")
  elif computer_score == 21 and len(computer_result) == 2:
    final_score(player_result, computer_result)
    print ("Lose, opponent has Blackjack")
  elif player_score > 21:
    final_score(player_result, computer_result)
    print("You went over. You lose")
  elif computer_score > 21:
    final_score(player_result, computer_result)
    print("Opponent went over. You win")
  elif player_score == computer_score: 
    final_score(player_result, computer_result)
    print("Draw")
  elif computer_score > player_score:
    final_score(player_result, computer_result)
    print("You lose")
  elif player_score > computer_score:
    final_score(player_result, computer_result)
    print("You win")
  return True
    
def twenty_one(cards): 
  if sum(cards) > 21:
    for i in range(len(cards)):
      if cards[i] == 11:
        cards[i] = 1
  return cards

def player_round(player_result, computer_result):
  while input(f"Type 'y' to get another card, type 'n' to pass: ") == 'y':
    card = deal_cards()
    player_result.append(card)
    player_result = twenty_one(player_result)
    current_score(player_result, computer_result)
  return player_result

def computer_round(computer_result):
  computer_score = sum(computer_result)
  while computer_score < 17 and (computer_score != 21 and len(computer_result) == 2):
    card = deal_cards()
    computer_result.append(card)
    computer_result = twenty_one(computer_result)
    computer_score = sum(computer_result)
  return computer_result

def play_game():
  print(logo)
  player_score = []
  dealer_score = []

  end_game = False
  while not end_game:    
    for i in range(2):
      player_score.append(deal_cards())
      dealer_score.append(deal_cards())
    current_score(player_score, dealer_score)

    player_score = player_round(player_score, dealer_score)
    dealer_score = computer_round(dealer_score) 
    end_game = check_score(player_score, dealer_score)
    print(player_score)
    print(dealer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()