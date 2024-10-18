import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.controlesPlagas import *
import unittest

class TestControlesPlagas(unittest.TestCase):

    def setUp(self):
        self.controlPlagas = ControlesPlagas("4321", "controlPlagas1", 3000, 20, 10)

    def test_getRegistroICA(self):
        self.assertEqual(self.controlPlagas.getRegistroICA, "4321")
    
    def test_getNombre(self):
        self.assertEqual(self.controlPlagas.getNombre, "controlPlagas1")
    
    def test_getPrecio(self):
        self.assertEqual(self.controlPlagas.getPrecio, 3000.0)
    
    def test_getFrecuencia(self):
        self.assertEqual(self.controlPlagas.getFrecAplicacion, 20)
    
    def test_getPeriodoCarencia(self):
        self.assertEqual(self.controlPlagas.getPeriodoCarencia, 10)

    def test_setRegistroICA(self):
        self.controlPlagas.setRegistroICA("1234")
        self.assertEqual(self.controlPlagas.getRegistroICA, "1234")
    
    def test_setNombre(self):
        self.controlPlagas.setNombre("controlPlagas2")
        self.assertEqual(self.controlPlagas.getNombre, "controlPlagas2")
    
    def test_setPrecio(self):
        self.controlPlagas.setPrecio(4000)
        self.assertEqual(self.controlPlagas.getPrecio, 4000.0)
    
    def test_setFrecuencia(self):
        self.controlPlagas.setFrecAplicacion(30)
        self.assertEqual(self.controlPlagas.getFrecAplicacion, 30)
    
    def test_setPeriodoCarencia(self):
        self.controlPlagas.setPeriodoCarencia(15)
        self.assertEqual(self.controlPlagas.getPeriodoCarencia, 15)
    

if __name__ == '__main__':
    unittest.main()
