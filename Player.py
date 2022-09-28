import pygame

from IMoveable import IMoveable


class Player(IMoveable):
    width: int = 50
    height: int = 50
    speed: int = 10

    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.rect = pygame.Rect(pos.x, pos.y, self.width, self.height)

    def update(self):
        self.move()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def input_handler(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.direction.x = -1
            if event.key == pygame.K_d:
                self.direction.x = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.direction.x = 1
                else:
                    self.direction.x = 0
            elif event.key == pygame.K_d:
                if pygame.key.get_pressed()[pygame.K_a]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

    def move(self):
        self.pos.x += self.direction.x * self.speed
