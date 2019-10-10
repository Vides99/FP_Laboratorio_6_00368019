conteoPares = 0
numPar = 0
decision = ""

def solicitudDePares(conteoPares):
    numPar = int(input("introduce un numero par"))
    if numPar % 2 == 0:
        conteoPares = conteoPares + 1
        decision = str(input("¿Quiere escribir otro número par? (S/N):"))
        if decision == "S":
            solicitudDePares(conteoPares)
        else:
            print("el programa a finalizado, has ingresado ", conteoPares, " numeros paes")
    else:
        print("el numero que ingreso es inpar")
        decision = str(input("¿Quiere escribir otro número par? (S/N):"))
        if decision == "S":
            solicitudDePares(conteoPares)
        else:
            print("el programa a finalizado, has ingresado ", conteoPares, " numeros paes")

numPar = int(input("introduce un numero par"))
if numPar % 2 == 0:
    conteoPares = conteoPares + 1
    decision = str(input("¿Quiere escribir otro número par? (S/N):"))
    if decision == "S":
        solicitudDePares(conteoPares)
    else:
        print("el programa a finalizado, has ingresado ", conteoPares, " numeros paes")
else:
    print("el numero que ingreso es inpar")
    decision = str(input("¿Quiere escribir otro número par? (S/N):"))
    if decision == "S":
        solicitudDePares(conteoPares)
    else:
        print("el programa a finalizado, has ingresado ", conteoPares, " numeros paes")
            