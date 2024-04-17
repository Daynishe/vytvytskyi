def find_divisors(a, b, c, k):
    lst = [a,b,c]
    for number in lst:
        if number % k == 0:
            print (f"Число {k} є дільником для числа {number}")


try:
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    c = int(input("Введіть число c: "))
    k = int(input("Введіть число k: "))
except ValueError as err:
    raise ValueError(err)

find_divisors(a, b, c, k)
