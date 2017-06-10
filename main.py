'''
Created on Feb 14, 2017

@author: jejje
'''
from Game import Game
from Board import Board

def main():
    game = Game()
    game.AI_vs_AI()
    game.play_games(1)
    #game.test_play()
    
if __name__ == '__main__':
    main()