import sys
import pygame

from Player import Player


def main():
    pygame.init()

    size = (1280, 720)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    player: Player = Player(pygame.Vector2(100, 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            player.input_handler(event)

        screen.fill((0, 0, 0))
        player.update()
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
