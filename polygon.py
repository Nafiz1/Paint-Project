import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
cooordinate = []
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN: #if mouse click then coordinate array will append x,y tuple 
            cooordinate.append(event.pos)

    if len(cooordinate) >= 5:
        pygame.draw.polygon(screen, (255,255,100), cooordinate, 3)
     

    pygame.display.update()
