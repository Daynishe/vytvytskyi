def calc_func(x, y):
    return (x ** 2 + y ** 2) ** 0.5


try:
    AxOne = int(input("Enter A x1:"))
    AyOne = int(input("Enter A y1:"))
    BxOne = int(input("Enter B x1:"))
    ByOne = int(input("Enter B y1:"))
except ValueError as err:
    raise ValueError(err)

if calc_func(AxOne, AyOne) < calc_func(BxOne, ByOne):
    print(f"Точка А ({AxOne}, {ByOne}) знаходиться ближче до початку координат.")
else:
    print(f"Точка В ({BxOne}, {ByOne}) знаходиться ближче до початку координат.")
