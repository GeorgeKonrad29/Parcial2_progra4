import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5 import QtWidgets
from Diseños.interfazPrincipal import Ui_MainWindow
from Diseños.interfazRegistroCliente import Ui_MainWindow as RegistroClienteWindow
from Diseños.BuscarCliente import Ui_Form as BuscarClienteWindow
from Diseños.informacionCliente import Ui_Form as InformacionClienteWindow
from controller.controlerMostrarCliente import controlerMostrarCliente
from model.factura import *
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
class InformacionCliente(QtWidgets.QMainWindow, InformacionClienteWindow):
    def __init__(self, cliente):
        super().__init__()
        self.setupUi(self)
        self.montar_informacion(cliente)
    def montar_informacion(self, cliente):
        self.label_2.setText("Informacion del cliente")
        self.label_2.setText(f"Nombre: {cliente.getNombre}\nCedula: {cliente.getCedula}" )
        facturas = controlerMostrarCliente().obtenerFacturasCliente(cliente)
        for factura in facturas:
            self.label_2.setText(f"Fecha: {factura.getFecha}\n")
            for producto in factura.getProductos:
                self.label_2.setText(f"{producto.getNombre} - ${producto.getPrecio}\n")
            self.label_2.setText("\n")
        self.show()
class BuscarCliente(QtWidgets.QMainWindow, BuscarClienteWindow):
    def __init__(self, main_window):

        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buscar_cliente)
        self.main_window = main_window
    def buscar_cliente(self):
        cedula = self.lineEdit.text()
        if cedula:
            cliente = controlerMostrarCliente().buscarPorCedula(self.main_window.clientes, cedula)
            if cliente:
                self.informacion_cliente_window = InformacionCliente(cliente)
                self.informacion_cliente_window.show()
            else: 
                QtWidgets.QMessageBox.warning(self, "Error", "Cliente no encontrado")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese la cédula")
            
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, inventario: list = [], clientes: list = []):
        super().__init__()
        self.inventario = inventario
        self.clientes = clientes
        self.setupUi(self)
        self.toolButton.clicked.connect(self.realizar_compra)
        self.toolButton_2.clicked.connect(self.registrar_cliente)
        self.toolButton_3.clicked.connect(self.buscar_cliente)

    def registrar_cliente(self):
        self.registro_cliente_window = RegistroCliente(self)  
        self.registro_cliente_window.show()  

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)  
        print(f"Cliente registrado: {cliente.getNombre}, Cédula: {cliente.getCedula}")

    def buscar_cliente(self):
        self.buscar_cliente_window = BuscarCliente(self)
        self.buscar_cliente_window.show()
    
    def realizar_compra(self):
        print("Realizar compra")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
