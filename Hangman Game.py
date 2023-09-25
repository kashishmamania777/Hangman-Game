import random

class Hangman:
    def __init__(self):
        self.category = None  # Initialize category variable
        self.words = []  # Initialize words list
        self.word = None  # Initialize word variable
        self.guesses = []  # Initialize guesses list
        self.max_attempts = 0  # Initialize maximum number of attempts
        self.attempts_left = 0  # Initialize number of attempts remaining

    def choose_category(self):
        categories = ["animals", "countries", "fruits_vegetables", "cars", "dictionary"]
        print("Choose a category:")
        for i, category in enumerate(categories, start=1):
            print("{}. {}".format(i, category))
        while True:
            choice = input("Enter the category number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            print("Invalid choice. Please enter the number corresponding to the category.")

    def choose_difficulty(self):
        
        # Prompt the user to choose the level of difficulty and set the maximum number of attempts accordingly.
        
        print("Choose the level of difficulty:")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (4 attempts)")
        while True:
            choice = input("Enter the difficulty level number: ")
            if choice.isdigit() and 1 <= int(choice) <= 3:
                if choice == "1":
                    self.max_attempts = 10
                elif choice == "2":
                    self.max_attempts = 7
                else:
                    self.max_attempts = 4
                self.attempts_left = self.max_attempts
                break
            print("Invalid choice. Please enter the number corresponding to the difficulty level.")

    def load_words(self, category):
    
        #Load words from the chosen category file and return a list of lowercase words.
    
        filename = "{}.txt".format(category)
        with open(filename, "r") as file:
            words = file.readlines()
        return [word.strip().lower() for word in words]

    def get_masked_word(self):
    
        # Return a masked version of the word, with hidden characters represented by underscores.
    
        masked_word = ""
        for char in self.word:
            if char in self.guesses:
                masked_word += char
            else:
                masked_word += "_"
        return masked_word

    def play(self):
        print("Welcome to Hangman!")
        self.category = self.choose_category()
        self.choose_difficulty()
        self.words = self.load_words(self.category)
        self.word = random.choice(self.words)

        print("Guess the word. You have {} attempts.".format(self.max_attempts))

        while self.attempts_left > 0:
            print("\nAttempts left: {}".format(self.attempts_left))
            masked_word = self.get_masked_word()
            print("Word: {}".format(masked_word))

            guess = input("Enter a letter: ").lower()

            if guess in self.guesses:
                print("You already guessed that letter. Try again!")
                continue

            self.guesses.append(guess)

            if guess not in self.word:
                self.attempts_left -= 1
                print("Wrong guess!")

            if "_" not in self.get_masked_word():
                print("\nCongratulations! You guessed the word: {}".format(self.word))
                break

        if self.attempts_left == 0:
            print("\nGame over! You failed to guess the word. The word was: {}".format(self.word))

        self.ask_play_again()

    def ask_play_again(self):
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                self.__init__()
                self.play()
                break
            elif play_again == "no":
                print("Thank you for playing Hangman!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    game = Hangman()
    game.play()