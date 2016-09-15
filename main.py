from GameRandomNumber import GameRandomNumber
from GameGuess import GameGuess
from GameUIShell import GameUIShell

game = GameGuess()
game.setNumberGenerator(GameRandomNumber())
game.setGameUI(GameUIShell())
game.start()


