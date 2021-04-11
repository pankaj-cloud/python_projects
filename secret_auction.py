from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
bidding_not_continued = False

def highest_bidding(bidder_record):
  # "ABC" : 100, "SRT" : 120
  highest_bid = 0
  winner = ''
  for bidder_record in bidder_record:
    quoted_bid = bidder_record[bidder_record]
    if quoted_bid > highest_bid:
      highest_bid = quoted_bid
      winner = bidder_record
  print(f"Highest bidder is {winner} and bid amount is $ {highest_bid} ")


while not bidding_not_continued:
  name = input("What is your name ?:  ")
  bid_amount = int(input("What is your bid amount ? : $"))
  bids[name] = bid_amount
  new_bidder = input("If there is other user who want to bid, please type 'yes' or 'no'\n")
  if new_bidder == "yes":
    clear()
  elif new_bidder == "no":
    bidding_not_continued = True
    highest_bidding(bids)