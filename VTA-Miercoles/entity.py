import pygame


class Player:
    def __init__(self, coords, color):
        self.rect = pygame.Rect(coords[0], coords[1], 60, 60)
        self.color = color
        self.speed = 4
        self.canJump = True

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if pygame.key.get_pressed()[pygame.K_UP] and self.canJump == True:
            self.rect.y -= 10
            self.canJump = False

        self.rect.y += 1
