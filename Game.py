'''
Created on Feb 14, 2017

@author: jejje
'''
from Board import Board
from States import StateActions
from Player import Qplayer
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
        self.games = 0
    def play_game(self, maxGames):
        games = 0
        self.board.print_board()
        while(self.games<maxGames):
            
            prev_state = self.board.get_board_state()
            if self.turns%2==0:
                #print "Player ones turn"
                while True:
                    #action = int(raw_input("Enter position [1-9] "))
                    action = self.player1.get_move(self.board)
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
            
            curr_state = self.board.get_board_state()

            #self.board.print_board()
            game_state = self.board.game_state()

            if game_state == 0:
                print "Draw"
                player1_reward = 0.5
                player2_reward = 0.5
                terminal = 1
                self.resetGame()
            elif game_state == 1:
                print "Player one wins"
                player1_reward = 1
                player2_reward = -1
                terminal = 1
                self.resetGame()
            elif game_state == -1:
                print "Player two wins"
                player1_reward = -1
                player2_reward = 1
                terminal = 1
                self.resetGame()
            else:
                terminal = 0
                player1_reward = 0
                player2_reward = 0
            
            all_actions = self.board.get_empty_pos()
            
            if self.turns%2==0:
                self.player1.updateQNetwork(prev_state, curr_state, action, player1_reward, all_actions, terminal)
            if self.turns%2!=0:
                self.player2.updateQNetwork(prev_state, curr_state, action, player2_reward, all_actions, terminal)
            
            self.turns +=1 

            #updateQvalues()

    def resetGame(self):
        self.games+=1
        self.turns = 0
        self.board.reset_board()