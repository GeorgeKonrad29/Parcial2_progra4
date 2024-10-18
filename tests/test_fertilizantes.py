import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.fertilizantes import *
import unittest


class TestFertilizantes(unittest.TestCase):
    def setUp(self):
        self.fertilizante = Fertilizantes(12345, "fertilizante1", 1200, 2, "01/10/2023")
    
    def test_get_registro_ica(self):
        self.assertEqual(self.fertilizante.getRegistroICA, 12345)

    def test_get_nombre(self):
        self.assertEqual(self.fertilizante.getNombre, "fertilizante1")

    def test_get_precio(self):
        self.assertEqual(self.fertilizante.getPrecio, 1200)

    def test_get_frec_aplicacion(self):
        self.assertEqual(self.fertilizante.getFrecAplicacion, 2)

    def test_get_ult_aplicacion(self):
        self.assertEqual(self.fertilizante.getUltAplicacion, "01/10/2023")

    def test_set_registro_ica(self):
        self.fertilizante.setRegistroICA(12346)
        self.assertEqual(self.fertilizante.getRegistroICA, 12346)

    def test_set_nombre(self):
        self.fertilizante.setNombre("fertilizante2")
        self.assertEqual(self.fertilizante.getNombre, "fertilizante2")

    def test_set_precio(self):
        self.fertilizante.setPrecio(1300)
        self.assertEqual(self.fertilizante.getPrecio, 1300)

    def test_set_frec_aplicacion(self):
        self.fertilizante.setFrecAplicacion(3)
        self.assertEqual(self.fertilizante.getFrecAplicacion, 3)
    
    def test_set_ult_aplicacion(self):
        self.fertilizante.setUltAplicacion("02/10/2023")
        self.assertEqual(self.fertilizante.getUltAplicacion, "02/10/2023")
    

if __name__ == '__main__':
    unittest.main()