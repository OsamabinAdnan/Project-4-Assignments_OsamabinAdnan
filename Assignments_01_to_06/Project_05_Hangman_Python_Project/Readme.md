# Hangman Game

A classic word guessing game implemented in Python where players try to guess a word letter by letter before running out of lives.

## Description

This implementation of Hangman is a command-line based game where:
- A random word is selected from a predefined list
- Players get 6 lives (attempts) to guess the word
- Players guess one letter at a time
- The game shows the word progress with dashes (-) for unguessed letters
- Previously guessed letters are tracked and displayed

## Features

- Random word selection from a custom word list
- Input validation for letters
- Tracking of used letters
- Live count display
- Word progress visualization

## Requirements

- Python 3.x
- `random` module (built-in)
- `string` module (built-in)
- `words.py` file containing the word list

## Installation

1. Clone or download the repository
2. Ensure you have Python 3.x installed
3. Make sure `words.py` is in the same directory as `hangman.py`

## How to Play

1. Run the game:
```bash
python hangman.py
```

2. The game will:
   - Select a random word
   - Show you how many letters are in the word using dashes
   - Display your remaining lives
   - Show letters you've already guessed

3. Gameplay:
   - Enter one letter at a time
   - If correct, the letter will be revealed in the word
   - If wrong, you lose a life
   - Keep guessing until you either:
     - Successfully guess the word
     - Run out of lives

## Code Structure

- `get_valid_word(words)`: Selects a random valid word from the word list
- `hangman()`: Main game function containing the game logic
- Input validation for:
  - Already guessed letters
  - Invalid characters
  - Valid alphabet letters

## Example Game Output

```
You have 6 lives left. You have used these letters: 
Current word: - - - - -
Guess a letter: A
```

## Contributing

Feel free to fork this repository and make improvements. Some possible enhancements:
- Add ASCII art for the hangman
- Implement difficulty levels
- Add categories for words
- Create a GUI version

## License

This project is open source and available under the MIT License.