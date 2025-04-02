import random

def main():
    print("\nGuess my number!\n")
    secret_number:int = random.randint(1,100)
    user_input:int = int(input("Enter a number between 1 and 100: "))
    while user_input != secret_number:
        if user_input > secret_number:
            print("You guess is too high")
        else:
            print("Your guess is too low")
        
        user_input = int(input("Enter a new guess: "))
    
    print(f"\nYou guessed correctly!, the number is: {secret_number}\n")

if __name__ == "__main__":
    main()

