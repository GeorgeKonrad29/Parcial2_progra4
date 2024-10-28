
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from model.antibioticos import Antibioticos
class CrudAntibioticos():

    @staticmethod
    def create_antibiotico():
        antibiotico = Antibioticos("Antibiotico1", 100.0, 10, "Perro")
        return antibiotico
    
    @staticmethod
    def create_lista_antibioticos():
        antibioticos = []
        antibiotico = Antibioticos("Antibiotico1", 100.0, 10, "Perro")
        antibioticos.append(antibiotico)
        antibiotico = Antibioticos("Antibiotico2", 200.0, 20, "Gato")
        antibioticos.append(antibiotico)
        antibiotico = Antibioticos("Antibiotico3", 300.0, 30, "Conejo")
        antibioticos.append(antibiotico)
        return antibioticos