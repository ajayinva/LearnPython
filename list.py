test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_three = test[-3:]
first_part = test[0:6]
print(last_three)
print(first_part)

last_three.extend(first_part)

print(last_three)


