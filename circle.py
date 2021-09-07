from math import pi
class Circle:

    def __init__(self, radio):
        self.radio= radio
    # calcula la circunferencia de un circulo segun el radio
    def circunference(self):
        return pi * self.radio*2

    def printCircunference(self):
        print(f'La circunferencia de un circulo con radio de {self.radio} es igual {round(self.circunference(),2)}')




circle1 = Circle(2)
circle2 = Circle(5)
circle3 = Circle(7)

circle1.printCircunference()
circle2.printCircunference()
circle3.printCircunference()