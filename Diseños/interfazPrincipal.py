from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 451, 81))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(110, 240, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(110, 150, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(110, 320, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(110, 410, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setObjectName("toolButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.toolButton.clicked.connect(self.realizar_compra)
        self.toolButton_2.clicked.connect(self.registrar_cliente)
        self.toolButton_3.clicked.connect(self.buscar_cliente)
        self.toolButton_4.clicked.connect(self.salir)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Facturacion Agricola"))
        self.toolButton.setText(_translate("MainWindow", "Realizar compra"))
        self.toolButton_2.setText(_translate("MainWindow", "Registrar Cliente"))
        self.toolButton_3.setText(_translate("MainWindow", "Buscar Cliente por numero de cedula"))
        self.toolButton_4.setText(_translate("MainWindow", "Salir"))
    def realizar_compra(self):
        print("Realizar compra")

    def registrar_cliente(self):
        print("Registrar cliente")

    def buscar_cliente(self):
        print("Buscar cliente por numero de cedula")

    def salir(self):
        print("Salir")
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
