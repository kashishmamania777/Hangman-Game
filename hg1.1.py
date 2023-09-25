import random

class Hangman:
    def __init__(self):
        self.words = self.load_words()  # Load words from a file
        self.word = random.choice(self.words)  # Choose a random word from the loaded words
        self.guesses = []  # Store the guessed letters
        self.max_attempts = 6  # Maximum number of attempts
        self.attempts_left = self.max_attempts  # Number of attempts left

    def load_words(self):
        with open("words.txt", "r") as file:  # Open the "words.txt" file in read mode
            words = file.readlines()  # Read all lines from the file
        return [word.strip().lower() for word in words]  # Return a list of words after removing whitespace and converting to lowercase

    def get_masked_word(self):
        masked_word = ""
        for char in self.word:
            if char in self.guesses:
                masked_word += char  # Append the guessed letter
            else:
                masked_word += "_"  # Append an underscore for unguessed letters
        return masked_word  # Return the masked word

    def play(self):
        print("Welcome to Hangman!")
        print("Guess the word. You have {} attempts.".format(self.max_attempts))

        while self.attempts_left > 0:
            print("\nAttempts left: {}".format(self.attempts_left))
            masked_word = self.get_masked_word()  # Get the masked word with guessed letters
            print("Word: {}".format(masked_word))

            guess = input("Enter a letter: ").lower()  # Get user's guess and convert to lowercase

            if guess in self.guesses:
                print("You already guessed that letter. Try again!")
                continue

            self.guesses.append(guess)  # Add the guess to the list of guesses

            if guess not in self.word:
                self.attempts_left -= 1  # Decrement the attempts left if the guess is wrong
                print("Wrong guess!")

            if "_" not in self.get_masked_word():
                print("\nCongratulations! You guessed the word: {}".format(self.word))
                break

        if self.attempts_left == 0:
            print("\nGame over! You failed to guess the word. The word was: {}".format(self.word))

if __name__ == "__main__":
    game = Hangman()
    game.play()