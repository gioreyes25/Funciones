from funci import calcular
while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            num1=int(input("Ingrese num 1"))
            num2=int(input("Ingrese num 2"))
            print(calcular(num1,num2,op))
        case 2:
            num1=int(input("Ingrese num 1"))
            num2=int(input("Ingrese num 2"))
            print(calcular(num1,num2,op))
        case 3:
            num1=int(input("Ingrese num 1"))
            num2=int(input("Ingrese num 2"))
            print(calcular(num1,num2,op))
        case 4:
            num1=int(input("Ingrese num 1"))
            num2=int(input("Ingrese num 2"))
            print(calcular(num1,num2,op))