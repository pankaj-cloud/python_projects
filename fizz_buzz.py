
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 != 0:
#     number = "Fizz"
#   elif number % 5 == 0 and number % 3 != 0:
#     number = "Buzz"
#   elif number % 3 == 0 and number % 5 == 0:
#     number = "FizzBuzz"
#   print(number)

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
   print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)