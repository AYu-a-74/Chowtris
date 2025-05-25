import pygame,sys#Van You See itself
from VanYouSee import VanYouSeee
from Twiddydinkies import try_use, apply_purchase, get_inventory
from Chowin import Chowin
from NoChowShop import ChowShop
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
    level_time_limits = [3, 40, 45, 50, 30, 55, 60, 70, 90] 
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
    chowin=Chowin()
    shop=ChowShop(window,chowin)
    dialogue_index=0
    shop_open=False
    shop_exit_time=0
    God_purchase_times=0
    while running:
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                running = False
        if shop_open:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        shop_open=False
                        chowin.reset()
                        shop_exit_time=pygame.time.get_ticks()
                    elif event.key==pygame.K_t:
                        dialogue_index=(dialogue_index + 1) % len(shop.get_dialogues())
                    elif event.key==pygame.K_LEFT:
                        if chowin.try_spend(5):
                            apply_purchase("bomb")
                    elif event.key==pygame.K_RIGHT:
                        if chowin.try_spend(4):
                            apply_purchase("boost")
                    elif event.key==pygame.K_UP:
                        if God_purchase_times==0:
                            if chowin.try_spend(50):
                                apply_purchase("bless")
                                God_purchase_times=1
                        else:
                            print("No")
            shop.draw()
            Chowseconds.tick(30)
            continue
            
        if next_level is not None:
            elapsed=pygame.time.get_ticks()-shop_exit_time
            window.fill(ChowTrisssss)
            cnt=max(0, 3 - int(elapsed/1000))
            text=title_font.render(f"Next Level in {cnt}...", True,(255,255,255))
            window.blit(text,(150,300))
            pygame.display.update()
            if elapsed>=3000:
                if next_level is None or next_level >= len(level_clear_numbers):
                    vanyousee_win = True
                else:
                    your_level = next_level
                    vanyousee.reset()
                    vanyousee.lines_cleared_current_level = 0
                    level_start_time = pygame.time.get_ticks()
                    pygame.time.set_timer(VANYOUSEE_UPDATE, level_drop_speed[your_level])
                next_level=None
            Chowseconds.tick(60)
            continue
        for event in events:
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    vanyousee.move_left()
                elif event.key == pygame.K_d:
                    vanyousee.move_right()
                elif event.key == pygame.K_s:
                    vanyousee.move_down()
                elif event.key == pygame.K_e:
                    vanyousee.rotate()
                elif event.key == pygame.K_1 and try_use("bomb"):
                    vanyousee.activate_bomb()
                elif event.key == pygame.K_2 and try_use("boost"):
                    vanyousee.activate_boost(10000)
                elif event.key == pygame.K_3 and try_use("bless"):
                    vanyousee.activate_bless()
            elif event.type == VANYOUSEE_UPDATE:
                vanyousee.move_down()
                if vanyousee.game_over and your_level==4:
                    vanyousee.game_over=False
                    level_change=True
                    change_start_time=pygame.time.get_ticks()
                    next_level=your_level+1
        if not shop_open and next_level is None and not vanyousee.game_over and not vanyousee_win:
            now = pygame.time.get_ticks()
            elapsed_sec = (now - level_start_time) / 1000.0
            lines = vanyousee.lines_cleared_current_level
            clear_target = level_clear_numbers[your_level]
            time_limit    = level_time_limits[your_level]
            if clear_target>0 and lines>=clear_target:
                next_level=your_level+1 if your_level < 8 else None
                chowin.calculate_earnings(lines,your_level)
                shop_open=True
                dialogue_index=0
                continue
            if elapsed_sec>=time_limit:
                next_level=your_level+1 if your_level < 8 else None
                chowin.calculate_earnings(lines,your_level)
                shop_open=True
                dialogue_index=0
                continue
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
                        start_transition=True
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