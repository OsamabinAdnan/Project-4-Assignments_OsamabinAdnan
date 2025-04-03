# Python Tic-Tac-Toe Game

A command-line implementation of the classic Tic-Tac-Toe game where a human player can play against a computer opponent.

## Features

- Human vs Computer gameplay
- Random computer moves
- Visual board representation
- Input validation
- Win condition checking

## Files

### game.py
Contains the main game logic with:
- `TicTacToe` class for managing the game board and moves
- Board visualization
- Move validation
- Win condition checking
- Main game loop

### player.py
Implements player classes:
- `Player`: Base class for all players
- `HumanPlayer`: Handles human input
- `RandomComputerPlayer`: Makes random valid moves

## How to Play

1. Run the game:
```python
python game.py
```

2. The board positions are numbered 0-8:
```
| 0| 1| 2|
| 3| 4| 5|
| 6| 7| 8|
```

3. When prompted, enter a number (0-8) to place your mark (X) in that position.

4. The computer (O) will automatically make its move.

5. First player to get 3 in a row (horizontally, vertically, or diagonally) wins!

## Requirements

- Python 3.x
- No additional packages required

## Game Rules

- X always goes first (Human player)
- Players take turns placing their marks
- Game ends when:
  - A player gets 3 in a row (winner)
  - The board is full (tie) (draw)