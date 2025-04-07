# Import necessary modules
import random

# Display welcome message
print('\nWelcome to the Password Generator!\n')

# Define characters to be used in password generation
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?1234567890'

# Get user input for number of passwords
no_of_passwords = int(input('How many passwords do you want to generate?'))

# Get user input for password length
length = int(input('Enter the length of the password:'))

# Display header for password output
print('\nHere are your passwords:')

# Generate the specified number of passwords
for pwd in range(no_of_passwords):
    # Initialize empty password string
    password = ''
    # Build password by adding random characters
    for c in range(length):
        password += random.choice(char)
    
    # Display the generated password
    print(password)