import pygame,sys,os
from Twiddydinkies import AllItem as items
from Chowin import Chowin
class ChowShop:
    def __init__(self,window,chowin):
        self.window=window
        self.chowin=chowin
        self.base=os.path.dirname(__file__)
        self.assets=os.path.join(self.base,"assets")
        self.bg_image=pygame.image.load(os.path.join(self.assets,"bg.png")).convert()
        self.npc_image=pygame.image.load(os.path.join(self.assets,"NPC.png")).convert_alpha()
        self.sold_out_npc_image=pygame.image.load(os.path.join(self.assets,"Sold_out_NPC.png")).convert_alpha()
        self.sold_out_image=pygame.image.load(os.path.join(self.assets,"Sold out.png")).convert_alpha()
        self.bomb_icon=pygame.image.load(os.path.join(self.assets,"bomb.png")).convert_alpha()
        self.boost_icon=pygame.image.load(os.path.join(self.assets,"boost.png")).convert_alpha()
        self.bless_icon=pygame.image.load(os.path.join(self.assets,"blesss.png")).convert_alpha()
        self.title_font=pygame.font.Font(None,45)
        self.dialoge_font=pygame.font.Font(None,30)
        self.dialoges=[
            "You survived a level?! Impressive! You should buy something for the following levels!!"
            "You are back! I think you have a lot of Chowins now! Buy whatever you want!"
            "There is only one level ahead! I, the Conehead Zombie Prince, wish you succeed!"
            "Even if Chow Mian is not here, I will say:'If You have Chowins, use them wisely.'"
            "If you want to leave here with some chowins unused, I will take them."
            "Why are you staring at me? I am a zombie! But I will not eat your brains!"
            "You cannot read my flag? It says:'Definetely true! No FAKES!', with no BRAINS!"
            "The bomb makes you blast 3 rows in a clear, the boost makes you gain 2x clears in 10s."
            "This Chow God's Bless, I dont know what it can do, but it is powerful."
            "WHAT ARE YOU DOING?! Dont try to buy stuff when you dont have enough Chowins!"
            "You have a good taste! Wish Chow God make you complete every level!"
            "Why are you staring at that! Chow God's Bless is alreasy sold out!"
        ]
        self.current_dialogue=""
        self.dialog_index=0
    def set_dialogue(self,text):
        self.current_dialogue=text
    def draw(self,dialogue_index=None):
        self.window.blit(self.bg_image,(0,0))
        npc_rect = self.npc_image.get_rect(bottomright=(
        self.window.get_width() - 20,
        self.window.get_height() - 20
    ))
        self.window.blit(self.npc_image,npc_rect)
        title_surf = self.title_font.render("CRAZY CHOW'S TWIDDYDINKIES", True, (0,0,0))
        self.window.blit(title_surf, (5,20))
        y=120
        self.window.blit(self.bomb_icon, (20,y))
        txt = f"Left – Bomb (4) x{items[0].count}"
        surf = self.dialoge_font.render(txt, True, (255,255,255))
        self.window.blit(surf, (70,y+8))
        y += 50
        self.window.blit(self.boost_icon, (20,y))
        txt = f"Up    – Boost (5) x{items[1].count}"
        surf = self.dialoge_font.render(txt, True, (255,255,255))
        self.window.blit(surf, (70,y+8))
        y += 50
        self.window.blit(self.bless_icon, (20,y))
        txt = f"Right – Bless (50) {'✔' if items[2].count>0 else ''}"
        surf = self.dialoge_font.render(txt, True, (255,255,255))
        self.window.blit(surf, (70,y+8))
        dlg = self.dialoge_font.render(self.current_dialogue, True, (175,238,238))
        dlg_rect = dlg.get_rect(center=(self.window.get_width()//2, self.window.get_height()-40))
        self.window.blit(dlg, dlg_rect)
        pygame.display.flip()