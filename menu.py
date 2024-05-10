def menu_principal():
    print("****************************************************************")
    print("MENÚ PRINCIPAL:")
    print("(Marque la opción correspondiente para desplegar las opciones)")
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
    print("(5) Registrar interacción de usuario con la empresa")
    print("(0) Regresar al Menú principal")
    print("----------------------------------------------------------------")

def menu_gestion_servicios():
    print("----------------------------------------------------------------")
    print("MENÚ GESTIÓN DE SERVICIOS:")
    print("(Marque la opción correspondiente)")
    print("")
    print("(1) Agregar nuevo servicio")
    print("(2) Mostrar información de algún servicio")
    print("(3) Actualizar servicio")
    print("(4) Eliminar servicio")
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