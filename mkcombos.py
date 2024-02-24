from itertools import combinations_with_replacement


def make_combos(letters, num_char, key=None):
    lst = list(combinations_with_replacement(letters, num_char))
    if key is None:
        return lst

    else:
        temp = []
        for combo in lst:
            if key in combo:
                temp.append(combo)
        lst = temp
        return temp
