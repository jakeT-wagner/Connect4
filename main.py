import pygame
from connect.constants import WIDTH, HEIGHT, SQUARE_SIZE
from connect.game import Game
import time

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect4")

def get_row_col_mouse(pos):
    x,y = pos #pos is a tuple
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return col

def main():
    clock = pygame.time.Clock()
    running = True
    game = Game(WIN)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = get_row_col_mouse(pos)
                game.make_move(col)
    
        if game.update() != None:
            print(f"{game.update()} has won the game!")
            time.sleep(2)
            running = False
    
    pygame.quit()

main()