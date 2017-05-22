'''
Created on Feb 14, 2017

@author: jejje
'''

from __future__ import print_function
import numpy as np
from __builtin__ import True
from docutils.nodes import row


class Board(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.board = [0 for x in range(9)]
        self.num_x = 0
        self.num_o = 0
        self.current_res = [0 for x in range(8)]
        self.empty_pos = range(9)
        
    def place_spot(self,pos,mark):
        value = 0
        if self.board[pos-1] == 0:
            row,col = self.get_row_and_col(pos-1)
            if mark == 'x':
                self.board[pos-1] = 1
                self.num_x+=1
                value = 1
            elif mark == 'o':
                self.board[pos-1] = -1
                self.num_o+=1
                value = -1
            self.increment_res(row,col,value)
            self.empty_pos.remove(pos)
            return True
        return False
        
    def increment_res(self,row,col,value):
        self.current_res[row]+=value
        self.current_res[col+3]+=value
        if (row==col):
            self.current_res[2*3]+=value
        if(row==3-1-col):
            self.current_res[2*3+1]+=value
            
    def get_row_and_col(self, pos):
        row = pos/3
        column = pos%3
        return row, column
        
    def print_board(self):
        for i in range(9):
            if self.board[i] == 1:
                print('x',end='')
            elif self.board[i] == -1:
                print('o',end='')
            else:
                print('0',end='')
            if ((i+1)%3) != 0:
                print('|',end='')
            if ((i+1)%3) == 0:
                print('\n',end='')
       
    def board_state_to_string(self, mark):
        board_state = mark
        for i in range(9):
            if (self.board[i]==1):
                board_state += 'x'
            elif (self.board[i]==-1):
                board_state += 'o'
            else:
                board_state += '0'
            
        return board_state
    '''
    Check if the game is over.
    
    Returns: 0 if the game is draw
            -10 if a player can still do moves
             1 if player 1 wins
            -1 if player 2 wins
    
    '''
    def game_state(self):
        if self.num_o<3 and self.num_x<3:
            return -10

        for i in range(len(self.current_res)):
            if (self.current_res[i]==3):
                return 1
            elif(self.current_res[i]==-3):
                return -1
        
        if self.is_full():
            return 0

        return -10
    
    def is_full(self):
        return ((self.num_o+self.num_x)==9)
    
    def reset_board(self): 
        self.board = [0 for x in range(9)]
        self.num_x = 0
        self.num_o = 0
        self.current_res = [0 for x in range(8)]
    
    def get_empty_pos(self):
        return self.empty_pos
    