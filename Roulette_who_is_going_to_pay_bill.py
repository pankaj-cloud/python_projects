import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(len(names))

total_number_of_persons = len(names)
# print(total_number_of_persons)

random_number = random.randint(0, total_number_of_persons - 1)
# print(random_number)

bill_paid_by = names[random_number]
print(bill_paid_by + ' is going to buy the meal today! ')