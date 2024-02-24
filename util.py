from itertools import combinations_with_replacement


def make_combos(letters, num_char, key=None):
    combos = list(combinations_with_replacement(letters, num_char))
    if key is None:
        return list(combos)

    return [combo for combo in combos if key in combo]


def get_single_letter():
    while True:
        user_input = input(">")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        else:
            print("Invalid input. Please enter a single letter.")
