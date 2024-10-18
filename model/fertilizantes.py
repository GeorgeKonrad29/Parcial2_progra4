import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.productos_control import ProductosControl

class Fertilizantes(ProductosControl):
    # Constructor de la clase
    def __init__(self,registroICA: str, nombre: str, precio: float, frecAplicacion: int,ultAplicacion: str):
        super().__init__(registroICA, nombre, precio, frecAplicacion)
        self.__ultAplicacion = ultAplicacion

        
    @property
    def getUltAplicacion(self):
        return self.__ultAplicacion
    
    def setUltAplicacion(self, ultAplicacion):
        self.__ultAplicacion = ultAplicacion