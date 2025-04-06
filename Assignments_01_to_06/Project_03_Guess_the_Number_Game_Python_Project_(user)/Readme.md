# Number Guessing Game

A simple interactive Python game where the computer tries to guess a number that you're thinking of.

## Description

This game implements a binary search algorithm where the computer attempts to guess a number that the player has in mind. The player provides feedback after each guess, helping the computer narrow down the possible range until it finds the correct number.

## How to Play

1. Think of a number between 1 and 100
2. The computer will make a guess
3. Respond to each guess with:
   - `H` if the guess is too high
   - `L` if the guess is too low
   - `C` if the guess is correct
4. Continue providing feedback until the computer guesses your number correctly

## Features

- Uses binary search algorithm for efficient guessing
- Interactive command-line interface
- Customizable range (currently set to 1-100)
- Case-insensitive input handling

## Requirements

- Python 3.x
- random module (included in Python standard library)

## Usage

```bash
python main.py
```

## Example Interaction

```
Is 50 too high (H), too low (L), or correct (C)?? l
Is 75 too high (H), too low (L), or correct (C)?? h
Is 62 too high (H), too low (L), or correct (C)?? c
Yay! The computer guessed your number, 62, correctly!
```

## How It Works

The program uses a binary search approach by:
1. Maintaining a range of possible numbers (low to high)
2. Making a random guess within that range
3. Adjusting the range based on user feedback
4. Repeating until the correct number is found

## Author

Osama bin Adnan

## License

This project is open source and available under the [MIT License](LICENSE).