def get_single_letter():
    while True:
        user_input = input(">")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        else:
            print("Invalid input. Please enter a single letter.")
