datos={}
from funci import nota
while True:
    print("1. Ingresar Nota")
    print("2. Ver Estudiantes Aprobados")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre: ").title()
            notas=int(input("Ingrese nota "))
            print(nota(op,notas))
        