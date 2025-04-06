# Number Guessing Game

A simple command-line number guessing game implemented in Python where the user tries to guess a randomly generated number.

## Description

This game randomly generates a number between 1 and 100 (configurable) and prompts the user to guess it. After each guess, the game provides feedback whether the guess was too high or too low, helping the user narrow down the correct number.

## Features

- Random number generation within a specified range
- Interactive command-line interface
- Continuous feedback on guesses
- Simple and intuitive gameplay

## How to Play

1. Run the Python script
2. The computer will generate a random number between 1 and 100
3. Enter your guess when prompted
4. Receive feedback (too high/too low)
5. Keep guessing until you find the correct number
6. Receive congratulations when you guess correctly!

## Requirements

- Python 3.x
- `random` module (included in Python standard library)

## Usage

```bash
python main.py
```

## Code Structure

- `get_random_number(num)`: Main game function that:
  - Generates a random number
  - Handles user input
  - Provides feedback
  - Manages game loop

## Example Output

```
Guess a number between 1 and 100: 50
You are too high!

Guess a number between 1 and 100: 25
You are too low!

Guess a number between 1 and 100: 37
Congrats! You have guessed the number 37 correctly!
```

## License

This project is open source and available under the MIT License.