import random  # Importing random for generating random positions and letters
import string  # Importing string to use lowercase letters for filling empty spaces

class WordSearchGame:
    """Class to generate a word search game with a given grid size and words."""

    def __init__(self, grid_size=10, words=None):
        """
        Initializes the word search game.
        :param grid_size: The size of the grid (default is 10x10).
        :param words: A list of words to be placed in the grid.
        """
        self.grid_size = grid_size
        self.word_list = words if words else ['apple', 'banana', 'grape', 'kiwi', 'pear']
        # Default word list if no words are provided

        # Validate grid size before proceeding
        self.validate_grid_size()

        # Create an empty grid
        self.grid = self.generate_grid()

        # Possible directions for word placement
        self.directions = ['h', 'h_rev', 'v', 'v_rev', 'd1', 'd1_rev', 'd2', 'd2_rev']

        # Lists to store placed and unplaced words
        self.placed_words = []
        self.unplaced_words = []

        # Try to place words in the grid
        self.place_words()

        # Fill empty spaces with random letters
        self.fill_empty_spaces()

        # Print summary of placed and unplaced words
        self.print_summary()

    def validate_grid_size(self):
        """Validates that the grid is large enough to fit the longest word."""
        max_word_length = max(len(word) for word in self.word_list)
        if self.grid_size < max_word_length:
            raise ValueError(
                f"Grid size ({self.grid_size}x{self.grid_size}) is too small for the longest word '{max(self.word_list, key=len)}' (length: {max_word_length})."
            )

    def generate_grid(self):
        """Generates an empty grid filled with spaces."""
        return [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def place_words(self):
        """Attempts to place each word in a random direction until a valid position is found."""
        for word in self.word_list:
            placed = False  # Flag to track if the word was placed successfully
            attempts = 0  # Counter to prevent infinite loops
            invalid_positions = set()  # Set to track invalid positions

            while not placed and attempts < 50:  # Limit attempts to avoid infinite loops
                direction = random.choice(self.directions)  # Randomly choose a direction
                row, col = self.get_random_start(word, direction)  # Get a random start position
                position_key = (row, col, direction)  # Store the position key for tracking

                # Check if the position is valid and the word can be placed
                if position_key not in invalid_positions and self.can_place_word(word, row, col, direction):
                    self.place_word(word, row, col, direction)  # Place the word in the grid
                    placed = True  # Mark as placed
                    self.placed_words.append((word, row, col, direction))  # Store placement info
                else:
                    invalid_positions.add(position_key)  # Mark the position as invalid

                attempts += 1  # Increment attempt counter

            if not placed:
                self.unplaced_words.append(word)  # If word couldn't be placed, add to unplaced list

    def get_random_start(self, word, direction):
        """Gets a random valid start position based on word length and direction."""
        word_len = len(word)
        
        # Ensure grid is big enough
        if self.grid_size < word_len:
            raise ValueError(f"Cannot place word '{word}', grid size too small.")

        # Define valid ranges based on direction
        if direction == 'h':  # Horizontal (left to right)
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - word_len)
        elif direction == 'h_rev':  # Horizontal reverse (right to left)
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(word_len - 1, self.grid_size - 1)
        elif direction == 'v':  # Vertical (top to bottom)
            row = random.randint(0, self.grid_size - word_len)
            col = random.randint(0, self.grid_size - 1)
        elif direction == 'v_rev':  # Vertical reverse (bottom to top)
            row = random.randint(word_len - 1, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
        elif direction == 'd1':  # Diagonal (top-left to bottom-right)
            row = random.randint(0, self.grid_size - word_len)
            col = random.randint(0, self.grid_size - word_len)
        elif direction == 'd1_rev':  # Diagonal reverse (bottom-right to top-left)
            row = random.randint(word_len - 1, self.grid_size - 1)
            col = random.randint(word_len - 1, self.grid_size - 1)
        elif direction == 'd2':  # Diagonal (top-right to bottom-left)
            row = random.randint(0, self.grid_size - word_len)
            col = random.randint(word_len - 1, self.grid_size - 1)
        else:  # 'd2_rev' (bottom-left to top-right)
            row = random.randint(word_len - 1, self.grid_size - 1)
            col = random.randint(0, self.grid_size - word_len)

        return row, col

    def can_place_word(self, word, row, col, direction):
        """Checks if a word can be placed at a given location."""
        for i in range(len(word)):
            if direction == 'h':
                r, c = row, col + i
            elif direction == 'h_rev':
                r, c = row, col - i
            elif direction == 'v':
                r, c = row + i, col
            elif direction == 'v_rev':
                r, c = row - i, col
            elif direction == 'd1':
                r, c = row + i, col + i
            elif direction == 'd1_rev':
                r, c = row - i, col - i
            elif direction == 'd2':
                r, c = row + i, col - i
            elif direction == 'd2_rev':
                r, c = row - i, col + i

            if not (0 <= r < self.grid_size and 0 <= c < self.grid_size):  # Ensure within bounds
                return False
            if self.grid[r][c] not in (' ', word[i]):  # Ensure it doesn't overlap incorrectly
                return False

        return True

    def place_word(self, word, row, col, direction):
        """Places a word in the grid."""
        for i in range(len(word)):
            if direction == 'h':
                r, c = row, col + i
            elif direction == 'h_rev':
                r, c = row, col - i
            elif direction == 'v':
                r, c = row + i, col
            elif direction == 'v_rev':
                r, c = row - i, col
            elif direction == 'd1':
                r, c = row + i, col + i
            elif direction == 'd1_rev':
                r, c = row - i, col - i
            elif direction == 'd2':
                r, c = row + i, col - i
            elif direction == 'd2_rev':
                r, c = row - i, col + i

            self.grid[r][c] = word[i]

    def fill_empty_spaces(self):
        """Fills empty spaces with random letters."""
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] == ' ':
                    self.grid[r][c] = random.choice(string.ascii_lowercase)

    def print_summary(self):
        """Prints a summary of placed and unplaced words."""
        print("\nPlacement Summary:")
        for word, row, col, direction in self.placed_words:
            print(f"- {word} at ({row}, {col}) in direction {direction}")
        if self.unplaced_words:
            print("Unplaced Words:", ", ".join(self.unplaced_words))

    def get_grid(self):
        """Returns the current grid."""
        return self.grid
