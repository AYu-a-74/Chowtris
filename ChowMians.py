from ChowColors import Colors
import pygame
from XYZs import Position
class Block:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.cell_size=60
        self.row_offset=0
        self.column_offset=0
        self.rotation_state=0
        self.colors=Colors.get_cell_colors()
    def move(self,rows,columns):
        self.row_offset+=rows
        self.column_offset+=columns
    def get_cell_positions(self):
        tiles=self.cells[self.rotation_state]
        moved_tiles=[]
        for position in tiles:
            position=Position(position.row+self.row_offset, position.column+self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    def draw(self,window):
        tiles=self.get_cell_positions()
        for tile in tiles:
            tile_rect=pygame.Rect(tile.column*self.cell_size+1,tile.row*self.cell_size+1,self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(window,self.colors[self.id],tile_rect)