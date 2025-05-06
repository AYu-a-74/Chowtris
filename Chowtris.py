import pygame,sys#Van You See itself
from ChowRayTube import Grid
from TheRealChows import *
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
    game_grid=Grid()
    Chow1=LChow()
    Chow2=JChow()
    Chow3=IChow()
    Chow4=OChow()
    Chow5=SChow()
    Chow6=ZChow()
    Chow7=Tam()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False#Quit Van You See
        window.fill(ChowTrisssss)
        game_grid.draw(window)
        #Chow1.draw(window)
        #Chow2.draw(window)
        #Chow3.draw(window)
        #Chow4.draw(window)
        #Chow5.draw(window)
        #Chow6.draw(window)
        #Chow7.draw(window)
        pygame.display.update()
        Chowseconds.tick(60)
Chowtris()