import random
from words_list import words  # Importing word list from separate file
import string

def get_valid_word(words):
    """
    Select a random word from the word list that doesn't contain hyphens or spaces
    Args:
        words (list): List of possible words to choose from
    Returns:
        str: A valid word in uppercase
    """
    word = random.choice(words) # Select a random word
    while '-' in word or " " in word: # Check if word contains hyphens or spaces
        word = random.choice(words) # If yes, select another word
    
    return word.upper() # Return word in uppercase

def hangman():
    """
    Main game function that implements the hangman game logic
    """
    # Initialize game variables
    word = get_valid_word(words)  # Get random word to guess
    word_letters = set(word)      # Convert word to set of unique letters
    alphabet = set(string.ascii_uppercase)  # Set of all uppercase letters A-Z
    used_letters = set()          # Track letters already guessed by user
    lives = 6                     # Number of wrong guesses allowed

    # Main game loop - continues while there are unguessed letters and player has lives
    while len(word_letters) > 0 and lives > 0:
        # Display game status - remaining lives and used letters
        print(f"\nYou have {lives} lives left. You have used these letters: ", " ".join(used_letters))

        # Show current state of word with dashes for unguessed letters
        # Using list comprehension to build the display string
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_list)) # Print the display string

        # Get player's guess and convert to uppercase
        user_letters = input("Guess a letter: ").upper()

        # Check if guess is valid (unused letter from alphabet)
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)  # Add letter to used letters set
            if user_letters in word_letters:
                word_letters.remove(user_letters)  # Remove from target letters if correct
            else:
                lives -= 1  # Decrease lives for wrong guess
                print(f"{user_letters} is not in word.")
        
        # Handle case where letter was already guessed
        elif used_letters in used_letters:
            print("You have already used that letter. Please try again.")
        
        # Handle invalid input (not a letter)
        else:
            print("Invalid character. Please try again.")
            
    # Game over - Display result
    if lives == 0:
        print("Sorry, you died. The word was", word)  # Loss condition
    else:
        print(f'You guessed the word correctly "{word}"!!\n')  # Win condition

# Only run the game if this file is run directly (not imported)
if __name__ == "__main__":
    hangman()