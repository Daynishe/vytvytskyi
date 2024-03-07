try:
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))
except ValueError as err:
    raise ValueError(err)

if x < y:
    smaller = x
    bigger = y
else:
    smaller = y
    bigger = x

new_smaller = (x + y) / 2
new_bigger = 2 * x * y

print(f"Менше число замінено на {new_smaller:.2f}")
print(f"Більше число замінено на {new_bigger:.2f}")
