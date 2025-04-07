# Countdown Timer

A simple Python countdown timer that displays time in minutes and seconds format.

## Description

This project implements a command-line countdown timer in Python. It takes user input for the duration in seconds and displays a countdown in the format MM:SS (minutes:seconds). The timer updates in real-time, overwriting the previous display to create a smooth countdown experience.

## Features

- User-friendly command-line interface
- Real-time countdown display in MM:SS format
- Automatic conversion of seconds to minutes and seconds
- Clean display that updates in place (no scrolling)
- Completion notification when timer reaches zero

## Requirements

- Python 3.x
- Standard library modules only (no external dependencies)

## Installation

1. Clone this repository or download the source code
2. Navigate to the project directory
3. No additional installation steps required as the project uses only Python standard libraries

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. When prompted, enter the desired countdown duration in seconds
   ```
   Enter the time in seconds: 120
   ```

3. The countdown will begin immediately, displaying the time in MM:SS format
   ```
   02:00
   01:59
   01:58
   ...
   ```

4. When the countdown reaches zero, a completion message will be displayed
   ```
   Timer completed!
   ```

## How It Works

The countdown timer uses the following key components:

1. **Time Module**: Used for the `sleep()` function to create the 1-second delay between updates.

2. **divmod() Function**: Converts total seconds into minutes and remaining seconds.
   - Returns a tuple of (quotient, remainder) from division
   - Example: `divmod(125, 60)` returns `(2, 5)` for 2 minutes and 5 seconds

3. **String Formatting**: Uses `'{:02d}:{:02d}'.format(mins, secs)` to ensure minutes and seconds are always displayed with two digits (e.g., "01:05" instead of "1:5").

4. **Carriage Return**: Uses `end="\r"` in the print function to overwrite the previous line, creating a smooth countdown effect.

## Code Structure

- `countdown(t)`: Main function that handles the countdown logic
  - Takes an integer parameter `t` representing total seconds
  - Converts seconds to minutes and seconds
  - Displays the formatted time
  - Decrements the counter
  - Repeats until the timer reaches zero

## Example

```
Enter the time in seconds: 65
01:05
01:04
01:03
...
00:02
00:01
00:00
Timer completed!
```

## License

This project is open source and available under the MIT License.

## Author

Created as part of the Python programming course assignments.
