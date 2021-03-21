import pygame
 
RED =   (255, 0,  0)
GREEN = (0,  255, 0)
BLUE =  (0,   0, 255)
pygame.init()
screen=pygame.display.set_mode((640,480))
 
#pygame.draw.line(screen, BLUE, (60, 60), (120,60), 4)
#pygame.draw.ellipse(screen, RED, (300, 250, 40,80), 1)
 
#pygame.draw.rect(screen, RED, (50,50,100,25)) 
#pygame.draw.polygon(screen, GREEN, ((146, 0),
 #   (291, 106), (236, 277), (56, 277), (0, 106)))
 
for i in range(50,300,15):
    screen=pygame.display.set_mode((640,480))
    pygame.draw.circle(screen, RED, (50,i), 15)
    input()
    pygame.display.flip()
#pygame.draw.polygon(screen, GREEN, ((250,100),(300,0),(350,50)))
#pygame.draw.arc(screen, BLUE,(400,10,150,100), 0, 3.14)


