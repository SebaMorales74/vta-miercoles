import pygame
import entity

pygame.init()
size = width, height = 800, 600
window = pygame.display.set_mode(size=size)
clock = pygame.time.Clock()

# Colores
white = (255, 255, 255)

jugador1 = entity.Player(coords=(50, 50), color=(255, 0, 0))
jugador2 = entity.Player(coords=(150, 50), color=(0, 255, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(white)

    pygame.draw.rect(window, jugador1.color, jugador1.rect)
    pygame.draw.rect(window, jugador2.color, jugador2.rect)
    pygame.draw.rect(window, (0,0,255), pygame.Rect(50, 500, 300, 60))
    
    jugador1.move()
    jugador2.move()

    pygame.display.flip()
    clock.tick(60)
