def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It is prime number")
  else:
    print("It is not prime number") 
  # sum_n = 0
  # for digit in str(n):  
  #   sum_n += int(digit)
  # if n == 2:
  #    print("It is prime number")
  # elif n % 2 != 0 and sum_n % 3 != 0:
  #   print("It is prime number")
  # else:
  #   print("It is not prime number")     

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
