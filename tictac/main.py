from tictac.board import play_game, play_random_move


def play_user_move(board):
    board.print_board()
    move = input("Pick a spot: ")
    new_board = board.play_move(int(move))
    new_board.print_board()
    return new_board


def play():
    game_board = play_game(play_user_move, play_random_move)
    game_board.print_board()


play()
