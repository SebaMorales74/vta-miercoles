lista = []

print("Se creó la lista: ", lista)

# Cómo agregar elementos a una lista
lista.append(2.6) # 0
lista.append(940924) # 1
lista.append("Hola mundo") # 2

# Imprimir en pantalla todos los elementos de una lista
print(lista)

# Consultar el dato con su respectivo indice o posicion
print(lista[0]) # lista.append(2.6)
print(lista[1]) # lista.append(940924)
print(lista[2]) # lista.append("Hola mundo")

# Consultar el último dato
print(lista[-1]) # lista.append("Hola mundo")
print(lista[-2]) # lista.append(940924)
print(lista[-3]) # lista.append(2.6)

lista[0] = 3.3 
print(lista[0]) # lista[0] = 3.3 

# Elimino un elemento según su valor
lista.remove(3.3)
print(lista)

# Elimino un elemento según su posicion
lista.pop(0)
print(lista)

# Limpio toda la lista
lista.clear()
print(lista)