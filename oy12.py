import pygame
import random
from time import sleep
import sys
pygame.init()

scr=pygame.display.set_mode((800,600))
red=(255,0,0)
green=(0,255,0)
aka=(0,255,255)
pygame.display.set_caption('oyun programı')

clk=pygame.time.Clock()
x=140
y=500
arka=pygame.image.load("arka.jpg")
                       
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
def fire(x,y):
        
      ates="vur"  
         
      pygame.draw.circle(scr, aka,(x+25,y), 2)
      sleep(0.06)
      
      #pygame.display.flip()

def ats():
       global ates 
       pygame.mixer.init()
       pygame.mixer.music.load("Alien_Machine_Gun-Matt_Cutillo-2023875589.wav")
       pygame.mixer.music.play()
        
       ates="vur"
       #print(ates) 
       
       
            
#global ates
ates="hazır"

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
    #y =M  
    gemi(x,M)
    
    pygame.display.flip()
 
    keys = pygame.key.get_pressed() 
    
    scr.fill((0,0,0))
    
    for event in pygame.event.get():
            
       if event.type== pygame.QUIT:
          pygame.quit()
          quit()



       
       if event.type == pygame.KEYDOWN:
              
  
          if event.key == pygame.K_LEFT:
               
              if x > 5:              
                  x -=9
              else:
                  x = 5
          if  event.key==pygame.K_RIGHT:
            
             if x < 734:              
                  x += 9
             else:
                  x = 734           
                 
          #   scr=pygame.display.set_mode((800,600))   
           #  gemi(x,M)
                     
        
                      
##             x = x + 9
            # scr=pygame.display.set_mode((800,600))   
             #gemi(x,M)

          elif event.key == pygame.K_UP:
             
             if M > 5:              
                  M=M-9
             else:
                  M = 5
             if M < 135 and M > 5:
                  M= 135    

          elif event.key == pygame.K_DOWN:

             if M < 500:              
                  M=M+9
             else:
                  M = 550
            
                
             scr=pygame.display.set_mode((800,600))   
             gemi(x,M)
                       
    
      
          if event.key == pygame.K_SPACE:
             #M = y
              #ates="vur"  
              ats()
              
               


    
    if sekil1y == 550:
       sekil1y = y1

    if sekil2y == 550:
       sekil2y = 95

    
      
                

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
        ind = -4
    if x1 <= 0:
        ind = 4
             
    x2 = x2 + ind1    
    if x2 >= 740:
        ind1 = -4
    if x2 <= 0:
        ind1 = 4

    if y< 0:
        ates="hazır"
        y = 550
        
    if sekil1y> 550:
         sekil1y = y1
    if sekil2y> 550:
         sekil2y = y2

    scr=pygame.display.set_mode((800,600))
    scr.blit(arka,(0,0))

    if sekil1y != 550:
        sekil1y=sekil1y + 9
        s= x1      
        
        pygame.draw.circle(scr, red,(s+16,sekil1y), 4)
                
        sleep(0.0026)

    if sekil2y != 550:
        sekil2y=sekil2y + 9
        s1= x2      
        
        pygame.draw.circle(scr, green,(s1+26,sekil2y), 4)
                
        sleep(0.0026)


    
    if ates=="vur":
        y = y - 5
        pygame.draw.circle(scr, aka,(x+25,y), 2)         
        sleep(0.00001)
       
      
    dusman2(x2,y2)
    dusman1(x1,y1)
    pygame.display.flip

    #y1=random.randint(50,350)

    if x > 800 or x < 0:
           
            son = True
      # print(x)     
      # print(event)
    
quit()    

