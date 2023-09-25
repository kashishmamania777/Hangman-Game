import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        
        self.category = None
        self.categories = ["animals", "countries", "fruits_vegetables", "cars", "dictionary"]
        
        self.difficulty = None
        self.difficulties = ["Easy (10 attempts)", "Medium (7 attempts)", "Hard (4 attempts)"]
        
        self.words = []
        self.word = None
        self.guesses = []
        self.max_attempts = 0
        self.attempts_left = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        # Increase font size
        self.large_font = tkfont.Font(family='Helvetica', size=20)
        
        # Category selection
        self.category_label = tk.Label(self.root, text="Choose a category:", font=self.large_font)
        self.category_label.pack()
        
        self.category_var = tk.StringVar()
        self.category_var.set(self.categories[0])
        
        for category in self.categories:
            category_radio = tk.Radiobutton(self.root, text=category, variable=self.category_var, value=category, font=self.large_font)
            category_radio.pack()
        
        self.next_button = tk.Button(self.root, text="Next", command=self.select_difficulty, font=self.large_font)
        self.next_button.pack()
    
    def select_difficulty(self):
        self.category = self.category_var.get()
        
        # Difficulty selection
        self.category_label.pack_forget()
        for widget in self.root.winfo_children():
            widget.pack_forget()
        
        self.difficulty_label = tk.Label(self.root, text="Choose the level of difficulty:", font=self.large_font)
        self.difficulty_label.pack()
        
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set(self.difficulties[0])
        
        for difficulty in self.difficulties:
            difficulty_radio = tk.Radiobutton(self.root, text=difficulty, variable=self.difficulty_var, value=difficulty, font=self.large_font)
            difficulty_radio.pack()
        
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, font=self.large_font)
        self.start_button.pack()
    
    def load_words(self):
        filename = "{}.txt".format(self.category)
        with open(filename, "r") as file:
            words = file.readlines()
        return [word.strip().lower() for word in words]
    
    def get_masked_word(self):
        masked_word = ""
        for char in self.word:
            if char in self.guesses:
                masked_word += char
            else:
                masked_word += "_"
        return masked_word
    
    def start_game(self):
        self.difficulty = self.difficulty_var.get()
        
        for widget in self.root.winfo_children():
            widget.pack_forget()
        
        self.words = self.load_words()
        self.word = random.choice(self.words)
        self.max_attempts = 10 if "Easy" in self.difficulty else (7 if "Medium" in self.difficulty else 4)
        self.attempts_left = self.max_attempts
        
        self.attempts_label = tk.Label(self.root, text="Attempts left: {}".format(self.attempts_left), font=self.large_font)
        self.attempts_label.pack()
        
        self.word_label = tk.Label(self.root, text="Word: {}".format(self.get_masked_word()), font=self.large_font)
        self.word_label.pack()
        
        self.guess_entry = tk.Entry(self.root, font=self.large_font)
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, font=self.large_font)
        self.guess_button.pack()
    
    def make_guess(self):
        guess = self.guess_entry.get().lower()
        
        if guess in self.guesses:
            messagebox.showinfo("Invalid Guess", "You already guessed that letter. Try again!")
        else:
            self.guesses.append(guess)
            if guess not in self.word:
                self.attempts_left -= 1
            
            self.attempts_label.config(text="Attempts left: {}".format(self.attempts_left))
            self.word_label.config(text="Word: {}".format(self.get_masked_word()))
            
            if "_" not in self.get_masked_word():
                messagebox.showinfo("Congratulations!", "You guessed the word: {}".format(self.word))
                self.ask_play_again()
            elif self.attempts_left == 0:
                messagebox.showinfo("Game Over", "You failed to guess the word. The word was: {}".format(self.word))
                self.ask_play_again()
        
        self.guess_entry.delete(0, tk.END)
    
    def ask_play_again(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        
        play_again = messagebox.askquestion("Play Again?", "Do you want to play again?")
        if play_again == "yes":
            self.setup_ui()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # Increase window size
    app = HangmanGUI(root)
    root.mainloop()
