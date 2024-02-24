class LocalDict:
    def __init__(self):
        with open("words_alpha.txt") as f:
            self.__dictionary = set(f.read().splitlines())

    def possible_words(self, letters, key):
        words = []
        for word in self.__dictionary:
            if key in word and all(letter in letters for letter in word):
                words.append(word)
        return words


d = LocalDict()
letters = ['c', 'o', 'v', 'n', 'i', 'g', 'u']
key = 'o'
print(d.possible_words(letters, key))
