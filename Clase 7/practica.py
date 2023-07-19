class Persona:
    def __init__(
        self, nombre=str, apellido=str, estatura=float, estilo_vida=str, gmail=str
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.estatura = estatura
        self.estilo_vida = estilo_vida
        self.gmail = gmail

    def __str__(self):
        return f"""Nombre: {self.nombre} \nApellido: {self.apellido} \nEstatura: {self.estatura} \nEstilo de vida: {self.estilo_vida} \nGmail: {self.gmail} \n"""

personas = []
Sebastian = Persona(nombre="Sebastian",apellido="Morales",estatura=1.75,estilo_vida="Estresado",gmail="sebastian@gmail.com")
Maria = Persona(nombre="Maria",apellido="Morales",estatura=1.75,estilo_vida="Estresado",gmail="sebastian@gmail.com")

contador = 1
for persona in personas:
    print(f"Persona N°{contador}")
    print(persona)
    contador += 1
