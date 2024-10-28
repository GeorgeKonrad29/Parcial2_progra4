#necesito crear clases estructurales de todas las clases que tengo en el modelo
#para poder hacer el crud
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from model.fertilizantes import Fertilizantes

class CrudFertilizantes():
    @staticmethod
    def create_fertilizante():
        fertilizante = Fertilizantes("4321","fertilizante1", 100.0, 10, "11/12/2023")
        return fertilizante
    @staticmethod
    def create_lista_fertilizantes():
        fertilizantes = []
        fertilizante = Fertilizantes("4321","fertilizante1", 100.0, 10, "11/12/2023")
        fertilizantes.append(fertilizante)
        fertilizante = Fertilizantes("4322","fertilizante2", 200.0, 20, "11/12/2024")
        fertilizantes.append(fertilizante)
        fertilizante = Fertilizantes("4323","fertilizante3", 300.0, 30, "11/12/2025")
        fertilizantes.append(fertilizante)
        return fertilizantes
