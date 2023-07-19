# Operadores Logicos
# = Asignar o Definir
# == ¿Es igual que?
# < ¿Es menor que?
# > ¿Es mayor que?

# not NO
# not == ¿Es diferente de?
# not < ¿No es menor que?
# not > ¿No es mayor que?

a = 1
b = 2

if a == b:
    print("a es igual a b")

if not a == b: # -> verdadero
    print("a es diferente de b") 

if a < b: # -> verdadero
    print("a es menor que b") 

if a > b:
    print("a es mayor que b")

if not a < b:
    print("a no es menor que b")

if not a > b: # -> verdadero
    print("a no es mayor que b")
