'''
Created on Feb 26, 2017

@author: jejje
'''

class StateActions(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.states = []
        
    def add_state(self, board, player):
        next_state = player+board.board_to_string()
        if next_state not in self.states:
            self.states.append(next_state)
            
    
        