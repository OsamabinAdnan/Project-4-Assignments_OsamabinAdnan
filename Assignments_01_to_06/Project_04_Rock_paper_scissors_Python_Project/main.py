import random  # Import random module to generate computer's choice

def play():
    """
    Main game function that handles the rock-paper-scissors game logic
    Returns: String indicating game result (win/lose/tie)
    """
    # Game rules reminder in the function docstring:
    # rock beats scissors, scissors beats paper, paper beats rock
    
    # Get player's choice and convert to lowercase
    user_input = input("\nEnter your choice: 'r' for rock, 'p' for paper, 's' for scissors:").lower()
    
    # Generate random choice for computer from possible options
    computer_input = random.choice(['r', 'p', 's'])

    # Check for tie condition first
    if user_input == computer_input:
        return "It\'s a tie!"
    
    # Check if player wins using is_win helper function
    if is_win(user_input, computer_input):
        return "You win!"
    
    # If not a tie and player didn't win, then player loses
    return "You lose!"

def is_win(player, opponent):
    """
    Helper function to determine if the player wins against the opponent
    Args:
        player (str): Player's choice ('r', 'p', or 's')
        opponent (str): Computer's choice ('r', 'p', or 's')
    Returns:
        bool: True if player wins, False otherwise
    """
    # Return true if player wins using winning combinations:
    # Rock beats Scissors (r > s)
    # Scissors beats Paper (s > p)
    # Paper beats Rock (p > r)
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True

# Start the game by calling the play function
print(play())