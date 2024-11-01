import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from model.factura import Factura

class Clientes():
    def __init__(self, nombre:str, cedula:str):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = []

    @property
    def getNombre(self):
        return self.__nombre
    @property   
    def getCedula(self):
        return self.__cedula
    
    def addFactura(self, factura):
        #hay que asegurarse que factura sea un objeto de la clase Factura
        if isinstance(factura, Factura):
            self.__facturas.append(factura)
    @property
    def getFacturas(self):
        return self.__facturas
      
    def cantidadFacturas(self):
        return len(self.__facturas)

    