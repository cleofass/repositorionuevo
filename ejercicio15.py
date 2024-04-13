#Para tributar un determinado impuesto se debe ser mayor de 16 años y 
#tener unos ingresos superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
#y muestre por pantalla si el usuario tiene que tributar o no.



# Solicita la edad del usuario y la convierte a entero
edad = int(input("¿Cuál es tu edad? "))
# Solicita los ingresos mensuales del usuario y los convierte a número flotante
ingresos = float(input("¿Cuáles son tus ingresos mensuales?"))

# Verifica si el usuario cumple con las condiciones para tributar
if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")
# Si la edad es mayor a 16 y los ingresos son iguales o superiores a 1000, debe tributar
# En caso contrario, no debe hacerlo
