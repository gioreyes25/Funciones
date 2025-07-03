datos=[]
while True:
    print(datos)
    print("1. Agregar Producto")
    op=int(input("Ingrese una op: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de pan").title()
            precio=int(input("Ingrese precio de el prodyucto: "))
            info={"producto":nombre,"precio":precio}
            datos.append(info)
        case 2:
            for i in datos:
                print(f"Nombre: {i["producto"]}\nPrecio: {i["precio"]}")
                print()
            elegir=input("Ingrese producto que eliinara").title()
            if elegir ==i["producto"]:
                print("ja")
                del datos[elegir]