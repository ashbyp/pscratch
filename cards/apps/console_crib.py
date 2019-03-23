from cards.cribbage.player import HumanPlayer, DumbComputerPlayer
from cards.cribbage.game import CribGame

game = CribGame(HumanPlayer(), DumbComputerPlayer())
game.play()

# for _ in range(100):
#     game = CribGame(DumbComputerPlayer(), DumbComputerPlayer())
#     game.play()