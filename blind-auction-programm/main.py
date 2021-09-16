from replit import clear
from art import logo

print(logo)

auction = {}
auction_time = True
while auction_time:  
  name = input("What is your name? ")
  bid = int(input("What is your bid? $ "))
  auction[name] = bid
  new_member = input('Are there other users who wants to bid? Answer "yes" or "no" ').lower()
  clear() # replit function allows clear console
  if new_member == "no":
    auction_time = False

def find_highest_bidder(bids):
  max_bid = 0
  highest_bidder = []
  for name in auction:
    if auction[name] > max_bid:
      highest_bidder = [name, auction[name]]
  print(f"The winner is {highest_bidder[0]} with the bid {highest_bidder[1]}") 

find_highest_bidder(auction)    

