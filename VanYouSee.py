from ChowRayTube import Grid
from TheRealChows import *
import random

class VanYouSeee:
    def __init__(self):
        self.grid=Grid()
        self.blocks=[IChow(), JChow(), LChow(), OChow(), SChow(), ZChow(), Tam()]
        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()
    def get_random_block(self):
        if len(self.blocks)==0:
            self.blocks=[IChow(), JChow(), LChow(), OChow(), SChow(), ZChow(), Tam()]
        block=random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside()== False:
            self.current_block.move(0,1)
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside()== False:
            self.current_block.move(0,-1)
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside()== False:
            self.current_block.move(-1,0)
    def block_inside(self):
        tiles=self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column)==False:
                return False
            return True
    def draw(self,window):
        self.grid.draw(window)
        self.current_block.draw(window)