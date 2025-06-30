from funci import ingresos
datos={
    "panaderia":[],
    "carniceria":[],
    "fruteria":[]
}
while True:
    print("1. Agregar Ingresos")
    print("2. Ver Areas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print("1. Panaderia")
            print("2. Carniceria")
            print("3. Fruetria")
            ope=int(input("Ingrese area: "))
            if ope==1:
                area="panaderia"
                plata=int(input("Ingrese plata: "))
        case 2:
            print(ingresos(op,ope,plata,area))