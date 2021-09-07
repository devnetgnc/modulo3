from math import pi

#Clase circulo que modela el comportamiento de un circulo y sus funciones
class Circle:

    def __init__(self, radio):
        self.radio= radio
    # calcula la circunferencia de un circulo segun el radio
    def circunference(self):
        return pi * self.radio*2

    def printCircunference(self):
        print(f'La circunferencia de un circulo con radio de {self.radio} es igual {round(self.circunference(),2)}')




()