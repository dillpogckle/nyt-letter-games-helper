from util import get_single_letter
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

    d = LocalDict()
    answers = d.possible_words(letters, key)
    answers = [word for word in answers if len(word) >= 4]
    answers = list(set(answers))
    answers.sort()

    print("Here is a list of possible answers:\n")
    count = 0
    for word in answers:
        if count < 14:
            print(word + ", ", end="")
            count += 1
        elif count == 14:
            print(word)
            count = 0

    print("\n\nBut lets be honest you aren't just looking for any normal answers...")
    print("Hit Enter to see the possible \033[1;31;40mpangrams\033[0m")
    input()
    pangrams = d.possible_pangram(letters, answers)

    print("Today's potential \033[1;31;40mpangrams\033[0m are:")
    for pangram in pangrams:
        print("\033[1;31;40m" + pangram + "\033[0m")

    print("\nThanks for using the \033[1;33;40mSpelling Bee Solver\033[0m!")
