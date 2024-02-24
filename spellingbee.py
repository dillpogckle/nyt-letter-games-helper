from util import make_combos, get_single_letter
from localdict import LocalDict

if __name__ == "__main__":
    print("Welcome to the ", end="")
    print("\033[1;33;40mSpelling Bee Solver\033[0m!")
    print("Based on the NYT's hit game \033[1;33;40mSpelling Bee\033[0m\n")

    print("This game takes one key letter and 6 other letters then generates words")
    print("\nThese words must follow some rules:\n"
          "\t1. It can only be created using the 7 input letters\n"
          "\t2. it must contain the key letter\n"
          "\t3. All words must be at least 4 letters long")

    input("\nHit Enter when you're ready to input your characters\n")

    print("Enter your key letter")
    key = get_single_letter()

    letters =[key]
    print("\nEnter your other six letters")
    for i in range(6):
        letters.append(get_single_letter())

    print("Perfect! Please wait while we get all the possible words...\n")

    dictionary = LocalDict()

    seven_letter = make_combos(letters, 7, key)
    seven_letter_words = dictionary.any_words(seven_letter)
    print(seven_letter_words)
    four_letter = make_combos(letters, 4, key)
    four_letter_words = dictionary.any_words(four_letter)
    print(four_letter_words)

