
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()
total_letters_bothname = lowercase_name1 + lowercase_name2
# print(total_letters_bothname)

T_occurs = total_letters_bothname.count("t")
R_occurs = total_letters_bothname.count("r")
U_occurs = total_letters_bothname.count("u")
E_occurs = total_letters_bothname.count("e")

Total_true = T_occurs + R_occurs + U_occurs + E_occurs
str_Total_true = str(Total_true)
print(type(Total_true))

L_occurs = total_letters_bothname.count("l")
O_occurs = total_letters_bothname.count("o")
V_occurs = total_letters_bothname.count("v")
E_occurs = total_letters_bothname.count("e")

Total_love = L_occurs + O_occurs + V_occurs + E_occurs
str_Total_love = str(Total_love)
# print("Total love score : " +  str_Total_true + str_Total_love)

Overall_Total_love = str_Total_true + str_Total_love
print(type(Overall_Total_love))
Overall_Total_love = int(Overall_Total_love)
print(type(Overall_Total_love))
if Overall_Total_love < 10 or Overall_Total_love > 90:
  print(f"Your score is {Overall_Total_love}, you go together like coke and mentos.")
elif Overall_Total_love >= 40 and Overall_Total_love <= 50:
  print(f"Your score is {Overall_Total_love}, you are alright together.")
else:
  print(f"Your score is {Overall_Total_love}.")
