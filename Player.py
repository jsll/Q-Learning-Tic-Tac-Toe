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
            
class Qplayer(Player):
    def __init__(self, epsilon, mark,Q={}):
        super(Qplayer, self).__init__(mark=mark)
        self.Q_net
        self.epsilon = 0.9
        
    def set_Q_network(self, Q_network):
        self.Q_net = Q_network
        
    def get_move(self, board):
        if  np.random.uniform(0,1,1)>self.epsilon:
            return self.choose_randomly(board)
        else:
            _, action = self.Q_net.getMaxQvalue(board.get_board_state(),board.get_empty_pos())
            return action
            
    def choose_randomly(self, board):
        empty_pos = board.get_empty_pos()
        return random.choice(empty_pos)
    
    def updateQNetwork(self, curr_state, next_state, action, reward, allActions, terminal):
        curr_state.append(action)
        self.Q_net.train(curr_state, next_state, reward, allActions, terminal)

    def tuneHyperParameters(self, num_games):
        self.epsilon -= (1/10000)*num_games
        self.Q_net.reduceLearningRate()