import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.fertilizantes import *
from model.antibioticos import *
from model.controlesPlagas import *
from model.factura import *

import unittest

class TestFactura(unittest.TestCase):

    def setUp(self):
        productos = [Antibioticos("antibiotico1", 1000, 10, "perro"), Fertilizantes("1234", "fertilizante1", 1200, 2, "01/10/2023"), ControlesPlagas("4321", "controlPlagas1", 3000, 20, 10)]
        self.factura = Factura("01/10/2023", productos)
    
    def test_get_fecha(self):
        self.assertEqual(self.factura.getFecha, "01/10/2023")
    
    def test_get_precio_total(self):
        self.assertEqual(self.factura.getPrecioTotal, 5200)
    
    def test_get_productos(self):
        productos = self.factura.getProductos
        self.assertEqual(productos[0].getNombre, "antibiotico1")
        self.assertEqual(productos[1].getNombre, "fertilizante1")
        self.assertEqual(productos[2].getNombre, "controlPlagas1")
    
    def test_get_todos_los_precios(self):
        precios = self.factura.getTodosLosPrecios()
        self.assertEqual(precios, [1000.0, 1200.0, 3000.0])
    
    def test_add_producto(self):
        self.factura.addProducto(Antibioticos("antibiotico2", 2000, 20, "gato"))
        self.assertEqual(self.factura.getPrecioTotal, 7200)
    
    def test_set_fecha(self):
        self.factura.setFecha("02/10/2023")
        self.assertEqual(self.factura.getFecha, "02/10/2023")
    

if __name__ == '__main__':
    unittest.main()

