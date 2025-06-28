from funci import shop,shop2
while True:
    print("1. Comprar")
    print("2. Pagar Vip ")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            compra=int(input("Ingrese precio de su compra: "))
            print(shop(op,compra))
        case 2:
            vip=int(input("Ingrese $5000"))
            print(shop2(op,vip))