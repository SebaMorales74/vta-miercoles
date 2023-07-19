# Operadores lógicos
# = "Igual que", me permite asignar un valor a una variable.
texto = "Hola mundo"
numeroEntero = 123
numeroDecimal = 2.5
# Escribir
print("Ingresa la palabra secreta")
# Leer
textoUsuario = input()
# Concatenación: Escribir distintos valores, unos juntos a los otros.
print("Has dicho:",textoUsuario)
# Decisión es efecto de preguntar algo.
# == "¿Es igual?" Mi computadora va a comparar si esto es verdadero o falso.
# En caso de que sea verdadero, puedo tomar una decision.
# En caso de que sea falso, puedo tomar otra decision.
if textoUsuario == "123pormi":
    print("Has escrito la palabra secreta")
else:
    print("No has escrito la palabra secreta")
# Operadores lógicos
# < "¿Es menor que?" Me permite comparar si un numero es menor que el otro.
# > "¿Es mayor que?" Me permite comparar si un numero es mayor que el otro.
numeroEntero = int(input("Ingresa el numero entero: "))
if numeroEntero < 200:
    print("Mi numero entero es menor a 200")
else:
    print("Mi numero entero es mayor que 200")