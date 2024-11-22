import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5 import QtWidgets
from Diseños import interfazPrincipal
from Diseños import informacionCliente

class ControllerPrincipal:
    def __init__(self):
        self.inventarios = []
        self.clientes = []

    def set_inventarios(self, inventarios):
        self.inventarios = inventarios

    def set_clientes(self, clientes):
        self.clientes = clientes

    def show_main_window(self):
        self.main_window = MainApp(self)
        self.main_window.show()

    def show_informacion_cliente(self):
        self.informacion_cliente_window = InformacionClienteApp(self)
        self.informacion_cliente_window.show()

class MainApp(QtWidgets.QMainWindow, interfazPrincipal.Ui_MainWindow):
    def __init__(self, controller, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.controller = controller

    def realizar_compra(self):
        print("Realizar compra")
        self.controller.show_informacion_cliente()

    def registrar_cliente(self):
        print("Registrar cliente")
        self.controller.show_informacion_cliente()

    def buscar_cliente(self):
        print("Buscar cliente por numero de cedula")
        self.controller.show_informacion_cliente()

    def salir(self):
        print("Salir")
        QtWidgets.QApplication.quit()

class InformacionClienteApp(QtWidgets.QMainWindow, interfazPrincipal.Ui_MainWindow):
    def __init__(self, controller, *args, **kwargs):
        super(InformacionClienteApp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.controller = controller
        # Aquí puedes usar self.controller.inventarios y self.controller.clientes
        print("Inventarios:", self.controller.inventarios)
        print("Clientes:", self.controller.clientes)