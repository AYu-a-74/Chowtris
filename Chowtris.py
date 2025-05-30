#Important message! VanYouSee means game!
# Import those critical modules!
import pygame,sys,os#Van You See itself
from pygame.mixer import Sound
from VanYouSee import VanYouSeee
from Twiddydinkies import try_use, apply_purchase, get_inventory
from Chowin import Chowin
from NoChowShop import ChowShop
import random#random spawn
import time#Timer
RE=(500, 620)#Limits of Van You See
def Chowtris():#VanYouSee itself!
    pygame.init()
    pygame.mixer.init()
    #Fonts and surfaces
    title_font=pygame.font.Font(None,40)
    score_surface=title_font.render("Forces",True,(255,255,255))
    next_surface=title_font.render("Next",True,(255,255,255))
    game_over_surface=title_font.render("Wasted!",True, (255,0,0))
    victory_surface=title_font.render("Victory!", True, (255, 255, 0))
    score_rect=pygame.Rect(320,55,170,60)
    next_rect=pygame.Rect(320,215,170,180)
    #Level stuff
    level_clear_numbers = [5, 10, 15, 20, 0, 20, 25, 30, 40] 
    #level_time_limits =[1,1,1,1,100,1,,1,2] #Only for testing
    level_time_limits = [60, 70, 80, 90, 75, 105, 120, 150, 180] 
    level_drop_speed = [700, 600, 500, 400, 150, 300, 250, 200, 150]
    your_level=0
    #Colors
    ChowTrisssss=((44,44,177))
    OrigChow=(100,100,100)
    BaldChow=(0,0,200)
    OldChow=(135,0,0)
    ThiefChow=(135,0,135)
    PoliceChow=(175,175,0)
    YoungChow=(0,175,0)
    bgc=(235,255,255)
    #Display
    window = pygame.display.set_mode(RE)
    pygame.display.set_caption("Forceful Tetris")
    #Image and Sounds
    base = os.path.dirname(__file__)
    noises=os.path.join(base,"noises")
    level_bgms=[os.path.join(noises,f"Level{i}.mp3") for i in range(9)]
    shop_bgm=os.path.join(noises,"zombie_shop.mp3")
    lose_noise = [
        Sound(os.path.join(noises, "brains.mp3")),
        Sound(os.path.join(noises, "nooo.mp3"))
    ]
    win_noise = Sound(os.path.join(noises, "winwin.mp3"))

    assets = os.path.join(base, "assets")
    bomb_raw  = pygame.image.load(os.path.join(assets, "bomb.png")).convert_alpha()
    boost_raw = pygame.image.load(os.path.join(assets, "boost.png")).convert_alpha()
    icon_size=(100,100)
    bomb_icon  = pygame.transform.scale(bomb_raw,  icon_size)
    boost_icon = pygame.transform.scale(boost_raw, icon_size)
    def play_bgm(path):
        pygame.mixer.music.load(path)
        pygame.mixer_music.play(-1)
    play_bgm(level_bgms[0])
    #Game run variables
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
    shop_countdown=False
    dialogue_index=0
    shop_open=False
    shop_exit_time=0
    God_purchase_times=0
    while running:#While game is running
        events=pygame.event.get()#Quit
        for event in events:
            if event.type==pygame.QUIT:
                running = False
        if vanyousee.bless_triggered==True:#Bless save you from failing
            vanyousee.bless_triggered = False
            pygame.time.set_timer(VANYOUSEE_UPDATE, 0)
            next_level = your_level + 1
            chowin.calculate_earnings(
                vanyousee.lines_cleared_current_level,
                your_level,
                boost_active=vanyousee.boost_active
                        )
            shop.set_dialogue("Finish")
            shop_open = True
            pygame.mixer.music.fadeout(500)
            play_bgm(shop_bgm)
            shop_countdown = False
            shop_exit_time = pygame.time.get_ticks()
            continue
        if shop_open:#Entering shop
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:#Leave
                        shop_open=False
                        shop_countdown=True
                        shop_exit_time=pygame.time.get_ticks()
                    elif event.key==pygame.K_t:#Talk
                        shop.cycle_talk()
                    elif event.key==pygame.K_LEFT:#Buy bomb
                        if chowin.try_spend(5):
                            apply_purchase("bomb")
                        else:
                            shop.set_dialogue("too_poor")
                    elif event.key==pygame.K_RIGHT:#Buy boost
                        if chowin.try_spend(4):
                            apply_purchase("boost")
                        else:
                            shop.set_dialogue("too_poor")
                    elif event.key==pygame.K_UP:#Buy Bless
                        if God_purchase_times==0:
                            if chowin.try_spend(50):
                                apply_purchase("bless")
                                vanyousee.activate_bless()
                                God_purchase_times=1
                                shop.set_dialogue("buy_bless")
                            else:
                                shop.set_dialogue("too_poor")
                        else:
                            shop.set_dialogue("buy_after_bless")
            shop.draw()
            Chowseconds.tick(30)
            continue
            
        if next_level is not None:#Exiting shop
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
                    play_bgm(level_bgms[your_level])
                next_level=None
            Chowseconds.tick(60)
            continue
        for event in events:#Key events
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    vanyousee.move_left()
                elif event.key == pygame.K_d:
                    vanyousee.move_right()
                elif event.key == pygame.K_s:
                    vanyousee.move_down()
                    if vanyousee.game_over:#Losing
                        if your_level == 4:#Losing level 4
                            vanyousee.game_over = False
                            chowin.calculate_earnings(vanyousee.lines_cleared_current_level, your_level,boost_active=vanyousee.boost_active)
                            shop.set_dialogue("Finish_4")
                            next_level = your_level + 1
                            shop_open = True
                            pygame.mixer.music.fadeout(500)
                            play_bgm(shop_bgm)
                            shop_countdown= False
                            shop_exit_time= pygame.time.get_ticks()
                        if vanyousee.game_over and not vanyousee.bless_triggered:#Normal lose
                            pygame.mixer.music.fadeout(500)
                            lose_noise[0].play()
                            time.sleep(1)
                            lose_noise[1].play()
                            window.fill(ChowTrisssss)
                            vanyousee.draw(window)
                            window.blit(game_over_surface, (355, 450))
                            pygame.display.update()
                            pygame.time.set_timer(VANYOUSEE_UPDATE, 0)
                            waiting = True#Waiting for your key to restart
                            while waiting:
                                ev = pygame.event.wait()
                                if ev.type in (pygame.KEYDOWN, pygame.QUIT):
                                    waiting = False
                                    if ev.type == pygame.QUIT:
                                        running = False
                            your_level = 0
                            vanyousee_win = False
                            vanyousee.reset()
                            play_bgm(level_bgms[0])
                            level_start_time = pygame.time.get_ticks()
                            pygame.time.set_timer(VANYOUSEE_UPDATE, level_drop_speed[your_level])
                            continue
                elif event.key == pygame.K_e:
                    vanyousee.rotate()
                elif event.key == pygame.K_1 and try_use("bomb"):
                    vanyousee.activate_bomb()
                elif event.key == pygame.K_2 and try_use("boost"):
                    vanyousee.activate_boost(10000)
                elif event.key == pygame.K_3 and try_use("bless"):
                    vanyousee.activate_bless()
            elif event.type == VANYOUSEE_UPDATE:#Auto drop
                vanyousee.move_down()
                if vanyousee.game_over:
                    if your_level==4:
                        vanyousee.game_over=False
                        chowin.calculate_earnings(vanyousee.lines_cleared_current_level, your_level,boost_active = vanyousee.boost_active)
                        shop.set_dialogue("Finish_4")
                        next_level = your_level + 1
                        shop_open= True
                        pygame.mixer.music.fadeout(500)
                        play_bgm(shop_bgm)
                        shop_countdown = False
                        shop_exit_time = pygame.time.get_ticks()
                    if vanyousee.game_over and not vanyousee.bless_triggered:
                        pygame.mixer.music.fadeout(500)
                        lose_noise[0].play()
                        time.sleep(1)
                        lose_noise[1].play()
                        window.fill(ChowTrisssss)
                        vanyousee.draw(window)
                        window.blit(game_over_surface, (355, 450))
                        pygame.display.update()
                        pygame.time.set_timer(VANYOUSEE_UPDATE, 0)
                        waiting = True
                        while waiting:
                            ev = pygame.event.wait()
                            if ev.type in (pygame.KEYDOWN, pygame.QUIT):
                                waiting = False
                                if ev.type == pygame.QUIT:
                                    running = False
                        your_level = 0
                        vanyousee_win = False
                        vanyousee.reset()
                        play_bgm(level_bgms[0])
                        level_start_time = pygame.time.get_ticks()
                        pygame.time.set_timer(VANYOUSEE_UPDATE, level_drop_speed[your_level])
                        continue
        if not shop_open and next_level is None and not vanyousee.game_over and not vanyousee_win:#Game running
            now = pygame.time.get_ticks()
            elapsed_sec = (now - level_start_time) / 1000.0
            lines = vanyousee.lines_cleared_current_level
            clear_target = level_clear_numbers[your_level]
            time_limit= level_time_limits[your_level]
            if (clear_target>0 and lines>=clear_target) or elapsed_sec>=time_limit:#If you meet requirements
                if your_level==len(level_clear_numbers)-1:#Level 8 finishing
                    vanyousee_win=True
                    pygame.time.set_timer(VANYOUSEE_UPDATE,0)
                    continue
                next_level=your_level+1
                chowin.calculate_earnings(lines,your_level,boost_active = vanyousee.boost_active)
                if your_level in (0,1,2,3,5,6):
                    shop.set_dialogue("Finish")
                elif your_level == 4:
                    shop.set_dialogue("Finish_4")
                elif your_level == 7:
                    shop.set_dialogue("Finish_7")
                shop_open=True
                pygame.mixer.music.fadeout(500)
                play_bgm(shop_bgm)
                shop_countdown=False
                shop_exit_time=0
                continue
            if elapsed_sec>=time_limit:#Survived the required time
                if your_level==len(level_clear_numbers)-1:
                    vanyousee_win=True
                    pygame.time.set_timer(VANYOUSEE_UPDATE,0)
                    continue
                next_level=your_level+1
                chowin.calculate_earnings(lines,your_level,boost_active = vanyousee.boost_active)
                shop_open=True
                pygame.mixer.music.fadeout(500)
                play_bgm(shop_bgm)
                continue
        if start_transition:#Game run, but rarely used
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
        #Display update
        window.fill(ChowTrisssss)
        window.blit(score_surface,(365,20,50,50))
        window.blit(next_surface,(375,180,50,50))
        current_time   = pygame.time.get_ticks()
        elapsed_level  = (current_time - level_start_time) / 1000.0
        remaining_secs = max(0, int(level_time_limits[your_level] - elapsed_level))
        time_surf      = title_font.render(f"Time: {remaining_secs}s", True, (255,255,255))
        window.blit(time_surf, (345, 135))
        if vanyousee_win:#Winning
            pygame.mixer.music.stop()
            win_noise.play()
            window.fill(ChowTrisssss)
            vanyousee.draw(window)
            window.blit(victory_surface, (360, 450))
            pygame.display.update()
            waiting = True
            while waiting:
                ev = pygame.event.wait()
                if ev.type in (pygame.KEYDOWN, pygame.QUIT):
                    waiting = False
                    if ev.type == pygame.QUIT:
                        running = False
            your_level = 0
            vanyousee_win = False
            vanyousee.reset()
            play_bgm(level_bgms[0])
            level_start_time = pygame.time.get_ticks()
            pygame.time.set_timer(VANYOUSEE_UPDATE, level_drop_speed[your_level])
            continue
        #More display update
        pygame.draw.rect(window, bgc, score_rect, 0, 10)
        pygame.draw.rect(window,bgc,next_rect,0,10)
        lines_text = f"{vanyousee.lines_cleared_current_level}"
        lines_surf = title_font.render(lines_text, True, (0,0,0))
        window.blit(lines_surf, (400, 73))
        vanyousee.draw(window)
        #Bliting the items
        inv=get_inventory()
        bomb_count  = inv["bomb"]
        boost_count = inv["boost"]
        bomb_pos  = (320, 420)
        boost_pos = (320, 500)
        window.blit(bomb_icon,  bomb_pos)
        window.blit(boost_icon, boost_pos)
        count_surf = title_font.render(str(bomb_count),  True, (255,255,255))
        window.blit(count_surf, (390, 480))

        count_surf = title_font.render(str(boost_count), True, (255,255,255))
        window.blit(count_surf, (390, 560))
        pygame.display.update()
        Chowseconds.tick(60)
def Intro():#Introduction of the VanYouSee, in the terminal
    os.system('cls')#For Windows
    #os.system('clear') #For Apple
    print("Important message!\n")
    time.sleep(1)
    print("This is an 'original' Tetris game\n!")
    time.sleep(1)
    print("There are 9 levels in the game, Level 0 to Level 8!\nYou complete a level either by clearing enough lines, or surviving through the time given!\nThe block's falling speed will increase each level! Level 4 and Level 8 are the quickest!\n Failing those levels makes you lose the game! But Failing Level 4 does not!\nEach time you pass a level, you will go to a shop with a zombie NPC inside!\nThe zombie NPC will sell you powerful items to help you succeed in the game!\nYou will receive Chowins once you complete a level! Quadruple Chowins for completing Level 4!\nYou use Chowins to buy items in the shop!\nBomb costs 5 Chowins! Clear Boost causes 4 Chowins! Chow God's Bless costs 50 Chowins!\nBe aware! You Chowins will be cleared to 0 once you leave the shop! So buy items as much as you can!\nYou enter the next level once you exits the shop! and you can use your newly bought items!\n")
    time.sleep(10)
    print("Keys for the game:\n'A' for moving the block left!\n'D' for moving the block right!\n'S' for moving the block down faster!\n'E' for rotating the block!\n'1' for using the bomb item!\n'2' for using the clear boost item!\n")
    time.sleep(3)
    print("Keys for the shop:\n'T' for talking with the NPC zombie!\n'Q' for exiting the shop!\n'Left_arrow' for purchasing the bomb item!\n'Right_arrow' for purchasing the clear boost item!\n'Up_arrow' for purchasing the Chow God's Bless item!\n")
    time.sleep(3)
    print("Item information:\n'Bomb': When activated, your next line clear can destroy 2 rows above the actual line clear you made!\n'Clear boost': When activated, your clears made in the next 10 seconds will be doubled!\n'Chow God's Bless': When you have this item and loses a level, this item will save you from losing the game,\nmaking you complete that level instantly, and send you to the shop!\n You can only buy this item once from the shop!\n")
    time.sleep(5)
    print("After you pass level 8, you win!\nIf your blocks are stuck to the top, you lose!\n You will not lose the game if you fail Level 4,\nor if you fail a level with Chow God's Bless in hand!\n")
    time.sleep(2)
    print("Good Luck from saving you from FORCES!")
    time.sleep(1)
Intro()#Introduce the VanYouSee
Chowtris()#Start the VanYouSee