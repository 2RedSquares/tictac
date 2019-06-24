from tictac.common import CELL_O, play_games
from tictac.random_moves import play_random_move
from tictac.minimax import play_minimax_move
from tictac.qtable import play_training_games, play_q_table_move

print("Playing random games: ")
print("---------------------")
play_games(1000, play_random_move, play_random_move)
print("")
print("Playing minimax games: ")
print("----------------------")
play_games(1000, play_minimax_move, play_minimax_move)
print("")
print("Playing minimax vs random games: ")
print("--------------------------------")
play_games(1000, play_minimax_move, play_random_move)
print("")
print("Playing random vs minimax games: ")
print("--------------------------------")
play_games(1000, play_random_move, play_minimax_move)
print("")


print("Training qtable X vs. minimax...")
play_training_games()
print("Training qtable O vs. minimax...")
play_training_games(q_table_player=CELL_O, x_strategy=play_minimax_move,
                    o_strategy=None)
print("Training qtable X vs. random...")
play_training_games(o_strategy=play_random_move)
print("Training qtable O vs. random...")
play_training_games(q_table_player=CELL_O, x_strategy=play_random_move,
                    o_strategy=None)

print("Playing qtable vs random games:")
print("-------------------------------")
play_games(1000, play_q_table_move, play_random_move)
print("")
print("Playing qtable vs minimax:")
print("-------------------------------")
play_games(1000, play_q_table_move, play_minimax_move)
print("")
print("Playing qtable vs qtable:")
print("-------------------------------")
play_games(1000, play_q_table_move, play_q_table_move)
print("")
