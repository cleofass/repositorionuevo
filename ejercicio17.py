#Escribe un programa que pregunte al usuario por el número de horas trabajadas 
#y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.



# Solicita al usuario el número de horas trabajadas y el costo por hora
horas = int(input("Ingrese el número de horas trabajadas: "))
costo = int(input("Ingrese el costo por hora: "))

# Calcula el pago total
pago = horas * costo

# Muestra el pago total al usuario
print("Tu paga es: ", pago)
