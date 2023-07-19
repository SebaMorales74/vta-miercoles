import time
import numpy


def cronometrar(func):
    def ejecucion():
        tiempo_inicial = time.time()
        func()
        tiempo_final = time.time() - tiempo_inicial
        print("La ejecución demoró:", tiempo_final, "segundos")

    return ejecucion


def test(func):
    def testear():
        try:
            func()
            print("✅ ¡Funcion ejecutada correctamente!")
        except:
            print("⛔ ¡Hubo un error!")

    return testear


@test
def suma():
    resultado = numpy.sum([i for i in range(100000)])
    return resultado


@cronometrar
def multiplicar():
    resultado = numpy.prod([i for i in range(100000)])
    return resultado


def raiz(numero):
    print(numpy.sqrt(numero))

cronometrar(raiz(numero=4))

suma()
multiplicar()


print("Holaaa estoy ejecutando la 2da parte del codigo 👋👋👋")
