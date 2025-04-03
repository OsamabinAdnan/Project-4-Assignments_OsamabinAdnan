def main():
    fruit_list:list[str] = ["apples", "bananas", "oranges", "pineapple", "grapes"]

    # Print the list
    print(fruit_list)

    # Print the length of the list
    print(f"The length of the list is: {len(fruit_list)}")

    # Add 'mango' to the list
    fruit_list.append("mango")

    # Print the updated list
    print(f"Updated list: {fruit_list}")

if __name__ == "__main__":
    main()