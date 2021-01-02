import pygame
from .constants import DBLUE, WHITE, YELLOW, RED, GRAY, WIDTH, HEIGHT, SQUARE_SIZE, RADIUS, PADDING,  ROWS, COLS
from .piece import Piece

class Board:
    def __init__(self, win):
        self.board = []
        self.win = win
        self.initiate_board()
        self._draw()
    
    def draw_plastic(self):
        self.win.fill(DBLUE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.circle(self.win, GRAY, (row*SQUARE_SIZE + SQUARE_SIZE//2, col*SQUARE_SIZE + SQUARE_SIZE//2), RADIUS+PADDING)
                pygame.draw.circle(self.win, WHITE, (row*SQUARE_SIZE + SQUARE_SIZE//2, col*SQUARE_SIZE + SQUARE_SIZE//2), RADIUS)
    
    def initiate_board(self):
        for row in range(ROWS):
            self.board.append([])
            for _ in range(COLS):
                self.board[row].append(0)

    def _draw(self):
        self.draw_plastic()
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(self.win)
    
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def create_piece(self, row, col, color):
        self.board[row][col] = Piece(row,col,color)
    

            
