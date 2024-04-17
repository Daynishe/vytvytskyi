def func(angle1, angle2, angle3):
    res = ""
    if angle3 > 0:
        res += "Трикутник існує.\n"
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            res += "Це прямокутний трикутник.\n"
        elif angle1 < 90 and angle2 < 90 and angle3 < 90:
            res += "Це гострокутний трикутник.\n"
        else:
            res += "Це тупокутний трикутник.\n"
    else:
        res += "Такого трикутника не існує.\n"
    return res


try:
    angle1 = float(input("Введіть перший кут (в градусах): "))
    angle2 = float(input("Введіть другий кут (в градусах): "))
    angle3 = 180 - (angle1 + angle2)
except ValueError as err:
    raise ValueError(err)

print(func(angle1, angle2, angle3))
