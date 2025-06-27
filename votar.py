from funci import votar
while True:
    print("1. Votar")
    op=int(input("Ingrese una op:"))
    if op==1:
        edad=int(input("Ingrese su edad"))
        print(votar(op,edad))