#Imports
from menu import *

while True:
    menu_principal()
    menu = pedir_opcion()
    if menu == 1:
        menu_gestion_usuarios()
        opc = pedir_opcion()
    elif menu == 2:
        menu_gestion_servicios()
        opc = pedir_opcion()
    elif menu == 3:
        menu_ventas()
        opc = pedir_opcion()
    elif menu == 4:
        menu_reportes()
        opc = pedir_opcion()
    elif menu == 0:
        print("SALIR")
        print("****************************************************************")
        break
    else:
        print("No existe esta opción")