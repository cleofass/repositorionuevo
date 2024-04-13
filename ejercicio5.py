#Escribir un programa que pida al usuario que introduzca una frase en la consola
#y muestre por pantalla la frase invertida.


# Eliminamos la línea duplicada para pedir la frase al usuario
# y agregamos un mensaje para informar al usuario de lo que sucederá con la frase

frase=input("Ingrese la frase: ")
print("La frase invertida es:", frase[::-1])
