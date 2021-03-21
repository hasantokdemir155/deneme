import pygame
from time import sleep
i= 95
m=235

def ekr():
    scr1=pygame.display.set_mode((300,300))
    #pygame.draw.circle(scr1, red,(i,260), 10)
    pygame.draw.line(scr1, BLUE, (10, 280), (290,280), 9)
    pygame.draw.line(scr1, akua, (10, 60), (30,60), 12)
    pygame.draw.line(scr1, akua, (90, 60), (120,60), 12)
    pygame.draw.line(scr1, akua, (160, 60), (185,60), 12)
    pygame.draw.line(scr1, akua, (210, 60), (230,60), 12)
def ekr1():
    image = pygame.image.load("gm1.jpg")
    rect = image.get_rect()
    rect.x,rect.y = (i,m)
    scr1.blit(image,rect)
def ekr2():
    scr1=pygame.display.set_mode((300,300))
    #pygame.draw.circle(scr1, red,(i,260), 10)
    pygame.draw.line(scr1, BLUE, (10, 280), (290,280), 9)
    pygame.draw.line(scr1, akua, (10, 60), (30,60), 12)
 #   pygame.draw.line(scr1, akua, (90, 60), (120,60), 12)
    pygame.draw.line(scr1, akua, (160, 60), (185,60), 12)
    pygame.draw.line(scr1, akua, (210, 60), (230,60), 12)
    image = pygame.image.load("gm1.jpg")
    rect = image.get_rect()
    rect.x,rect.y = (i,m)
    scr1.blit(image,rect)


red =(255,0,0)
akua = (0,255,255)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
pygame.init()


scr1=pygame.display.set_mode((300,300))
scr1.fill(BLUE)
#pygame.draw.circle(scr1, red,(120,260), 10)
#image = pygame.image.load("gm1.jpg")
#rect = image.get_rect()
#rect.x,rect.y = (120,235)
#scr1.blit(image,rect)
ekr()
ekr1()

#pygame.draw.line(scr1, BLUE, (10, 280), (290,280), 9)
#pygame.draw.line(scr1, akua, (10, 60), (30,60), 12)
#pygame.draw.line(scr1, akua, (90, 60), (120,60), 12)
#pygame.draw.line(scr1, akua, (160, 60), (185,60), 12)
#pygame.draw.line(scr1, akua, (210, 60), (230,60), 12)
pygame.display.flip()



while True:  
        s=m
        k = 15
        scr1=pygame.display.set_mode((300,300))
    #pygame.draw.circle(screen, RED, (30,i), 10)
        
    
        for event in pygame.event.get():

            
            
            if event.type==pygame.K_ESCAPE:
                break
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    pygame.mixer.init()
                    pygame.mixer.music.load("Alien_Machine_Gun-Matt_Cutillo-2023875589.wav")
                    pygame.mixer.music.play()
                    
                    while s> 10 : 
                            scr1=pygame.display.set_mode((300,300))

                            
                            ekr1()    
                            #pygame.draw.circle(scr1, red,(120,260), 10)

                            pygame.draw.line(scr1, BLUE, (10, 280), (290,280), 9)
                            pygame.draw.line(scr1, akua, (10, 60), (30,60), 12)
                                
                            pygame.draw.line(scr1, akua, (90, 60), (120,60), 12)

                            pygame.draw.line(scr1, akua, (160, 60), (185,60), 12)

                            pygame.draw.line(scr1, akua, (210, 60), (230,60), 12)    

                            pygame.draw.line(scr1, BLUE, (10, 280), (290,280), 9)
                                
                            #pygame.draw.line(scr1, GREEN, (i+24,s), (i+24,s+5), 6)
                            pygame.draw.circle(scr1, red,(i+26,s+5), 3)    
                            
                            
                            if i >90    and i < 120:

                                   # scr1=pygame.display.set_mode((300,300))
                                    ekr1()    
                                    ekr2()
                                        
                                    
                                    #pygame.draw.circle(scr1, red,(120,260), 10)

                                   # pygame.draw.line(scr1, BLUE, (10, 280), (290,280), 9)
                                    #pygame.draw.line(scr1, akua, (10, 60), (30,60), 12)
                                        
                                   # pygame.draw.line(scr1, akua, (90, 60), (120,60), 12)

                                    #pygame.draw.line(scr1, akua, (160, 60), (185,60), 12)
                                    #pygame.draw.line(scr1, akua, (210, 60), (230,60), 12)    
                                    #pygame.draw.line(scr1, BLUE, (10, 280), (290,280), 9)

                                    s = 14
                                    
                            pygame.display.flip()
                            sleep(0.02)
                            s = s - 5    
            
                   # print('enter tuşu')
                    
                if event.key == pygame.K_LEFT and i > 10:
                    i=i-5
                    
                   # print(i)
                    #print('sola bastın')               
                    #pygame.draw.circle(scr1, red, (i,260), 10)
                        
                    ekr()            
                    ekr1() 
                    pygame.display.flip()

                if event.key == pygame.K_RIGHT and i < 230:
                    #print('sağa bastın')
                                
                    i= i + 5
                    ekr()
                    ekr1()
                    #pygame.draw.circle(scr1, red, (i,260), 10)
                       
                    pygame.display.flip()
                    
                if event.key == pygame.K_DOWN and m < 235:
                    m= m +5        
                    ekr()
                    ekr1()
                    #pygame.draw.circle(scr1, red, (i,m), 10)
                    
                    pygame.display.flip()

                if event.key == pygame.K_UP and m  > 70:
                    m= m -5        
                    ekr()
                    ekr1()
                    #pygame.draw.circle(scr1, red, (i,m), 10)
                    
                    pygame.display.flip()
    
