# pip install pygame
import pygame  # OBLIGATORIO -> Importar el modulo de pygame

pygame.init()  # OBLIGATORIO -> Iniciar pygame
size = width, height = 800, 600
screen = pygame.display.set_mode(
    size
)  # OBLIGATORIO -> Declarar las dimensiones de la ventana
clock = pygame.time.Clock()  # OBLIGATORIO -> Declarar que existe un tiempo a respetar


class Pelota:
    def __init__(self):
        self.speed = [2, 2]
        self.imagen = pygame.image.load("ball.png").convert_alpha()
        self.imagen.set_colorkey((163,73,164))
        self.rect = self.imagen.get_rect()

    def movimiento(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


pelota = Pelota()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((44, 207, 222))

    pelota.movimiento()
    screen.blit(pelota.imagen, pelota.rect)

    pygame.display.flip()
    clock.tick(60)

# CONTESTAR LA SIGUIENTE ENCUESTA
# https://strawpoll.com/polls/2ayLkV0YeZ4
