class Transport:
    def __init__(self, transport_type, transport_name):
        self.transport_type = transport_type
        self.transport_name = transport_name

    def __str__(self):
        return f"Це є {self.transport_type}. Його назва {self.transport_name}"

    def get_transport_type(self):
        return f"Це є {self.transport_type}."


class Land(Transport):
    # def __init__(self, transport_type, transport_name):
    #     super().__init__(transport_type, transport_name)

    def __str__(self):
        return f"Це дорожній транспорт. Його тип {self.transport_type}. Назва {self.transport_name}"


class Water(Transport):
    def __init__(self, transport_type, transport_name):
        super().__init__(transport_type, transport_name)

    def __str__(self):
        return f"Це водневий транспорт. Його тип {self.transport_type}. Назва {self.transport_name}"


class Auto(Land):
    def __init__(self, transport_type, transport_name):
        super().__init__(transport_type, transport_name)

    def __str__(self):
        return f"Це автомобіль . Його тип {self.transport_type}. Назва {self.transport_name}"


class Boat(Water):
    def __init__(self, transport_type, transport_name):
        super().__init__(transport_type, transport_name)


class Gibrid(Water, Land):
    def __init__(self, transport_type, transport_name):
        super().__init__(transport_type, transport_name)


car = Auto("Car", "Toyota")
ship = Boat("Ship", "Titanic")
hybrid = Gibrid("Hybrid", "ToyotaTitanic")

print(car.get_transport_type())
print(ship.get_transport_type())
print(hybrid.get_transport_type())
print(car)
print(ship)
print(hybrid)
