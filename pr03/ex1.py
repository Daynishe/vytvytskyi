def func(lst):
    lstt = list()
    for number in lst:
        if number > 0:
            lstt.append(pow(number, 2))
        if number < 0:
            lstt.append(pow(number, 4))
    return lstt


try:
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))
    c = float(input("Enter a number: "))
except ValueError as err:
    raise ValueError(err)

lst = [a, b, c]

print(func(lst))
