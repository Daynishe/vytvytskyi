try:
    angle1 = float(input("Введіть перший кут (в градусах): "))
    angle2 = float(input("Введіть другий кут (в градусах): "))
    angle3 = 180 - (angle1 + angle2)
except ValueError as err:
    raise ValueError(err)


if angle3 > 0:
    print("Трикутник існує.")
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Це прямокутний трикутник.")
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("Це гострокутний трикутник.")
    else:
        print("Це тупокутний трикутник.")
else:
    print("Такого трикутника не існує.")
