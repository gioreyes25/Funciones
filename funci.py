def calcular (num1,num2,op):
    if op == 1:
        return num1+num2
    elif op == 2:
        return num1-num2
    elif op == 3:
        return num1*num2
    elif op ==4:
        return num1/num2

def votar(op,edad):
    if op==1:
        if edad>18:
            return ("Usted Puede Votar")
        else:
            return ("Usted No Puede Votar")
def nota(op,notas):
    if op==1:
        if notas>=4:
            return ("Usted Aprueba")
        else:
            return ("Usted Reprueba")
def stoca(op,i):
    if op==2:
        if i["cantidad"]<=0:
            return ("Este Producto Esta sin stock")