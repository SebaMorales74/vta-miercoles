class Persona:
    def __init__(self, dni=str, nombre=str, edad=int, altura=int):
        self.__dni = dni
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    def identificarse(self):
        print("Mi dni es",self.__dni,"Mi nombre completo es",self.nombre)

sebastian = Persona(dni="12.345.678-9",nombre="Sebastian Morales",edad=20,altura=175)
luna = Persona(dni="21.324.567-0",nombre="Luna Carrizo",edad=20,altura=158)

sebastian.identificarse()
luna.identificarse()