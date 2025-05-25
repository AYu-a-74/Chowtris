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
        self.bomb_image=pygame.image.load(os.path.join(self.assets,"bomb.png")).convert_alpha()
        self.boost_image=pygame.image.load(os.path.join(self.assets,"boost.png")).convert_alpha()
        self.bless_image=pygame.image.load(os.path.join(self.assets,"bless.png")).convert_alpha()
        self.title_font=pygame.font.Font(None,50)
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
        self.dialog_index=0
    def draw(self,dialogue_text):
        self.window.blit(self.bg_image,(0,0))
        npc_rect = self.npc_image.get_rect(bottomright=(
        self.window.get_width() - 20,
        self.window.get_height() - 20
    ))
        self.window.blit(self.npc_image,npc_rect)