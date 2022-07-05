import pygame
from pygame import mixer
pygame.display.init()
pygame.font.init()
textfont = pygame.font.SysFont("monospace",16)
file = 'chad.jpg'
render = input(str("O que queres:"))
render2 = input(str("O que queres:"))

screen = pygame.display.set_mode((640, 480))
load = pygame.image.load(file)
screen.blit(load,(0,0))

textTBD = textfont.render(render, 1, (0,0,0))
screen.blit(textTBD, (0,22))

textTBD2 = textfont.render(render2, 1, (0,0,0))
screen.blit(textTBD2, (322,22))

mixer.init()
music = 'musica.mp3'
mixer.music.load(music)
mixer.music.play()

pygame.display.update
pygame.display.flip()
