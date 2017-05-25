'''
Created on Feb 14, 2017

@author: jejje
'''
from Game import Game
from Board import Board

def main():
#     board = Board()
#     board.place_spot(6,'x')
#     board.place_spot(1,'o')
#     print board.game_over()
#     board.place_spot(4,'o')
#     print board.game_over()
#     board.place_spot(7,'o')
#     print board.game_over()
#     board.print_board()
#     print board.board_to_string()

    game = Game()
    game.play_game(1000)
if __name__ == '__main__':
    main()