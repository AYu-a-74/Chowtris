import pygame,sys
from Twiddydinkies import AllItem as items
from Chowin import Chowin
class ChowShop:
    def __init__(self,window,chowin):
        self.window=window
        self.chowin=chowin
        self.title_font=pygame.font.Font(None,50)
        self.dialoge_font=pygame.font.Font(None,30)
        self.dialoges=[
            "You survived a level?! Impressive! You should buy something for the following levels!!"
            "You are back! I think you have a lot of Chowins now! Buy whatever you want!"
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
    def draw(self,dialogue_index):
        self.window.fill((0,0,0))
        title_surface=self.title_font.render("CRAZY CHOW'S TWIDDYDINKIES",True,(255,255,255))
        title_rect=title_surface.get_rect(center=(self.window.get_width()//2,50))
        self.window.blit(title_surface,title_rect)
        coin_text = f"Chowins: {self.chowin.total}"
        coin_surface = self.dialoge_font.render(coin_text, True, (255, 255, 0))
        coin_rect = coin_surface.get_rect(topright=(self.window.get_width() - 20, 10))
        self.window.blit(coin_surface, coin_rect)
        item_texts=[
            f"Left Arrow - {items[0].name} (Cost: {items[0].cost}) [Owned: {items[0].count}]",
            f"Up Arrow - {items[1].name} (Cost: {items[1].cost}) [Owned: {items[1].count}]",
            f"Right Arrow - {items[2].name} (Cost: {items[2].cost}) [Owned: {items[2].count}]"
        ]
        start_y=150
        for text in item_texts:
            text_surface = self.dialoge_font.render(text, True, (255, 255, 255))
            self.window.blit(text_surface, (50, start_y))
            start_y += 40
        dialogue_surface=self.dialoge_font.render(self.dialoges[dialogue_index],True,(175,238,238))
        dialogue_rect=dialogue_surface.get_rect(center=(self.window.get_width()//2,580))
        self.window.blit(dialogue_surface,dialogue_rect)
        pygame.display.flip()
        def get_dialogues(self):
            return self.dialogues