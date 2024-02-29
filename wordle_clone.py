import random
from colorama import Fore, Style

# List of words for the game
words = ["apple", "banana", "cherry", "orange", "grape", "lemon", "kiwi"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to check the guess against the chosen word
def check_guess(word, guess):
    guess = guess.ljust(len(word))  # Pad guess with spaces if it's shorter than the word
    correct_positions = sum(1 for i in range(len(word)) if word[i] == guess[i])
    correct_letters = sum(min(word.count(letter), guess.count(letter)) for letter in set(guess))
    return correct_positions, correct_letters - correct_positions


# Function to print feedback for the guess
def print_feedback(word, guess):
    for i in range(len(word)):
        if word[i] == guess[i]:
            print(Fore.GREEN + guess[i], end="")
        elif guess[i] in word:
            print(Fore.YELLOW + guess[i], end="")
        else:
            print(Fore.RED + guess[i], end="")
    print(Style.RESET_ALL)

# Main function to play the game
def main():
    word = choose_word()
    attempts = 6
    print("Welcome to Wordle!")
    print("Guess the word. You have 6 attempts.")

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
