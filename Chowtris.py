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
    victory_surface=title_font.render("Victory!", True, (255, 255, 0))
    score_rect=pygame.Rect(320,55,170,60)
    next_rect=pygame.Rect(320,215,170,180)
    level_clear_numbers = [5, 10, 15, 20, 0, 20, 25, 30, 40]  
    level_time_limits = [30, 40, 45, 50, 30, 55, 60, 70, 90] 
    level_drop_speed = [700, 600, 500, 400, 150, 300, 250, 200, 150]
    your_level=0
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
    level_start_time = pygame.time.get_ticks()
    vanyousee=VanYouSeee()
    VANYOUSEE_UPDATE=pygame.USEREVENT
    pygame.time.set_timer(VANYOUSEE_UPDATE,level_drop_speed[your_level])
    start_transition=False
    change_start_time=0
    next_level=0
    level_change=False
    change_start_time=0
    next_level=None
    vanyousee_win=False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False#Quit Van You See
            if event.type==pygame.KEYDOWN:
                if vanyousee.game_over==True or vanyousee_win:
                    your_level=0
                    vanyousee_win=False
                    vanyousee.game_over=False
                    vanyousee.reset()
                    level_start_time=pygame.time.get_ticks()
                    pygame.time.set_timer(VANYOUSEE_UPDATE,level_drop_speed[your_level])
                    vanyousee.lines_cleared_current_level=0
                    level_change=False
                    continue
                if not level_change:

                    if event.key==pygame.K_a and vanyousee.game_over==False and not vanyousee_win and not start_transition and not level_change:
                        vanyousee.move_left()
                    if event.key==pygame.K_d and vanyousee.game_over==False and not vanyousee_win and not start_transition and not level_change:
                        vanyousee.move_right()
                    if event.key==pygame.K_s and vanyousee.game_over==False and not vanyousee_win and not start_transition and not level_change:
                        vanyousee.move_down()
                        if vanyousee.game_over and your_level==4:
                            vanyousee.game_over=False
                            level_change=True
                            change_start_time=pygame.time.get_ticks()
                            next_level=your_level+1
                    if event.key==pygame.K_e and vanyousee.game_over==False and not vanyousee_win and not start_transition and not level_change:
                        vanyousee.rotate()
            if event.type==VANYOUSEE_UPDATE and vanyousee.game_over==False and not vanyousee_win and not start_transition and not level_change:
                if vanyousee.game_over==False and not level_change and not vanyousee_win:
                    vanyousee.move_down()
                    if vanyousee.game_over and your_level==4:
                        vanyousee.game_over=False
                        level_change=True
                        change_start_time=pygame.time.get_ticks()
                        next_level=your_level+1
        if start_transition:
            time_passed = pygame.time.get_ticks() - change_start_time
            if time_passed >= 3000:
                your_level = next_level
                if your_level >= len(level_clear_numbers):
                    vanyousee_win = True
                else:
                    vanyousee.reset()
                    vanyousee.lines_cleared_current_level = 0
                    level_start_time = pygame.time.get_ticks()
                    pygame.time.set_timer(VANYOUSEE_UPDATE, level_drop_speed[your_level])
                start_transition = False
            else:
                remaining = 5 - int(time_passed / 1000)
                countdown_surface = title_font.render(f"Next Level in {remaining}...", True, (255, 255, 0))
                window.blit(countdown_surface, (330, 500))
        elif not vanyousee_win and vanyousee.game_over==False:
            current_time=pygame.time.get_ticks()
            elapsed_time=(current_time-level_start_time)/1000.0
            if your_level!=4:
                if vanyousee.lines_cleared_current_level>=level_clear_numbers[your_level]:
                    if elapsed_time<level_time_limits[your_level]:
                        level_change=True
                        change_start_time=current_time
                        if your_level<8:
                            next_level=your_level+1
                        else:
                            next_level=None
                    else:
                        if your_level<8:
                            your_level+=1
                            vanyousee.reset()
                            vanyousee.lines_cleared_current_level=0
                            level_start_time=current_time
                            pygame.time.set_timer(VANYOUSEE_UPDATE,level_drop_speed[your_level])
                        else:
                            vanyousee_win=True
                else:
                    if elapsed_time>=level_time_limits[your_level]:
                        start_transition=True
                        next_level=your_level+1
                        change_start_time=pygame.time.get_ticks()
                        vanyousee.game_over = False
            else:
                if elapsed_time>=level_time_limits[4]:
                    level_change=True
                    start_transition=True
                    change_start_time = pygame.time.get_ticks()
                    next_level = 5
        if level_change:
            current_time=pygame.time.get_ticks()
            change_elapsed=current_time-change_start_time
            if change_elapsed>=3000:
                level_change=False
                if next_level is None or next_level>8:
                    vanyousee_win=True
                else:
                    your_level=next_level
                    vanyousee.reset()
                    vanyousee.lines_cleared_current_level=0
                    level_start_time=current_time
                    pygame.time.set_timer(VANYOUSEE_UPDATE,level_drop_speed[your_level])
                next_level=None
        window.fill(ChowTrisssss)
        window.blit(score_surface,(365,20,50,50))
        window.blit(next_surface,(375,180,50,50))
        if vanyousee.game_over==True:
            window.blit(game_over_surface,(355,450,50,50))
        if vanyousee_win:
            window.blit(victory_surface,(360,450,50,50))
        if level_change or start_transition:
            seconds_left=3-int((pygame.time.get_ticks()-change_start_time)/1000)
            if next_level is None or next_level>8:
                msg = f"End of Forces in {seconds_left}..."
            else:
                msg = f"Level {next_level} in {seconds_left}s..."
            countdown_surface=title_font.render(msg, True, (255, 255, 255))
            window.blit(countdown_surface, (320, 500,50,50))
        pygame.draw.rect(window, bgc, score_rect, 0, 10)
        pygame.draw.rect(window,bgc,next_rect,0,10)
        vanyousee.draw(window)
        
       
        pygame.display.update()
        Chowseconds.tick(60)
Chowtris()