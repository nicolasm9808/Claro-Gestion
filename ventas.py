from servicios import lista_productos_servicios
from traceback import format_exc
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
            for j in range(len(usuarios["usuarios"])):
                if usuarios["usuarios"][j]["documento"] == documento:
                    nuevo["cliente"] = documento
                    es_cliente = True
                    x = j
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
                exc = format_exc()
                hora = str(datetime.now())
                with open("excepciones.txt","a") as e:
                    e.write(hora+"\n "+ exc+"\n ")
            if usuarios["usuarios"][x]["estrato"] < 3:
                print("El cliente tiene un descuento del 20%")
                valor = datos[tipo][categoria][i]["precio"] * 0.8
            else:
                valor = datos[tipo][categoria][i]["precio"]
            nuevo["valor"] = valor * nuevo["cantidad"]
            
            ventas[tipo].append(nuevo)
            print("Venta registrada con éxito!")
            #Incluir la venta en usuarios
            for k in range(nuevo["cantidad"]):
                usuarios["usuarios"][x][tipo].append(seleccion)
            #Incluir la venta en el catálogo
            antiguo = False
            datos[tipo][categoria][i]["vendidos"] += nuevo["cantidad"]
            for y in range(len(datos[tipo][categoria][i]["clientes"])):
                if datos[tipo][categoria][i]["clientes"][y]["documento"] == documento:
                    datos[tipo][categoria][i]["clientes"][y]["cantidad"] += nuevo["cantidad"]
                    antiguo = True
            if antiguo == False:
                venta = {}
                venta["documento"] = documento
                venta["nombre"] = usuarios["usuarios"][x]["nombre"]
                venta["cantidad"] = nuevo["cantidad"]
                datos[tipo][categoria][i]["clientes"].append(venta)
            return(ventas,usuarios,datos)

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
