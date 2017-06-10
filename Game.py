'''
Created on Feb 14, 2017

@author: jejje
'''
from Board import Board
from States import StateActions
from Player import *
from QNetwork import QNetwork
from twisted.python.reflect import isinst
class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.board = Board()
        self.turns = 0
        self.games = 0
        self.QNet = QNetwork()
        
    def AI_vs_AI(self):
        self.player1 = self.create_Qplayer('x',0.99)
        self.player2 = self.create_Qplayer('o',0.99)
        self.set_Q_network()
        self.set_players()
        
    def Human_vs_AI(self):
        self.player1 = self.create_HumanPlayer('x')
        self.player2 = self.create_Qplayer('o',0)
        self.set_Q_network()
        self.set_players()
        
    def Human_vs_Human(self):
        self.player1 = self.create_HumanPlayer('x')
        self.player2 = self.create_HumanPlayer('o')
        self.set_players()
        
    def set_players(self):
        self.current_player = self.player1
        self.other_player = self.player2  

    def activate_Qlearning(self):
        self.learnQ = True
    
    def deactivate_Qlearning(self):
        self.learnQ = False
    
    def create_HumanPlayer(self, mark):
        player = HumanPlayer(mark)
        return player
    
    def create_Qplayer(self, mark, exploration):
        player = Qplayer(mark)
        self.set_Qplayer_parameters(player, exploration)
        return player
    
    def set_Qplayer_parameters(self, Qplayer, exploration):
        Qplayer.set_exploration_rate(exploration)
        Qplayer.set_decay_rate(10000)
        
    def set_Q_network(self):
        if isinstance(self.player1,Qplayer):
            self.player1.set_Q_network(self.QNet)
        if isinstance(self.player2, Qplayer):
            self.player2.set_Q_network(self.QNet)
            
    def play_games(self, maxNumGames):
        while(self.games<maxNumGames):
            while not self.board.game_over():
                self.play_turn()

            self.resetGame()
        
    def play_turn(self):
        move = self.current_player.get_move(self.board)
        self.handle_move(move)
        self.switch_player()
        
    def handle_move(self, move):
        self.learn_Q(move)
        self.board.place_mark(move, self.current_player.mark)
        
    def learn_Q(self, move):
        next_board = self.board.get_next_board(move, self.current_player.mark)
        next_board.print_board()
        reward = next_board.get_board_reward()
        curr_state = self.board.get_board_state()
        next_state = next_board.get_board_state()
        curr_state.append(move)
        terminal = next_board.game_over()
        allActions = next_board.get_empty_pos()
        sign = "max" if self.current_player.mark == "x" else "min"
        print sign
        self.QNet.train(curr_state, next_state, reward, allActions, terminal, sign)
        
    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.other_player = self.player1
        else:
            self.current_player = self.player1
            self.other_player = self.player2
            
    def resetGame(self):
        self.games+=1
        self.turns = 0
        if isinstance(self.player1,Qplayer):
            self.player1.reduce_exploration(self.games)
        if isinstance(self.player2, Qplayer):
            self.player2.reduce_exploration(self.games)
            
        self.set_players()
        self.board.reset_board()