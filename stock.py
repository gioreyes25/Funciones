datos={}
from funci import stoca
while True:
    print("1. Agregar Producto")
    print("2. Ver Disponibilidad")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese nombre de el producto: ").title()
            cantidad=int(input("Ingrese cantidad: "))
            datos[producto]={"cantidad":cantidad}
        case 2:
            for n,i in datos.items():
                if i["cantidad"]<=0:
                    print(stoca(op,i))
                print(f"{n}\nCantidad: {i["cantidad"]}")