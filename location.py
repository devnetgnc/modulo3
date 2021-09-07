class Location:
    def __init__(self,name, country) :
        self.name =name
        self.country = country
    
    def myLocation(self):
        print(f"Hola, mi nombre es {self.name} y vivo en {self.country}")


loc1 = Location("Gaston", "Argentina")
loc1.myLocation()

loc2 = Location("Juan", "Australia")
loc2.myLocation()

loc3 = Location("Maria", "España")
loc3.myLocation()