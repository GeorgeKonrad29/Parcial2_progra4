import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from model.productos_control import ProductosControl

class ControlesPlagas (ProductosControl):
    # Constructor de la clase
    def __init__(self,registroICA: str, nombre: str, precio: float, frecAplicacion: int,periodoCarencia: int):
        super().__init__(registroICA, nombre, precio, frecAplicacion)
        self.__periodoCarencia = periodoCarencia

        
    @property
    def getPeriodoCarencia(self):
        return self.__periodoCarencia
    
    def setPeriodoCarencia(self, periodoCarencia):
        self.__periodoCarencia = periodoCarencia
    