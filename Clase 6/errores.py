# Definir una variable correctamente
contraseña = input("Ingresa la contraseña: ")

# Forma erronea de definir texto
variable1 = Ingrese la contraseña:

# Sangría o Identación con la tecla tabulador

#Correcto. Tabulador
if contraseña == "123pormi":
    print("Adivinaste la contraseña")
else:
    print("Contraseña invalida")

# No recomendado. Espacio.
if contraseña == "123pormi":
 print("Adivinaste la contraseña")
else:
 print("Contraseña invalida")

# Incorrecto. Sin identación.
if contraseña == "123pormi":
print("Adivinaste la contraseña")
else:
print("Contraseña invalida")


# Semantica
numero1 = 1
numero2 = 2
Numero1 = "1"
Numero2 = "2"

suma = numero1 + numero2 # -> = 3
suma = Numero1 + Numero2 # -> = "12"

print(suma)