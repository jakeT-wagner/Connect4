import pygame
from .board import Board
from .constants import YELLOW, RED, ROWS, COLS
from .piece import Piece

class Game:
    def __init__(self, win):
        self.board = Board(win)
        self.turn = YELLOW
        self.last_row = -1
        self.last_col = -1

    def switch_turn(self):
        if self.turn == YELLOW:
            self.turn = RED
        else:
            self.turn =YELLOW
    
    def update(self):
        self.board._draw()
        pygame.display.update()
        if self.check_winner() != None:
            return self.check_winner()
        return None

    def make_move(self, col):
        found_next = False
        counter = ROWS-1
        col = int(col)
        while  not found_next:#use not instead of !operator
            piece = self.board.get_piece(counter,col)
            if piece == 0:
                self.board.create_piece(counter,col,self.turn)
                self.switch_turn()
                found_next = True
                self.last_row = counter 
                self.last_col = col
            if (counter == 0):
                found_next = True
            counter -= 1
            
    
    def check_winner(self):
        if self.last_row != -1 and self.last_col != -1:
            player = self.board.get_piece(self.last_row,self.last_col).color
            count = 0
            for i in range(COLS):
                if self.board.get_piece(self.last_row,i) != 0:
                    piece = self.board.get_piece(self.last_row,i)
                    if (piece.color == player):
                        count += 1
                    else:
                        count = 0
                    if count >= 4:
                        return player
                else:
                    count = 0
            count = 0
            for j in range(ROWS):
                if self.board.get_piece(j,self.last_col) != 0:
                    piece = self.board.get_piece(j, self.last_col)
                    if (piece.color == player):
                        count += 1
                    else:
                        count = 0
                    if count >= 4:
                        return player
                else:
                    count = 0
            count = 0
            #diagonal in the positive direction(row++, col++)
            indexDiff = min(self.last_col, self.last_row)
            start_row = self.last_row - indexDiff
            start_col = self.last_col - indexDiff
            steps = min(ROWS - start_row, COLS - start_col)
            for i in range(steps):
                if self.board.get_piece(start_row+i,start_col+i) != 0:
                    piece = self.board.get_piece(start_row+i, start_col+i)
                    if piece.color == player:
                        count += 1
                    else:
                        count = 0
                    if count >= 4:
                        return player
                        
                else:
                    count = 0
            
            count = 0
            #diagonal in the negative direction
            indexDiff = min(self.last_col, ROWS-1 - self.last_row)
            start_row = self.last_row + indexDiff
            start_col = self.last_col - indexDiff
            steps = min(start_row, COLS-start_col)
            for i in range(steps):
                if self.board.get_piece(start_row-i, start_col+i) != 0:
                    piece = self.board.get_piece(start_row-i, start_col+i)
                    if piece.color == player:
                        count += 1
                    else:
                        count = 0
                    if count >= 4:
                        return player
                else:
                    count = 0
        return None


