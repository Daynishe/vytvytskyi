try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
except ValueError as err:
    raise ValueError(err)

lst = [a, b, c]

for number in lst:
    if number > 0:
        print(pow(number, 2))
    if number < 0:
        print(pow(number, 4))
