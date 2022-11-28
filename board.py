from node import Node
import random
from math import inf
import time
import pygame
# import button
import sys

ROWS = 5

class Board():
    def __init__(self):
        self.board = []
        self.create_board()

    def initialise_fils(self):
        for row in range(ROWS):
            COLS = pow(2,row)
            for col in range(COLS):
                noeud = self.board[row][col]
                if row == 4:
                    val = random.randrange(-50,50)
                    noeud.set_value(val)

    
    def create_board(self):
        
        for row in range(ROWS):
            COLS = pow(2,row)
            self.board.append([])
            for col in range(COLS):
                
                if(row == 0):
                    parent = None
                    leftChild = None
                    rightChild = None
                elif(row == 4):
                    parent = self.board[row-1][col//2]
                    leftChild = None
                    rightChild = None
                else: 
                    parent = self.board[row-1][col//2]
                    leftChild = None
                    rightChild = None
                self.board[row].append(Node(parent,leftChild, rightChild, None, row, col))
        
        for row in range(ROWS):
            COLS = pow(2,row)
            for col in range(COLS):
                if(row != 4):
                    leftChild = self.board[row+1][col*2]
                    self.board[row][col].set_leftChild(leftChild)
                    rightChild = self.board[row+1][col*2+1]
                    self.board[row][col].set_rightChild(rightChild)

        self.initialise_fils()

    def draw_text(self,win,text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        win.blit(img, (x, y))

    def draw(self, win,fp):
        x=800
        y=35
        for row in range(ROWS):
            if fp ==1:
                minmax="MAX"
            elif fp==-1:
                minmax="MIN"
            
            TEXT_COL = (255, 255, 255)
            font = pygame.font.SysFont("arialblack", 30)
            self.draw_text(win,minmax,font, TEXT_COL,x,y)
            COLS = pow(2,row)
            for col in range(COLS):
                noeud = self.board[row][col]
                noeud.draw(win)
            fp=fp*(-1)
            y=y+145

    # max_img = pygame.image.load("assets/button_max.png").convert_alpha()
    # max_button = button.Button(275, 250, max_img, 1)

    def minimax(self,node, win, player, depth=5 ): #intial depth is 5
        
        # launched = True
        # menu_state = "selected"
        # algorithm_state = "minmax"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # max_button.draw(win)

        if (depth == 1):
            #Display the current node’s value and mark it as explored
            node.draw_explored(win)
            pygame.display.update()
            time.sleep(1.0)
            
            node.explored = True
        else:
            #Mark the current node as explored
            node.draw_explored(win)
            pygame.display.update()
            time.sleep(1.0)

            listChildren = [node.leftChild, node.rightChild]
            if (player == 1): # MAX = +1
                bestValue = -inf
                bestPath = None
                indice = 0
                for child in listChildren:
                    #Mark the link between the current node and the child node as explored
                    child.draw_explored(win)
                    pygame.display.update()
                    time.sleep(1.0)

                    self.minimax (child, win,-player, depth-1) #Apply the MiniMax function on each child
                    if child.value > bestValue :
                        bestValue = child.value
                        bestPath = child
                        indice = indice + 1

            else: # If the player is MIN (MIN = -1)
                bestValue = +inf
                bestPath = None
                for child in listChildren:
                    # Mark the link between the current node and the child node as explored
                    child.draw_explored(win)
                    pygame.display.update()
                    time.sleep(1.0)

                    self.minimax (child, win, -player, depth-1) # Apply the MiniMax function on each child
                    if child.value < bestValue:
                        bestValue = child.value
                        bestPath = child

            node.value = bestValue
            node.path = bestPath
            #node.set_value(bestValue) # je peut la supprimer
            node.draw_find(win)
            pygame.display.update()
            time.sleep(2.0)
            #Display the best path and the current node’s value
        




    def negaMax (self, node, win, player, depth): # Initial depth is 5
        # launched = True
        # menu_state = "selected"
        # algorithm_state = "negamax"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         break

        if depth == 1 :
            if player == -1 :
                node.value = -node.value
            #Display the current node’s value and mark it as explored
            node.draw_explored(win)
            pygame.display.update()
            time.sleep(1.0)

        else:
            #Mark the current node as explored
            node.draw_explored(win)
            pygame.display.update()
            time.sleep(1.0)

            listChildren = [node.leftChild, node.rightChild] 
            bestValue = -inf
            bestPath = None
            for child in listChildren :
                #Mark the link between the current node and the child node as explored
                child.draw_explored(win)
                pygame.display.update()
                # time.sleep(1.0)

                self.negaMax(child, win, -player, depth-1) #Apply the NegaMax function on each child
                child.value = -child.value
                if child.value > bestValue:
                    bestValue = child.value
                    bestPath = child

            node.value = bestValue
            node.path = bestPath
            #node.set_value(bestValue)
            node.draw_find(win)
            pygame.display.update()
            time.sleep(2.0)
            #Display the best path and the current node’s value
            
    def negaMaxAlphaBetaPruning(self, node, win, player, depth, alpha, beta):
   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        #Initially, depth=5, alpha=-inf and beta=+inf 
        if depth == 1:
            if player == -1 :
                node.value = - node.value
            node.draw_explored(win)
            node.displayAlphaBeta(win,alpha,beta)
            pygame.display.update()
            time.sleep(1.0)
            launched = False
            menu_state = "player selection"
            algorithm_state = ""
            #Display the current node’s value and mark it as explored
            #Display the values of alpha and beta 

        else:
            node.draw_explored(win)
            #node.displayAlphaBeta(win,alpha,beta)
            pygame.display.update()
            time.sleep(1.0)
            #Mark the current node as explored
            #Display the values of alpha and beta

            listChildren = [node.leftChild, node.rightChild] 
            bestValue = -inf
            bestPath = None
            for child in listChildren :
                #Mark the link between the current node and the child node as explored
                node.draw_explored(win)
                node.displayAlphaBeta(win,alpha,beta)
                pygame.display.update()
                # time.sleep(1.0)

                self.negaMaxAlphaBetaPruning (child, win, -player, depth-1, -beta, -alpha) 
                child.value = - child.value
                if child.value > bestValue :
                    bestValue = child.value
                    bestPath = child

                if bestValue > alpha:
                    alpha = bestValue
                    #Display the new value of alpha
                    node.displayAlphaBeta(win,alpha,beta)
                    pygame.display.update()
                    time.sleep(1.0)

                if beta <= alpha:
                    break
            node.value = bestValue
            node.path = bestPath
            node.draw_find(win)
            node.displayAlphaBeta(win,alpha,beta)
            pygame.display.update()
            time.sleep(2.0)
            #Display the best path and the current node’s value
        


        
