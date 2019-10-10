from random import *
valorAleatorio = 0
numIntentos = 0

def CreadorValorAleatorio(numIntentos):
    numUsuario = int(input("ingrese un nuevo valor"))
    numIntentos = numIntentos + 1;
    if valorAleatorio == numUsuario:
        print("tu valor coincide con el de la maquina, te a tomado ", numIntentos, " intentos!")
    else:
        if valorAleatorio > numUsuario:
            print("el valor que ingresaste es menor que el valor creado al azar por la maquina, sigue intentando!")
            CreadorValorAleatorio(numIntentos)
        else:
            print("el valor que ingresaste es mayor que el valor creado al azar por la maquina, sigue intentando!")
            CreadorValorAleatorio(numIntentos)

print("ingrese un valor entre 1 - 10, el cual sera comparado con un valor creado al azar por la maquina, veamos cuantos intentos te toma para que tu valor sea el mismo que el de la maquia")
numUsuario = int(input("ingrese el valor"))
numIntentos = numIntentos + 1;
valorAleatorio = randrange(1,10)
if valorAleatorio == numUsuario:
    print("tu valor coincide con el de la maquina, te a tomado ", numIntentos, " intentos!")
else:
    if valorAleatorio > numUsuario:
        print("el valor que ingresaste es menor que el valor creado al azar por la maquina, sigue intentando!")
        CreadorValorAleatorio(numIntentos)
    else:
        print("el valor que ingresaste es mayor que el valor creado al azar por la maquina, sigue intentando!")
        CreadorValorAleatorio(numIntentos)

