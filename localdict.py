class LocalDict:
    """
    Class that contains the local dictionary from dictionary.txt

    Attributes
    ----------
    __dictionary : list
        All words contained in dictionary.txt.

    Methods
    ---------
    possible_words(letters, key=None)
        Creates a list of words from dictionary that can be made using specified letters
    """
    def __init__(self):
        """
        Initializes a LocalDict
        """
        with open("dictionary.txt") as f:
            self.__dictionary = set(word.strip().lower() for word in f)

    def possible_words(self, letters, key=None):
        """
        Creates a list of words from dictionary that can be made using specified letters.

        :param letters: List of letters that can be used to make words.
        :param key: Optional argument. A letter that must be present in every word.
        :return: A list of all words in dictionary that match parameters.
        """
        words = []
        for word in self.__dictionary:
            if (key is None or key in word) and all(letter in letters for letter in word):
                words.append(word)
        return words
