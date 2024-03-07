def replace_numbers(a, b):
    if a != b:
        a = max(a, b)
        b = max(a, b)
    else:
        a = 0
        b = 0
    return a, b


try:
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
except ValueError as err:
    raise ValueError(err)

result_a, result_b = replace_numbers(a, b)
print(f"Після заміни: {a} = {result_a}, {b} = {result_b}")
