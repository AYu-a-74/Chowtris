from ChowColors import Colors
import pygame
class Block:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.cell_size=60
        self.rotation_state=0
        self.colors=Colors.get_cell_colors()
    def draw(self,window):
        tiles=self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect=pygame.Rect(tile.column*self.cell_size+1,tile.row*self.cell_size+1,self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(window,self.colors[self.id],tile_rect)