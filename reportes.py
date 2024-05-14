def cantidad_productos_servicios(datos):
    datos = dict(datos)
    print("----------------------------------------------------------------")
    cont = 0
    for i in datos["productos"]:
        for j in range(len(datos["productos"][i])):
            cont += 1
    print("CANTIDAD DE PRODUCTOS: ",cont)
    print("")
    print("----------------------------------------------------------------")
    cont = 0
    for i in datos["servicios"]:
        for j in range(len(datos["servicios"][i])):
            cont += 1
    print("CANTIDAD DE SERVICIOS: ",cont)

def mas_populares(datos):
    datos = dict(datos)
    dato_mayor = 0
    mayor = ""
    print("----------------------------------------------------------------")
    for i in datos["productos"]:
        for j in range(len(datos["productos"][i])):
            if datos["productos"][i][j]["vendidos"] > dato_mayor:
                dato_mayor = datos["productos"][i][j]["vendidos"]
                mayor = datos["productos"][i][j]["nombre"]
    print("PRODUCTO MÁS POPULAR: ",mayor)
    dato_mayor = 0
    mayor = ""
    print("----------------------------------------------------------------")
    for i in datos["servicios"]:
        for j in range(len(datos["servicios"][i])):
            if datos["servicios"][i][j]["vendidos"] > dato_mayor:
                dato_mayor = datos["servicios"][i][j]["vendidos"]
                mayor = datos["servicios"][i][j]["nombre"]
    print("SERVICIO MÁS POPULAR: ",mayor)

def usuarios_por_producto_servicio(datos):
    datos =dict(datos)
    print("----------------------------------------------------------------")
    print("LISTA DE PRODUCTOS:")
    for i in datos["productos"]:
        print("")
        print(i.upper())
        print("")
        for j in range(len(datos["productos"][i])):
            print(datos["productos"][i][j]["nombre"])
            print(datos["productos"][i][j]["clientes"])
    print("----------------------------------------------------------------")
    print("LISTA DE SERVICIOS:")
    for i in datos["servicios"]:
        print("")
        print(i.upper())
        print("")
        for j in range(len(datos["servicios"][i])):
            print(datos["servicios"][i][j]["nombre"])
            print(datos["servicios"][i][j]["clientes"])