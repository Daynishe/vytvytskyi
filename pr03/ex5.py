def determine_point_location(x, y):
    if x == 0 and y == 0:
        return "Точка А знаходиться в початку координат."
    elif x == 0:
        return f"Точка А лежить на осі OY (вертикальна лінія) при y = {y}."
    elif y == 0:
        return f"Точка А лежить на осі OX (горизонтальна лінія) при x = {x}."
    elif x > 0 and y > 0:
        return "Точка А знаходиться в I квадранті."
    elif x < 0 and y > 0:
        return "Точка А знаходиться в II квадранті."
    elif x < 0 and y < 0:
        return "Точка А знаходиться в III квадранті."
    else:
        return "Точка А знаходиться в IV квадранті."


try:
    x_coordinate = float(input("Введіть координату x для точки А: "))
    y_coordinate = float(input("Введіть координату y для точки А: "))
except ValueError as err:
    raise ValueError(err)

location_result = determine_point_location(x_coordinate, y_coordinate)
print(location_result)
