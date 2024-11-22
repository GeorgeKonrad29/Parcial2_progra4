import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crud.CRUDAntibioticos import CrudAntibioticos
from crud.CRUDControlPlagas import CrudControlPlagas
from crud.CRUDFertilizantes import CrudFertilizantes

def crear_inventario():
    inventario = CrudAntibioticos.create_lista_antibioticos()
    inventario += CrudFertilizantes.create_lista_fertilizantes()
    inventario += CrudControlPlagas.create_lista_controlPlagas()
    
    return inventario

if __name__ == "__main__":
    inventario = crear_inventario()
    print(inventario)