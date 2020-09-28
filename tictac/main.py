from tictac.board import Board, play_game, play_random_move


def play_user_move(board):
    spot = input("Pick a spot: ")
    print("Spot: " + spot)
    return board.play_move(spot)


def play():
    game_board = play_game(play_random_move, play_random_move)
    game_board.print_board()


play()