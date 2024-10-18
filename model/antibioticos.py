
class Antibioticos():

    def __init__(self,nombre: str, precio: float, dosis: int, especie: str):
        self.__nombre = nombre
        self.__precio = precio
        self.__dosis = dosis
        self.__especie = especie

    @property
    def getNombre(self):
        return self.__nombre
    
    @property
    def getPrecio(self):
        return self.__precio    
    
    @property
    def getDosis(self):
        return self.__dosis
    
    @property
    def getEspecie(self):
        return self.__especie
    
    def setNombre(self, nombre: str):
        self.__nombre = nombre
    
    def setPrecio(self, precio: float):
        self.__precio = precio
    
    def setDosis(self, dosis: int):
        self.__dosis = dosis
    
    def setEspecie(self, especie: str):
        self.__especie = especie
    