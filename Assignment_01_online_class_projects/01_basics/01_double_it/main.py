# Program that doubles a number until it exceeds 100
print("\nDouble It\n")

# Get user input and convert to integer
user_input:int = int(input("Enter a number less than 100: "))

# Validate input - exit if number is >= 100
if user_input >=100:
    print("Invalid input\n")
    exit()

# Keep doubling the number until it reaches or exceeds 100
while user_input < 100:
    user_input *= 2  # Double the current number
    print(user_input, end=" ")  # Print number with space separator
    if user_input >= 100:
        break  # Exit loop when number reaches/exceeds 100

# Print newlines for formatting
print("\n")
print("Done\n")