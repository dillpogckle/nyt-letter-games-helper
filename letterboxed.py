from util import get_single_letter, print_answers, get_box_answers, remove_repeated_letters


def main():
    # welcome message
    print("Welcome to \033[1;31;40mLetter Boxed Helper\033[0m!")
    print("Based on a game from the New York Times called \033[1;31;40mLetter Boxed\033[0m.\n")
    print("This helper program takes the letters from your \033[1;31;40mLetter Box\033[0m "
          "and helps you brainstorm words to try!")
    input("Hit Enter when you're ready to put in your letters.\n")

    # get letter input
    print("Please enter side 1 letters.")
    side1 = []
    for i in range(3):
        side1.append(get_single_letter())

    print("Please enter side 2 letters.")
    side2 = []
    for i in range(3):
        side2.append(get_single_letter())

    print("Please enter side 3 letters.")
    side3 = []
    for i in range(3):
        side3.append(get_single_letter())

    print("Please enter side 4 letters.")
    side4 = []
    for i in range(3):
        side4.append(get_single_letter())

    answers = get_box_answers(side1, side2, side3, side4)
    # answers = remove_repeated_letters(answers)

    # output helpful words
    print("\nHere is a list of words to help with your \033[1;31;40mLetter Box\033[0m:")
    print_answers(answers)

    # outro message
    print("\n(Please note that our dictionary does not always match up with NYT's dictionary)")
    print("\nThanks for using the \033[1;31;40mLetter Boxed Helper\033[0m!\n")


if __name__ == '__main__':
    main()