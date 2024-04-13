#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
#y muestre por pantalla el número de euros y el número de céntimos del precio introducido.


# Solicitar al usuario el precio del producto
precio = input("Introduzca el precio del producto con dos decimales: ")

# Encontrar la posición del punto decimal
posicion_punto = precio.find('.')

# Extraer la cantidad de euros y céntimos
lempiras = precio[:posicion_punto]
tostones = precio[posicion_punto+1:]

# Imprimir el resultado
print(lempiras, 'lempiras y', tostones, 'tostones.')