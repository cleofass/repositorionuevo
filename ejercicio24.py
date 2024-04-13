#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año 
#que dura la inversión.


cantidad = float(input("Ingrerse la cantidad a invertir:"))
interes = float(input("Ingrese el interes porcentual anual: "))
años = int(input("Ingrese los años "))
for i in range(años):
    cantidad *= 1 + interes/100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))