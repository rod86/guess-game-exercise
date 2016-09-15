import random as rand


class GameRandomNumber(object):

    __MIN = 0
    __MAX = 100

    def __generate(self):
        return rand.randint(self.__MIN, self.__MAX)

    def getBaseNumber(self):
        return self.__generate()

    def getNumber(self):
        return self.__generate()