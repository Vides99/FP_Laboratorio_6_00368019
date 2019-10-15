print("ingrese un numero entero, el cual sera invertido")
numero = str(input("ingresa tu numero!"))
if len(numero) == 2:
    print("tu numero invertido es: " + numero[1] + numero [0])
elif len(numero) == 1:
    print("para poder invertir el numero,tu numero debe tener 2 digitos")
elif len(numero) == 3:
    print("tu numero invertido es: " + numero[2] + numero [1] + numero[0])
elif len(numero) == 4:
    print("tu numero invertido es: " + numero[3] + numero [2] + numero[1] + numero[0])
elif len(numero) == 5:
    print("tu numero invertido es: " + numero[4] + numero [3] + numero[2] + numero[1] + numero[0])
elif len(numero) == 6:
    print("tu numero invertido es: " + numero[5] + numero [4] + numero[3] + numero[2] + numero[1] + numero[0])