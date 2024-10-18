
class ProductosControl():

    def __init__(self,registroICA: str, nombre: str, precio: float,frecAplicacion: int):
        self.__registroICA = registroICA
        self.__nombre = nombre
        self.__precio = precio
        self.__frecAplicacion = frecAplicacion
        
    
    @property
    def getRegistroICA(self):
        return self.__registroICA
    @property
    def getNombre(self):
        return self.__nombre
    @property
    def getPrecio(self):
        return self.__precio
    @property
    def getFrecAplicacion(self):
        return self.__frecAplicacion
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setRegistroICA(self, registroICA):
        self.__registroICA = registroICA
    
    def setPrecio(self, precio):
        self.__precio = precio
    
    def setFrecAplicacion(self, frecAplicacion):
        self.__frecAplicacion = frecAplicacion