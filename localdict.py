class LocalDict:
    def __init__(self):
        with open("/usr/share/dict/words") as f:
            self.__dictionary = set(f.read().splitlines())

    def __is_a_word(self, word):
        return word in self.__dictionary

    def any_words(self, combos):
        words = []
        for combo in combos:
            if self.__is_a_word("".join(combo)):
                words.append("".join(combo))
        return words
