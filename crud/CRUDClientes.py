
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from model.clientes import Clientes
from model.factura import Factura

class CrudClientes():
    @staticmethod
    def create_cliente():
        cliente = Clientes("Cliente0", "1234")
        return cliente
    
    @staticmethod
    def create_lista_clientes():
        clientes = []
        cliente = Clientes("Cliente1", "123456789")
        clientes.append(cliente)
        cliente = Clientes("Cliente2", "987654321")
        clientes.append(cliente)
        cliente = Clientes("Cliente3", "456789123")
        clientes.append(cliente)
        return clientes
    
    @staticmethod
    def buscar_por_cedula(listaClientes, cedula):
        for cliente in listaClientes:
            if cliente.getCedula == cedula:
                return cliente
        return False
    
    @staticmethod
    def obtener_facturas_cliente(cliente):
        facturas= cliente.getFacturas
        return facturas
    
    @staticmethod
    def vender_producto(producto,cliente):
        factura = Factura()
        factura = factura.venderProducto(producto)
        cliente.addFactura(factura)
        return cliente