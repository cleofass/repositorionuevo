#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el siguiente formato:

#<producto>: <unidades> unidades x <precio>€ = <total>L

#donde <unidades> es el número de unidades con cinco dígitos, 
#<precio> es el precio unitario con 6 dígitos enteros y 2 decimales y 
#<total> es el coste total con 8 dígitos enteros y 2 decimales.




# Solicitar el precio por unidad del producto
precio=float(input('Introduzca el precio por unidad: '))
# Solicitar el número de unidades del producto
unidades=int(input('Introduzca el número de unidades: '))

# Calcular el total
total = unidades * precio

# Imprimir el resultado con el formato especificado
print('{producto}: {unidades:05d} unidades x {precio:06.2f}€ = {total:010.2f}€'.format(producto=producto, unidades=unidades, precio=precio, total=total))
