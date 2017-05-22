'''
Created on Feb 26, 2017

@author: jejje
'''
import numpy as np
import random
class Player(object):
    '''
    classdocs
    '''


    def __init__(self, mark):
        '''
        Constructor
        '''
        self.mark = mark
        self.get_opponent_mark(mark)
        
    def get_opponent_mark(self, mark):
        if (mark == 'x'):
            self.opponent_mark = 'o'
        elif (mark == 'o'):
            self.opponent_mark = 'x'
        else:
            print "Mark has to be either 'o' or 'x'"
            
class Qplayer(Player):
    def __init__(self, epsilon, mark,Q={}):
        super(Qplayer, self).__init__(mark=mark)
        self.Q_net = ??
        self.epsilon = 0
        
    def get_move(self, board):
        if  np.random.uniform(0,1,1)>self.epsilon:
            return self.choose_randomly(board)
        #else:
            return self.Q_net.choose(board)
            
    def choose_randomly(self, board):
        empty_pos = board.get_empty_pos()
        return random.choice(empty_pos)
    
