'''
Created on Feb 14, 2017

@author: jejje
'''
from Board import Board
from States import StateActions
from Player import Qplayer
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
        self.player1 = Qplayer(0,'x')
        self.player2 = Qplayer(0,'o')
        self.current_player = self.player1
        self.other_player = self.player2
        self.games = 0
        self.QNet = QNetwork
        self.set_shared_Q_network()
        
    def set_shared_Q_network(self):
        if isinstance(self.player1,Qplayer):
            self.player1.set_Q_network(self.QNet)
        if isinstance(self.player2, Qplayer):
            self.player2.set_Q_network(self.QNet)
            
    def play_game(self, maxGames):
        while(self.games<maxGames):
            if isinstance(self.player1,Qplayer) and isinstance(self.player2, Qplayer):
                while not self.board.game_over():
                    self.play_turn()
            self.resetGame()
        
    def play_turn(self):
        move = self.current_player.get_move(self.board)
        self.handle_move(move)
        self.switch_player()
        
    def handle_move(self, move):
        self.learn_Q(move)
        self.board.place_mark(action, self.current_player.mark)
        
    def learn_Q(self, move):
        next_board = self.board.get_next_board(move, self.current_player.mark)
        next_reward = next_board.get_board_reward()
        curr_state = self.board.get_state()
        next_state = next_board.get_state()
        curr_state.append(move)
        terminal = next_board.game_over()
        allActions = next_board.get_empty_pos()
        self.QNet.train(curr_state, next_state, reward, allActions, terminal)
        
    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.other_player = self.player1
        else:
            self.current_player = self.player1
            self.other_player = self.player2
            
    def test_play(self):
        self.board.print_board()
        self.turns = 0
        while(True):
            
            if self.turns%2==0:
                print "Player ones turn"
                while True:
                    action = int(raw_input("Enter position [1-9] "))
                    if self.board.place_spot(action,'x'):
                        break
                    else:
                        print "Position taken. Please choose another position."
            else:
                #print "Player twos turn"
                while True:
                    action = self.player2.get_move(self.board)
                    if self.board.place_spot(action,'o'):
                        break
                    else:
                        print "Position taken. Please choose another position."
            
            self.board.print_board()
            game_state = self.board.game_state()

            if game_state == 0:
                print "Draw"
                self.resetGame()
            elif game_state == 1:
                print "Player one wins"
                self.resetGame()
            elif game_state == -1:
                print "Player two wins"
                self.resetGame()
                            
            self.turns +=1

    def updatePlayersHyperParameters(self, player1, player2):
        player1.tuneHyperParameters(self.games)
        player2.tuneHyperParameters(self.games)

    def resetGame(self):
        self.games+=1
        self.turns = 0
        self.board.reset_board()