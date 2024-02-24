class LocalDict:
    def __init__(self):
        with open("dictionary.txt") as f:
            self.__dictionary = set(word.strip().lower() for word in f)

    def possible_words(self, letters, key):
        words = []
        for word in self.__dictionary:
            if key in word and all(letter in letters for letter in word):
                words.append(word)
        return words

    def possible_pangram(self, letters, words):
        panagrams = []
        for word in words:
            copy_letters = letters[:]
            for char in word:
                if char in letters:
                    if char in copy_letters:
                        copy_letters.remove(char)
            if len(copy_letters) == 0:
                panagrams.append(word)
        return panagrams