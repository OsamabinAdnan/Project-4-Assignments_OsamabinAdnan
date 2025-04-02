# Import random module for generating random numbers
import random

# Constants for number of random numbers to generate and their range
n_numbers  = 10  # How many random numbers to generate
min_value = 1    # Minimum value for random numbers
max_value = 100  # Maximum value for random numbers


def main():
    # Generate and print n_numbers random integers between min_value and max_value
    for i in range(n_numbers):
        # Print each number followed by a space instead of newline
        print(random.randint(min_value, max_value), end=' ')

# Call the main function to execute the program
main()