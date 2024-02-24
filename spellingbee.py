from util import get_single_letter
from localdict import LocalDict
from time import sleep

if __name__ == "__main__":
    print("\nWelcome to the ", end="")
    print("\033[1;33;40mSpelling Bee Solver\033[0m!")
    print("Based on the NYT's hit game \033[1;33;40mSpelling Bee\033[0m\n")

    print("This solver takes one key letter and 6 other letters then generates words from those letters.")
    print("\nHowever, these words must follow some rules:\n"
          "\t1. They can only be created using the 7 input letters\n"
          "\t2. They must contain the key letter\n"
          "\t3. All words must be at least 4 letters long")

    input("\nHit Enter when you're ready to input your characters\n")

    print("Enter your key letter")
    key = get_single_letter()

    letters =[key]
    print("\nEnter your other six letters")
    for i in range(6):
        letters.append(get_single_letter())

    print("\nPerfect! Please wait while we get all the possible words...\n")
    sleep(2)

    d = LocalDict()
    answers = d.possible_words(letters, key)
    answers = [word for word in answers if len(word) >= 4]
    answers = list(set(answers))
    answers.sort()

    print("Here is a list of possible answers:")
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

    print("\n\nBut lets be honest you aren't here looking for normal answers...")
    print("Hit Enter to see today's possible \033[1;31;40mpangrams\033[0m")
    input()
    pangrams = d.possible_pangram(letters, answers)

    if len(pangrams) == 0:
        print("Looks like our dictionary can't find any \033[1;31;40mpangrams\033[0m...\n"
              "Are you sure you put in the right letters?")
    else:
        print("Today's potential \033[1;31;40mpangrams\033[0m are:")
        for pangram in pangrams:
            print("\033[1;31;40m" + pangram + "\033[0m")

    print("\n(Please note that our dictionary does not always match up with NYT's dictionary)")

    print("\nThanks for using the \033[1;33;40mSpelling Bee Solver\033[0m!\n")
