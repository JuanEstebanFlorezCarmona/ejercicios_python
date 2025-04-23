total_cuenta = float(input("ingrese el total de la cuenta: "))
while True: 
    propina = int(input("ingrese el porcentaje de la propina: "))
    if propina in (10,15,20):
        break
    else:
        print("esta opcion no es valida")

propina=total_cuenta*(propina/100)
print(propina)
total= propina + total_cuenta 
print(total)