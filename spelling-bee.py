from itertools import combinations_with_replacement

import enchant


key = "r"
letters = ["r", "l", "o", "d", "k", "w", "a"]

seven_letters = combinations_with_replacement(letters, 7)
six_letters = combinations_with_replacement(letters, 6)
five_letters = combinations_with_replacement(letters, 5)
four_letters = list(combinations_with_replacement(letters, 4))

print(four_letters)
