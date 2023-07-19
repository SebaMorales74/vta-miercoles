promedio = 0
for i in range(5):
    nota = int(input("Ingresa la nota de un estudiante: "))
    promedio += nota
promedio = promedio/5
# Operadores logicos
# >= ¿mayor o igual que?
# <= ¿menor o igual que?
if promedio >= 40:
    print("El alumno ha aprobado",promedio)
else:
    print("Alumno ha reprobado",promedio)