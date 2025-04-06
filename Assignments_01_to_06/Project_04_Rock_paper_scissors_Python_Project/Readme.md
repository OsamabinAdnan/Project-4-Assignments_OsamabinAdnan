# Rock Paper Scissors Game

A simple command-line implementation of the classic Rock Paper Scissors game in Python.

## Description

This project implements a Rock Paper Scissors game where a player competes against the computer. The game uses simple text-based inputs and provides immediate feedback on the game result.

## Features

- Player vs Computer gameplay
- Random computer choice generation
- Simple text-based interface
- Input validation and case-insensitive handling
- Immediate game result feedback

## How to Play

1. Run the game using Python:
```python
python main.py
```

2. When prompted, enter your choice using:
   - 'r' for Rock
   - 'p' for Paper
   - 's' for Scissors

3. The computer will randomly choose its move
4. The game will display whether you won, lost, or tied

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choices result in a tie

## Code Structure

- `play()`: Main game function that handles game logic
- `is_win()`: Helper function to determine the winner

## Requirements

- Python 3.x
- random module (included in Python standard library)