#cree una clase vehiculo que contenga los atributos de instancia velocidad maxima y kilometraje
class Vehiculo:
    def __init__ (self,velocidad,kilometraje):
        self.velocidad:int=velocidad
        self.kilometraje:int=kilometraje


a=Vehiculo(180,90000)
print(a.velocidad,a.kilometraje)




