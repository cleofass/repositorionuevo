#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.



# Solicitamos al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Verificamos si el número es par o impar
if n % 2 == 0:
    print(f"El número {n} es par")
else:
    print(f"El número {n} es impar")

