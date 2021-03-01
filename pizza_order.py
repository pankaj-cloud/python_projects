
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


# Small_Pizza_price = 15
# Medium_Pizza_price = 20
# Large_Pizza_price = 25
# Pepperoni_for_SmallPizza = 2
# Pepperoni_for_MediumPizza = 3
# Pepperoni_for_LargePizza = 3
# Extracheese = 1

bill = 0
if size == "S":
  bill = 15 
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")
else:
  print("No other sizes are available")



