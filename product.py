class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"{self.__dict__}"
