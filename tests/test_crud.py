import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from model.clientes  import Clientes
import ui.ui as ui
from crud.CRUDClientes import CrudClientes
from crud.CRUDFacturas import CrudFactura
from crud.CRUDControlPlagas import CrudControlPlagas
from crud.CRUDFertilizantes import CrudFertilizantes
from crud.CRUDAntibioticos import CrudAntibioticos

class TestCrud(unittest.TestCase):
    def test_crud(self):
        print("test_crud")
        crudC = CrudClientes()
        crudF = CrudFactura()
        crudP = CrudControlPlagas()
        crudFer = CrudFertilizantes()
        crudA = CrudAntibioticos()
        clientes = []
        cedula=0
        cedula="1234"
        stockAntibioticos = crudA.create_lista_antibioticos()
        stockFertilizantes = crudFer.create_lista_fertilizantes()
        stockControlPlagas = crudP.create_lista_controlPlagas()
        nuevoCliente = crudC.create_cliente()
        nuevaFactura = crudF.create_factura()
        nuevaFactura = crudF.venderProducto(nuevaFactura, stockAntibioticos[0])
        nuevaFactura = crudF.venderProducto(nuevaFactura, stockFertilizantes[0])
        nuevaFactura = crudF.venderProducto(nuevaFactura, stockControlPlagas[0])
        
        nuevoCliente.addFactura(nuevaFactura)
        
        clientes = crudC.create_lista_clientes()
        clientes.append(nuevoCliente)
        cliente = crudC.buscar_por_cedula(clientes, cedula)
        facturas = crudC.obtener_facturas_cliente(cliente)
        crudF.listarFacturasCliente(facturas)

if __name__ == '__main__':
    unittest.main()