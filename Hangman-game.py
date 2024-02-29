import random

# Words for guessing
words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "blackbarry", "potatos", "kualiena"]


def choose_word(words):
    """Choose a random word from the list."""
    return random.choice(words)


def initialize(word):
    """Initialize the game."""
    guessed_letters = set()  # List of guessed letters
    incorrect_guesses = 0  # Number of incorrect guesses
    return guessed_letters, incorrect_guesses, word


def get_user_input():
    """Get user input."""
    return input("Enter a letter: ").lower()


def validate_input(user_input, guessed_letters):
    """Validate user input."""
    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter a single letter.")
        return False
    elif user_input in guessed_letters:
        print("You've already guessed that letter.")
        return False
    else:
        return True


def update_game_state(user_input, word, guessed_letters, incorrect_guesses):
    """Update game state based on user input."""
    guessed_letters.add(user_input)  # Add the entered letter to the list of guessed letters
    if user_input not in word:
        incorrect_guesses += 1  # Increase the incorrect guesses counter if the letter is not in the word
    return guessed_letters, incorrect_guesses


def display_word(word, guessed_letters):
    """Display the word with guessed letters and underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "  # If the letter is guessed, add it to the displayed string
        else:
            display += "_ "  # If the letter is not guessed, add an underscore
    return display


def draw_hanged_man(incorrect_guesses):
    """Display ASCII art of a hanged man based on the number of incorrect guesses."""
    hangman_images = [
        """
           -----
           |   |
               |
               |
               |
               |
               |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
               |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          ---  |
               |
               |
               |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          ---  |   
          /|\  |
               |
               |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          ---  |   
          /|\  |
           |   |
               |
               |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          ---  |
          /|\  |
           |   |
          ---  |
         /   \ |
               |
          -------
        """
    ]
    print(hangman_images[incorrect_guesses])


def check_game_over(word, guessed_letters, incorrect_guesses):
    """Check for game over conditions."""
    if incorrect_guesses >= 6:
        return True, f"You lost! The word was: {word.capitalize()}"
    elif all(letter in guessed_letters for letter in word):
        return True, f"Congratulations! You won! {word.capitalize()}!"
    else:
        return False, ""

# main part - inputs, game world, display, guessed letters status, conditions
def main():
    word = choose_word(words)
    guessed_letters, incorrect_guesses, word = initialize(word)
    game_over = False

    while not game_over:
        display = display_word(word, guessed_letters)
        print(display)
        draw_hanged_man(incorrect_guesses)

        user_input = get_user_input()
        while not validate_input(user_input, guessed_letters):
            user_input = get_user_input()

        guessed_letters, incorrect_guesses = update_game_state(user_input, word, guessed_letters, incorrect_guesses)
        game_over, message = check_game_over(word, guessed_letters, incorrect_guesses)
        if game_over:
            print(message)


if __name__ == "__main__":
    main()

