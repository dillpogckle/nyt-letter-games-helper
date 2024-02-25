from util import get_single_letter, get_answers, print_answers, remove_repeated_letters
from time import sleep


def main():
    # welcome messaging
    print("Welcome to \033[1;31;40mLetter Boxed Helper\033[0m!")
    print("Based on a game from the New York Times called \033[1;31;40mLetter Boxed\033[0m.\n")
    print("This helper program takes the letters from your \033[1;31;40mLetter Box\033[0m "
          "and helps you brainstorm words to try!")
    input("Hit Enter when you're ready to put in your letters.\n")

    # get letter input
    print("Please enter your 12 letters.")
    letters = []
    for i in range(12):
        letters.append(get_single_letter())

    # output helpful words
    print("Perfect! Please give us a moment while we determine some helpful words.")
    sleep(1.5)
    answers = get_answers(letters)
    answers = remove_repeated_letters(answers)
    print("\nHere is a list of words to help with your \033[1;31;40mLetter Box\033[0m:")
    print_answers(answers)

    # outro message
    print("\n(Please note that our dictionary does not always match up with NYT's dictionary)")
    print("\nThanks for using the \033[1;31;40mLetter Boxed Helper\033[0m!\n")


if __name__ == '__main__':
    main()