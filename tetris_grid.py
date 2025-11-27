import pygame
from tetris_color import Color

class Grid:
    #sets the size of the tetris board and the size of square
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Color.get_cell_colors()

    #prints the grid on the console
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    #used to check in the piece is still inside the board boundry
    def is_inside(self, row, column):
        if row >=0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    #checks to see if a cell is empy in the row and colume (has a value of 0)
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    #checks to see if a row is full (has a value > 0)
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    #clears the row if all cells in that row have a value > 0
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    #this is used after clear_row() it moves all rows above the cleared row down by 1 row 
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    #this function uses the above three functions and excecutes them if required 
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows -1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    #when you have a game over and replay this function sets all cells to 0 (clear the board)
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
    
    #this function draws the board and sets the color of the board 
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +11, row*self.cell_size +11, 
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)