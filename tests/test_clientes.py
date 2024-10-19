import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.clientes import *
from model.factura import *
import unittest

class TestClientes(unittest.TestCase):

    def setUp(self):
        
        self.cliente = Clientes("1234", "cliente1")

    def test_getNombre(self):
        self.assertEqual(self.cliente.getNombre, "1234")
    
    def test_getCedula(self):
        self.assertEqual(self.cliente.getCedula, "cliente1")
    
    def test_addFactura(self):
        facturas = []
        for i in range(3):
            facturas.append(Factura("12/12/199"+str(i),[]))
        self.cliente.addFactura(facturas[0])
        self.cliente.addFactura(facturas[1])
        self.cliente.addFactura(facturas[2])
        self.assertEqual(self.cliente.getFacturas, facturas)
    
    def test_cantidadFacturas(self):
        facturas = []
        for i in range(3):
            facturas.append(Factura("12/12/199"+str(i),[]))
        self.cliente.addFactura(facturas[0])
        self.cliente.addFactura(facturas[1])
        self.cliente.addFactura(facturas[2])
        self.assertEqual(self.cliente.cantidadFacturas(), 3)

if __name__ == '__main__':
    unittest.main()