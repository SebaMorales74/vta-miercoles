class Mascota:
    def __init__(
        self,
        nombre=str(),
        especie=str(),
        raza=str(),
        fechaDeNacimiento=str(),
        color=str(),
    ):
        self.__diagnostico = ""
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.fechaDeNacimiento = fechaDeNacimiento
        self.color = color

    def asignarDiagnostico(self, diagnostico=str()):
        self.__diagnostico = diagnostico

    def __str__(self) -> str:
        return f"""
        Nombre: {self.nombre},
        Especie: {self.especie},
        Raza: {self.raza},
        Fecha de nacimiento: {self.fechaDeNacimiento},
        Color: {self.color},
        Diagnostico: {self.__diagnostico}"""

lista_de_mascotas = []

cantidadDePacientes = int(input("Dime la cantidad de animales a guardar: "))

for animal in range(cantidadDePacientes):
    nombre = input("Ingresa el nombre de la mascota: ")
    especie = input("Ingresa la especia de la mascota: ")
    raza = input("Ingresa la raza de la mascota: ")
    fechaDeNacimiento = input("Ingresa la fecha de nacimiento de la mascota: ")
    color = input("Ingresa el color de la mascota: ")
    diagnostico = input("Ingresa el diagnostico de la mascota: ")
    mascota_a_registrar = Mascota(
        nombre=nombre,
        especie=especie,
        raza=raza,
        fechaDeNacimiento=fechaDeNacimiento,
        color=color,
    )
    mascota_a_registrar.asignarDiagnostico(diagnostico)
    lista_de_mascotas.append(mascota_a_registrar)
    print("¡Mascota registrada! \n")


print("Lista total de mascotas registradas:")
contador = 1
for mascota in lista_de_mascotas:
    print(f"Mascota N°{contador}")
    print(f"{mascota} \n")
    contador += 1
