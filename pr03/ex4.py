def func(x, y):
    if x < y:
        smaller, bigger = x, y
    else:
        smaller, bigger = y, x

    new_smaller = (x + y) / 2
    new_bigger = 2 * x * y
    return new_smaller, new_bigger



try:
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))
except ValueError as err:
    raise ValueError(err)

smaller, bigger = func(x,y)
print(f"Менше число замінено на {smaller:.2f}")
print(f"Більше число замінено на {bigger:.2f}")