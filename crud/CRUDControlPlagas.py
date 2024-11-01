import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from model.controlesPlagas import ControlesPlagas

class CrudControlPlagas():
    @staticmethod
    def create_controlPlagas():
        controlPlagas = ControlesPlagas("1234", "ControlPlagas1", 100.0, 10,15)
        return controlPlagas
    
    @staticmethod
    def create_lista_controlPlagas():
        listaControlPlagas = []
        controlPlagas = ControlesPlagas("1234", "ControlPlagas1", 100.0, 10,15)
        listaControlPlagas.append(controlPlagas)
        controlPlagas = ControlesPlagas("1235", "ControlPlagas2", 200.0, 20,25)
        listaControlPlagas.append(controlPlagas)
        controlPlagas = ControlesPlagas("1236", "ControlPlagas3", 300.0, 30,35)
        listaControlPlagas.append(controlPlagas)
        
        return listaControlPlagas
