import random
import time
# Implementation of Binary Search Algorithm

# We will prove that binary search is faster than naive search

# navive search: scan the entire list and ask if the element is equal to the target
# if yes, return the index of the element, else return -1


def navive_search(lst, target):
    # example of lst = [1, 3, 10, 12]
    # Iterate through each element in the list sequentially
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Return index if target is found
    return -1  # Return -1 if target is not found in the list

# binary search: divide the list in half and check if the target is in the left or right half
# if yes, repeat the process on that half, else return -1

def binary_search(lst, target ,low=None, high=None):
    # Initialize default values for first call
    if low  is None:
        low = 0
    if high is None:
        high = len(lst) - 1
    
    # Base case: if low becomes greater than high, element not found
    if high < low:
        return -1

    # example of lst = [1, 3, 5, 10, 12] and target = 10 which is at index 3
    # Calculate the middle point of current search range
    midpoint = (low + high)  // 2 # midpoint = 2

    # If target found at midpoint, return its index
    if lst[midpoint] == target:
        return midpoint
    # If target is less than midpoint value, search in left half
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint - 1)
    # If target is greater than midpoint value, search in right half
    else: # target > lst[midpoint]
        return binary_search(lst, target, midpoint + 1, high)

if __name__ == '__main__':

    # Test case with small list (commented out)
    # lst = [1, 3, 5, 10, 12]
    # target = 10
    # print("Navie Search: ",navive_search(lst, target))
    # print("Binary Search: ",binary_search(lst, target))


    # Performance comparison with large dataset
    # test the binary search with a large list
    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    # Generate random numbers and ensure no duplicates using set
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))  # Convert to sorted list for binary search

    # Time the naive search implementation
    start = time.time() # Start timing naive search
    for target in sorted_list:
        navive_search(sorted_list, target) # Perform naive search for current target
    end = time.time() # End timing naive search
    # Print average time per search for naive method
    print("Navie Search Time: ", (end - start)/length, "seconds")

    # Time the binary search implementation
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target) # Perform binary search for current target
    end = time.time() # End timing binary search
    # Print average time per search for binary method
    print("Binary Search Time: ", (end - start)/length, "seconds")