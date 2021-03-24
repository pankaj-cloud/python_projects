student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)
total = 0
# for n in range(0, len(student_heights)):
for n in range(0, len(student_heights)):
  total = total + student_heights[n]
# print(total)
count = 0
for i in student_heights:
  count += 1
# print(count)
average_height = int(total / count)
print(average_height)
