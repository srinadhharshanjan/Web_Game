# import random
# import tkinter as tk
# from tkinter import messagebox

# class WordSearchGame:
#     def __init__(self, master, grid_size=8, words=None):
#         self.master = master
#         self.master.title("Cross Visual")

#         self.grid_size = grid_size
#         self.word_list = words if words else ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'mango', 'pear']
#         self.grid = self.generate_grid()
#         self.place_words()
#         self.create_widgets()

#     def generate_grid(self):
#         return [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

#     def place_words(self):
#         for word in self.word_list:
#             placed = False
#             attempts = 0
#             while not placed and attempts < 100:  # Limit attempts to avoid infinite loops
#                 direction = random.choice(['h', 'v'])  # Horizontal or Vertical
#                 if direction == 'h':
#                     row = random.randint(0, self.grid_size - 1)
#                     col = random.randint(0, self.grid_size - len(word))
#                     if self.can_place_word(word, row, col, 'h'):
#                         self.place_word(word, row, col, 'h')
#                         placed = True
#                 else:  # Vertical
#                     row = random.randint(0, self.grid_size - len(word))
#                     col = random.randint(0, self.grid_size - 1)
#                     if self.can_place_word(word, row, col, 'v'):
#                         self.place_word(word, row, col, 'v')
#                         placed = True
#                 attempts += 1
            
#             if not placed:
#                 print(f"Could not place the word: {word}")

#     def can_place_word(self, word, row, col, direction):
#         for i in range(len(word)):
#             if direction == 'h':
#                 if self.grid[row][col + i] not in (' ', word[i]):
#                     return False
#             else:  # Vertical
#                 if self.grid[row + i][col] not in (' ', word[i]):
#                     return False
#         return True

#     def place_word(self, word, row, col, direction):
#         for i in range(len(word)):
#             if direction == 'h':
#                 self.grid[row][col + i] = word[i]
#             else:  # Vertical
#                 self.grid[row + i][col] = word[i]

#     def create_widgets(self):
#         # Create a frame for the grid
#         self.frame = tk.Frame(self.master)
#         self.frame.pack()

#         # Create buttons for the grid
#         for r in range(self.grid_size):
#             for c in range(self.grid_size):
#                 letter = self.grid[r][c]
#                 if letter != ' ':  # Create button only if there's a letter
#                     btn = tk.Button(self.frame, text=letter, width=4, height=2, font=('Arial', 12))
#                     btn.grid(row=r, column=c)
        
#         # Create a button to show the words
#         self.show_words_button = tk.Button(self.master, text="Show Words", command=self.show_words)
#         self.show_words_button.pack(pady=10)

#     def show_words(self):
#         words_str = "\n".join(self.word_list)
#         messagebox.showinfo("Words to Find", words_str)

# if __name__ == "__main__":
#     root = tk.Tk()
#     # Set the grid size and words here
#     grid_size = 8
#     words = ['apple', 'pear', 'kite', 'cake', 'oak', 'tea', 'ear', 'ape']

    
#     game = WordSearchGame(root, grid_size, words)
#     root.mainloop()
import random
import string

class WordSearchGame:
    def __init__(self, grid_size=10, words=None):
        self.grid_size = grid_size
        self.grid = self.generate_grid()  # Generate grid
        self.word_list = words if words else ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'mango', 'pear']
        self.directions = ['h', 'h_rev', 'v', 'v_rev', 'd1', 'd1_rev', 'd2', 'd2_rev']
        self.place_words()
        self.fill_empty_spaces()

    def generate_grid(self):
        """Generates an empty grid filled with spaces."""
        return [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def place_words(self):
        """Places words in all possible directions (horizontal, vertical, diagonal, and their reverses)."""
        for word in self.word_list:
            placed = False
            attempts = 0
            while not placed and attempts < 100:  # Avoid infinite loops
                direction = random.choice(self.directions)
                row, col = self.get_random_start(word, direction)

                if self.can_place_word(word, row, col, direction):
                    self.place_word(word, row, col, direction)
                    placed = True

                attempts += 1
            
            if not placed:
                print(f"Could not place the word: {word}")

    def get_random_start(self, word, direction):
        """Gets a random valid start position based on the word length and direction."""
        if direction in ['h', 'h_rev']:  # Horizontal
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - len(word))
        elif direction in ['v', 'v_rev']:  # Vertical
            row = random.randint(0, self.grid_size - len(word))
            col = random.randint(0, self.grid_size - 1)
        elif direction in ['d1', 'd1_rev']:  # Diagonal (Top-Left to Bottom-Right)
            row = random.randint(0, self.grid_size - len(word))
            col = random.randint(0, self.grid_size - len(word))
        else:  # Diagonal (Top-Right to Bottom-Left)
            row = random.randint(0, self.grid_size - len(word))
            col = random.randint(len(word) - 1, self.grid_size - 1)

        return row, col

    def can_place_word(self, word, row, col, direction):
        """Checks if a word can be placed at a given location in the chosen direction."""
        for i in range(len(word)):
            r, c = row, col

            if direction == 'h':  # Left to Right
                c += i
            elif direction == 'h_rev':  # Right to Left
                c -= i
            elif direction == 'v':  # Top to Bottom
                r += i
            elif direction == 'v_rev':  # Bottom to Top
                r -= i
            elif direction == 'd1':  # Diagonal ↘ (Top-Left to Bottom-Right)
                r += i
                c += i
            elif direction == 'd1_rev':  # Diagonal ↖ (Bottom-Right to Top-Left)
                r -= i
                c -= i
            elif direction == 'd2':  # Diagonal ↙ (Top-Right to Bottom-Left)
                r += i
                c -= i
            elif direction == 'd2_rev':  # Diagonal ↗ (Bottom-Left to Top-Right)
                r -= i
                c += i

            if self.grid[r][c] not in (' ', word[i]):
                return False

        return True

    def place_word(self, word, row, col, direction):
        """Places a word in the grid in the chosen direction."""
        for i in range(len(word)):
            r, c = row, col

            if direction == 'h':  # Left to Right
                c += i
            elif direction == 'h_rev':  # Right to Left
                c -= i
            elif direction == 'v':  # Top to Bottom
                r += i
            elif direction == 'v_rev':  # Bottom to Top
                r -= i
            elif direction == 'd1':  # Diagonal ↘ (Top-Left to Bottom-Right)
                r += i
                c += i
            elif direction == 'd1_rev':  # Diagonal ↖ (Bottom-Right to Top-Left)
                r -= i
                c -= i
            elif direction == 'd2':  # Diagonal ↙ (Top-Right to Bottom-Left)
                r += i
                c -= i
            elif direction == 'd2_rev':  # Diagonal ↗ (Bottom-Left to Top-Right)
                r -= i
                c += i

            self.grid[r][c] = word[i]

    def fill_empty_spaces(self):
        """Fills empty spaces in the grid with random uppercase letters."""
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] == ' ':
                    self.grid[r][c] = random.choice(string.ascii_uppercase)

    def get_grid(self):
        """Returns the current grid."""
        return self.grid
