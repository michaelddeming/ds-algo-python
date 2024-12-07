"""Draw a class inheritance diagram for the following set of classes:
• Class Goat extends object and adds an instance variable tail and
methods milk() and jump().
• Class Pig extends object and adds an instance variable nose and
methods eat(food) and wallow().
• Class Horse extends object and adds instance variables height and
color, and methods run() and jump().
• Class Racer extends Horse and adds a method race().
• Class Equestrian extends Horse, adding an instance variable weight
and methods trot() and is trained()."""


class Animal:

    def __init__(self):
        pass


class Goat(Animal):

    def __init__(self, tail):
        super().__init__()
        self._tail = tail

    def milk():
        pass

    def jump():
        pass


class Pig(Animal):

    def __init__(self, nose):
        super().__init__()
        self._nose = nose

    def eat(food):
        pass

    def wallow():
        pass


class Horse(Animal):
    def __init__(self, height, color):
        super().__init__()
        self._height = height
        self._color = color

    def run():
        pass

    def jump():
        pass


class Racer(Horse):
    def __init__(self, height, color):
        super().__init__(height, color)

    def race():
        pass


class Equestrian(Horse):
    def __init__(self, height, color, weight):
        super().__init__(height, color)
        self._weight = weight

    def trot():
        pass

    def is_trained():
        pass
