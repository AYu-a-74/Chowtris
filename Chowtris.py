import pygame,sys#Van You See itself
from VanYouSee import VanYouSeee
import random#random spawn
import time#Timer
RE=(600, 1200)#Limits of Van You See
def Chowtris():
    pygame.init()
    ChowTrisssss=((44,44,177))
    OrigChow=(100,100,100)
    BaldChow=(0,0,200)
    OldChow=(135,0,0)
    ThiefChow=(135,0,135)
    PoliceChow=(175,175,0)
    YoungChow=(0,175,0)
    window = pygame.display.set_mode(RE)
    pygame.display.set_caption("Forceful Tetris")
    running = True
    Chowseconds=pygame.time.Clock()
    vanyousee=VanYouSeee()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False#Quit Van You See
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    vanyousee.move_left()
                if event.key==pygame.K_d:
                    vanyousee.move_right()
                if event.key==pygame.K_s:
                    vanyousee.move_down()
        window.fill(ChowTrisssss)
        vanyousee.draw(window)
       
        pygame.display.update()
        Chowseconds.tick(60)
Chowtris()