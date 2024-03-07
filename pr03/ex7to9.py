def count_numbers(a, b, c):
    negative_count, positive_count, integer_count = 0, 0, 0
    for num in [a, b, c]:
        if num < 0:
            negative_count += 1
        elif num > 0:
            positive_count += 1
        if num == int(num):
            integer_count += 1

    return negative_count, positive_count, integer_count


try:
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
except ValueError as err:
    raise ValueError(err)

negatives, positives, integers = count_numbers(a, b, c)
print(f"Кількість негативних чисел: {negatives}")
print(f"Кількість додатних чисел: {positives}")
print(f"Кількість цілих чисел: {integers}")
