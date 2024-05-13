def menu_principal():
    print("****************************************************************")
    print("MENÚ PRINCIPAL:")
    print("(Marque la opción correspondiente para desplegar el siguiente menú)")
    print("")
    print("(1) GESTIÓN DE USUARIOS")
    print("(2) GESTIÓN DE SERVICIOS")
    print("(3) VENTAS")
    print("(4) INFORMES")
    print("(0) SALIR")
    print("****************************************************************")

def menu_gestion_usuarios():
    print("----------------------------------------------------------------")
    print("MENÚ GESTIÓN DE USUARIOS:")
    print("(Marque la opción correspondiente)")
    print("")
    print("(1) Crear usuario")
    print("(2) Mostrar información de usuario")
    print("(3) Actualizar usuario")
    print("(4) Eliminar usuario")
    print("(5) Registrar PQRS")
    print("(0) Regresar al Menú principal")
    print("----------------------------------------------------------------")

def menu_gestion_servicios():
    print("----------------------------------------------------------------")
    print("MENÚ GESTIÓN DE SERVICIOS:")
    print("(Marque la opción correspondiente)")
    print("")
    print("(1) Agregar nuevo producto / servicio")
    print("(2) Mostrar información de algún producto / servicio")
    print("(3) Actualizar producto / servicio")
    print("(4) Eliminar producto / servicio")
    print("(0) Regresar al Menú principal")
    print("----------------------------------------------------------------")

def menu_ventas():
    print("----------------------------------------------------------------")
    print("MENÚ DE VENTAS:")
    print("(Marque la opción correspondiente)")
    print("")
    print("(1) Mostrar catálogo")
    print("(2) Registrar venta de producto")
    print("(3) Registrar venta de servicio")
    print("(4) Mostrar ventas")
    print("(0) Regresar al Menú principal")
    print("----------------------------------------------------------------")

def menu_reportes():
    print("----------------------------------------------------------------")
    print("MENÚ DE REPORTES:")
    print("(Marque la opción correspondiente)")
    print("")
    print("(1) Generar informe de cantidad de productos y servicios")
    print("(2) Generar informe de servicios y productos más populares")
    print("(3) Generar informe de usuarios que adquirieron cada producto o servicio")
    print("(0) Regresar al Menú principal")
    print("----------------------------------------------------------------")

def pedir_opcion():
    try:
        opc = int(input("Ingrese su opción: "))
        return opc
    except Exception:
        print("Valor inválido")
        return -1

def seleccionar_tipo():
    print("----------------------------------------------------------------")
    print("Seleccione la categoría")
    print("(1) Producto")
    print("(2) Servicio")
    print("(0) para regresar al Menú anterior")
    opc = pedir_opcion()
    if opc == 0:
        return 0
    elif opc == 1:
        return "productos"
    elif opc == 2:
        return "servicios"
    
    print("Opción no válida")
    return -1

def seleccionar_categoria(tipo):
    if tipo == "productos":
        print("----------------------------------------------------------------")
        print("¿A cuál categoría pertenece el producto?")
        print("(1) Celulares")
        print("(2) Computadores")
        print("(3) Audifonos")
        print("(0) Regresar al Menú anterior")
        opc = pedir_opcion()
        if opc == 0:
            return 0
        elif opc == 1:
            return "celulares"
        elif opc == 2:
            return "computadores"
        elif opc == 3:
            return "audifonos"

    elif tipo == "servicios":
        print("----------------------------------------------------------------")
        print("¿A cuál categoría pertenece el servicio?")
        print("(1) Planes prepago móvil")
        print("(2) Planes postpago móvil")
        print("(3) Planes de internet hogar")
        print("(0) Regresar al Menú anterior")
        opc = pedir_opcion()
        if opc == 0:
            return 0
        elif opc == 1:
            return "prepago_movil"
        elif opc == 2:
            return "postpago_movil"
        elif opc == 3:
            return "internet_hogar"
    
    print("Opción no válida")
    return -1