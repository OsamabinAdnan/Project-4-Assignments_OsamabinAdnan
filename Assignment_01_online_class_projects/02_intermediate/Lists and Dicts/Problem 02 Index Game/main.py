def access_element(lst, index):
    """
    Safely access an element from the list at given index
    Args:
        lst (list): Input list
        index (int): Index to access
    Returns:
        The element at index or error message if index invalid
    """
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

def modify_element(lst, index, new_value):
    """
    Modify an element in the list at given index
    Args:
        lst (list): Input list
        index (int): Index to modify
        new_value: Value to insert at index
    Returns:
        Modified list or error message if index invalid
    """
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range"

def slice_list(lst, start, end):
    """
    Slice the list from start to end index
    Args:
        lst (list): Input list
        start (int): Starting index
        end (int): Ending index
    Returns:
        Sliced list or error message if indices invalid
    """
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices"

def index_game():
    """
    Main game function that demonstrates list operations:
    - Accessing elements
    - Modifying elements
    - Slicing lists
    """
    # Initialize demo list
    lst = [1, 2, 3, 4, 5] # Example list
    print(f"Current list: {lst}")
    
    # Display available operations
    print('Choose an operation: access, modify, slice')
    operation = input('Enter Operation: ')

    # Handle different operations
    if operation == 'access'.strip().lower():
        # Access operation - get single element
        index = int(input('Enter index: '))
        print(f"Element at index {index}: {access_element(lst, index)}")
    elif operation == 'modify'.strip().lower():
        # Modify operation - change element at index
        index = int(input('Enter index: '))
        new_value = int(input('Enter new value: '))
        print(f"Modified list: {modify_element(lst, index, new_value)}")
    elif operation == 'slice'.strip().lower():
        # Slice operation - get subset of list
        start = int(input('Enter start index: '))
        end = int(input('Enter end index: '))
        print(f"Sliced list: {slice_list(lst, start, end)}")
    else:
        print('Invalid operation')

# Start the game when script is run
index_game()

