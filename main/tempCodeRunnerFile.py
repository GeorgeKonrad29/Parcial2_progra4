crudC = CrudClientes()
    crudF = CrudFactura()
    crudP = CrudControlPlagas()
    crudFer = CrudFertilizantes()
    crudA = CrudAntibioticos()
    clientes = []
    cedular=0
    cedula=ui.buscar()
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
