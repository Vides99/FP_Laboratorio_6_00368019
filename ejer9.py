print("en este programa, tu introduces un rango de numeros y luego introduces un numero x el cual te retornara los valores divisibles de tu rango entre x")
num1 = int(input("ingrese el valor de inicio de su rango"))
num2 = int(input("ingrese el valor final de su rango"))
valorDivisor = int(input("introduce el numero x"))

for i in range(num1,num2 + 1):
    if i % valorDivisor == 0:
        print(i, "es multiplo de ", valorDivisor)
