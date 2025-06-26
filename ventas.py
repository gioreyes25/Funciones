datos={
    "Panaderia":{
        "Pan":22,
        "Galleta":13,
    },
    "Carniceria":{
        "Vacuno":33,
        "Cerdo":28
    },
    "Fruteria":{
        "Manzana":19,
        "Pera":11
    }
}
while True:
    print(datos)
    producto=input("Ingrese producto: ")
    ventas=int(input("Inggrese ventas: "))
    area=input("Ingrese area: ").title()
    if producto not in datos[area]:
        datos[area][producto]=ventas
    else:
        datos[area][producto]+=ventas