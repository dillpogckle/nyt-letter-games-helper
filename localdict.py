class LocalDict:
    def __init__(self):
        with open("/usr/share/dict/words") as f:
            self.__dictionary = set(f.read().splitlines())

    def is_a_word(self, word):
        return word in self.__dictionary
