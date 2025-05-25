import pygame
from ChowRayTube import Grid
from TheRealChows import *
import random

class VanYouSeee:
    def __init__(self):
        self.grid=Grid()
        self.blocks=[IChow(), JChow(), LChow(), OChow(), SChow(), ZChow(), Tam()]
        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()
        self.game_over=False
        self.lines_cleared_current_level = 0
        self.bomb_active=False
        self.boost_active=False
        self.boost_end_time=0
        self.bless_active=False
    def get_random_block(self):
        if len(self.blocks)==0:
            self.blocks=[IChow(), JChow(), LChow(), OChow(), SChow(), ZChow(), Tam()]
        block=random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    def activate_bomb(self):
        self.bomb_active=True
    def activate_boost(self,duration_ms):
        self.boost_active=True
        self.boost_end_time=pygame.time.get_ticks()+duration_ms
    def activate_bless(self):
        self.bless_active=True
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside()== False or self.block_fits()==False:
            self.current_block.move(0,1)
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside()== False or self.block_fits()==False:
            self.current_block.move(0,-1)
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside()== False or self.block_fits()==False:
            self.current_block.move(-1,0)
            self.lock_block() 
    def lock_block(self):
        tiles=self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column]=self.current_block.id
        cleared=self.grid.clear_full_rows()
        if self.bomb_active:
            if cleared<3:
                cleared=3
            self.bomb_active=False
        now=pygame.time.get_ticks()
        if self.boost_active:
            if now<=self.boost_end_time:
                cleared*=2
            else:
                self.boost_active=False
        self.lines_cleared_current_level+=cleared
        self.current_block=self.next_block
        self.next_block=self.get_random_block()
        if self.block_fits()==False:
            if self.bless_active==True:
                self.bless_active=False
            else:
                self.game_over=True
    def reset(self):
        self.grid.reset()
        self.blocks=[IChow(), JChow(), LChow(), OChow(), SChow(), ZChow(), Tam()]
        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()
        self.game_over=False
        self.lines_cleared_current_level=0
        self.bomb_active=False
        self.boost_active=False
    def block_fits(self):
        tiles=self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row,tile.column)==False:
                return False
        return True
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.undo_rotation()
    def block_inside(self):
        tiles=self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column)==False:
                return False
        return True
    def draw(self,window):
        self.grid.draw(window)
        self.current_block.draw(window,11,11)
        if self.next_block.id==6:
            self.next_block.draw(window,255,290)
        elif self.next_block.id==1:
            self.next_block.draw(window,255,280)
        else:
            self.next_block.draw(window,270,270)