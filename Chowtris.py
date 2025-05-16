import pygame,sys#Van You See itself
from VanYouSee import VanYouSeee
import random#random spawn
import time#Timer
RE=(500, 620)#Limits of Van You See
def Chowtris():
    pygame.init()
    title_font=pygame.font.Font(None,40)
    score_surface=title_font.render("Forces",True,(255,255,255))
    next_surface=title_font.render("Next",True,(255,255,255))
    game_over_surface=title_font.render("Wasted!",True, (255,0,0))
    score_rect=pygame.Rect(320,55,170,60)
    next_rect=pygame.Rect(320,215,170,180)
    
    ChowTrisssss=((44,44,177))
    OrigChow=(100,100,100)
    BaldChow=(0,0,200)
    OldChow=(135,0,0)
    ThiefChow=(135,0,135)
    PoliceChow=(175,175,0)
    YoungChow=(0,175,0)
    bgc=(235,255,255)
    window = pygame.display.set_mode(RE)
    pygame.display.set_caption("Forceful Tetris")
    running = True
    Chowseconds=pygame.time.Clock()
    vanyousee=VanYouSeee()
    VANYOUSEE_UPDATE=pygame.USEREVENT
    pygame.time.set_timer(VANYOUSEE_UPDATE,500)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False#Quit Van You See
            if event.type==pygame.KEYDOWN:
                if vanyousee.game_over==True:
                    vanyousee.game_over=False
                    vanyousee.reset()
                if event.key==pygame.K_a and vanyousee.game_over==False:
                    vanyousee.move_left()
                if event.key==pygame.K_d and vanyousee.game_over==False:
                    vanyousee.move_right()
                if event.key==pygame.K_s and vanyousee.game_over==False:
                    vanyousee.move_down()
                if event.key==pygame.K_e and vanyousee.game_over==False:
                    vanyousee.rotate()
            if event.type==VANYOUSEE_UPDATE and vanyousee.game_over==False:
                vanyousee.move_down()
        window.fill(ChowTrisssss)
        window.blit(score_surface,(365,20,50,50))
        window.blit(next_surface,(375,180,50,50))
        if vanyousee.game_over==True:
            window.blit(game_over_surface,(355,450,50,50))
        pygame.draw.rect(window, bgc, score_rect, 0, 10)
        pygame.draw.rect(window,bgc,next_rect,0,10)
        vanyousee.draw(window)
        
       
        pygame.display.update()
        Chowseconds.tick(60)
Chowtris()