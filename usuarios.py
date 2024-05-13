def crear_ususario(datos):
    datos = dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["telefono"]=input("Ingrese el número de teléfono: ")
    usuario["correo"]=input("Ingrese el correo electrónico: ")
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        print("Valor ingresado no válido, se debe actualizar luego con la opción (3)Actualizar ususario")
        usuario["edad"] = 999
    try:
        usuario["estrato"] = int(input("Ingrese el estrato económico: "))
    except Exception:
        print("Valor ingresado no válido, se debe actualizar luego con la opción (3)Actualizar ususario")
        usuario["estrato"] = 999
    usuario["direccion"]=input("Ingrese la dirección: ")
    usuario["departamento"]=input("Ingrese el departamento: ")
    usuario["municipio"]=input("Ingrese el municipio: ")
    usuario["categoria"]="Cliente nuevo"
    usuario["productos"]=[]
    usuario["servicios"]=[]
    usuario["historial"]=[]
    
    datos["usuarios"].append(usuario)
    print("Usuario registrado con éxito!")
    return datos

def mostrar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            print(datos["usuarios"][i])
            return(datos)
    print("Usuario no encontrado")

def actualizar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"][i]["nombre"]=input("Ingrese el nombre: ")
            datos["usuarios"][i]["documento"]=input("Ingrese el documento: ")
            datos["usuarios"][i]["telefono"]=input("Ingrese el número de teléfono: ")
            datos["usuarios"][i]["correo"]=input("Ingrese el correo electrónico: ")
            try:
                datos["usuarios"][i]["edad"] = int(input("Ingrese la edad: "))
            except Exception:
                print("Valor ingresado no válido, se debe actualizar luego con la opción (3)Actualizar ususario")
                datos["usuarios"][i]["edad"] = 999
            try:
                datos["usuarios"][i]["estrato"] = int(input("Ingrese el estrato económico: "))
            except Exception:
                print("Valor ingresado no válido, se debe actualizar luego con la opción (3)Actualizar ususario")
                datos["usuarios"][i]["estrato"] = 999
            datos["usuarios"][i]["direccion"]=input("Ingrese la dirección: ")
            datos["usuarios"][i]["departamento"]=input("Ingrese el departamento: ")
            datos["usuarios"][i]["municipio"]=input("Ingrese el municipio: ")
            
    print("Usuario actualizado con éxito!")
    return datos

def eliminar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"].pop(i)
            print("Usuario eliminado!")
            return datos
    print("Participante no existe")
    return datos    

def registrar_pqrs(datos):
    datos = dict(datos)
    print("Sistema de Peticiones, Quejas, Reclamos y Sugerencias (PQRS)")
    print("")
    documento = input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            pqrs = input("Ingrese el PQRS del usuario: ")
            datos["usuarios"][i]["historial"].append(pqrs)
            print("PQRS registrado con éxito")
            return(datos)
    print("Usuario no encontrado")