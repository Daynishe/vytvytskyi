def find_divisors(a, b, c, k):
    divisors_a = [i for i in range(1, a + 1) if a % i == 0]
    divisors_b = [i for i in range(1, b + 1) if b % i == 0]
    divisors_c = [i for i in range(1, c + 1) if c % i == 0]

    common_divisors = set(divisors_a) & set(divisors_b) & set(divisors_c)

    if k in common_divisors:
        print(f"{k} є дільником чисел a, b, c.")
    else:
        print(f"{k} не є дільником чисел a, b, c.")


try:
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    c = int(input("Введіть число c: "))
    k = int(input("Введіть число k: "))
except ValueError as err:
    raise ValueError(err)

find_divisors(a, b, c, k)
