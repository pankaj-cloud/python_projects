total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number
print(total)

total2 = 0
for number in range(2, 100, 2):
  total2 += number

print(total2)