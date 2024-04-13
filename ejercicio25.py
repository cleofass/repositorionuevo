#Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
#triángulo rectángulo como el de más abajo, de altura el número introducido.


a=int(input("Introduzca la altura del triangulo: "))


for i in range(a):
   
   print("*"*(i+1))