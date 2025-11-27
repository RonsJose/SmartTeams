from tetris_color import Color
import pygame
from tetris_position import Position

class Block:
    #this is how the blocks are id'ed and is used in relation to their roatation aswell
    def __init__(self, id):
        self.id = id #each block has an id (1-7)
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.color = Color.get_cell_colors()

    #moves the block using its row and column offset 
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    #gets the celss position for current rotation and applis the new offset and 
    #returns the position of the 4 cells 
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)  
            moved_tiles.append(position)
        return moved_tiles     

    #rotates the blocks to its new rotation state
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    #if the rotation takes the cell out of bounds or will move the cells into a stationary cell
    #the function will revert the rotation to the last rotation state 
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    #draws each tile f the blocks to the board in its assigned color 
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.color[self.id], tile_rect)