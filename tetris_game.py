from tetris_grid import Grid
from tetris_blocks import *
import random
import pygame

class Game:
    #gets the drawing of the board, the diffrent blocks aswell as the sounds and weather or not the game is over  
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("sounds/clear.ogg")
    
    #when you clear a line, depending on moving the block down or how many rows you cleared (up to 4 at once) 
    #this is how the score is determened 
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 1000
        self.score += move_down_points

    #gets the 7 blocks in the tetris_blocks.py file and will select a random block
    #when all blocks are used it resets the blocks  
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    #moves the block left and if its an illigal move it resets 
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    #moves the block right and if its an illigal move it resets 
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    #moves the block down and if it interacts with a filled cell (has value > 0) 
    #it undos the move and uses anouther function to lock the block in place 
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    #locks the new block in place aswell loads new block and new preview of following block to come 
    #clears rows and updates score, when a new block is loaded in if it doesnt fit (interacts with a cell > 0)
    #the gmae will end
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows() 
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    #uses functions in outher files to reset the game board and score to start the game again 
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    #checks to see if the block fits (doesnt hit a cell > 0)
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    #rotates the block and if it cant be done cause it goes out the board or is going to hit anouther piece 
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    #makes sure all blocks are in the games boundrys 
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    #draws the games board play area and preview screen for nex block 
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)