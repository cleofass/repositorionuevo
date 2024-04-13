#Escribir un programa que pregunte el correo electrónico del usuario en la consola
#y muestre por pantalla otro correo electrónico con el mismo nombre 
#(la parte delante de la arroba @) pero con dominio ceu.es.\

# Solicitar al usuario su correo electrónico
email = input("Introduce tu correo electrónico: ")

# Extraer el nombre del usuario (parte antes de la arroba)
nombre_usuario = email[:email.find('@')]

# Crear el nuevo correo electrónico con el dominio ceu.es
nuevo_email = nombre_usuario + '@ceu.es'

# Mostrar el nuevo correo electrónico por pantalla
print("Tu nuevo correo electrónico es:", nuevo_email)