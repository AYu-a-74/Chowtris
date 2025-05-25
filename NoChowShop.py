import pygame,sys,os
from Twiddydinkies import AllItem as items
from Chowin import Chowin
class ChowShop:
    def __init__(self,window,chowin):
        self.window=window
        self.chowin=chowin
        self.base=os.path.dirname(__file__)
        self.assets=os.path.join(self.base,"assets")
        icon_size=(100,100)
        zombie_size=(500,500)
        npc_size=(770,550)
        bomb_raw=pygame.image.load(os.path.join(self.assets,"bomb.png")).convert_alpha()
        boost_raw=pygame.image.load(os.path.join(self.assets,"boost.png")).convert_alpha()
        bless_raw=pygame.image.load(os.path.join(self.assets,"blesss.png")).convert_alpha()
        npc_raw=pygame.image.load(os.path.join(self.assets,"NPC.png")).convert_alpha()
        self.bg_image=pygame.image.load(os.path.join(self.assets,"bg.png")).convert()
        self.npc_image=pygame.transform.scale(npc_raw, npc_size)
        self.sold_out_npc_image=pygame.image.load(os.path.join(self.assets,"Sold_out_NPC.png")).convert_alpha()
        self.sold_out_image=pygame.image.load(os.path.join(self.assets,"Sold out.png")).convert_alpha()
        self.bomb_icon=pygame.transform.scale(bomb_raw, icon_size)
        self.boost_icon=pygame.transform.scale(boost_raw, icon_size)
        self.bless_icon=pygame.transform.scale(bless_raw, zombie_size)
        self.title_font=pygame.font.Font(None,45)
        self.dialoge_font=pygame.font.Font(None,30)
        self.dialoges={
            "Finish":"You survived a level?! Impressive! You should\n buy something for the following levels!!",
            "Finish_4":"You are back! I think you have a lot of\n Chowins now! Buy whatever you want!",
            "Finish_7":"There is only one level ahead! I, the\n Conehead Zombie Prince, wish you succeed!",
            "T_1":"Even if Chow Mian is not here, I will say:\n'If You have Chowins, use them wisely.'",
            "T_2":"If you want to leave here with\n some chowins unused, I will take them.",
            "T_3":"Why are you staring at me? I am a zombie!\n But I will not eat your brains!",
            "T_4":"You cannot read my flag? It says:\n'Definetely true! No FAKES!', with no BRAINS!",
            "T_5":"The bomb makes you blast 3 rows in a clear,\n the boost makes you gain 2x clears in 10s.",
            "T_without_bless":"This Chow God's Bless, I dont know\n what it can do, but it is powerful.",
            "too_poor":"WHAT ARE YOU DOING?! Dont try to buy stuff\n when you dont have enough Chowins!",
            "buy_bless":"You have a good taste! Wish Chow God\n make you complete every level!",
            "buy_after_bless":"Why are you staring at that!\n Chow God's Bless is alreasy sold out!"
        }
        self.current_dialogue=""
        self.talk_keys_before=["T_1","T_2","T_3","T_4","T_5","T_without_bless"]
        self.talk_keys_after=["T_1","T_2","T_3","T_4","T_5"]
        self.talk_index=0
        self.BOMB_POS  = (60, 445)
        self.BOOST_POS = (160, 445)
        self.BLESS_POS = (-95, 175)
    def set_dialogue(self,key):
        self.current_dialogue=self.dialoges.get(key,"")
    def cycle_talk(self):
        if items[2].count>0:
            keys=self.talk_keys_after
        else:
            keys=self.talk_keys_before
        self.talk_index=(self.talk_index+1)%len(keys)
        key = keys[self.talk_index]
        self.current_dialogue = self.dialoges.get(key,"")
    def draw(self):
        w, h = self.window.get_size()
        self.window.blit(self.bg_image,(0,0))
        npc_pos = (30, 180)
        npc_rect = self.npc_image.get_rect(topleft=npc_pos)
        self.window.blit(self.npc_image, npc_rect)
        title_surf = self.title_font.render("CRAZY CHOW'S TWIDDYDINKIES", True, (0,0,177))
        self.window.blit(title_surf, (5,20))
        coin_surf=self.dialoge_font.render(f"Choins: {self.chowin.total}", True, (200,200,0))
        self.window.blit(coin_surf,(395,50))
        self.window.blit(self.bomb_icon, (self.BOMB_POS))
        txt = f"Left – Bomb (5) x{items[0].count}"
        surf = self.dialoge_font.render(txt, True, (0,0,0))
        self.window.blit(surf, (5,150))
        self.window.blit(self.boost_icon, (self.BOOST_POS))
        txt = f"Right – Boost (4) x{items[1].count}"
        surf = self.dialoge_font.render(txt, True, (0,0,0))
        self.window.blit(surf, (5,200))
        self.window.blit(self.bless_icon, (self.BLESS_POS))
        txt = f"Up – Bless (50) {'✔' if items[2].count>0 else ''}"
        surf = self.dialoge_font.render(txt, True, (0,0,0))
        self.window.blit(surf, (5,100))
        if self.current_dialogue:
            lines=self.current_dialogue.split("\n")
            rendered=[self.dialoge_font.render(l,True,(0,0,0)) for l in lines]
            widths=[s.get_width() for s in rendered]
            heights = [s.get_height() for s in rendered]
            text_w  = max(widths)
            text_h  = sum(heights)
            padding = 8
            bubble_w = text_w + padding*2
            bubble_h = text_h + padding*2
            bubble_midbottom = (npc_rect.centerx-150, npc_rect.top +120)
            bubble_rect = pygame.Rect(0,0,bubble_w,bubble_h)
            bubble_rect.centerx = bubble_midbottom[0]
            bubble_rect.bottom  = bubble_midbottom[1]
            pygame.draw.rect(self.window, (255,255,255), bubble_rect, border_radius=6)
            pygame.draw.rect(self.window, (0,0,0), bubble_rect, 2,        border_radius=6)
            y_offset = bubble_rect.y + padding
            for surf in rendered:
                self.window.blit(surf, (bubble_rect.x + padding, y_offset))
                y_offset += surf.get_height()
        pygame.display.flip()