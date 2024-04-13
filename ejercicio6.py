#Escribir un programa que pida al usuario que introduzca una frase en la consola y 
#una vocal en minúscula,
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

# Solicitar al usuario que ingrese una frase
frase = input("Introduce una frase: ")
# Solicitar al usuario que ingrese una vocal en minúscula
vocal = input("Introduce una vocal en minuscula: ")
# Verificar que la entrada es una vocal en minúscula
if vocal in "aeiou" and len(vocal) == 1:
    # Reemplazar la vocal en la frase por su versión en mayúscula
    frase_modificada = frase.replace(vocal, vocal.upper())
    # Mostrar la frase modificada
    print(frase_modificada)
else:
    # Mostrar un mensaje de error si la entrada no es válida
    print("Error: Debes introducir una vocal en minuscula.")