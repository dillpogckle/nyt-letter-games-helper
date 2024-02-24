from util import get_single_letter, get_words

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

    all_words = []
    ten_letter_words = get_words(10, letters)
    all_words.append(ten_letter_words)
    nine_letter_words = get_words(9, letters)
    all_words.append(nine_letter_words)
    eight_letter_words = get_words(8, letters)
    all_words.append(eight_letter_words)
    seven_letter_words = get_words(7, letters)
    all_words.append(seven_letter_words)
    six_letter_words = get_words(6, letters)
    all_words.append(six_letter_words)
    five_letter_words = get_words(5, letters)
    all_words.append(five_letter_words)
    four_letter_words = get_words(4, letters)
    all_words.append(four_letter_words)

    len_words = 10
    for lst in all_words:
        print("All the possible words that are " + str(len_words) + " words long:")
        if len(lst) == 0:
            print("There are none :(\n")
        else:
            print(", ".join(lst))
            print()
        len_words -= 1





