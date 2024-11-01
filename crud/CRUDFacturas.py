import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.factura import Factura

class CrudFactura():
    @staticmethod
    def create_factura():
        factura = Factura("12/12/2024")
        return factura
    
    @staticmethod
    def create_lista_facturas():
        facturas = []
        factura = Factura("12/12/2024")
        facturas.append(factura)
        factura = Factura("12/12/2025")
        facturas.append(factura)
        factura = Factura("12/12/2026")
        facturas.append(factura)
        return facturas
    @staticmethod
    def listarFacturasCliente(listaFacturas):
        
        for factura in listaFacturas:
            print(factura.getFecha)
            productos=factura.getProductos
            for producto in productos:
                print(producto.getNombre,producto.getPrecio)

    @staticmethod
    def venderProducto(factura,producto):
        factura.addProducto(producto)
        return factura