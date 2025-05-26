import pygame
from ChowColors import Colors
class Grid:#Tetris grid!
    def __init__(self):#Grid setup
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30
        self.grid=[[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors=Colors.get_cell_colors()
    def print_grid(self):#Printing how the grid looks like
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end="")
            print()
    def is_inside(self,row,column):#Determine the blocks are inside the grid or not
        if row >=0 and row<self.num_rows and column>=0 and column<self.num_cols:
            return True
        return False
    def is_empty(self,row,column):#Determine if the grid block is empty or not
        if self.grid[row][column]==0:
            return True
        return False
    def is_row_full(self,row):#Determining is the row full or not
        for column in range(self.num_cols):
            if self.grid[row][column]==0:
                return False
        return True
    def clear_row(self,row):#Clearing full rows
        for column in range(self.num_cols):
            self.grid[row][column]=0
    def move_row_down(self,row,num_rows):#Move rows down if a clear happens
        for column in range(self.num_cols):
            self.grid[row+num_rows][column]=self.grid[row][column]
            self.grid[row][column]=0
    def clear_full_rows(self):#Clearing multiple rows
        completed=0
        for row in range(self.num_rows-1, 0,-1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed+=1
            elif completed>0:
                self.move_row_down(row,completed)
        return completed
    def clear_full_rows_with_indices(self):#Bomb clears
        cleared_indices=[]
        shift=0
        for row in range(self.num_rows-1,-1,-1):
            if self.is_row_full(row):
                self.clear_row(row)
                cleared_indices.append(row)
                shift += 1
            elif shift > 0:
                self.move_row_down(row, shift)
        return cleared_indices
    def reset(self):#Reset the game
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column]=0
    def draw(self,window):#Draw the grid
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value=self.grid[row][column]
                cell_rect=pygame.Rect(column*self.cell_size+11,row*self.cell_size+11,self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(window,self.colors[cell_value],cell_rect)