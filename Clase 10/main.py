# pip install pygame
import pygame # OBLIGATORIO -> Importar el modulo de pygame

pygame.init() # OBLIGATORIO -> Iniciar pygame
size = width, heigth = 900, 600
screen = pygame.display.set_mode(size) # OBLIGATORIO -> Declarar las dimensiones de la ventana
clock = pygame.time.Clock() # OBLIGATORIO -> Declarar que existe un tiempo a respetar

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((44, 207, 222))
    
    pygame.display.flip()

    clock.tick(60)