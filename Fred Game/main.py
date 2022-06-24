import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_BACKQUOTE,
    KEYDOWN,
    QUIT,
)


pygame.init()

HEIGHT, WIDTH = 800, 1000

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FRED GAME")
WHITE = (255, 255, 255)

FPS = 60


def draw_window():
    win.fill("white")
    surf = pygame.Surface((50,50))
    surf.fill((0,0,0))
    rect = surf.get_rect()
    win.blit(surf, ((WIDTH - surf.get_width())/2,
                 (HEIGHT - surf.get_height())/2))
    ENEMY = pygame.draw.circle(win, (2, 2, 255), (250, 250), 75)
    pygame.display.flip()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                print(event.type)
                if event.key == K_ESCAPE:
                    print("ESCAPE")
                    running = False
            elif event.type == QUIT:
                running = False

        draw_window()
    pygame.quit()



if __name__== "__main__":
    main()
