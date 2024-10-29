import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
import model.clientes  as cl
import ui.ui as ui
import crud.CRUDClientes as crudC
import crud.CRUDFacturas as crudF
import crud.CRUDControlPlagas as crudP
import crud.CRUDFertilizantes as crudFer
import crud.CRUDAntibioticos as crudA

def main():
    cedular=0
    cedula=ui.buscar()
    stockAntibioticos = crudA.create_lista_antibioticos()
    stockFertilizantes = crudFer.create_lista_fertilizantes()
    stockControlPlagas = crudP.create_lista_control_plagas()
    nuevoCliente = crudC.create_cliente()
    nuevaFactura = crudF.create_factura()
    
    nuevoCliente.add_factura(nuevaFactura)
    clientes = crudC.create_lista_clientes()
    cliente = crudC.buscar_por_cedula(clientes, cedula)