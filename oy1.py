import pygame
import random
from time import sleep
pygame.init()

scr=pygame.display.set_mode((800,600))
red=(255,0,0)
green=(0,255,0)
aka=(0,255,255)
pygame.display.set_caption('oyun programı')

clk=pygame.time.Clock()
x=140
y=500
def gemi(x,y):
    gem = pygame.image.load("gm1.jpg")
    scr.blit(gem,(x,y))
def dusman1(x,y):
    dsm1 = pygame.image.load("dsman1.png")
    scr.blit(dsm1,(x,y))

def dusman2(x,y):
    dsm2 = pygame.image.load("dsman2.png")
    scr.blit(dsm2,(x,y))

def pat1():
     pygame.draw.circle(scr,green,(x,93),4)
                    # sleep(0.01)
     pygame.draw.circle(scr,green,(x+25,92),4)
                     #sleep(0.01)   
     pygame.draw.circle(scr,green,(x-8,110),4)
                     #sleep(0.01)                    

     pygame.draw.circle(scr,green,(x+4,125),4)
                     #sleep(00,.01)
     pygame.draw.circle(scr,green,(x-15,125),4)
                     #sleep(0.01)
     pygame.draw.circle(scr,green,(x+16,125),4)
     pygame.draw.circle(scr,green,(x+8,125),4)
     pygame.draw.circle(scr,green,(x-32,125),4)

     pygame.draw.circle(scr,green,(x+21,125),4)
     pygame.draw.circle(scr,green,(x-23,114),4)
     pygame.draw.circle(scr,green,(x+8,107),4)
     pygame.draw.circle(scr,green,(x-45,102),4) 
                    
def pat2():
     pygame.draw.circle(scr,green,(x,93),2)
                    # sleep(0.01)
     pygame.draw.circle(scr,green,(x+25,92),2)
                     #sleep(0.01)   
     pygame.draw.circle(scr,green,(x-8,110),2)
                     #sleep(0.01)                    

     pygame.draw.circle(scr,green,(x+4,125),2)
                     #sleep(00,.01)
     pygame.draw.circle(scr,green,(x-15,125),2)
                     #sleep(0.01)
     pygame.draw.circle(scr,green,(x+16,125),2)
     pygame.draw.circle(scr,green,(x+8,125),2)
     pygame.draw.circle(scr,green,(x-32,125),2)

     pygame.draw.circle(scr,green,(x+21,125),2)
     pygame.draw.circle(scr,green,(x-23,114),2)
     pygame.draw.circle(scr,green,(x+8,107),2)
     pygame.draw.circle(scr,green,(x-45,102),2) 
def pat3():
     pygame.draw.circle(scr,green,(x,93),1)
                    # sleep(0.01)
     pygame.draw.circle(scr,green,(x+25,92),1)
                     #sleep(0.01)   
     pygame.draw.circle(scr,green,(x-8,110),1)
                     #sleep(0.01)                    

     pygame.draw.circle(scr,green,(x+4,125),1)
                     #sleep(00,.01)
     pygame.draw.circle(scr,green,(x-15,125),1)
                     #sleep(0.01)
     pygame.draw.circle(scr,green,(x+16,125),1)
     pygame.draw.circle(scr,green,(x+8,125),1)
     pygame.draw.circle(scr,green,(x-32,125),1)

     pygame.draw.circle(scr,green,(x+21,125),1)
     pygame.draw.circle(scr,green,(x-23,114),1)
     pygame.draw.circle(scr,green,(x+8,107),1)
     pygame.draw.circle(scr,green,(x-45,102),1) 
def sek():
        if sekil1 !=0:
            pygame.draw.circle(scr, green,(sekil1,95), 25)
                  
        if sekil2 != 0:   
            pygame.draw.circle(scr, green,(sekil2,95), 25)

        if sekil3 !=0:
            pygame.draw.circle(scr, green,(sekil3,95), 25)
        if sekil4 != 0:   
            pygame.draw.circle(scr, green,(sekil4,95), 25)
 
        if sekil5 != 0:   
            pygame.draw.circle(scr, green,(sekil5,95), 25)


M=y
sekil1=x
sekil2=x+98
sekil3=x+98+112
sekil4=x+98+112+112
sekil5=x+98+112+112+112
ind = 0
ind1=0
sekil2y=95
sekil3y=95
sekil4y=95
sekil5y=95
x1=760
y1=random.randint(50,140)
x2=-10
y2=y1+95
sekil1y=y1
son= False

while not son  :
    y =M  
    gemi(x,M)
    
    pygame.display.flip()
    
    for event in pygame.event.get():

       if event.type== pygame.QUIT:
          pygame.quit()
          quit()

       if event.type == pygame.KEYDOWN:

          if event.key == pygame.K_LEFT:
             if x > 5:              
                  x = x - 9
             else:
                  x = 5
                 
             scr=pygame.display.set_mode((800,600))   
             gemi(x,M)
                     
          if event.key == pygame.K_RIGHT:
             if x < 734:              
                  x = x + 9
             else:
                  x = 734
              
             x = x + 9
             scr=pygame.display.set_mode((800,600))   
             gemi(x,M)

          if event.key == pygame.K_UP:
             
             if M > 5:              
                  M=M-9
             else:
                  M = 5
             if M < 135 and M > 5:
                  M= 135    
          if event.key == pygame.K_DOWN:

             if M < 300:              
                  M=M+9
             else:
                  M = 550
            
                
             scr=pygame.display.set_mode((800,600))   
             gemi(x,M)
                       
    
          if event.key == pygame.KEYUP:
               if event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  x=x+0 

          if event.key == pygame.K_RETURN:
             #M = y
             pygame.mixer.init()
             pygame.mixer.music.load("Alien_Machine_Gun-Matt_Cutillo-2023875589.wav")
             pygame.mixer.music.play()
            
             #while y > 0:

             scr=pygame.display.set_mode((800,600))   
             gemi(x,M)  

             if y > 95:
                    pass
                    # print('aaaa')   
                 
             else :   

                     if x+46 >= sekil1 and x+46 <= sekil1+46 :
                       
                         #pat3()
                         pygame.mixer.init()
                         pygame.mixer.music.load("Bomb-SoundBible.com-891110113.wav")
                         pygame.mixer.music.play()
                        # scr=pygame.display.set_mode((800,600))   
                         gemi(x,M) 
                         sekil1=0
            
                     if x+46 >= sekil2 and x+46 <= sekil2+46:                        

                         #pat3()
                         pygame.mixer.init()
                         pygame.mixer.music.load("Bomb-SoundBible.com-891110113.wav")
                         pygame.mixer.music.play()
                        # scr=pygame.display.set_mode((800,600))   
                         gemi(x,M)
                         sekil2=0
                         
                     if x+46 >= sekil3 and x+46 <= sekil3+46 :
                       
                         #pat3()
                         pygame.mixer.init()
                         pygame.mixer.music.load("Bomb-SoundBible.com-891110113.wav")
                         pygame.mixer.music.play()
                        # scr=pygame.display.set_mode((800,600))   
                         gemi(x,M) 
                         sekil3=0
            
                     if x+46 >= sekil4 and x+46 <= sekil4+46:                        

                         #pat3()
                         pygame.mixer.init()
                         pygame.mixer.music.load("Bomb-SoundBible.com-891110113.wav")
                         pygame.mixer.music.play()
                        # scr=pygame.display.set_mode((800,600))   
                         gemi(x,M)
                        # print('ddddd')
                       #  pygame.draw.circle(scr, green,(sekil4,95), 25)
                         sekil4=0

                     if x+46 >= sekil5 and x+46 <= sekil5+46:                        

                         #pat3()
                         pygame.mixer.init()
                         pygame.mixer.music.load("Bomb-SoundBible.com-891110113.wav")
                         pygame.mixer.music.play()
                        # scr=pygame.display.set_mode((800,600))   
                         gemi(x,M)
                        # print('ddddd')
                       #  pygame.draw.circle(scr, green,(sekil4,95), 25)
                         sekil5=0

                                 
             pygame.draw.circle(scr, aka,(x+25,y), 2)
                      
 
             y = y - 5
                 
                     
             pygame.display.flip()
             sleep(0.009)

    if sekil1y == 550:
       sekil1y = y1

    if sekil2y == 550:
       sekil2y = 95

    
      
    if sekil1y != 550:
        sekil1y=sekil1y + 9
        #scr=pygame.display.set_mode((800,600))
        #sek()
        s= x1      
        pygame.draw.circle(scr, red,(s+16,sekil1y), 4)
        
        gemi(x,M)  
        
        sleep(0.006)
         
        
        pygame.display.flip()
       # print(seki11y)




    if sekil1y== M:         

        if sekil1 > x1 and sekil1 < x1+49:
            pygame.mixer.init()
            pygame.mixer.music.load("MP5_SMG-GunGuru-703432894.wav")
            pygame.mixer.music.play()

    if sekil2y== M:         

        if sekil2 > x2 and sekil2 < x2+49:
            pygame.mixer.init()
            pygame.mixer.music.load("MP5_SMG-GunGuru-703432894.wav")
            pygame.mixer.music.play()


    x1 = x1 + ind    
    if x1 >= 740:
        ind = -5
    if x1 <= 0:
        ind = 5
             
    x2 = x2 + ind1    
    if x2 >= 740:
        ind1 = -7
    if x2 <= 0:
        ind1 = 7
    
    scr=pygame.display.set_mode((800,600))
    dusman2(x2,y2)
    dusman1(x1,y1)
    pygame.display.flip
    if x > 800 or x < 0:
           
            son = True
      # print(x)     
      # print(event)
    
quit()    

