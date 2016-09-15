
class GameUIShell(object):

    def __init__(self):
        self.__baseNumber = 0

    def setBaseNumber(self, number):
        self.__baseNumber = number

    def onWelcome(self):
        print("Welcome to the Game App")

    def onRestart(self):
        print("You restarted the game")

    def onDisplayLives(self, lives):
        print("Lifes: %s" %(lives))

    def onLivesUpdate(self, lives):
        print("Lifes Remaining: %s" % (lives))

    def onGameOver(self):
        print("You don't have lives")

    def getUserInput(self):
        print("Here's the number %s" %(self.__baseNumber))
        print("Do you think next number I show will be higher or lower?")
        return input("Type H for higher, L for Lower, R to restart, Q to quit:")

    def onUserInputError(self):
        print("Please, introduce a valid value.")

    def onWin(self, number):
        print("The next number was %s" %(number))
        print("You won")

    def onLoose(self, number):
        print("The next number was %s" %(number))
        print("You lost")
