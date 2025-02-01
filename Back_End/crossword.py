# import random
# import string

# class CrosswordGame:
#     def __init__(self, grid_size=10, words=None):
#         self.grid_size = grid_size
#         self.grid = self.generate_grid()  # Generate an empty grid
#         self.word_list = words if words else ['apple', 'banana', 'grape', 'kiwi', 'pear']
#         self.place_words()
#         self.fill_empty_spaces()

#     def generate_grid(self):
#         """Generates an empty grid filled with spaces."""
#         return [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

#     def place_words(self):
#         """Places words in all possible directions (horizontal, vertical)."""
#         for word in self.word_list:
#             placed = False
#             attempts = 0
#             while not placed and attempts < 100:  # Avoid infinite loops
#                 direction = random.choice(['h', 'v'])  # Horizontal or Vertical
#                 row, col = self.get_random_start(word, direction)

#                 if self.can_place_word(word, row, col, direction):
#                     self.place_word(word, row, col, direction)
#                     placed = True

#                 attempts += 1
            
#             if not placed:
#                 print(f"Could not place the word: {word}")

#     def get_random_start(self, word, direction):
#         """Gets a random valid start position based on the word length and direction."""
#         if direction == 'h':  # Horizontal
#             row = random.randint(0, self.grid_size - 1)
#             col = random.randint(0, self.grid_size - len(word))  # Ensure word fits horizontally
#         else:  # Vertical
#             row = random.randint(0, self.grid_size - len(word))  # Ensure word fits vertically
#             col = random.randint(0, self.grid_size - 1)
#         return row, col

#     def can_place_word(self, word, row, col, direction):
#         """Checks if a word can be placed at a given location in the chosen direction."""
#         for i in range(len(word)):
#             r, c = row, col

#             if direction == 'h':  # Left to Right
#                 c += i
#             elif direction == 'v':  # Top to Bottom
#                 r += i

#             # Check if the grid position is either empty or already contains the current letter
#             if self.grid[r][c] not in (' ', word[i]):
#                 return False

#         return True

#     def place_word(self, word, row, col, direction):
#         """Places a word in the grid in the chosen direction."""
#         for i in range(len(word)):
#             r, c = row, col

#             if direction == 'h':  # Left to Right
#                 c += i
#             elif direction == 'v':  # Top to Bottom
#                 r += i

#             self.grid[r][c] = word[i]

#     def fill_empty_spaces(self):
#         """Fills empty spaces in the grid with random uppercase letters."""
#         for r in range(self.grid_size):
#             for c in range(self.grid_size):
#                 if self.grid[r][c] == ' ':
#                     self.grid[r][c] = random.choice(string.ascii_uppercase)

#     def get_grid(self):
#         """Returns the current grid."""
#         return self.grid

import random

class CrosswordGame:
    def __init__(self, grid_size=10, words=None):
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.word_list = words if words else ['tree', 'river', 'mountain', 'valley']
        self.place_words()

    def place_words(self):
        for word in self.word_list:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - len(word))
            self.place_word(word, row, col)

    def place_word(self, word, row, col):
        for i in range(len(word)):
            self.grid[row][col + i] = word[i]

    def get_grid(self):
        return self.grid
