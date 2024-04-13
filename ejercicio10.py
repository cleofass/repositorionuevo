#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
#separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.


# Solicitar al usuario los productos de la cesta de la compra
cesta = input('Introduce los productos de la cesta separados por comas:')

# Dividir los productos por comas y mostrar cada uno en una línea nueva
productos = cesta.split(',')
for producto in productos:
    print(producto)