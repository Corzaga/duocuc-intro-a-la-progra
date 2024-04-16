import os
import random

os.system("cls")

#ciclo for
for i in range(1, 33, 3):
    print(i)

contadorNota = 0
try:
    cantidad = int (input("ingrese cantidad de notas: "))
    for i in range(cantidad):
        nota = float (input (f"ingresa nota {i + 1} \n"))
        contadorNota = contadorNota + nota
    promedio = contadorNota/cantidad
    promedioRedondeado = round(promedio, 1)
    print(f"el resultado de los {cantidad} nota es: {promedioRedondeado}")

except:
    print("tipo de dato incompatible")
    
#while
bandera = True
while bandera:
    numero = int (input("ingrese un numero: "))
    if numero % 2 == 0:
        print("puede elegir otro numero")
    else:
        print("numero impar, c acaba")
        bandera = False