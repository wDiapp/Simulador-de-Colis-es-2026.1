#Thales Weigert Diapp (RA: 2877643)

import pygame
from random import randint
from math import sqrt
 
pygame.init()

larg, alt = 900, 700
White = (255, 255, 255)
Black = (0, 0, 0)
nBolas = 6

run = True 
clock = pygame.time.Clock()
Display = pygame.display.set_mode((larg, alt))

class Bola:
    def __init__(self, x, y, vx, vy, r):
        self.x, self.y, self.vx, self.vy, self.r = x, y, vx, vy, r

    def movimento(self):
        self.x += self.vx
        self.y += self.vy
          
        if(self.x+self.r>=larg):
            self.vx *= -1
        elif(self.x<self.r):
            self.vx *= -1

        if(self.y+self.r>=alt):
            self.vy *= -1
        elif(self.y<self.r):
            self.vy *= -1

    def desBola(self):
        pygame.draw.circle(Display, White, (self.x , self.y), self.r)

def temColisao(b1, b2):
    distx = b1.x - b2.x
    disty = b1.y - b2.y
    distTotal = sqrt(distx**2 + disty**2)

    if distTotal == 0:
        distTotal = 0.1

    if(distTotal < b1.r + b2.r):
        b1.vx, b2.vx = b2.vx, b1.vx
        b1.vy, b2.vy = b2.vy, b1.vy

        erro = b1.r + b2.r - distTotal

        nx = distx / distTotal
        ny = disty / distTotal

        correcao = (erro) * 0.5

        b1.x += nx * correcao
        b2.x -= nx * correcao
        b1.y += ny * correcao
        b2.y -= ny * correcao

        if b1.x - b1.r < 0: 
            b1.x = b1.r
        elif b1.x + b1.r > larg: 
            b1.x = larg - b1.r
        if b1.y - b1.r < 0: 
            b1.y = b1.r
        elif b1.y + b1.r > alt: 
            b1.y = alt - b1.r

        if b2.x - b2.r < 0: 
            b2.x = b2.r
        elif b2.x + b2.r > larg: b2.x = larg - b2.r
        if b2.y - b2.r < 0: 
            b2.y = b2.r
        elif b2.y + b2.r > alt: 
            b2.y = alt - b2.r
 
bolas = []
for i in range(nBolas):
    r = randint(20, 40)
    bolas.append(Bola (randint(r, larg-r), randint(r, alt-r), randint(1,4), randint(1,4), randint(20,40)))




while(run):
    clock.tick(100)
    Display.fill(Black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(nBolas):   
        bolas[i].desBola()     
        bolas[i].movimento()
        
        for i in range(nBolas):
            for j in range(i + 1, nBolas):            
                temColisao(bolas[i], bolas[j])
        
            

    

    
    pygame.display.update()

pygame.quit()





