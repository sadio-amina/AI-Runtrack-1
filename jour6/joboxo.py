import pygame
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('TicTacToe1337')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    screen.blit(background, (0, 0))
    pygame.display.flip()