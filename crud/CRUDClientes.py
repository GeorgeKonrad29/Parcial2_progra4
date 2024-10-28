
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from model.clientes import Clientes
from model.factura import Factura

class CRUDClientes():
    @staticmethod
    def create_cliente():
        cliente = Clientes("Cliente1", "123456789")
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
        return None
    
    @staticmethod
    def obtener_facturas_cliente(cliente):
        return cliente.getFacturas