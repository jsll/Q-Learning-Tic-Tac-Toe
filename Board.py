'''
Created on Feb 14, 2017

@author: jejje
'''

from __future__ import print_function
import numpy as np
from __builtin__ import True
from docutils.nodes import row
import copy

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
        self.empty_pos = range(1,10)
        
    def place_mark(self,pos,mark):
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
        for i in range(3):
            print ("--",end='')
        print ("\n")

    def get_board_state(self):
        return copy.deepcopy(self.board)
    
    def game_over(self):
        return (self.is_full() or self.get_winner() is not None)

    def get_winner(self):
        for i in range(len(self.current_res)):
            if self.current_res[i]==3:
                return "X"
            elif self.current_res[i]==-3:
                return "O"

        return None
    
    def is_full(self):
        return ((self.num_o+self.num_x)==9)
    
    def get_next_board(self, move, mark):
        next_board = copy.deepcopy(self)
        next_board.place_mark(move, mark)
        return next_board
        
    def reset_board(self): 
        self.board = [0 for x in range(9)]
        self.num_x = 0
        self.num_o = 0
        self.current_res = [0 for x in range(8)]
        self.empty_pos = range(1,10)
        
    def get_empty_pos(self):
        return self.empty_pos
    
    def get_board_reward(self):
        if not self.game_over():
            return 0
        else:
            winner = self.get_winner()
            if winner == "X":
                return 1
            elif winner == "O":
                return -1
            else:
                return 0.5
        