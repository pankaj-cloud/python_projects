#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

### below is my code for this project


#Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password1 = random.choices(letters, k = nr_letters)
# password2 = random.choices(numbers, k = nr_numbers)
# password3 = random.choices(symbols, k = nr_symbols)
# password = password1 + password2 + password3
# random.shuffle(password)
# print("Your password is: ", *password,  sep = "")

###Eazy Level--below is code as per given Solution


# password = ""
# for letter in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for symbol in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for number in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

###Hard Level -- below is code as per given Solution


password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
