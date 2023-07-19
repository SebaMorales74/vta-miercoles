import pygame
import entidades
import os

path = os.getcwd()

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
titulo = pygame.display.set_caption("Proyecto RPG")
icono = pygame.image.load(
    os.path.join(path, "Proyecto RPG", "icon.png")
).convert_alpha()
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

jugador = entidades.Jugador()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((44, 207, 222))

    screen.blit(jugador.imagen, jugador.rect)

    jugador.movimiento()

    pygame.display.flip()
    clock.tick(60)
