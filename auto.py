#Definicion de clase Auto
class Auto:
    #Constructor de la clase
    def __init__(self, marca, modelo,tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

    #Imprime datos del auto
    def imprimir(self):
        print(f'Marca: {self.marca}, Modelo:{self.modelo}, Tipo: {self.tipo}.')

    #Enciende el vehiculo
    def encender(self,key):
        if (key =='777'):
            print('Auto encendido.')
        else:
            print(f'Llave {key} incorrecta para encender el auto') 

    #Apaga el vehiculo
    def apagar(self):
        print("Auto apagado.")


