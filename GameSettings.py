import json


class GameSettings(object):

    __FILE = 'config/settings.json'

    def __init__(self):
        self.__settings = self.__load()

        if not self.__settings:
            self.__settings = {}

    def __load(self):
        try:
            fh = open(self.__FILE, 'r')
            data = json.load(fh)
            fh.close()
            return data
        except FileNotFoundError:
            return False
        except json.JSONDecodeError:
            return False
        except:
            print("Error ocurred. contact IT team.")
            return False

    def __save(self):
        fh = open(self.__FILE, 'w')
        fh.write(json.dumps(self.__settings))
        fh.close()

    def getSetting(self, key, fallback = None):
        if key in self.__settings:
            return self.__settings[key]
        else:
            return fallback

    def setSetting(self, key, value):
        self.__settings[key] = value
        self.__save()
