import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5 import QtWidgets
from Diseños.interfazPrincipal import Ui_MainWindow
from Diseños.interfazRegistroCliente import Ui_MainWindow as RegistroClienteWindow
from model.clientes import *

class RegistroCliente(QtWidgets.QMainWindow, RegistroClienteWindow):
    
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.guardar_cliente)
        self.main_window = main_window  

    def guardar_cliente(self):
        nombre = self.lineEdit.text()
        cedula = self.lineEdit_2.text()
        if nombre and cedula:
            nuevo_cliente = Clientes(nombre, cedula)
            self.main_window.agregar_cliente(nuevo_cliente)
            QtWidgets.QMessageBox.information(self, "Guardado", f"Cliente {nombre} guardado correctamente")
            self.close()  
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese todos los campos")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toolButton_2.clicked.connect(self.registrar_cliente)
        self.clientes = []  

    def registrar_cliente(self):
        self.registro_cliente_window = RegistroCliente(self)  
        self.registro_cliente_window.show()  

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)  
        print(f"Cliente registrado: {cliente.getNombre}, Cédula: {cliente.getCedula}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
