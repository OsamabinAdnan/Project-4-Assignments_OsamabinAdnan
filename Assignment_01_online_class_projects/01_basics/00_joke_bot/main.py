import random

user_input:str = input("\nWhat do you want?\nYour input: ")
Joke:str = [
    "\nWhy did the math book look sad? Because it had too many problems!\n",
    "\nWhy did the scarecrow win an award? Because he was outstanding in his field!\n",
    "\nWhy did the tomato turn red? Because it saw the salad dressing!\n",
    "\nWhy did the cookie go to the doctor? Because it felt crumbly!\n",
    "\nWhy don't skeletons fight each other? They don't have the guts!\n"
]
Sorry:str = "I'm sorry, I only tell joke"

def main():
    input = user_input.strip().lower()

    if "joke" in user_input:
        print(random.choice(Joke))
    else:
        print(Sorry)

if __name__ == "__main__":
    main()