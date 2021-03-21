import pygame
pygame.init()

scr1=pygame.display.set_mode((400,400))

image = pygame.image.load("gm1.jpg")
rect = image.get_rect()
rect.x,rect.y = (40,350)
scr1.blit(image,rect)
pygame.display.flip()
