# Import random module to generate random numbers
import random

def get_random_number(num: int):
    """
    A number guessing game where user tries to guess a random number.
    Args:
        num (int): The upper bound for the random number range (1 to num)
    """
    # Generate a random number between 1 and the given upper bound
    random_number = random.randint(1, num)
    # Initialize guess variable to store user input
    guess = 0
    
    # Continue loop until user guesses the correct number
    while guess != random_number:
        # Get user input and convert to integer
        guess = int(input(f"\nGuess a number between 1 and {num}: "))
        
        # Give feedback based on the guess
        if guess < random_number:
            print("You are too low! Try again.\n")
        elif guess > random_number:
            print("You are too high! Try again.\n")
    
    # Congratulate user when correct number is guessed
    print(f"\nCongrats! You have guessed the number {random_number} correctly!\n")

# Start the game with numbers from 1 to 100
get_random_number(100)