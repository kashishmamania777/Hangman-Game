import random

class Hangman:
    def __init__(self):
        self.category = self.choose_category()  # Choose a category for the game
        self.words = self.load_words(self.category)  # Load words from the chosen category
        self.word = random.choice(self.words)  # Select a random word from the loaded words
        self.guesses = []  # List to store the user's guesses
        self.max_attempts = 7  # Maximum number of attempts allowed
        self.attempts_left = self.max_attempts  # Number of attempts remaining

    def choose_category(self):
        categories = ["animals", "countries", "fruits_vegetables", "cars", "dictionary"]
        print("Choose a category:")
        for i, category in enumerate(categories, start=1):  # Enumerate through categories with index starting at 1
            print("{}. {}".format(i, category))  # Print the category with its corresponding number
        while True:
            choice = input("Enter the category number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(categories):  # Validate the user's choice
                return categories[int(choice) - 1]  # Return the chosen category
            print("Invalid choice. Please enter the number corresponding to the category.")

    def load_words(self, category):
        filename = "{}.txt".format(category)  # Construct the filename based on the chosen category
        with open(filename, "r") as file:  # Open the file for reading
            words = file.readlines()  # Read all lines from the file
        return [word.strip().lower() for word in words]  # Return a list of words with leading/trailing whitespaces removed and converted to lowercase

    def get_masked_word(self):
        masked_word = ""
        for char in self.word:  # Iterate through each character in the word
            if char in self.guesses:  # If the character is in the user's guesses
                masked_word += char  # Add the character to the masked word
            else:
                masked_word += "_"  # Otherwise, add an underscore to represent a hidden character
        return masked_word  # Return the masked word

    def play(self):
        print("Welcome to Hangman!")
        print("Guess the word. You have {} attempts.".format(self.max_attempts))

        while self.attempts_left > 0:  # Continue the game while there are attempts left
            print("\nAttempts left: {}".format(self.attempts_left))
            masked_word = self.get_masked_word()  # Get the masked version of the word
            print("Word: {}".format(masked_word))  # Display the masked word

            guess = input("Enter a letter: ").lower()  # Prompt the user to enter a letter guess and convert it to lowercase

            if guess in self.guesses:  # Check if the letter has already been guessed
                print("You already guessed that letter. Try again!")
                continue  # Skip the rest of the loop and go to the next iteration

            self.guesses.append(guess)  # Add the guess to the list of guesses

            if guess not in self.word:  # If the guess is not in the word
                self.attempts_left -= 1  # Decrement the number of attempts left
                print("Wrong guess!")

            if "_" not in self.get_masked_word():  # If there are no more hidden characters in the masked word
                print("\nCongratulations! You guessed the word: {}".format(self.word))
                break  # Exit the loop as the game has been won

        if self.attempts_left == 0:
            print("\nGame over! You failed to guess the word. The word was: {}".format(self.word))

        self.ask_play_again()

    def ask_play_again(self):
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                self.__init__()  # Reinitialize the game
                self.play()  # Start the game
                break  # Exit the loop
            elif play_again == "no":
                print("Thank you for playing Hangman!")
                break  # Exit the loop
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    game = Hangman()  # Create an instance of the Hangman class
    game.play()  # Start the game