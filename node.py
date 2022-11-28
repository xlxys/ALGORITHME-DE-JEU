from copy import deepcopy
import numpy as np
from math import inf
import itertools
import pygame

import time


RED = (255, 0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

WIDTH = 800
HEIGHT = 700 

class Node:

    def __init__(self,parent, leftChild, rightChild, value, row, col):
        self.row = row
        self.col = col
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.value = value
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.color = pygame.color.Color('#627f9e')
        self.path = None 

    def set_leftChild(self, leftChild):
        self.leftChild = leftChild
    
    def set_rightChild(self, rightChild):
        self.rightChild = rightChild

    def set_value(self, value):
        self.value = value

    def set_color(self, value):
        self.color = value

    def calc_pos(self):
        self.x = ( WIDTH//(pow(2,self.row)) * self.col ) + ( WIDTH//(pow(2,self.row)) // 2 )
        self.y = ( (HEIGHT//5) * self.row ) + ( ( HEIGHT//5 ) // 2 )
        

    def draw(self, win):
        
        if self.parent != None:
            pygame.draw.line(win, self.color ,(self.x, self.y), (self.parent.x, self.parent.y))

        pygame.draw.circle(win, self.color, (self.x, self.y), 20)

        if self.value != None :
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render(str(self.value), True, BLACK )
            textRect = text.get_rect()
            textRect.center = (self.x, self.y)
            win.blit(text, textRect)
    
    def draw_explored(self, win):
        
        pygame.draw.circle(win, [0,0,255], (self.x, self.y), 20)
        if self.parent != None:
            pygame.draw.line(win,  [0,0,255] ,(self.x, self.y), (self.parent.x, self.parent.y))
        if self.value != None :
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render(str(self.value), True, BLACK )
            textRect = text.get_rect()
            textRect.center = (self.x, self.y)
            win.blit(text, textRect)
    


    def draw_find(self, win):
        pygame.draw.line(win,  [255,0,0] ,(self.x , self.y), (self.path.x, self.path.y))
        pygame.draw.circle(win, [255,0,0], (self.path.x, self.path.y), 20)
        
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(str(-self.path.value), True, BLACK )
        textRect = text.get_rect()
        textRect.center = (self.path.x, self.path.y)
        win.blit(text, textRect)


        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(str(self.value), True, BLACK )
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        win.blit(text, textRect)
    
    def displayAlphaBeta(self, win, alpha, beta):
        
        font = pygame.font.Font('freesansbold.ttf', 9)
        text = font.render("\u03B1= "+str(alpha), True, BLACK )
        textRect = text.get_rect()
        if self.leftChild == None:
        
            textRect.center = (self.x , self.y+30)
        else:
            pygame.draw.rect(win,[255,0,0],pygame.Rect(self.x-20, self.y-50, 40,25) )
            textRect.center = (self.x , self.y-40)

        win.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 9)
        text = font.render("\u03B2= "+str(beta), True, BLACK)
        textRect = text.get_rect()
        if self.leftChild == None:

            textRect.center = (self.x , self.y+40)
        else:

            textRect.center = (self.x , self.y-30)
        win.blit(text, textRect)
    
        
