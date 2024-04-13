#Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario 
#y después muestre en pantalla la suma de todos los enteros desde 1 hasta  n . 
#La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma:
#suma=n(n+1)/2


# Solicitamos al usuario que ingrese un número entero positivo
n = int(input("Ingrese un numero entero positivo: "))

# Calculamos la suma de todos los enteros desde 1 hasta n
suma = n * (n + 1) // 2  # Utilizamos la división entera para evitar decimales

# Mostramos el resultado en pantalla
print(f"La suma de los números del 1 al {n} es {suma}")
