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
        #self.AI = AIPlayer()
        self.turns = 0
#         self.state = StateActions()
#         self.player1 = player1
        self.player2 = Qplayer(0,'o')
        
    def play_game(self, maxGames):
        games = 0
        self.board.print_board()

        while(games<maxGames):

            if self.turns%2==0:
                print "Player ones turn"
                while True:
                    pos = int(raw_input("Enter position [1-9] "))
                    if self.board.place_spot(pos,'x'):
                        break
                    else:
                        print "Position taken. Please choose another position."
            else:
                print "Player twos turn"
                while True:
                    pos = self.player2.get_move(self.board)
                    if self.board.place_spot(pos,'o'):
                        break
                    else:
                        print "Position taken. Please choose another position."
            
#             self.state.add_state(self.board, self.turn%2)
            
            game_state = self.board.game_state()
            self.board.print_board()
            self.turns +=1 

            if game_state == 0:
                print "Draw"
                games+=1
                player1_reward = 0
                player2_reward = 0
                self.resetGame(games)
            elif game_state == 1:
                print "Player one wins"
                games+=1
                player1_reward = 1
                player2_reward = -1
                self.resetGame(games)
            elif game_state == -1:
                print "Player two wins"
                games+=1
                player1_reward = -1
                player2_reward = 1
                self.resetGame(games)
            else:
                player1_reward = -1
                player2_reward = 1

            #updateQvalues()

    def resetGame(self, games):
        self.turns = games
        self.board.reset_board()