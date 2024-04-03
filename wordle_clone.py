import random
from colorama import Fore, Style

# List of words for the game
words = ["apple", "banana", "cherry", "orange", "grape", "lemon", "kiwi", "peach", "pear", "plum", "mango",
         "papaya", "pineapple", "watermelon", "strawberry", "raspberry", "blueberry"]
# You have 6 attempts and 16 words to guessing the correct word
def choose_word():
    """Choose a random word from the list."""
    return random.choice(words)
# random word choising
def check_guess(word, guess):
    """Check the guess against the chosen word and calculate feedback."""
    guess = guess[:len(word)].ljust(len(word), ' ')  # Truncate or pad guess to match word length
    correct_positions = sum(1 for i in range(len(word)) if word[i] == guess[i])
    correct_letters = sum(min(word.count(letter), guess.count(letter)) for letter in set(guess))
    return correct_positions, correct_letters - correct_positions

# logic of guessing

def print_feedback(word, guess):
    """Print feedback for the guess, highlighting correct positions and letters."""
    min_length = min(len(word), len(guess))
    for i in range(min_length):
        if word[i] == guess[i]:
            print(Fore.GREEN + guess[i], end="")  # Green for correct positions
        elif guess[i] in word:
            print(Fore.YELLOW + guess[i], end="")  # Yellow for correct letters in wrong positions
        else:
            print(Fore.RED + guess[i], end="")  # Red for incorrect letters
    print(Style.RESET_ALL)

# here a rules to guessing letters
def main():
    """Main function to play the Wordle game."""
    word = choose_word()
    attempts = 6
    print("Welcome to Wordle!")
    print(f"Guess the word. You have {attempts} attempts.")
    print(f"Rules: You need to guess the name of a fruit within {attempts} attempts. The word contains {len(word)} letters.")
    print("Feedback: Green letters indicate correct positions, yellow letters indicate correct letters in wrong positions, and red letters indicate incorrect letters.")

    while attempts > 0:
        print(f"Attempts left: {attempts}")
        guess = input("Enter your guess: ").lower()

        if guess == word:
            print("Congratulations! You guessed the word correctly.")
            break

        feedback = check_guess(word, guess)
        print_feedback(word, guess)
        print(f"Correct positions: {feedback[0]}, Correct letters: {feedback[1]}")
        print()

        attempts -= 1

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    main()
