
a = int(input("Enter number of amount простих чисел:"))

number = 2
count = 0
while count < a:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
        count += 1

    number += 1
