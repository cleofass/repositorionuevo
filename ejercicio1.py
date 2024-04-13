#Escribir un programa que preunte el nombre del usuario en la consola y un numero entero
#e imprima por pantalla en lineas distintas el nombre del usuario tantas veces 
#como el numero introducido


nombre=input("¿Cómo te llamas? ")
n=int(input("Introduce un número entero: "))
for i in range(n):
    print(nombre)
