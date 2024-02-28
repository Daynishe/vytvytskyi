a, b, counter = 0, 1, 1
while counter != 21:
    temp = a + b
    a, b = b, temp
    if counter >= 5:
        print(f"{counter}. {temp}")
    counter += 1

counter = 1
print(f"Парні числа:")
while counter <= 20:
    if counter % 2 == 0:
        print(f"{counter}")
    counter += 1


counter = -1
print(f"Парні числа негативні:")
while counter >= -21:
    if counter % 2 == 0:
        print(f"{counter}")
    counter -= 1
