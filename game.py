import pygame
import os

from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,100)

screen = pygame.display.set_mode((700,600))
pygame.display.set_caption("Play Sudoku!")

grid=Grid()
running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    grid.draw_line(pygame,screen)

    pygame.display.flip()

