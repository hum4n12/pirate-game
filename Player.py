import pygame

from IMoveable import IMoveable


class Player(IMoveable):
    width: int = 50
    height: int = 50

    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.rect = pygame.Rect(pos.x, pos.y, self.width, self.height)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self):
        pass