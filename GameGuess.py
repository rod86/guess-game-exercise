from GameSettings import GameSettings

class GameGuess(object):

    __DEFAULT_LIVES = 3

    def __init__(self):
        # Instance of the class that handles the UI
        self.__gameUI = None

        # Instance of the class that generates number
        self.__numberGenerator = None

        # Base number (is generated when game starts and is the same in all game)
        self.__baseNumber = None

        # Generated number that is compared with the base number
        self.__number = None

        # user value
        self.__userValue = ''

        # settings instance
        self.__settings = GameSettings()

    def setNumberGenerator(self, val):
        self.__numberGenerator = val

    def setGameUI(self, val):
        self.__gameUI = val

    def __addLives(self, amount):
        lives = self.__lives + amount

        if lives <= 0:
            self.__lives = 0
        else:
            self.__lives = lives

    def __isWin(self, value):
        return (value == 'H' and self.__number > self.__baseNumber) or (value == 'L' and self.__number < self.__baseNumber)

    def __runGame(self):
        # show lives
        self.__gameUI.onDisplayLives(self.__lives)

        # ask user for input value
        self.__userValue = str(self.__gameUI.getUserInput()).upper()

        # if user quit or restart
        if self.__userValue == 'Q':
            # save lives in settings
            return
        elif self.__userValue == 'R':
            self.__restart()
            self.__runGame()

        # if user an invalid value, restart try
        if not self.__userValue == 'L' and not self.__userValue == 'H':
            self.__gameUI.onUserInputError()
            self.__runGame()

        # generate number to compare with base number
        self.__number = self.__numberGenerator.getNumber()

        # check if is a win or loose and show its message
        if self.__isWin(self.__userValue):
            self.__gameUI.onWin(self.__number)
            self.__addLives(1)
        else:
            self.__gameUI.onLoose(self.__number)
            self.__addLives(-1)

        self.__settings.setSetting('lives', self.__lives)
        self.__gameUI.onLivesUpdate(self.__lives)

        if self.__lives <= 0:
            self.__gameUI.onGameOver()
            return

        print()
        self.__runGame()

    def __restart(self):
        self.__lives = self.__DEFAULT_LIVES
        self.__settings.setSetting('lives', self.__lives)
        self.__gameUI.onRestart()

    def start(self):
        # welcome the user
        self.__gameUI.onWelcome()

        # load settings from file
        self.__lives = self.__settings.getSetting('lives', self.__DEFAULT_LIVES)

        # Generate base number and pass it to UI
        self.__baseNumber = self.__numberGenerator.getBaseNumber()
        self.__gameUI.setBaseNumber(self.__baseNumber)

        # run a try
        self.__runGame()


