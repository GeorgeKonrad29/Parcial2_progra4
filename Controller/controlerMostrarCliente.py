import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.clientes import Clientes
from crud.CRUDClientes import CrudClientes

class controlerMostrarCliente():
    def buscarPorCedula(self,clientes,cedula):
        cliente = CrudClientes.buscar_por_cedula(clientes,cedula)
        return cliente
    def obtenerFacturasCliente(self,cliente):
        facturas = CrudClientes.obtener_facturas_cliente(cliente)
        return facturas