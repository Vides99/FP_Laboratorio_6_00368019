saldoCuenta = 1000
decisionRetiroDeposito = 0
cantidadDepositarOretirar = 0

def ValidacionDeRetiro(saldoCuenta):
    cantidadDepositarOretirar = int(input("ingrese la cantidad que quiere retirar de su cuenta"))
    if cantidadDepositarOretirar > saldoCuenta:
        print("no tienes fondos suficientes, ingrese otra cantidad, sus fondos son: ", saldoCuenta)
        ValidacionDeRetiro(saldoCuenta)
    else:
        saldoCuenta = saldoCuenta - cantidadDepositarOretirar
        print("su retiro a sido completado exitosamente, sus fondos son: ", saldoCuenta)
    

print("bienvenido a la banca digital")
print("¿Que desea hacer?")
print("-Estado de cuenta - ingrese numero 1\n -Depositar a tu cuenta - ingrese numero 2\n -Retirar de su cuenta - ingrese numero 3")
decisionRetiroDeposito = int(input("ingrese su accion"))
if decisionRetiroDeposito == 1:
    print("sus fondos disponibles son: ",saldoCuenta)
elif decisionRetiroDeposito == 2:
    cantidadDepositarOretirar = int(input("ingrese la cantidad que quiere depositar a su cuenta"))
    saldoCuenta = saldoCuenta + cantidadDepositarOretirar
    print("Su transaccion a sido completada, sus fondos son: ", saldoCuenta)
elif decisionRetiroDeposito == 3:
    cantidadDepositarOretirar = int(input("ingrese la cantidad que quiere retirar de su cuenta"))
    if cantidadDepositarOretirar > saldoCuenta:
        print("no tienes fondos suficientes, ingrese otra cantidad, sus fondos son: ", saldoCuenta)
        ValidacionDeRetiro(saldoCuenta)
    else:
        saldoCuenta = saldoCuenta - cantidadDepositarOretirar
        print("su retiro a sido completado exitosamente, sus fondos son: ", saldoCuenta)