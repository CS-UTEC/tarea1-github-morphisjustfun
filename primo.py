import math
print("Este algoritmo verifica si el numero ingresado es primo")
num = int( input("Ingresa el numero: "))
condicion  = 0
if num<0:
    print("El numero no es positivo")
    quit()
if num==1:
    condicion=2
for i in range(2,num):
    if num%i == 0:
        condicion = 1
if num==0:
    condicion = 1
if condicion==1:
    print("El numero no es primo")
elif condicion ==2:
    print("El numero no es ni primo ni compuesto")
else:
    print("El numero es primo")
