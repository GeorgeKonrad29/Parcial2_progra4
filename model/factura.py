import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.antibioticos import Antibioticos
from model.fertilizantes import Fertilizantes
from model.controlesPlagas import ControlesPlagas

class Factura():
    def __init__(self, fecha: str):
        self.__fecha = fecha
        self.__precioTotal = 0
        self.__productos = []

    def __init__(self, fecha: str, productos: list):
        self.__fecha = fecha
        self.__productos = productos

    @property
    def getFecha(self):
        return self.__fecha
    
    @property
    def getPrecioTotal(self):
        precioTotal = 0
        for producto in self.__productos:
            precioTotal += producto.getPrecio
        return precioTotal
    
    @property
    def getProductos(self):
        return self.__productos
    
    def getTodosLosPrecios(self):
        resultado = []
        for producto in self.__productos:
            resultado.append(producto.getPrecio)
        return resultado

    def addProducto(self, producto):
        #hay que asegurarse que producto sea un objeto de la clase ProductosControl
        if isinstance(producto, Fertilizantes) or isinstance(producto, ControlesPlagas) or isinstance(producto, Antibioticos):
            self.__productos.append(producto)

    def setFecha(self, fecha):
        self.__fecha = fecha