import random
import string

class WordSearchGame:
    def __init__(self, grid_size=10, words=None):
        self.grid_size = grid_size
        self.grid = self.generate_grid()
        self.word_list = words if words else ['apple', 'banana', 'grape', 'kiwi', 'pear']
        self.directions = ['h', 'h_rev', 'v', 'v_rev', 'd1', 'd1_rev', 'd2', 'd2_rev']
        self.placed_words = []
        self.unplaced_words = []
        self.place_words()
        self.fill_empty_spaces()
        self.print_summary()

    def generate_grid(self):
        """Generates an empty grid filled with spaces."""
        return [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def place_words(self):
        """Places words in all possible directions (horizontal, vertical, diagonal, and their reverses)."""
        for word in self.word_list:
            placed = False
            attempts = 0
            invalid_positions = set()

            while not placed and attempts < 50:
                direction = random.choice(self.directions)
                row, col = self.get_random_start(word, direction)
                position_key = (row, col, direction)

                if position_key not in invalid_positions and self.can_place_word(word, row, col, direction):
                    self.place_word(word, row, col, direction)
                    placed = True
                    self.placed_words.append((word, row, col, direction))
                    print(f"Placed word: {word} at ({row}, {col}) in direction {direction}")
                else:
                    invalid_positions.add(position_key)
                    print(f"Failed to place word: {word} at ({row}, {col}) in direction {direction}")

                attempts += 1

            if not placed:
                self.unplaced_words.append(word)
                print(f"Could not place the word: {word}. Giving up after {attempts} attempts.")

    def get_random_start(self, word, direction):
        """Gets a random valid start position based on the word length and direction."""
        if direction == 'h':
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - len(word))
        elif direction == 'h_rev':
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(len(word) - 1, self.grid_size - 1)
        elif direction == 'v':
            row = random.randint(0, self.grid_size - len(word))
            col = random.randint(0, self.grid_size - 1)
        elif direction == 'v_rev':
            row = random.randint(len(word) - 1, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
        elif direction == 'd1':
            row = random.randint(0, self.grid_size - len(word))
            col = random.randint(0, self.grid_size - len(word))
        elif direction == 'd1_rev':
            row = random.randint(len(word) - 1, self.grid_size - 1)
            col = random.randint(len(word) - 1, self.grid_size - 1)
        elif direction == 'd2':
            row = random.randint(0, self.grid_size - len(word))
            col = random.randint(len(word) - 1, self.grid_size - 1)
        else:  # 'd2_rev'
            row = random.randint(len(word) - 1, self.grid_size - 1)
            col = random.randint(0, self.grid_size - len(word))

        return row, col

    def can_place_word(self, word, row, col, direction):
        """Checks if a word can be placed at a given location in the chosen direction."""
        for i in range(len(word)):
            if direction == 'h':
                c = col + i
                r = row
            elif direction == 'h_rev':
                c = col - i
                r = row
            elif direction == 'v':
                r = row + i
                c = col
            elif direction == 'v_rev':
                r = row - i
                c = col
            elif direction == 'd1':
                r = row + i
                c = col + i
            elif direction == 'd1_rev':
                r = row - i
                c = col - i
            elif direction == 'd2':
                r = row + i
                c = col - i
            elif direction == 'd2_rev':
                r = row - i
                c = col + i

            if not (0 <= r < self.grid_size and 0 <= c < self.grid_size):
                return False
            if self.grid[r][c] not in (' ', word[i]):
                return False

        return True

    def place_word(self, word, row, col, direction):
        """Places a word in the grid in the chosen direction."""
        for i in range(len(word)):
            if direction == 'h':
                c = col + i
                r = row
            elif direction == 'h_rev':
                c = col - i
                r = row
            elif direction == 'v':
                r = row + i
                c = col
            elif direction == 'v_rev':
                r = row - i
                c = col
            elif direction == 'd1':
                r = row + i
                c = col + i
            elif direction == 'd1_rev':
                r = row - i
                c = col - i
            elif direction == 'd2':
                r = row + i
                c = col - i
            elif direction == 'd2_rev':
                r = row - i
                c = col + i

            self.grid[r][c] = word[i]

    def fill_empty_spaces(self):
        """Fills empty spaces in the grid with random uppercase letters."""
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] == ' ':
                    self.grid[r][c] = random.choice(string.ascii_uppercase)

    def print_summary(self):
        """Prints a summary of placed and unplaced words."""
        print("\nPlacement Summary:")
        print("Placed Words:")
        for word, row, col, direction in self.placed_words:
            print(f"- {word} at ({row}, {col}) in direction {direction}")

        if self.unplaced_words:
            print("Unplaced Words:")
            for word in self.unplaced_words:
                print(f"- {word}")

    def get_grid(self):
        """Returns the current grid."""
        return self.grid

# Example usage:
game = WordSearchGame(grid_size=10, words=['apple', 'banana', 'grape'])
grid = game.get_grid()

# Print the final grid
for row in grid:
    print(" ".join(row))

# Print the placement summary
game.print_summary()