import random

def computer_guess(x):
    # Initialize the search range
    low = 1      # Lower bound of the possible number range
    high = x     # Upper bound of the possible number range
    feedback = '' # Store user's feedback about the guess

    # Continue guessing until the correct number is found
    while feedback != 'c':
        # If there's more than one possible number in the range
        if low != high:
            # Generate a random guess within the current range
            guess = random.randint(low, high)
        else:
            # If low equals high, we've narrowed it down to one number
            guess = low

        # Get feedback from the user about our guess
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()

        # Adjust the search range based on feedback
        if feedback == 'h':
            # If guess was too high, adjust the upper bound
            high = guess - 1
        if feedback == 'l':
            # If guess was too low, adjust the lower bound
            low = guess + 1

    # Once the correct number is guessed, display success message
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# Start the game with numbers from 1 to 100
computer_guess(100)