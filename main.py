import pygame
import button
from board import Board
from math import inf
import time


pygame.init()


# SCREEN_WIDTH = 900
# SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((900, 700))
background = pygame.color.Color('#212020')
screen.fill(background)

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)


menu_state = "player selection"
algorithm_state = ""


#load button images
max_img = pygame.image.load("assets/button_max.png").convert_alpha()
min_img = pygame.image.load("assets/button_min.png").convert_alpha()

minmax_img = pygame.image.load("assets/button_minmax.png").convert_alpha()
negamax_img = pygame.image.load("assets/button_negamax.png").convert_alpha()
alphabeta_img = pygame.image.load("assets/button_alphabeta.png").convert_alpha()

#create button instances
max_button = button.Button(100, 450, max_img, 1)
min_button = button.Button(550, 450, min_img, 1)

minmax_button = button.Button(350, 225, minmax_img, 1)
negamax_button = button.Button(350, 325, negamax_img, 1)
alphabeta_button = button.Button(350, 425, alphabeta_img, 1)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


launched = True
while launched:

    screen.fill((52, 78, 91))
    


    
    if menu_state == "selected":

        board = Board()
        board.draw(screen,fp)
        

        if algorithm_state == "alphabeta":
            board.negaMaxAlphaBetaPruning(board.board[0][0],screen,fp,depth=5, alpha = -inf, beta= inf )
            time.sleep(1)
            menu_state = "player selection"
            algorithm_state = ""

        if algorithm_state == "minmax":
            board.minimax(board.board[0][0],screen,fp,depth=5)
            time.sleep(1)
            menu_state = "player selection"
            algorithm_state = ""

        if algorithm_state == "negamax":
            board.negaMax(board.board[0][0],screen,fp,depth=5)
            time.sleep(1)
            menu_state = "player selection"
            algorithm_state = ""

    
    if menu_state == "algorithm selection":

        draw_text("veuiller choisir un agorithme", font, TEXT_COL, 150, 50)

        if minmax_button.draw(screen):
            menu_state = "selected"
            algorithm_state = "minmax"
        if negamax_button.draw(screen):
            menu_state = "selected"
            algorithm_state = "negamax"
        if alphabeta_button.draw(screen):
            menu_state = "selected"
            algorithm_state = "alphabeta"


    if menu_state == "player selection":

        draw_text("veuiller choisir qui commence", font, TEXT_COL, 120, 250)

        if min_button.draw(screen):
            menu_state = "algorithm selection"
            fp = -1
        if max_button.draw(screen):
            menu_state = "algorithm selection"
            fp = 1

      

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            menu_state = "player selection"
            algorithm_state = ""
            pygame.quit()
            

    
    pygame.display.update()
   
    

pygame.quit()

    





