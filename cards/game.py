from cards.crib_player import HumanPlayer, DumbComputerPlayer
from cards.crib_game import CribGame

game = CribGame(HumanPlayer(), DumbComputerPlayer())
game.play()

# for _ in range(100):
#     game = CribGame(DumbComputerPlayer(), DumbComputerPlayer())
#     game.play()