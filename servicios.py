def crear_producto_servicio(datos, tipo, categoria):
    datos = dict(datos)
    nuevo={}
    for i in datos[tipo][categoria][0]:
        if i == "anios_garantia" or i == "precio" or i == "dias_vigencia":
            try:
                nuevo[i]=int(input(i.title()+": "))
            except Exception:
                print("¡Valor ingresado no válido!")
                print("Se debe actualizar luego con la opción (3) Actualizar producto / servicio")
                nuevo[i] = 0
        else:
            nuevo[i]=input(i.title()+": ")
    
    datos[tipo][categoria].append(nuevo)
    print("Registro realizado con éxito!")
    return datos

def lista_productos_servicios(datos, tipo, categoria):
    datos = dict(datos)
    if tipo == "productos":
        print("----------------------------------------------------------------")
        print("Lista de productos:")
    elif tipo == "servicios":
        print("----------------------------------------------------------------")
        print("Lista de servicios:")
    for i in range(len(datos[tipo][categoria])):
        print(datos[tipo][categoria][i]["nombre"])
    print("----------------------------------------------------------------")

def mostrar_producto_servicio(datos, tipo, categoria):
    datos = dict(datos)
    lista_productos_servicios(datos, tipo, categoria)
    seleccion = input("Escriba el nombre para mostrar la información completa: ")
    for i in range(len(datos[tipo][categoria])):
        if datos[tipo][categoria][i]["nombre"] == seleccion:
            print("----------------------------------------------------------------")
            print("Información completa:")
            for llave, valor in datos[tipo][categoria][i].items():
                print(llave.title()," : ",valor)
            return(datos)
    print("Producto / Servicio no encontrado")

def actualizar_producto_servicio(datos, tipo, categoria):
    datos = dict(datos)
    lista_productos_servicios(datos, tipo, categoria)
    seleccion = input("Escriba el nombre para seleccionar y actualizar: ")
    for i in range(len(datos[tipo][categoria])):
        if datos[tipo][categoria][i]["nombre"] == seleccion:
            print("----------------------------------------------------------------")
            print("Actualizar la siguiente información:")
            print("")
            for j in datos[tipo][categoria][i]:
                if j == "anios_garantia" or j == "precio" or j == "dias_vigencia":
                    try:
                        datos[tipo][categoria][i][j]=int(input(j.title()+": "))
                    except Exception:
                        print("¡Valor ingresado no válido!")
                        print("Se debe actualizar luego con la opción (3) Actualizar producto / servicio")
                        datos[tipo][categoria][i][j] = 0
                else:
                    datos[tipo][categoria][i][j]=input(j.title()+": ")
            print("Actualización realizada con éxito!")
            return datos
    print("Producto / Servicio no encontrado")
    return(datos)

def eliminar_producto_servicio(datos, tipo, categoria):
    datos = dict(datos)
    lista_productos_servicios(datos, tipo, categoria)
    seleccion = input("Escriba el nombre para seleccionar y eliminar: ")
    for i in range(len(datos[tipo][categoria])):
        if datos[tipo][categoria][i]["nombre"] == seleccion:
            datos[tipo][categoria].pop(i)
            print("Eliminado con éxito")
            return datos
    print("Producto / Servicio no encontrado")
    return(datos)