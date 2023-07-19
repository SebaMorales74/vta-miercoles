import pygame
import os

path = os.getcwd()
class Jugador:
    def __init__(self):
        self.imagen = pygame.image.load(
            os.path.join(path, "Proyecto RPG", "sprites/jugador", "idle.png")
        ).convert_alpha()
        self.rect = self.imagen.get_rect()
        self.rect.y = 300
        self.rect.x = 400
        self.speed = 5

    def movimiento(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


class NPC:
    def __init__(self):
        pass
