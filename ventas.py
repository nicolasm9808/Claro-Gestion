from servicios import lista_productos_servicios
from datetime import datetime

def mostrar_catalogo(datos):
    datos =dict(datos)
    print("----------------------------------------------------------------")
    print("LISTA DE PRODUCTOS:")
    for i in datos["productos"]:
        print("")
        print(i.upper())
        print("")
        for j in range(len(datos["productos"][i])):
            print(datos["productos"][i][j]["nombre"])
    print("----------------------------------------------------------------")
    print("LISTA DE SERVICIOS:")
    for i in datos["servicios"]:
        print("")
        print(i.upper())
        print("")
        for j in range(len(datos["servicios"][i])):
            print(datos["servicios"][i][j]["nombre"])

def registrar_venta(datos, tipo, categoria, ventas, usuarios):
    datos = dict(datos)
    ventas = dict(ventas)
    usuarios = dict(usuarios)
    lista_productos_servicios(datos, tipo, categoria)
    seleccion = input("Escriba el nombre para registrar la venta: ")
    for i in range(len(datos[tipo][categoria])):
        if datos[tipo][categoria][i]["nombre"] == seleccion:
            nuevo={}
            tamaño = len(ventas[tipo])
            nuevo["consecutivo"] = ventas[tipo][tamaño-1]["consecutivo"] + 1
            nuevo["fecha"] = str(datetime.today().date())
            nuevo["producto"] = seleccion
            es_cliente = False
            documento = input("Ingrese el documento del cliente: ")
            for i in range(len(usuarios["usuarios"])):
                if usuarios["usuarios"][i]["documento"] == documento:
                    nuevo["cliente"] = documento
                    es_cliente = True
                    x = i
            if not es_cliente:
                print("No existe este cliente")
                print("Debe crear el cliente antes de registrar la compra")
                return()
            try:
                nuevo["cantidad"] = int(input("Ingrese la cantidad de "+ seleccion+ " que se vendió: "))
            except Exception:
                print("¡Valor ingresado no válido!")
                print("Se registra cantidad 1")
                nuevo["cantidad"] = 1
            nuevo["valor"] = datos[tipo][categoria][x]["precio"] * nuevo["cantidad"]
            
            ventas[tipo].append(nuevo)
            print("Venta registrada con éxito!")
            for j in range(nuevo["cantidad"]):
                usuarios["usuarios"][i][tipo].append(seleccion)
            return(ventas,usuarios)

    print("Producto / Servicio no encontrado")
    return

def mostrar_ventas(ventas):
    ventas =dict(ventas)
    print("----------------------------------------------------------------")
    print("PRODUCTOS VENDIDOS:")
    print("")
    for i in range(len(ventas["productos"])):
        for llave, valor in ventas["productos"][i].items():
            print(llave.title()," : ",valor)
        print("")
    print("----------------------------------------------------------------")
    print("SERVICIOS VENDIDOS:")
    print("")
    for i in range(len(ventas["servicios"])):
        for llave, valor in ventas["servicios"][i].items():
            print(llave.title()," : ",valor)
        print("")
