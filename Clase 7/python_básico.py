texto = "lo que yo quiero"
entero = 1000
decimales = 1.005

if entero == 1000:
    print("Entero es igual a 1000")
else:
    print("Entero no es igual a 1000")

contraseña = ""

while contraseña != "123pormi":
    contraseña = input("Escribe la contraseña secreta: ")

def Hola():
    print("Hola mundo")

limite = int(input("¿Cuantas veces quieres saludar? "))

for i in range(limite):
    Hola()

def suma(a,b):
    return a+b

print(suma(a=1,b=2))