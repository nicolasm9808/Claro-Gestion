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
        usuario["edad"] = 999
    try:
        usuario["estrato"] = int(input("Ingrese el estrato económico: "))
    except Exception:
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