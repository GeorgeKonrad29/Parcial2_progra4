import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.clientes import Clientes
from crud.CRUDClientes import CrudClientes
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.controlerMostrarCliente import controlerMostrarCliente


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(501, 472)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cliente"))
        self.label_2.setText(_translate("Form", "Informacion del cliente"))
    
    def montar_informacion(self, cliente):
        self.label_2.setText("Informacion del cliente")
        self.label_2.setText(f"Nombre: {cliente.getNombre}\nCedula: {cliente.getCedula}" )


if __name__ == "__main__":
    import sys
    cliente= CrudClientes.create_cliente()
    print(cliente.getNombre)
    clientes=[cliente]

