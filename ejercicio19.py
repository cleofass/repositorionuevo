#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual 
#y el número de años, 
#y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.


# Solicitar al usuario la cantidad a invertir
cantidad = float(input("Ingrese la cantidad a invertir: "))
# Solicitar al usuario el interés porcentual anual
interes = float(input("Ingrese el interes porcentual anual: "))
# Solicitar al usuario el número de años de la inversión
años = int(input("Ingrese el numero de años: "))

# Calcular el capital final y mostrarlo redondeado con dos decimales
capital_final = cantidad * (interes / 100 + 1) ** años
print("Capital final: " + str(round(capital_final, 2)))
