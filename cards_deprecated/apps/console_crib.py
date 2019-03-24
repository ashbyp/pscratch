from cards_deprecated.cribbage import player
from cards_deprecated.cribbage.game import Game

game = Game(player.HumanPlayer(), player.ComputerPlayerV3())
game.play()

