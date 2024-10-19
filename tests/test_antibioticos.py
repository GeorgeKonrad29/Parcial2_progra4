import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.antibioticos import Antibioticos

import unittest

class TestAntibioticos(unittest.TestCase):

    def setUp(self):
        self.antibiotico = Antibioticos("antibiotico1", 3000, 20, "perro")
    
    def test_getNombre(self):
        self.assertEqual(self.antibiotico.getNombre, "antibiotico1")
    
    def test_getPrecio(self):
        self.assertEqual(self.antibiotico.getPrecio, 3000.0)
    
    def test_getDosis(self):
        self.assertEqual(self.antibiotico.getDosis, 20)
    def test_getEspecie(self):
        self.assertEqual(self.antibiotico.getEspecie, "perro")

    def test_setNombre(self):
        self.antibiotico.setNombre("antibiotico2")
        self.assertEqual(self.antibiotico.getNombre, "antibiotico2")
    
    def test_setPrecio(self):
        self.antibiotico.setPrecio(4000)
        self.assertEqual(self.antibiotico.getPrecio, 4000.0)
    
    def test_setDosis(self):
        self.antibiotico.setDosis(30)
        self.assertEqual(self.antibiotico.getDosis, 30)
        
    def test_setEspecie(self):
        self.antibiotico.setEspecie("gato")
        self.assertEqual(self.antibiotico.getEspecie, "gato")
    
if __name__ == '__main__':
    unittest.main()