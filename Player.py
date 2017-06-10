'''
Created on Feb 26, 2017

@author: jejje
'''
import numpy as np
import random
from QNetwork import QNetwork

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

class HumanPlayer(Player):
    def __init__(self, mark):
        super(HumanPlayer, self).__init__(mark=mark)
        
    def get_move(self, board):
        while True:
            move = int(raw_input("Enter position [1-9] "))
            if board.place_spot(move,self.mark):
                return move
            else:
                print "Position taken. Please choose another position."


class Qplayer(Player):
    def __init__(self, mark):
        super(Qplayer, self).__init__(mark=mark)
        self.epsilon = 0
        self.initial_epsilon = 0
        self.Q_net = 0
        
    def set_Q_network(self, Q_network):
        self.Q_net = Q_network
        
    def set_exploration_rate(self, new_epsilon):
        self.epsilon = new_epsilon
        self.initial_epsilon = self.epsilon
        
    def set_decay_rate(self, decay_rate):
        self.decay_rate = decay_rate
        
    def reduce_exploration(self, rate):
        self.epsilon = self.initial_epsilon*np.exp(-rate/self.decay_rate)
        
    def get_move(self, board):
        if  np.random.uniform(0,1,1)<self.epsilon:
            return self.choose_randomly(board)
        else:
            if self.mark == "x":
                _, action = self.Q_net.getBestQvalue(board.get_board_state(),board.get_empty_pos(), "max")
            elif self.mark == "o":
                _, action = self.Q_net.getBestQvalue(board.get_board_state(),board.get_empty_pos(), "min")
            return action
            
    def choose_randomly(self, board):
        empty_pos = board.get_empty_pos()
        return random.choice(empty_pos)