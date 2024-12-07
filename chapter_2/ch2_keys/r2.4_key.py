"""Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type."""


class Flower:

    def __init__(self, name: str, petals: int, price: float):

        self._name = name
        self._petals = petals
        self._price = price

    # setters
    def set_name(self, name: str):
        self._name = name

    def set_petals(self, petals: int):
        self._petals = petals

    def set_price(self, price: float):
        self._price = price

    # getters
    def get_name(self):
        print(self._name)

    def get_petals(self):
        print(self._petals)

    def get_price(self):
        print(self._price)


flower1 = Flower("Rose", 25, 10.0)

flower1.get_name()
flower1.get_petals()
flower1.get_price()

flower1.set_name("Lily")
flower1.set_petals(10)
flower1.set_price(15.0)

flower1.get_name()
flower1.get_petals()
flower1.get_price()


