import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crud.CRUDClientes import CrudClientes

class controlerVenta():
    def venderProducto(self,producto,cliente):
        cliente = CrudClientes.vender_producto(producto,cliente)
        return cliente