from cards.crib_player import HumanPlayer, DumbComputerPlayer
from cards.crib_game import CribGame

game = CribGame(HumanPlayer(), DumbComputerPlayer())
game.play()