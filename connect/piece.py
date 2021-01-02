import pygame
from .constants import SQUARE_SIZE, RADIUS

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x, self.y = 0,0
        self.get_x_y()
    
    def get_x_y(self):
        self.x = self.col*SQUARE_SIZE + SQUARE_SIZE//2
        self.y = self.row*SQUARE_SIZE + SQUARE_SIZE//2

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), RADIUS)
