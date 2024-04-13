#Escribir un programa que pida al usuario dos números y devuelva su división. 
#Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.


# Solicitar al usuario que ingrese el dividendo y el divisor
try:
    n = float(input("Ingrese el dividendo: "))
    m = float(input("Ingrese el divisor: "))

    # Verificar si el divisor es cero y lanzar un error
    if m == 0:
        raise ValueError("Error: No se puede dividir por cero")

    # Realizar la división e imprimir el resultado
    print("El resultado de la división es:", n/m)
except ValueError as e:
    # Capturar cualquier error de valor y mostrar un mensaje de error al usuario
    print("Error: Ingrese un número válido. ", e)

    