import math
def paint_calc(height, width, cover):
  number_of_cans = test_h * test_w / coverage
  number_of_cans = math.ceil(number_of_cans)
#   def RoundUP(number_of_cans):
#     if number_of_cans == int(number_of_cans):
#       return number_of_cans
#     else:
#       return int(number_of_cans + 1)
#   cans = RoundUP(number_of_cans) 
  print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)