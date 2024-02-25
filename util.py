from localdict import LocalDict


def get_single_letter():
    """
    Ensures input is a single letter

    :return: the single character if input is correct
    """
    while True:
        user_input = input(">")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        else:
            print("Invalid input. Please enter a single letter.")


def get_answers(letters, key=None):
    """
    Creates a list of words that can fit constraints.

    :param letters: List of letters that are used to form answer words.
    :param key: Optional argument that determines if a there is a letter that must be used in every word.
    :return: List of words according to specifications.
    """
    d = LocalDict()
    if key is not None:
        answers = d.possible_words(letters, key)
    else:
        answers = d.possible_words(letters)
    answers = [word for word in answers if len(word) >= 4]
    answers = list(set(answers))
    answers.sort()
    return answers


def print_answers(answers):
    """
    Prints answers in 15 word long lines following a standard format.

    :param answers: List of words to be formatted.
    """
    count = 0
    for i, word in enumerate(answers):
        if i == len(answers) - 1:
            print(word)
        else:
            if count < 14:
                print(word + ", ", end="")
                count += 1
            elif count == 14:
                print(word)
                count = 0


def possible_pangram(letters, words):
    """
    Determines possible pangrams from a list of words.

    :param letters: List of letters that must be used.
    :param words: List of words to be tested.
    :return: List of pangrams from words that used all letters.
    """
    pangrams = []
    for word in words:
        copy_letters = letters[:]
        for char in word:
            if char in letters:
                if char in copy_letters:
                    copy_letters.remove(char)
        if len(copy_letters) == 0:
            pangrams.append(word)
    return pangrams


def remove_repeated_letters(words):
    """
    Checks a list of words and only returns words without repeated letters.
    :param words: List of words to be checked.
    :return: List of words from parameter that do not contain repeated letters.
    """
    no_repeats = []
    for word in words:
        word_as_set = set(word)
        if len(word) == len(word_as_set):
            no_repeats.append(word)
    return no_repeats
