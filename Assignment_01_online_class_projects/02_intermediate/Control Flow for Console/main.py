import random

# Game configuration
number_of_rounds = 5

def main():
    """
    Main game function implementing the following milestones:
    Milestone 1: Random number generation
    Milestone 2: User input handling
    Milestone 3: Win condition logic
    Milestone 4: Multiple rounds
    Milestone 5: Score tracking
    Extensions: Input validation and conditional endings
    """
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Initialize score for Milestone 5
    your_score = 0

    # Milestone 4: Multiple rounds implementation
    for i in range(number_of_rounds):
        print(f"Round {i+1}")
        
        # Milestone 1: Random number generation
        # Generate numbers for both computer and player
        computer_number:int = random.randint(1, 100)
        player_number:int = random.randint(1, 100)
        print(f"Your number: {player_number}")

        # Milestone 2: User input for game choice
        # Get player's prediction with colored prompt
        choice = input("\033[1;34mDo you think your number is higher or lower than the computer?\033[0m")

        # Extension 1: Input validation
        # Ensure player enters valid choice
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher and lower: ")
        
        # Milestone 3: Win condition logic
        # Define winning scenarios
        higher_and_correct = choice == "higher" and player_number > computer_number
        lower_and_correct = choice == "lower" and player_number < computer_number

        # Process round result
        if higher_and_correct or lower_and_correct:
            print(f"You are correct! The computer's number was {computer_number}")
            # Milestone 5: Score tracking
            your_score += 1
        else:
            print(f"Aww! Thats incorrect. The computer's number was {computer_number}")
        
        # Milestone 5: Display current score
        print(f"Your score is now: {your_score}")
        print()
    
    # Extension 2: Conditional ending messages
    # Display final results with color formatting
    print("\033[1;31mGame over!\033[0m")
    print(f"\033[1;32mYour final score was: {your_score}\033[0m")

    # Performance-based feedback
    if your_score == number_of_rounds:
        print("\033[1;32mWow! You got a perfect score!\033[0m\n")
    elif your_score > number_of_rounds //2:
        print("Good job! You did well!\n")
    else:
        print("Better luck next time!\n")

# Program entry point
if __name__ == "__main__":
    main()